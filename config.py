import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_user_id": 0,
    "automation_interval": 60,
    "headless_mode": True,
    "proxy_list": []
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from file or returns defaults if file is missing."""
        if not os.path.exists(self.config_path):
            self._save_defaults()
            return DEFAULT_CONFIG

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def _save_defaults(self) -> None:
        """Writes initial configuration file to disk."""
        try:
            with open(self.config_path, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except IOError as e:
            print(f"Critical: Failed to save config: {e}")