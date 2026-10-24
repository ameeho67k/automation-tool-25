import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_user_id": 0,
    "automation_interval": 60,
    "headless_mode": True,
    "max_retries": 3
}

class ConfigLoader:
    """Handles loading and merging of automation configurations."""
    
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath

    def load(self) -> Dict[str, Any]:
        config = DEFAULT_CONFIG.copy()
        
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_data = json.load(f)
                    config.update(user_data)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load config, using defaults: {e}")
        else:
            self._save_defaults(config)
            
        return config

    def _save_defaults(self, config: Dict[str, Any]) -> None:
        try:
            with open(self.filepath, "w") as f:
                json.dump(config, f, indent=4)
        except IOError as e:
            print(f"Warning: Could not create default config file: {e}")

if __name__ == "__main__":
    loader = ConfigLoader()
    current_config = loader.load()
    print(f"Active config loaded: {current_config}")