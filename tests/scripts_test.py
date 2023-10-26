import unittest
from pathlib import Path

from pydantic import BaseModel

from koodu.scripts.checks import list_command


class ListArgsSchema(BaseModel):
    option: str


class TestScripts(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_list_model(self):
        args = ListArgsSchema(**{"option": "templates"})
        model_path = Path(__file__).parent.parent / Path("koodu/templates")
        models = model_path.rglob("**")
        output = list_command(args)
        self.assertEqual(len(output), len(list(models)) - 2)

    def test_list_template(self):
        args = ListArgsSchema(**{"option": "models"})
        template_path = Path(__file__).parent.parent / Path("koodu/models")
        templates = template_path.rglob("*")
        output = list_command(args)
        self.assertEqual(len(output), len(list(templates)))

    def tearDown(self):
        pass
