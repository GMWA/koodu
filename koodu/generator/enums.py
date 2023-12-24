from enum import Enum


class ModelTypeEmum(str, Enum):
    string = "String"
    integer = "Integer"
    bollean = "Boolean"
    date_and_time = "DateTime"
    just_date = "Date"
    ref = "reference"


class KooduTemplate(Enum):
    DJANGO = "django"
    FLASK = "flask"
    FASTAPI = "fastapi"
    EXPRESS = "express"
