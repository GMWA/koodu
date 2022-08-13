"The code generator module"
#std
import logging
import json
from typing import List, Tuple, Optional, Dict
from unittest import result
from jinja2 import DictLoader as JDictLoader, Environment as JEnvironment,Template as JTemplate
from jinja2.exceptions import TemplateNotFound
from koodu.generator.file import File

from .utils import get_all_files, load_template_config
#from generator.utils import read_template_code, read_sample_model_json
#from generator.models import Model, User as UserModel, TemplateGroup as TemplateGroupModel, TemplateType,Template

class Objectview():
    """Convenience object to generate an object out a of a dict"""

    def init(self, d):
        self.dict = d

    def str(self):
        return str(tuple(self))

    def iter(self):
        for item in self.dict:
            yield item

def coalesce(*arg):
    "Returns the first non none object. If all objects in list are none it returns none."
    return next((a for a in arg if a is not None), None)

class Generator():
    """The code generator"""

    def init(self, **kwargs):
        # generator status & error

        self.valid = False
        self.last_error = ""
        self.template_group = None

        # generator mandatory init parameters
        #self.template_group = kwargs.get("template_group", None)
        self.template_folder = kwargs.get("template_folder", None)
        self.model = kwargs.get("model", None)
        self.configs = load_template_config(self.template_folder)

        if self.configs is None:
            raise Exception("The config data ist not googd formatted")

        # check whether we are in valid state or not
        #if self.template_group is None:
        #    raise Exception("NO_TEMPLATEGROUP", "No template group found or specified")
        if self.model is None:
            raise Exception("NO_MODEL", "No model specified")
        elif self.configs["templates"] is None:
            raise Exception("NONE_TEMPLATES", "Template Group has no templates attribute")
        elif len(self.configs["templates"])<1:
            raise Exception("NO_TEMPLATES", "Template Group has no templates attached.")
        else:
            self.jinja_env = JEnvironment(loader=JDictLoader(self._get_templates()))
            self.valid = True
        print("LOADED TEMPLATES ----------------------")
        print(self._get_templates())

    def _get_template_code(self, template) -> str:
        """Gets the jinja expression out of the django template object"""
        if template["is-macro"]:
            return f"""{{% macro {template['template-code']}({'model'}) -%}}
                    {template['template-code']}
                    {{%- endmacro %}}"""
        else:
            return template['template-code']

    def _get_templates(self):
        result = {}
        for template in self.configs["templates"]:
            with open(template["template-path"], "r") as fp:
                template_code = fp.read()

            result[template["name"]] = {
                "template-code": template_code,
                "name": template["name"],
                "path": template["path"],
                "file-name": template["file-name"],
                "type": template["type"],
                "file-path": template["file-path"]
            }
        
        return result

    def _get_templateByName(self, template_name: str) ->Dict[str, str]:
        found_template = None
        
        for template in self.configs["templates"]:
            if template["name"] == template_name:
                with open(template["template-path"], "r") as fp:
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


    def print_templates(self):
        "prints templates"
        return self._get_templates()

    def getFileType(self, templateType):
        codeType = ""
        fileTypeEnding = ""
        if(templateType["codeType"]):
            codeType = templateType["codeType"]
        if(len(codeType)>0):
                fileTypeEnding = "."+codeType
        return fileTypeEnding
        # return fileType

    def renderFileName(self, template, model):

        fileName = ""

        # handle filename template is filled or empty
        if(len(template["file-name"])>0):
            args = { "model" : Objectview(model), "full_model": self.model}
            tm = JTemplate(template["file-name"])
            fileName=tm.render(args)
        else: 
            model_element_first_key = list(model.keys())[0]
            fileName=template["name"] + "_" + model[model_element_first_key] 

        # add file extention
        templateType=template["type"]
        fileName = fileName  + "." + template["type"] #self.getFileType(templateType)

        return fileName
    
    def renderFilePath(self, template, model):
        model_element_first_key = list(model.keys())[0]
        filepath = ""
        args = { "model" : Objectview(model), "full_model": self.model}
        if(len(template["file-path"])>0):
            tm = JTemplate(template["file-path"])
            filepath=tm.render(args)
            print(" FILE NAME-----------")
            print(filepath)
        return filepath
    

    def _render_model_element(self, template, model_element, from_list):
        model_element_first_key = list(model_element.keys())[0]
        ret_value="Nothing as been generated."
        if(model_element_first_key):
            try:
                jinja_template = self.jinja_env.get_template(template["name"])
                logging.warning(self.jinja_env)
                args = { "model" : Objectview(model_element), "full_model": self.model}
                ret_value = jinja_template.render(args)

            except TemplateNotFound as e:
                self.last_error = f"Could not find template in {template['name']}"
                ret_value = self.last_error
                logging.error(self.last_error)
            except Exception as ex:
                ret_value = f"Exception in {template['name']}: "+str(ex)
        else:
            ret_value = "Part of the Model not found or empty"
        return {
            "name": self.renderFileName(template, model_element),
            "filepath": self.renderFilePath(template, model_element),
            "content": ret_value
        }

    def _render_template(self, start_template_name: str) -> List[Dict[str, str]]:
        output = []
        template = self._get_templateByName(start_template_name)
        # print(template)
        model_part = self.model
        path_steps= template["path"].split("/")

        for step in path_steps:
            if(step and len(step)>0):
                try:
                    model_part = model_part[step]
                except:
                    print(f"\n\n template path {template['path']} \n\n model {model_part} \n\n")
                    output.append({
                        "name": start_template_name,
                        "filepath": template["file-path"],
                        "content": "ERR:Given Path "+template["path"]+" ist not Valid : Step "+step+" not found"
                    })
                    return output

        if(isinstance(model_part, list)):
            for element in model_part:
                 output.append(self._render_model_element(template, element, from_list=True))
        elif(isinstance(model_part, dict)):
            output.append(self._render_model_element(template, model_part, from_list=False))
        else: 
            output.append({
                "name": start_template_name,
                "filepath": template["file-path"],
                "content": "ERR: " + start_template_name + " Model Path contains not an List or Dictionary."
            })                    
        return output

    def _render_template_group(self):
        rendered_outputs = []

        for template in self.template_group["templates"] :
            output = []
            print("****************")
            if(not template["is-macro"] and not template["is-base"]):
                output = self._render_template(template["name"])
                rendered_outputs= rendered_outputs+output

        return rendered_outputs

    def render(self) -> List[File]:
        "the render method renders a deployment group"
        result = []
        for elem in self._render_template_group():
            #TODO imlement the file logic
            file = File()
            result.append(file)
        
        return result

    def render_template(self, template_name):
        "the render method renders one template"
        template = self._get_templateByName(template_name)
        if (template):
            return self._render_template(template["name"])
        return {"name": "ERR:"+template_name, "content": "template not found."}

    def list_templates(self):
        "list the templates in the actual jinja environment"
       
        return self.jinja_env.list_templates()

    def str(self):
        return f"""Template Group: {self.template_group['name']}
        Templates: {self.list_templates()}
        """