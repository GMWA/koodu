from typing import List
from pathlib import Path
from koodu.generator import Generator, File

TEMPLATE_FOLDER = Path("../templates")
MODEL_FOLDER = Path("../models")

def get_all_templates(t_dir: Path) -> List[Path]:
    return [f for f in t_dir.glob() if f.is_file()]


def generate(args):
    if not Path(args.output).is_dir():
        raise Exception("The Output should be a Folder!")

    if not Path(args.templates/"config.yaml").is_file():
        raise Exception("NOT TEMPLATE CONFIG FILE")

    if not Path(args.templates).is_dir():
        raise Exception(f"{args.templates} is not an Existing directory")

    if not args.model.endswith(".json"):
        raise Exception(f"The model should be a json file!")

    if not Path(args.model).is_file():
        raise Exception(f"{args.model} is not an Existing file")

    with open(args.model, "r") as f:
        model = f.read()
    
    if model is None:
        raise Exception(f"{args.model} is not a valid file")

    generator = Generator(
        model=model,
        template_folder=args.templates
    )
    
    for file in generator.render():
        file.write()

    print("Done", "\U00002705")
    print(f"generated file available at: {args.output}")
    