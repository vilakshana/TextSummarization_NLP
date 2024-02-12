import os
from box.exceptions import BoxValueError
import yaml
from TextSummarization_NLP.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as f:
            config = yaml.safe_load(f)
            logger.info(f"Yaml file: {path_to_yaml} successfully read")
        return ConfigBox(config)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directory(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"creating directory {path}")


@ensure_annotations
def get_size(path: Path)-> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"