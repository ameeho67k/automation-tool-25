import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "roblox_cookie": "",
    "worker_count": 5,
    "retry_limit": 3,
    "timeout_seconds": 30,
    "proxy_enabled": False
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with default settings.
    Returns a dictionary with complete configuration keys.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        # Save defaults if file does not exist
        try:
            with open(config_path, "w") as f:
                json.dump(config, f, indent=4)
        except IOError as e:
            print(f"[Error] Could not initialize config file: {e}")
        return config

    try:
        with open(config_path, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError) as e:
        print(f"[Error] Failed to parse config: {e}. Using defaults.")
        
    return config

if __name__ == "__main__":
    # Example usage for automation-tool-25
    current_config = load_config()
    print(f"Loaded settings with {current_config['worker_count']} workers")