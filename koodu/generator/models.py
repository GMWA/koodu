from typing import List, Optional, Union

from pydantic import BaseModel, ValidationError, field_validator

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

    @field_validator("model", mode='before', check_fields=False)
    def check_required_model(cls, value, values):
        attribute_type = values["type"]
        if attribute_type == ModelTypeEmum.ref and not value:
            raise ValidationError("Model is required when the type is reference")
        return value

    @field_validator("size", mode='before', check_fields=False)
    def check_required_size(cls, value, values):
        attribute_type = values["type"]
        if attribute_type == ModelTypeEmum.string and not value:
            raise ValidationError("Size is required when the type is String")
        return value


class ModelSchema(BaseModel):
    name: str
    attributs: List[AttributSchema]

    @field_validator("attributs", mode='before', check_fields=False)
    def check_reference_size(cls, values):
        models = [x["name"] for x in values]
        for value in values:
            if value["type"] == ModelTypeEmum.ref and value["model"] not in models:
                raise ValueError(f"Ref model '{value['model']}' does not exist")
        return values


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
