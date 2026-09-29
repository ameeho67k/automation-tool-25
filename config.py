import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_studio_path": "C:\\Program Files (x86)\\Roblox\\Versions",
    "auto_save_interval": 300,
    "debug_mode": False,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file or returns defaults if missing.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Failed to load {filepath}, using defaults.")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Persists current configuration state to disk.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving config: {e}")