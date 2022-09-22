import json
from pathlib import Path
from koodu.generator import Generator
from koodu.exceptions import ModelNotFoundException, ModelFileTypeException
from koodu.exceptions import NotFolderException, MissingConfigsException


def generate(args):
    if not Path(args.output).is_dir():
        raise NotFolderException("The Output should be a Folder!")
    
    # check if the input template path is a whole path
    if "/" in args.templates or "\\" in args.templates:
        template_path = Path(args.templates)
    else:

        template_path = Path("./koodu/templates").resolve() / Path(args.templates)

    if not Path(template_path/Path("config.yaml")).is_file():
        raise MissingConfigsException("NOT TEMPLATE CONFIG FILE")

    if not template_path.is_dir():
        raise NotFolderException(f"{args.templates} is not an Existing directory")

    if not args.model.endswith(".json"):
        raise ModelFileTypeException(f"The model should be a json file!")

    if not Path(args.model).is_file():
        raise ModelNotFoundException(f"{args.model} is not an Existing file")

    with open(args.model, "r") as f:
        model = json.load(f)
    
    if model is None:
        raise ModelFileTypeException(f"{args.model} is not a valid file")

    generator = Generator(
        model=model,
        template_folder=template_path,
        output=Path(args.output)
    )
    
    for file in generator.render():
        file.write()

    print("Done", "\U00002705")
    print(f"generated file available at: {args.output}")
    