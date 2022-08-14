"The code generator module"
#std
import pprint
import logging
import json
from pathlib import Path
from typing import List, Tuple, Optional, Dict
from unittest import result
from jinja2 import DictLoader as JDictLoader, Environment as JEnvironment,Template as JTemplate
from jinja2.exceptions import TemplateNotFound
from koodu.generator.file import File
from koodu.exceptions import MissingModeException

from .utils import get_all_files, load_template_config

pp = pprint.PrettyPrinter()

class Objectview():
    """Convenience object to generate an object out a of a dict"""

    def __init__(self, d):
        self.dict = d

    def __str__(self):
        return str(tuple(self))

    def __iter__(self):
        for item in self.dict:
            yield item

class Generator():
    """The Generator of the Code. It become Template and Model as parameter and
        generate files's content base on them..
    """

    def __init__(self, template_folder: Path, model: str=None) -> None:
        self.valid = False
        self.last_error = ""
        self.template_group = None
        self.template_folder = template_folder
        self.model = model
        self.configs = load_template_config(self.template_folder)

        if self.configs is None:
            raise Exception("The config data ist not googd formatted")

        if self.model is None:
            raise MissingModeException("NO_MODEL", "No model specified")
        elif self.configs["templates"] is None:
            raise Exception("NONE_TEMPLATES", "Template Group has no templates attribute")
        elif len(self.configs["templates"])<1:
            raise Exception("NO_TEMPLATES", "Template Group has no templates attached.")
        else:
            templates = self._get_templates()
            self.jinja_env = JEnvironment(loader=JDictLoader(templates))
            self.valid = True
        # print("LOADED TEMPLATES ----------------------")
        # print(self._get_templates())
    
    def __str__(self):
        return f"""Template Group: {self.template_group['name']}
        Templates: {self.list_templates()}
        """

    def _get_template_code(self, template) -> str:
        """Gets the jinja expression out of the template object"""
        if template["is-macro"]:
            return f"""{{% macro {template['template-code']}({'model'}) -%}}
                    {template['template-code']}
                    {{%- endmacro %}}"""
        else:
            return template['template-code']

    def _get_templates(self) -> Dict[str, Dict[str, str]]:
        """Load the templates Informations."""
        result = {}
        for template in self.configs["templates"]:
            with open(self.template_folder / Path(template["template-path"]), "r") as fp:
                template_code = fp.read()

            result[template["name"]] = template_code 
            #{
            #    "template-code": template_code,
            #    "name": template["name"],
            #    "path": template["path"],
            #    "file-name": template["file-name"],
            #    "type": template["type"],
            #    "file-path": template["file-path"]
            #}
        
        return result

    def _get_template_by_name(self, template_name: str) ->Dict[str, str]:
        """Find a Template from the list of template with it name."""
        found_template = None
        
        for template in self.configs["templates"]:
            if template["name"] == template_name:
                with open(self.template_folder / Path(template["template-path"]), "r") as fp:
                    template_code = fp.read()

                found_template = {
                    "template-code": template_code,
                    "name": template["name"],
                    "path": template["path"],
                    "file-name": template["file-name"],
                    "type": template["type"],
                    "file-path": template["file-path"]
                }
                break
        return found_template


    def print_templates(self) -> Dict[str, Dict[str, str]]:
        """Get the liste of Template"""
        return self._get_templates()

    def get_file_type(self, templateType):
        """Get the file extension from the template."""
        code_type = ""
        file_type_ending = ""
        if(templateType["codeType"]):
            code_type = templateType["codeType"]
        if(len(code_type)>0):
                file_type_ending = "." + code_type
        return file_type_ending


    def render_file_name(self, template, model):
        """Render file name"""
        file_name = ""
        # handle filename template is filled or empty
        if(len(template["file-name"])>0):
            args = { "model" : Objectview(model), "full_model": self.model}
            tm = JTemplate(template["file-name"])
            file_name=tm.render(args)
        else: 
            model_element_first_key = list(model.keys())[0]
            file_name=template["name"] + "_" + model[model_element_first_key] 

        # add file extention
        # template_type=template["type"]
        file_name = file_name  + "." + template["type"]  # self.get_file_type(templateType)

        return file_name
    
    def render_file_path(self, template, model):
        """Render the file path"""
        #model_element_first_key = list(model.keys())[0]
        filepath = ""
        args = { "model" : Objectview(model), "full_model": self.model}
        if(len(template["file-path"])>0):
            tm = JTemplate(template["file-path"])
            filepath=tm.render(args)
            # print(" FILE NAME-----------")
            # print(filepath)
        return filepath
    

    def _render_model_element(self, template, model_element, from_list):
        #model_element_first_key = list(model_element.keys())[0]
        ret_value="Nothing as been generated."
        # print(template)
        #if model_element_first_key:
        try:
            #print("get template")
            jinja_template = self.jinja_env.get_template(template["name"])
            #print("template for", jinja_template)
            logging.warning(self.jinja_env)
            args = { "model" : Objectview(model_element), "full_model": self.model}
            ret_value = jinja_template.render(args)

        except TemplateNotFound as e:
            self.last_error = f"Could not find template in {template['name']}"
            ret_value = self.last_error
            logging.error(self.last_error)
        except Exception as ex:
            ret_value = f"Exception in {template['name']}: "+str(ex)
        #else:
        #    ret_value = "Part of the Model not found or empty"
        return {
            "name": self.render_file_name(template, model_element),
            "filepath": self.render_file_path(template, model_element),
            "content": ret_value
        }

    def _render_template(self, name: str) -> List[Dict[str, str]]:
        output = []
        template = self._get_template_by_name(name)
        model_part = self.model
        path_steps = [elem for elem in template["path"].split("/") if elem]

        for step in path_steps:
            try:
                model_part = self.model[step]
            except:
                print(f"\n\n template path {template['path']} \n\n model {model_part} \n\n")
                output.append({
                    "name": name,
                    "filepath": template["file-path"],
                    "content": "ERR:Given Path "+template["path"] + " ist not Valid : Step " + step + " not found."
                })
                return output

        if isinstance(model_part, list):
            #for element in model_part:
            output.append(self._render_model_element(template, model_part, from_list=True))
        elif isinstance(model_part, dict) :
            output.append(self._render_model_element(template, model_part, from_list=False))
        else: 
            output.append({
                "name": name,
                "filepath": template["file-path"],
                "content": "ERR: " + name + " Model Path contains not an List or Dictionary."
            })                    
        return output

    def _render_template_group(self):
        rendered_outputs = []

        for template in self.configs["templates"]:
            output = []
            #print("****************")
            if not template["is-macro"] and not template["is-base"]:
                output = self._render_template(template["name"])
                rendered_outputs = rendered_outputs + output

        return rendered_outputs

    def render(self) -> List[File]:
        """the render method renders a deployment group"""
        return self._render_template_group()
        #result = []
        #for elem in self._render_template_group():
        #    #TODO imlement the file logic
        #    file = File()
        #    result.append(file)
        #
        #return result

    def render_template(self, template_name):
        """The render method renders one template"""
        template = self._get_template_by_name(template_name)
        if (template):
            return self._render_template(template["name"])
        return {"name": "ERR:"+template_name, "content": "template not found."}

    def list_templates(self):
        """List the templates in the actual jinja environment"""
       
        return self.jinja_env.list_templates()
