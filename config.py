import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cookie": "",
    "place_id": 0,
    "max_retries": 3,
    "request_timeout": 10,
    "rate_limit_delay": 1.5,
    "headless": True,
    "log_level": "INFO",
}


class ConfigLoader:
    """Manages loading and validating configuration settings for Roblox automation."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self._config: Dict[str, Any] = {}

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file, falling back to defaults for missing keys."""
        if not os.path.exists(self.config_path):
            self.save_defaults()
            self._config = DEFAULT_CONFIG.copy()
            return self._config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                if not isinstance(loaded_data, dict):
                    self._config = DEFAULT_CONFIG.copy()
                    return self._config

                # Merge defaults with loaded configuration values
                merged_config = DEFAULT_CONFIG.copy()
                merged_config.update(loaded_data)
                self._config = merged_config
                return self._config
        except (json.JSONDecodeError, OSError):
            self._config = DEFAULT_CONFIG.copy()
            return self._config

    def save_defaults(self) -> None:
        """Writes default configuration to disk if no file exists."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except OSError:
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific configuration value safely."""
        if not self._config:
            self.load_config()
        return self._config.get(key, default)
