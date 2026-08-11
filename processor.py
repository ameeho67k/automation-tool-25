import json
from typing import Any, Dict


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save data to a JSON file."
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def update_json(file_path: str, updates: Dict[str, Any]) -> None:
    """Update a JSON file with new data."
    data = load_json(file_path)
    data.update(updates)
    save_json(data, file_path)


def clear_json(file_path: str) -> None:
    """Clear all data in a JSON file."
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump({}, file)