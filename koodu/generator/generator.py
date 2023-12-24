"""The code generator module"""

import logging
from pathlib import Path
from typing import Dict, List

from jinja2 import (
    DictLoader as JDictLoader,
)
from jinja2 import (
    Environment as JEnvironment,
)
from jinja2 import (
    Template as JTemplate,
)
from jinja2.exceptions import TemplateNotFound

from koodu.exceptions import MissingModelException
from koodu.generator.file import File
from koodu.generator.models import GeneratorModelSchema, TemplateSchema
from koodu.generator.utils import (
    ConfigSchema,
    load_template_config,
)


class SingleModelView:
    """Convenience object to generate an object out a of a dict"""

    def __init__(self, model):
        self.elem = model

    def __str__(self):
        return str(tuple(self))

    def __iter__(self):
        for item in self.elem:
            yield item


class Generator:
    """The Generator is the Core of the engine, it takes as parameters a model, the
    path to the template folder, and the path of the folder where the generated
    code will be saved and it contains different methods that allow us to generate
    our code from the model and templates.
    """

    def __init__(
        self,
        template_folder: Path,
        model: GeneratorModelSchema = None,
        output: Path = Path("./"),
    ) -> None:
        self.valid = False
        self.last_error = ""
        self.template_folder = template_folder
        self.model = model
        self.output = output
        self.configs: ConfigSchema = load_template_config(self.template_folder)

        if self.configs is None:
            raise Exception("The config file is not good formated.")

        if self.model is None:
            raise MissingModelException("NO_MODEL", "Missing Model.")
        elif self.configs.templates is None:
            raise Exception("NO_TEMPLATES", "Missing Template")
        elif len(self.configs.templates) < 1:
            raise Exception("NO_ATTACHED_TEMPLATES", "Missing Attached Template.")
        else:
            templates = self.get_templates()
            self.jinja_env = JEnvironment(loader=JDictLoader(templates))
            self.valid = True

    def __str__(self):
        return f"""Configs: {self.configs}
        Templates: {self._list_templates()}
        """

    def get_templates(self) -> Dict[str, Dict[str, str]]:
        """Load the templates Informations."""
        result = {}
        for template in self.configs.templates:
            with open(self.template_folder / Path(template.template_path), "r") as fp:
                template_code = fp.read()

            result[template.name] = template_code

        return result

    def get_template_by_name(self, template_name: str) -> TemplateSchema:
        """Find a Template from the list of template with it name."""
        found_template = None

        for template in self.configs.templates:
            if template.name == template_name:
                with open(
                    self.template_folder / Path(template.template_path), "r"
                ) as fp:
                    template_code = fp.read()

                found_template = TemplateSchema(
                    **{
                        "template_code": template_code,
                        "name": template.name,
                        "path": template.path,
                        "file_name": template.file_name,
                        "type": template.type,
                        "file_path": template.file_path,
                    }
                )
                break
        return found_template

    def print_templates(self) -> Dict[str, Dict[str, str]]:
        """Get the liste of Template"""
        return self.get_templates()

    def render_file_name(self, template: TemplateSchema, model) -> str:
        """Render file name

        Args:
            template (dict): The Template to generate.
            model (str): The model from which we want to generate.

        Returns:
            (str): the file name
        """
        if len(template.file_name) > 0:
            args = {"model": model, "full_model": self.model}
            tm = JTemplate(template.file_name)
            file_name = tm.render(args)
        else:
            model_element_first_key = list(model.keys())[0]
            file_name = template.name + "_" + model[model_element_first_key]

        if template.type:
            file_name = file_name + "." + template.type

        return file_name

    def render_file_path(self, template: TemplateSchema, model) -> str:
        """Render file path

        Args:
            template (dict): The Template to generate.
            model (str): The model from which we want to generate.

        Returns:
            (str): the file path
        """
        filepath = ""
        args = {"model": SingleModelView(model), "full_model": self.model}
        if len(template.file_path) > 0:
            tm = JTemplate(template.file_path)
            filepath = tm.render(args)
        return filepath

    def render_model(
        self, template: TemplateSchema, model_element: Dict[str, str], from_list
    ):
        model_element_first_key = list(model_element.keys())[0]
        ret_value = "Nothing as been generated."
        if model_element_first_key:
            try:
                jinja_template = self.jinja_env.get_template(template.name)
                args = {
                    "model": model_element
                    if from_list
                    else SingleModelView(model_element),
                    "full_model": self.model,
                }
                ret_value = jinja_template.render(args)
            except TemplateNotFound:
                self.last_error = f"Could not find template in {template.name}"
                ret_value = self.last_error
                logging.error(self.last_error)
            except Exception as ex:
                ret_value = f"Exception in {template.name}: {str(ex)}"
        else:
            ret_value = "Part of the Model not found or empty"
        return {
            "name": self.render_file_name(template, model_element),
            "filepath": self.render_file_path(template, model_element),
            "content": ret_value,
        }

    def _render_template(self, name: str) -> List[Dict[str, str]]:
        output = []
        template = self.get_template_by_name(name)
        model_part = self.model
        path_steps = [elem for elem in template.path.split("/") if elem]

        for step in path_steps:
            try:
                model_part = self.model[step]
            except Exception:
                output.append(
                    {
                        "name": name,
                        "filepath": template.file_path,
                        "content": f"ERR:Given Path {template.path} ist not Valid:\
                               Step {step} not found.",
                    }
                )
                return output

        if isinstance(model_part, list):
            for element in model_part:
                output.append(self.render_model(template, element, from_list=True))
        elif isinstance(model_part, dict):
            output.append(self.render_model(template, model_part, from_list=False))
        else:
            output.append(
                {
                    "name": name,
                    "filepath": template.file_path,
                    "content": "ERR: "
                    + name
                    + " Model Path contains not an List or Dictionary.",
                }
            )
        return output

    def render_templates(self) -> List[Dict[str, str]]:
        rendered_outputs = []

        for template in self.configs.templates:
            output = []
            if not template.is_macro and not template.is_base:
                output = self._render_template(template.name)
                rendered_outputs.extend(output)

        return rendered_outputs

    def render(self) -> List[File]:
        """the render method renders a deployment group."""

        result = []
        for elem in self.render_templates():
            name = elem.get("name")
            content = elem.get("content")
            filepath: str = elem.get("filepath")
            if filepath == "/" or filepath == "./" or filepath == ".":
                root = self.output
            else:
                if filepath.startswith("/"):
                    root = self.output / Path(filepath[1:])
                else:
                    root = self.output / Path(filepath)
            file = File(name=name, root=root, content=content)
            result.append(file)

        return result

    def render_template(self, template_name):
        """The render method renders one template"""
        template = self.get_template_by_name(template_name)
        if template:
            return self._render_template(template.name)
        return {"name": f"ERR: {template_name}", "content": "template not found."}

    def _list_templates(self):
        """List the templates in the actual jinja environment"""

        return self.jinja_env.list_templates()
