import json
from typing import Any, Dict


def read_json_file(file_path: str) -> Dict[str, Any]:
    """Reads a JSON file and returns its content as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries into one, with dict2 values overriding dict1."""
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def validate_key_exists(dictionary: Dict[str, Any], key: str) -> bool:
    """Checks if a key exists in a dictionary."""
    return key in dictionary


def format_string(template: str, **kwargs: Any) -> str:
    """Formats a string using placeholders with keyword arguments."""
    return template.format(**kwargs)