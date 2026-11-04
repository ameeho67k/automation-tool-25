import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_account_id": None,
    "target_game_id": 123456789,
    "headless_mode": True,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(filepath):
        save_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            # Merge defaults for missing keys
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a json file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)

# Initialization helper
current_config = load_config()