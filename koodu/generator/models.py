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

    @model_validator(mode='after')
    def validate(self):
        attribute_type = self.type
        attribute_model = self.model
        attribut__type = self.type
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
        if attribute_type == ModelTypeEmum.string and not attribut__type:
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

    @model_validator(mode='after')
    def validate(self):
        models = [attrib.name for attrib in self.attributs]
        for attr in self.attributs:
            if attr.type == ModelTypeEmum.ref and attr.model not in models:
                raise ValidationError(
                    [
                        {
                            "loc": ["attributs"],
                            "msg": f"Ref model {attr.model} is not a valid model",
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
