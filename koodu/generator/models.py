from typing import List, Optional, Union

from pydantic import BaseModel, ValidationError, model_validator

from koodu.generator.enums import ModelTypeEmum


class AttributSchema(BaseModel):
    name: str
    type: ModelTypeEmum
    size: Optional[int] = None
    primary_key: bool = False
    index_key: bool = False
    unique_key: bool = False
    required: bool = False
    model: str = None

    @model_validator(mode='before')
    def validate(self):
        attribute_type = self.get('type', '')
        attribute_model = self.get('model', None)
        attribute_size = self.get('size', '')
        if attribute_type not in ModelTypeEmum:
            raise ValidationError(
                [
                    {
                        "loc": ["model"],
                        "msg": "Type is not valid",
                        "type": "value_error",
                    }
                ],
                self,
            )
        if attribute_type == ModelTypeEmum.ref and not attribute_model:
            raise ValidationError(
                [
                    {
                        "loc": ["model"],
                        "msg": "Model is required when the type is reference",
                        "type": "value_error",
                    }
                ],
                self,
            )
        if attribute_type == ModelTypeEmum.string and not attribute_size:
            raise ValidationError(
                [
                    {
                        "loc": ["model"],
                        "msg": "Size is required when the type is String",
                        "type": "value_error",
                    }
                ],
                self,
            )
        return self


class ModelSchema(BaseModel):
    name: str
    attributs: List[AttributSchema]

    @model_validator(mode='before')
    def validate(self):
        models = [attrib.get("name", "") for attrib in self.get('attributs', [])]
        for attr in self.get('attributs', []):
            if attr.get("type", "") == ModelTypeEmum.ref and attr.get('model', '') not in models:
                raise ValidationError(
                    [
                        {
                            "loc": ["attributs"],
                            "msg": f"Ref model {attr.get('model', '')} is not a valid model",
                            "type": "value_error",
                        }
                    ],
                    self,
                )
        return self


class TemplateSchema(BaseModel):
    template_code: str
    name: str
    path: str
    file_name: str
    type: Union[str, None] = None
    file_path: str


class GeneratorModelSchema(BaseModel):
    name: str
    models: List[ModelSchema]


class TemplateConfigSchema(BaseModel):
    template_path: str
    file_path: Union[str, None] = None
    path: Union[str, None] = None
    name: str
    file_name: Union[str, None] = None
    type: Union[str, None] = None
    is_base: Union[bool, None] = False
    is_macro: Union[bool, None] = False


class ConfigSchema(BaseModel):
    name: Union[str, None] = None
    templates: List[Union[TemplateConfigSchema, None]] = None
