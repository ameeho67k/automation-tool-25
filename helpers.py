import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_account_id": 0,
    "api_retries": 3,
    "headless": True,
    "proxy_url": None,
    "workspace_dir": "./workspace"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads user configuration with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        save_config(config, file_path)
        return config

    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass