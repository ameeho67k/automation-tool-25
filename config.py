import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_account_id": None,
    "target_game_id": 123456789,
    "polling_interval": 5.0,
    "headless_mode": True,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallbacks to defaults."""
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
    """Persists current configuration dictionary to json file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # Example usage for automation tool
    current_cfg = load_config()
    print(f"Loaded configuration: {current_cfg}")