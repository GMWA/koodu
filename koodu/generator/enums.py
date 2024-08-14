from enum import Enum


class ModelTypeEmum(str, Enum):
    string = "String"
    integer = "Integer"
    float = "Float"
    boolean = "Boolean"
    datetime = "DateTime"
    date = "Date"
    time = "Time"
    ref = "reference"


class KooduTemplate(Enum):
    DJANGO = "django"
    FLASK = "flask"
    FASTAPI = "fastapi"
    EXPRESS = "express"
