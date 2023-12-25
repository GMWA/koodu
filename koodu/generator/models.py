from typing import List, Optional, Union

from pydantic import BaseModel, ValidationError, validator

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

    @validator("model", pre=True, always=True)
    def check_required_model(cls, value, values):
        attribute_type = values.get("type")
        if attribute_type == ModelTypeEmum.ref and not value:
            raise ValidationError("Model is required when the type is reference")
        return value

    @validator("size", pre=True, always=True)
    def check_required_size(cls, value, values):
        attribute_type = values.get("type")
        if attribute_type == ModelTypeEmum.string and not value:
            raise ValidationError("Size is required when the type is String")
        return value


class ModelSchema(BaseModel):
    name: str
    attributs: List[AttributSchema]

    @validator("attributs", pre=True, always=True)
    def check_reference_size(cls, values):
        models = list(map(lambda x: x["name"], values))
        for value in values:
            if value["type"] == ModelTypeEmum.ref and value["model"] not in models:
                raise ValidationError("Ref model does not exist")
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
    models: List[AttributSchema]


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
