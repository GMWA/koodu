import unittest
import json

from pathlib import Path
from generator import Generator, File

MODEL_PATH = "../models/test.json"
TEMPLATE_PATH = "../template/tests"


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.output = Path("./output")
        self.template_path = Path(TEMPLATE_PATH)
        self.model = self.load_model(Path(MODEL_PATH))

    def test_init(self):
        # self.assertEqual("foo".upper(), "FOO")
        pass

    def load_model(model_path: Path) -> str:
        with open(MODEL_PATH, "r") as fp:
            model = json.loads(fp.read())
        return model

    def test_genrator_base(self):
        generator = Generator(
            model=self.model,
            template_folder=self.template_path,
            output=self.output
        )
        output = generator.render()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].name, "Test-Template.js")
        self.assertEqual(output[0].content, "import Otto")

    def test_genrator_path(self):
        generator_inst = Generator(
            model=self.model,
            template_folder=self.template_path,
            output=self.output
        )
        output = generator_inst.render()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].name, "Test-Template.js")
        self.assertEqual(output[0].content, "import Otto")

    def test_genrator_path_list(self):
        generator_inst = Generator(
            model=self.model,
            template_folder=self.template_path,
            output=self.output
        )
        output = generator_inst.render()
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0].name, "Test-Template_Otto.js")
        self.assertEqual(output[0].content, "import Otto")
        self.assertEqual(output[1].name, "Test-Template_Karl.js")
        self.assertEqual(output[1].content, "import Karl")

    def test_genrator_no_templates(self):
        error_msg = ""
        try:
            generator = Generator(
                model=self.model,
                template_folder=self.template_path,
                output=self.output
            )
            print(generator)
        except Exception as e:
            error_msg = e.args

        self.assertEqual(error_msg, ("NO_TEMPLATES", "Template Group has no templates attached."))

    def test_genrator_macros(self):
        generator = Generator(
            model=self.model,
            template_folder=self.template_path,
            output=self.output
        )
        output = generator.render()
        self.assertEqual(len(output), 0)

    def test_genrator_datei_name(self):
        pass

    def test_genrator_base_template(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
