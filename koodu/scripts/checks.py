from cgitb import reset
from typing import Dict
from pathlib import Path
from unittest import result
from koodu.scripts.utils import get_files_from_folder, check_all_template
from koodu.scripts.utils import convert_symbols

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
        model_path = Path(".").parent.absolute() / Path("models/")
        
        models = [elem for elem in model_path.iterdir() if elem.endswith(".json") or elem.endswith(".yaml")]
        print(models)
        print(list(model_path.glob("*")))
        for model in models:
            name = model.split(".")[0]
            print(f"{name}:\t{model}")

    elif args.option == "templates" or args.option == "t":
        template_path = Path(".").parent.absolute() / Path("templates/")
        print(template_path)
        templates = [elem for elem in template_path.iterdir() if elem.is_dir()]
        print(templates)
        print(list(template_path.glob("*")))
        for template in templates:
            name = template.split("/")[-1]
            print(f"{name}:\t{template}")