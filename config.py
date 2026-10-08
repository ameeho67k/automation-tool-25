import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblosecurity_token": "",
    "target_game_id": 123456789,
    "retry_delay": 5.0,
    "headless_mode": True,
    "proxy_url": None
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with default values.
    """
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        save_config(config, filepath)
        return config

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Persists the current configuration dictionary to disk.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")