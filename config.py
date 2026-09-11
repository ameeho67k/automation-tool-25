import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "roblox_api_key": "",
    "target_game_id": 0,
    "polling_interval": 30,
    "log_level": "INFO"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        """Loads configuration from disk or creates default if missing."""
        if not os.path.exists(self.config_path):
            self._save_defaults()
            return

        try:
            with open(self.config_path, "r") as f:
                loaded_data = json.load(f)
                self.config.update(loaded_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Config load error: {e}, using defaults")

    def _save_defaults(self) -> None:
        """Writes initial configuration file."""
        try:
            with open(self.config_path, "w") as f:
                json.dump(self.config, f, indent=4)
        except IOError as e:
            print(f"Failed to write default config: {e}")

    def get(self, key: str) -> Any:
        return self.config.get(key, DEFAULT_CONFIG.get(key))