import json
import unittest
from pathlib import Path

from koodu.generator import Generator

MODEL_PATH = "tests/models/test.json"
TEMPLATE_PATH = "koodu/templates/tests"


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.output = Path("output").resolve()
        self.template_path = Path(TEMPLATE_PATH).resolve()
        self.model = self.load_model(Path(MODEL_PATH).resolve())

    def test_init(self):
        pass

    def load_model(self, model_path: Path) -> str:
        with open(model_path, "r") as fp:
            model = json.loads(fp.read())
        return model

    def test_genrator_base(self):
        generator = Generator(
            model=self.model, template_folder=self.template_path, output=self.output
        )
        output = generator.render()
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0].name, "test-path.js")
        self.assertEqual(output[0].is_binary, False)
        self.assertEqual(output[0].content, "import Test")

    def test_genrator_path(self):
        generator_inst = Generator(
            model=self.model, template_folder=self.template_path, output=self.output
        )
        output = generator_inst.render()
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0].name, "test-path.js")
        self.assertEqual(output[0].content, "import Test")

    def test_genrator_path_list(self):
        generator_inst = Generator(
            model=self.model, template_folder=self.template_path, output=self.output
        )
        output = generator_inst.render()
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0].name, "test-path.js")
        self.assertEqual(output[0].content, "import Test")
        self.assertEqual(output[1].name, "test-generator.js")
        self.assertEqual(output[1].content, "import Test")

    def test_genrator_no_templates(self):
        error_msg = ""
        try:
            generator = Generator(
                model=self.model, template_folder=self.template_path, output=self.output
            )
            print(generator)
        except Exception as e:
            error_msg = e.args

        self.assertEqual(error_msg, "")

    def test_genrator_macros(self):
        generator = Generator(
            model=self.model, template_folder=self.template_path, output=self.output
        )
        output = generator.render()
        self.assertEqual(len(output), 3)

    def test_genrator_file_name(self):
        pass

    def test_genrator_base_template(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
