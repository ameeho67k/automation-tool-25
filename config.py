import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "roblox_cookie": "",
    "place_id": 0,
    "request_delay": 1.5,
    "max_retries": 3,
    "timeout": 10,
    "headless": True,
    "user_agent": "Roblox/WinInet",
    "webhook_url": ""
}


class ConfigLoader:
    """Loads and merges configuration settings for Roblox automation."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from JSON file and environment variables."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load {self.config_path}: {err}")

        # Override with environment variables if present
        env_cookie = os.getenv("ROBLOX_COOKIE")
        if env_cookie:
            self._config["roblox_cookie"] = env_cookie

        env_place_id = os.getenv("ROBLOX_PLACE_ID")
        if env_place_id and env_place_id.isdigit():
            self._config["place_id"] = int(env_place_id)

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._config.get(key, default)
