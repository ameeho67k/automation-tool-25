import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_studio_path": "C:/Program Files (x86)/Roblox/Versions/",
    "auto_save_interval": 300,
    "debug_mode": False,
    "api_retries": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(config_path):
        save_config(DEFAULT_CONFIG, config_path)
        return DEFAULT_CONFIG

    try:
        with open(config_path, "r") as f:
            data = json.load(f)
            # Merge with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists current configuration to a JSON file."""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

if __name__ == "__main__":
    config = load_config()
    print(f"Loaded config: {config}")