import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblosecurity_token": None,
    "auto_reconnect": True,
    "polling_interval": 30,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """
    loads configuration from file with fallback to defaults
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"failed to load config, using defaults: {e}")
    
    return config

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    """
    persists current configuration to file
    """
    try:
        with open(path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"failed to save config: {e}")