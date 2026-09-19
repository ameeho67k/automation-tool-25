import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_path": "C:/Program Files (x86)/Roblox/Versions",
    "auto_login": True,
    "retry_limit": 3,
    "headless": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        _save_config(filepath, config)
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def _save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration dictionary to json file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass

if __name__ == "__main__":
    # Example usage for automation-tool-25 initialization
    current_config = load_config()
    print(f"Loaded settings: {current_config}")