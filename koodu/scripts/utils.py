from pathlib import Path
from typing import List

from jinja2 import Environment
from jinja2.exceptions import TemplateSyntaxError


def get_files_from_folder(folder: Path = Path(__file__)) -> List[Path]:
    """Recusively get all template in a Folder
    Args:
        folder (Path): The path to the folder.

    Return: The list of all template Path.
    """
    return [path for path in folder.rglob("**/*") if "jinja" in path]


def check_all_template(templates: List[Path]) -> List[bool]:
    """Check if all template in a list are valid jinja Template.

    Args:
        templates (List(Path)): the liste of template

    Returns:
        result (List(bool)): the list that content boolen representing
                             if each template in the list is valid or not.
    """
    result = []
    env = Environment()

    for path in templates:
        try:
            with open(path, "r") as fp:
                template = fp.read()

            env.parse(template)

            result.append(True)
        except TemplateSyntaxError:
            result.append(False)

    return result


def convert_symbols(symbols: List[bool]) -> List[str]:
    """Convert a list if bolean to a list of emoji.

    Args:
        symbols (List(bool)): the list of symbols

    Returns:
        emojis (List(str)): the list of corresponding emoji.
    """
    emojis = []
    for sym in symbols:
        if sym:
            emojis.append("\U00002705")
        else:
            emojis.append("\U0000274C")

    return emojis
