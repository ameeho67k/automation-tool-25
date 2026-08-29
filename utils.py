import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "roblox_settings": {
        "username": "default_user",
        "place_id": 123456789,
        "server_join_delay": 5.0,
        "action_delay": 1.5,
        "max_retries": 5,
        "use_proxy": False
    },
    "tool_settings": {
        "log_to_file": True,
        "log_level": "DEBUG",
        "auto_save": True,
        "max_runtime_minutes": 60
    }
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration merging file data with defaults.
    If file does not exist, create it with defaults.
    """
    config = DEFAULT_CONFIG.copy()
    if os.path.isfile(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as config_file:
                user_config = json.load(config_file)
            # Merge user config into defaults, handling nested dicts
            def merge_dicts(base: Dict, update: Dict) -> Dict:
                for key, value in update.items():
                    if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                        base[key] = merge_dicts(base[key], value)
                    else:
                        base[key] = value
                return base
            config = merge_dicts(config, user_config)
        except (json.JSONDecodeError, IOError, OSError) as error:
            print(f"Warning: Could not load {config_path}: {error}")
            print("Using default configuration.")
    else:
        try:
            with open(config_path, "w", encoding="utf-8") as config_file:
                json.dump(DEFAULT_CONFIG, config_file, indent=4)
            print(f"Default configuration created at {config_path}")
        except (IOError, OSError) as error:
            print(f"Warning: Could not create {config_path}: {error}")
    return config

# Additional helper to save config
def save_config(config: Dict[str, Any], config_path: str = "config.json") -> bool:
    """Save the current config to file, overwriting if exists."""
    try:
        with open(config_path, "w", encoding="utf-8") as config_file:
            json.dump(config, config_file, indent=4)
        return True
    except (IOError, OSError) as error:
        print(f"Error saving config: {error}")
        return False

# Example of usage for the automation tool
if __name__ == "__main__":
    # Load the configuration
    current_config = load_config("roblox_config.json")
    print("Loaded Roblox automation config:")
    print(json.dumps(current_config, indent=2))