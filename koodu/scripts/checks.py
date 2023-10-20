from pathlib import Path
from typing import Dict

from koodu.scripts.utils import (
    check_all_template,
    convert_symbols,
    get_files_from_folder,
)


def check_templates(args) -> None:
    if not Path(args.templates).is_dir():
        raise Exception(f"{args.templates} is not an Existing directory")

    templates = get_files_from_folder()
    valids = check_all_template(templates)
    symbols = convert_symbols(valids)
    output = []
    for path, status in zip(templates, symbols):
        output.append(f"{path} {status}")
    return output


def list_command(args) -> Dict[str, str]:
    output = []
    if args.option == "models" or args.option == "m":
        model_path = Path(Path("./koodu/models").resolve())

        models = [
            elem
            for elem in model_path.glob("*")
            if str(elem).endswith(".json") or str(elem).endswith(".yaml")
        ]
        for model in models:
            name = model.stem
            output.append(f"{name}: {model}")

    elif args.option == "templates" or args.option == "t":
        template_path = Path("./koodu/templates").resolve()

        templates = [elem for elem in template_path.glob("*") if elem.is_dir()]
        for template in templates:
            name = template.stem
            output.append(f"{name}: {template}")

    return output
