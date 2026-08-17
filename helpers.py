import json
from typing import Any, Dict


def read_json_file(filepath: str) -> Dict[str, Any]:
    """Reads a JSON file and returns its content as a dictionary."""
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Error: The file {filepath} was not found.')
        return {}
    except json.JSONDecodeError:
        print(f'Error: The file {filepath} is not a valid JSON.')
        return {}


def write_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f'Error: An I/O error occurred while writing to {filepath}. {e}')


def update_json_file(filepath: str, new_data: Dict[str, Any]) -> None:
    """Updates a JSON file with new data, merging with existing data."""
    existing_data = read_json_file(filepath)
    existing_data.update(new_data)
    write_json_file(filepath, existing_data)
