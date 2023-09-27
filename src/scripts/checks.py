from typing import Dict
from pathlib import Path
from koodu.scripts.utils import get_files_from_folder, check_all_template
from koodu.scripts.utils import convert_symbols
from koodu.exceptions import BadArgumentsException


def check_templates(args) -> None:
    if not Path(args.templates).is_dir():
        raise Exception(f"{args.templates} is not an Existing directory")

    templates = get_files_from_folder()
    valids = check_all_template(templates)
    symbols = convert_symbols(valids)

    for (path, status) in zip(templates, symbols):
        print(path, status)


def list_command(args) -> Dict[str, str]:
    if args.option == "models" or args.option == "m":
        model_path = Path(Path("./koodu/models").resolve())

        models = [
            elem for elem in model_path.glob("*")
            if str(elem).endswith(".json") or str(elem).endswith(".yaml")
        ]
        for model in models:
            name = model.stem
            print(f"{name}:\t{model}")

    elif args.option == "templates" or args.option == "t":
        template_path = Path("./koodu/templates").resolve()

        templates = [elem for elem in template_path.glob("*") if elem.is_dir()]
        for template in templates:
            name = template.stem
            print(f"{name}:\t{template}")
    else:
        raise BadArgumentsException("the passed arguments do not match the requirements!")
