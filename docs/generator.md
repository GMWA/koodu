# Koodu Generator

The generator is the core of koodu. It generates code from a template(or a list of template) and a model model.

The template provides the structure for the code to be generated, i.e. the different files (their path and contents) in the files to be generated.

The model defines the data that the templates will use to generate these files.

The generator can be used both as a python module and as a cli tools.

## Generator as python module

To use the generator as python module users can just import the module ans use the deffirent provided method. following is ans example.

```python
import json
from pathlib import Path
from koodu.generator import Generator

with open(Path("./koodu/models/blog.json"), "r", encoding="utf-8") as fp:
    model = json.loads(fp.read())

template_path = Path("./koodu/templates/fastapi")
output_path = Path("./examples/blog")
generator = Generator(
    model=model,
    template_folder=template_path,
    output=Path(args.output)
)

for file in generator.render():
    file.write()
```

## Generator as cli tool

This is the method we recommend for using koodu because it's quick and efficient. Once koodu is installed, all you have to do is use the koodu command with its various options. The current version of koodu has two main options `generate` and `list`:

### koodu generate

This option is used to generate the code. it requires the following:parameters:

* -t path to template
* -m path to model
* -o output path

```sh
$ koodu list models
```

### koodu list

This option can be used to list the available templates or module.

### **List the available templates**

```sh
$ koodu list templates
```

### **List the available models**

```sh
$ koodu list models
```

### **List the available models**

```sh
$ koodu check models
```
