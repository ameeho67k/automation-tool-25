import json
import os
from typing import Any, Dict

# Default configuration tailored for Roblox automation tool
DEFAULT_CONFIG: Dict[str, Any] = {
    "cookie": "",
    "group_id": 0,
    "universe_id": 0,
    "request_timeout": 10.0,
    "max_retries": 3,
    "webhook_url": ""
}

class ConfigLoader:
    """Manages configuration loading from JSON and environment variables."""
    
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration, merging file data and environment variables with defaults."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        # Ensure we only update keys that are valid configurations
                        for key, value in file_data.items():
                            if key in self.config:
                                self.config[key] = value
            except (json.JSONDecodeError, IOError):
                # Gracefully fall back to defaults or env variables if file reading fails
                pass

        # Override config using environment variables (e.g. ROBLOX_COOKIE)
        for key in self.config.keys():
            env_key = f"ROBLOX_{key.upper()}"
            env_val = os.getenv(env_key)
            if env_val is not None:
                default_type = type(DEFAULT_CONFIG[key])
                try:
                    if default_type is bool:
                        self.config[key] = env_val.lower() in ("true", "1", "yes")
                    else:
                        self.config[key] = default_type(env_val)
                except ValueError:
                    pass

        return self.config

    def save(self) -> None:
        """Saves the current configuration back to the file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write configuration file: {e}")
