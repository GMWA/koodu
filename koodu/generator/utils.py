import yaml

from pathlib import Path
from typing import Dict, List


def get_all_files(folder: Path) -> Dict[str, Path]:
    """Iterate over the folder and return all file as Path.

    Args:
        folder (Path): the path to the folder to iterate on.

    Returns:
        (dict): a dict where the key are template's name and the value are template's code
    """
    result = {}
    for fil in folder.glob():
        if fil.is_file():
            result[fil.stem] = fil

    return result

def load_template_config(folder: Path) -> List[Dict[str, str]]:
    """Read the template config file.
    
    Args:
        folder (Path): the path to the folder to iterate on.

    Returns:
        (dict): a dict where the key are template's name and the value are template's code
    """
    configs = None
    config_path = folder / "config.yaml"
    with open(config_path, "r") as fp:
        configs = yaml.load(fp)
    
    return configs