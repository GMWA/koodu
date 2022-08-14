import unittest

from generator import Generator, File


class TestGenerator(unittest.TestCase):
    def setUp(self):
        # read test model
        pass

    def test_init(self):
        #self.assertEqual("foo".upper(), "FOO")
        pass


    def test_genrator_base(self):
        model = {"name" : "Otto"}
        template_group = {
            "name": "testGroup",
            "templates": [{
                "name": "Test-Template",
                "path": "",
                "templateType": "js",
                "templateCode": "import {{model.name}}",
                "isMacro": False
            }]
        }

        generator_inst = Generator(model=model, template_group=template_group)
        output = generator_inst.render()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].name, "Test-Template.js")
        self.assertEqual(output[0].content, "import Otto")

    
    def test_genrator_path(self):
        model = {"entity": {"name" : "Otto"}}
        template_group = {
            "name": "testGroup",
            "templates": [{
                "name": "Test-Template",
                "path": "/entity",
                "templateType": "js",
                "templateCode": "import {{model.name}}",
                "isMacro": False
            }]
        }

        generator_inst = Generator(model=model, template_group=template_group)
        output = generator_inst.render()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].name, "Test-Template.js")
        self.assertEqual(output[0].content, "import Otto")

    def test_genrator_path_list(self):
        model = {"entities": [{"name" : "Otto"}, {"name": "Karl"}]}
        template_group = {
            "name": "testGroup",
            "templates": [{
                "name": "Test-Template",
                "path": "entities",
                "templateType": "js",
                "templateCode": "import {{model.name}}",
                "isMacro": False
            }]
        }

        generator_inst = Generator(model=model, template_group=template_group)
        output = generator_inst.render()
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0].name, "Test-Template_Otto.js")
        self.assertEqual(output[0].content, "import Otto")
        self.assertEqual(output[1].name, "Test-Template_Karl.js")
        self.assertEqual(output[1].content, "import Karl")

    def test_genrator_no_templates(self):
        model = {"entities": [{"name" : "Otto"}, {"name": "Karl"}]}
        template_group = {
            "name": "testGroup",
            "templates": []
        }
        error_msg = ""
        try:
            generator_inst = Generator(model=model, template_group=template_group)
        except Exception as e:
            error_msg= e.args
           
        self.assertEqual(error_msg, ("NO_TEMPLATES", "Template Group has no templates attached."))


    def test_genrator_macros(self):
        model = {"entities": [{"name" : "Otto"}, {"name": "Karl"}]}
        template_group = {
            "name": "testGroup",
            "templates": [{
                "name": "Test-Template",
                "path": "entities",
                "templateType": "js",
                "templateCode": "import {{model.name}}",
                "isMacro": True
            }]
        }

        generator_inst = Generator(model=model, template_group=template_group)
        output = generator_inst.render()
        self.assertEqual(len(output), 0)

    def test_genrator_datei_name(self):
        pass

    def test_genrator_base_template(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
