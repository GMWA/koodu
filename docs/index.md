<p align="center">
  <a href="https://gmwa.github.io/koodu/"><img src="https://github.com/GMWA/koodu/blob/main/docs/assets/images/koodu.png" alt="Koodu"></a>
</p>
<p align="center">
    <em>Koodu, simple code generator engine written in python.</em>
</p>


<p align="center">
    <a href="https://pypi.org/project/koodu" target="_blank">
        <img src="https://img.shields.io/pypi/v/koodu?color=%2334D058&label=version" alt="Package version">
    </a>
    <a href="https://pypi.org/project/koodu" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/koodu.svg?color=%2334D058" alt="Supported Python versions">
    </a>
    <a href="https://pypi.org/project/koodu" target="_blank">
        <img src="https://img.shields.io/pypi/dm/koodu?color=%2334D058&label=downloads" alt="PyPI - Downloads">
    </a>
    <a href="https://pypi.org/project/koodu" target="_blank">
        <img src="https://img.shields.io/pypi/l/koodu?color=%2334D058&label=licence" alt="PyPI - License">
    </a>
</p>

---

**Documentation**: <a href="https://gmwa.github.io/koodu/" target="_blank">https://gmwa.github.io/koodu/</a>

**Source Code**: <a href="https://github.com/GMWA/koodu" target="_blank">https://github.com/GMWA/koodu</a>

---

Koodu is simple and lightweight code generator engine written in python.

## Goal

Koodu allows you to quickly generate project or file boilerplates, enabling developers to save time by focusing on the most complex features of their software.

## Principe

Write a template once and use it as many times as possible to generate code based on a model.

## Installation

### Requirements

* Python     >= 3.8
* pyyaml     >= 6.0.1
* jinja2     >= 3.1.2
* Pydantic   >= 1.10.9

The installation can be done using both `pip` and also using `the source code`.

### Installation with pip

```sh
$ pip install koodu
```

### Installation with the source code

```sh
$ git clone https://gmwa.github.io/koodu
$ cd koodu
$ pip install -e
```



## Examples
### using as CLI tool
generate code using a template and et model

```sh
$ koodu generate -t fastapi -m koodu/models/blog.json -o ./examples/blog
```

### using as Python package
koodu can be used as python library as follows:

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

### Notes

* The examples above use the template provided by koodu for generating backend applications with the FastAPI framework. The applications generated using this template are functional and have endpoints to enable users to create, modify and delete resources.

* koodu also comes with other templates for generating applications based on other frameworks such as Django, Flask or ExpressJS. You can also use it with your own templates by providing their path.

### Convention for koodu templating.
