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


# Koodu

Koodu is a simple universal code generator. It allows users to generate codes with the same structure in several projects to save time. Koodu allows users to follow the DRY(Don't Repeat Youself) philosophy, i.e. instead of writing the same code several times, write a template once and use it on several models to generate different code efficiently.

## Installation

### from code source

Clone this repository and run:

```console
$ python -m pip install .
```

### from the index

```console
$ pip install koodu
```

## Usage as CLI

### List the available templates

```console
$ koodu list templates
```

### List the available models

```console
$ koodu list models
```

### generate code using a template and et model

```console
$ koodu generate -t fastapi -m blog -o ./examples/blog
```

The path to template can be replace directly with build in template such as `fastapi` or `flask`


## Usage as python library

Koodu can also be used as python library as follows:

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
