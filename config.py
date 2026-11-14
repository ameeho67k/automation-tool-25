import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_cookie": "",
    "max_retries": 3,
    "headless_mode": True,
    "log_level": "INFO",
    "proxy_url": None
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Config load error: {e}, using defaults")
        
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration to disk."""
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)