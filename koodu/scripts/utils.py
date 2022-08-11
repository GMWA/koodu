from pathlib import Path
from typing import List
from jinja2 import Environment
from jinja2.exceptions import TemplateSyntaxError


def get_files_from_folder(folder: Path = Path("./")) ->List[Path]:
    """Recusively get all template in a Folder
    Args:
        folder (Path): The path to the folder.

    Return: The list of all template Path.
    """
    return [path for path in folder.rglob("*") if "jinja" in path]


def check_all_template(templates: List[Path]) -> List[bool]:
    result = []
    env = Environment()

    for path in templates:
        try:
            with open(path, "r") as fp:
                template= fp.read()
            
            env.parse(template)
            
            result.append(True)
        except TemplateSyntaxError:
            result.append(False)

    return result


def convert_symbols(result: List[bool]) -> List[str]:
    emojis = []
    for res in result:
        if res:
            emojis.append("\U00002705")
        else:
            emojis.append("\U0000274C")
    
    return emojis