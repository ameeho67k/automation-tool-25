import json
import os
import time
import random

def get_roblox_auth_header(cookie: str) -> dict:
    """Constructs authorization headers for Roblox API requests."""
    return {"Cookie": f".ROBLOSECURITY={cookie}", "User-Agent": "Roblox/WinInet"}

def simulate_human_delay(min_sec: float = 0.5, max_sec: float = 2.0):
    """Applies random sleep to mimic human interaction patterns."""
    time.sleep(random.uniform(min_sec, max_sec))

def save_to_json(data: dict, filename: str):
    """Utility to persist dictionary data into JSON files."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_config(filepath: str) -> dict:
    """Reads configuration from a specified JSON path."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def validate_roblox_id(asset_id: int) -> bool:
    """Ensures asset IDs are positive integers."""
    return isinstance(asset_id, int) and asset_id > 0