from pathlib import Path
from koodu.scripts.utils import get_files_from_folder, check_all_template
from koodu.scripts.utils import convert_symbols

def check_templates(args):
    if not Path(args.templates).is_dir():
        raise Exception(f"{args.templates} is not an Existing directory")

    templates = get_files_from_folder()
    valids = check_all_template(templates)
    symbols = convert_symbols(valids)
    
    for (path, status) in zip(templates, symbols):
        print(path, status)