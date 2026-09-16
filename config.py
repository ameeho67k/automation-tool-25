import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "roblox_cookie": "",
    "place_id": 0,
    "universe_id": 0,
    "request_timeout": 15,
    "max_retries": 3,
    "rate_limit_delay": 1.0,
    "discord_webhook_url": "",
    "headless_mode": True,
}

class ConfigManager:
    """Manages application configuration loading with fallback defaults."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or creates default configuration if missing."""
        config = DEFAULT_CONFIG.copy()

        if not self.config_path.exists():
            self.save_config(config)
            return config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update(user_config)
        except (json.JSONDecodeError, OSError) as err:
            print(f"[Warning] Failed to load {self.config_path}: {err}. Using defaults.")

        return config

    def save_config(self, data: Dict[str, Any] = None) -> None:
        """Saves current configuration to file."""
        to_save = data if data is not None else self.config
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(to_save, f, indent=4)
        except OSError as err:
            print(f"[Error] Could not save config file: {err}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)
