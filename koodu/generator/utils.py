from pathlib import Path
from typing import Dict, List, Union

import yaml
from pydantic import BaseModel


class TemplateConfigSchema(BaseModel):
    template_path: str
    file_path: Union[str, None] = None
    path: Union[str, None] = None
    name: str
    file_name: Union[str, None] = None
    type: Union[str, None] = None
    is_base: Union[bool, None] = False
    is_macro: Union[bool, None] = False


class ConfigSchema(BaseModel):
    name: Union[str, None] = None
    templates: List[Union[TemplateConfigSchema, None]] = None


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


def load_template_config(folder: Path) -> ConfigSchema:
    """Read the template config file.

    Args:
        folder (Path): the path to the folder to iterate on.

    Returns:
        (dict): a dict where the key are template's name and the value are template's code
    """
    configs = None
    config_path = folder / Path("config.yaml")
    with open(config_path, "r") as fp:
        configs = yaml.load(fp, Loader=yaml.FullLoader)

    return ConfigSchema(**configs)
