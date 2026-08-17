import json
from datetime import datetime


def read_json_file(file_path):
    """Reads a JSON file and returns the data as a dictionary."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error reading {file_path}: {e}')
        return None


def write_json_file(file_path, data):
    """Writes a dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f'Error writing to {file_path}: {e}')


def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.now().isoformat()


def filter_data_by_key(data, key):
    """Filters a list of dictionaries based on a provided key."""
    if not isinstance(data, list):
        return []
    return [item for item in data if key in item]


def transform_data(data, transform_func):
    """Applies a transformation function to each item in a list."""
    if not isinstance(data, list):
        return []
    return [transform_func(item) for item in data]
