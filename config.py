from typing import Dict, Any, Optional
import os

class RobloxConfig:
    """Configuration management for automation-tool-25."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "retry_limit": 3,
            "timeout": 30.0,
            "debug": False
        }

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def load_from_env(self) -> None:
        """Override default settings using environment variables."""
        raw_timeout = os.getenv("ROBLOX_TIMEOUT")
        if raw_timeout:
            self.settings["timeout"] = float(raw_timeout)

CONFIG = RobloxConfig()
