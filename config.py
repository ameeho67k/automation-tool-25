import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "robux_threshold": 100,
    "auto_retry": True,
    "log_level": "INFO",
    "target_game_id": None
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from json file, merging with defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
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
    Persists current configuration to disk.
    """
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)