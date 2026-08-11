import json
from typing import Any, Dict, List, Union

def read_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """
    Read a JSON file and return its content.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: Union[Dict[str, Any], List[Any]]) -> None:
    """
    Write data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flatten a nested dictionary.
    """
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def is_empty(value: Any) -> bool:
    """
    Check if a value is empty.
    """
    if isinstance(value, (list, dict, str)):
        return len(value) == 0
    return value is None


def generate_unique_id(prefix: str = '') -> str:
    """
    Generate a unique identifier string.
    """
    import uuid
    return f'{prefix}{uuid.uuid4()}'
