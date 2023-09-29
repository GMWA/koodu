<p align="center">
  <a href="https://kuudo.net"><img src="https://github.com/GMWA/koodu/blob/main/docs/assets/images/koodu.png" alt="Koodu"></a>
</p>
<p align="center">
    <em>Koodu, simple code generator engine written in python</em>
</p>


# Koodu

It is a simple universal code generator. Koodu allows the user to generate codes with the same structure in several projects to save time. Koodu allows you to follow the DRY(Don't Repeat Youself) philosophy, i.e. instead of writing the same code several times, write a template once and use it on several models to generate different code efficiently.

## Installation
Clone this repository and run:
```
python -m pip install .
```

## Usage as CLI

### List the available templates
```
koodu list templates
```

### List the available models
```
koodu list models
```

### generate code using a template and et model
```
koodu generate
> -t path-to-template
> -m path-to-model
> -o output-path
```
The path to temple can be replace directly with build in template such as `frontend` or `backend`


## Usage as python library

Koodu can also be used as python library as follows:
```python
import json
from pathlib import Path
from koodu.generator import Generator

with open(Path("path-to-model"), "r", encoding="utf-8") as fp:
    model = json.loads(fp.read())

template_path = Path("path-to-template")
output_path = Path("output-path")
generator = Generator(
    model=model,
    template_folder=template_path,
    output=Path(args.output)
)

for file in generator.render():
    file.write()
```

## How to contritube
