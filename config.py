import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cookie": "",
    "place_id": 0,
    "group_id": 0,
    "max_threads": 4,
    "request_timeout": 15,
    "retry_attempts": 3,
    "rate_limit_delay": 1.0,
    "webhook_url": "",
    "debug_mode": False
}

class ConfigManager:
    """Manages loading and merging configuration settings for Roblox automation."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file if it exists and merges with defaults."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"[Warning] Failed to read config file, using defaults: {err}")
        else:
            self.save_default_config()

        # Allow environment overrides for sensitive credentials
        env_cookie = os.getenv("ROBLOSECURITY")
        if env_cookie:
            self.config["cookie"] = env_cookie

        return self.config

    def save_default_config(self) -> None:
        """Saves current configuration to disk as default configuration file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except OSError as err:
            print(f"[Warning] Could not write default config file: {err}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)
