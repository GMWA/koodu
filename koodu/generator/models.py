from typing import List, Optional, Union

from pydantic import BaseModel, model_validator

from koodu.generator.enums import ModelTypeEmum
from koodu.exceptions import ModelValidationError


class AttributSchema(BaseModel):
    name: str
    type: ModelTypeEmum
    size: Optional[int] = None
    primary_key: bool = False
    index_key: bool = False
    unique_key: bool = False
    required: bool = False
    model: Optional[str] = None

    @model_validator(mode='after')
    def validate(self):
        attribute_type = self.type
        attribute_model = self.model
        attribute_size = self.size
        if attribute_type not in [item for item in ModelTypeEmum]:
            raise ModelValidationError("Type is not valid")
        if attribute_type == ModelTypeEmum.ref.value and not attribute_model:
            raise ModelValidationError("Model is required when the type is reference")
        if attribute_type == ModelTypeEmum.string.value and not attribute_size:
            raise ModelValidationError("Size is required when the type is string")
        return self


class ModelSchema(BaseModel):
    name: str
    attributs: List[AttributSchema]

    @model_validator(mode='after')
    def validate(self):
        models = [attrib.name for attrib in self.attributs]
        for attr in self.attributs:
            if attr.type == ModelTypeEmum.ref.value and attr.model not in models:
                raise ModelValidationError("Reference model not found")
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
