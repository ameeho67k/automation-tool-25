import json
import os
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "roblox_cookie": "",
    "request_timeout": 10,
    "max_retries": 3,
    "rate_limit_delay": 1.5,
    "webhook_url": "",
    "headless_mode": True,
    "user_agent": "RobloxAutomation/1.0"
}

class ConfigLoader:
    """Handles loading, validating, and saving config settings for Roblox automation."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file and fills missing fields with defaults."""
        config = DEFAULT_CONFIG.copy()
        
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        config.update(file_config)
            except (json.JSONDecodeError, OSError) as e:
                print(f"[Warning] Failed to load {self.config_path}, using defaults: {e}")
        else:
            self.save_config(config)

        return config

    def save_config(self, config_data: Dict[str, Any] = None) -> None:
        """Saves current configuration to a JSON file."""
        data_to_save = config_data if config_data is not None else self.config
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4)
        except OSError as e:
            print(f"[Error] Failed to save configuration: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific configuration option."""
        return self.config.get(key, default)