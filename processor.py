import json
import os
from typing import Any, Dict

DEFAULTS = {
    "roblox_api_key": "",
    "target_game": "",
    "delay_seconds": 1.0,
    "retry_count": 3,
    "headless_mode": True,
    "log_to_file": False,
    "max_runtime_minutes": 60
}

def load_configuration(config_path: str = "config.json") -> Dict[str, Any]:
    """Load config from JSON file with defaults fallback."""
    config = DEFAULTS.copy()
    
    if os.path.isfile(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as file:
                loaded = json.load(file)
            for key in DEFAULTS:
                if key in loaded:
                    config[key] = loaded[key]
        except (json.JSONDecodeError, IOError) as error:
            print(f"Config load error: {error}. Using defaults.")
    
    return config

def apply_defaults(user_config: Dict[str, Any]) -> Dict[str, Any]:
    """Merge user config with defaults."""
    result = DEFAULTS.copy()
    result.update({k: v for k, v in user_config.items() if k in DEFAULTS})
    return result

def process_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Main entry to load and process config with defaults."""
    raw_config = load_configuration(config_path)
    return apply_defaults(raw_config)

if __name__ == "__main__":
    config = process_config()
    print("Processed config keys:", list(config.keys()))
    print("Sample delay:", config["delay_seconds"])