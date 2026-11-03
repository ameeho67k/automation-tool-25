import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "roblox_cookie": "",
    "max_retries": 3,
    "proxy_url": None,
    "log_level": "INFO",
    "auto_reconnect": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        save_config(config_path, config)
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config_path: str, config: Dict[str, Any]) -> None:
    """Persists current configuration state to disk."""
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)