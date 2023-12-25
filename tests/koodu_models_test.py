import unittest

import pytest
from pydantic import ValidationError

from koodu.generator.models import AttributSchema, ModelSchema


class TestKooduModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_attribut_model(self):
        data = {
            "name": "name",
            "type": "String",
            "size": 255,
            "primary_key": True,
            "index_key": False,
            "unique_key": False,
            "required": True,
            "model": None,
        }
        mod = AttributSchema(**data)
        self.assertTrue(isinstance(mod, AttributSchema))

    def test_undefined_type(self):
        data = {
            "name": "name",
            "type": "non-existing-type",
            "size": 255,
            "primary_key": True,
            "index_key": False,
            "unique_key": False,
            "required": True,
            "model": None,
        }
        with pytest.raises(ValidationError):
            AttributSchema(**data)

    def test_ref_without_model(self):
        data = {
            "name": "name",
            "type": "reference",
            "size": 255,
            "primary_key": True,
            "index_key": False,
            "unique_key": False,
            "required": True,
            "model": None,
        }
        with pytest.raises(ValidationError):
            AttributSchema(**data)

    def test_int_without_size(self):
        data = {
            "name": "name",
            "type": "String",
            "primary_key": True,
            "index_key": False,
            "unique_key": False,
            "required": True,
        }
        with pytest.raises(ValidationError):
            AttributSchema(**data)

    def test_create_model(self):
        model = {
            "name": "Test Model",
            "attributs": [
                {
                    "name": "Model1",
                    "type": "String",
                    "size": 255,
                    "primary_key": True,
                    "index_key": False,
                    "unique_key": False,
                    "required": True,
                    "model": None,
                },
                {
                    "name": "Model2",
                    "type": "reference",
                    "model": "Model1",
                }
            ]
        }
        mod = ModelSchema(**model)
        self.assertTrue(isinstance(mod, ModelSchema))

    def test_create_model_bad_ref(self):
        model = {
            "name": "Test Model",
            "attributs": [
                {
                    "name": "Model1",
                    "type": "String",
                    "size": 255,
                    "primary_key": True,
                    "index_key": False,
                    "unique_key": False,
                    "required": True,
                    "model": None,
                },
                {
                    "name": "Model2",
                    "type": "reference",
                    "model": "BadModel",
                }
            ]
        }
        with pytest.raises(ValidationError):
            ModelSchema(**model)
