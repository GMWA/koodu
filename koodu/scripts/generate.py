import argparse
from re import template
from typing import List
from pathlib import Path
from webbrowser import get
from ..generator import Generator, File

TEMPLATE_FOLDER = Path("../templates")
MODEL_FOLDER = Path("../models")

def get_all_templates(t_dir: Path) -> List[Path]:
    return [f for f in t_dir.glob() if f.is_file()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model", "-m",
        type=str,
        required=True
    )
    parser.add_argument(
        "--template", "-t",
        type=str,
        required=True
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="./",
        required=True
    )

    args = parser.parse_args()

    if not Path(parser.output).is_dir():
        raise Exception("The Output should be a Folder!")

    t_path = TEMPLATE_FOLDER / args.template
    m_path = MODEL_FOLDER / args.model + ".json"

    if not Path(t_path/"config.yaml").is_file():
        raise Exception("NOT TEMPLATE CONFIG FILE")

    if t_path.is_dir():
        raise Exception(f"{t_path} is not an Existing directory")

    if not m_path.is_file():
         raise Exception(f"{m_path} is not an Existing File")

    with open(m_path, "r") as f:
            model = f.read()

    generator = Generator(
        model=model,
        template_folder=t_path
    )

    for a in generator.render():
        print(a)


if __name__ == "__main__":
    main()