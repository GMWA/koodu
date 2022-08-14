import json
from typing import List
from pathlib import Path
from koodu.generator import Generator
from koodu.exceptions import ModelNotFoundException, ModelFileTypeException


def generate(args):
    if not Path(args.output).is_dir():
        raise Exception("The Output should be a Folder!")

    if not Path(Path(args.templates)/Path("config.yaml")).is_file():
        raise Exception("NOT TEMPLATE CONFIG FILE")

    if not Path(args.templates).is_dir():
        raise Exception(f"{args.templates} is not an Existing directory")

    if not args.model.endswith(".json"):
        raise ModelFileTypeException(f"The model should be a json file!")

    if not Path(args.model).is_file():
        raise ModelNotFoundException(f"{args.model} is not an Existing file")

    with open(args.model, "r") as f:
        model = json.load(f)
    
    if model is None:
        raise Exception(f"{args.model} is not a valid file")

    generator = Generator(
        model=model,
        template_folder=Path(args.templates) / Path(args.templates)
    )
    
    for file in generator.render():
        #file.write()
        print(file)

    print("Done", "\U00002705")
    print(f"generated file available at: {args.output}")
    