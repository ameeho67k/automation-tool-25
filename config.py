import os
from typing import Dict, Any

# Roblox automation environment configuration

class Config:
    DEFAULT_SETTINGS: Dict[str, Any] = {
        "roblox_path": os.getenv("ROBLOX_PATH", "C:/Program Files (x86)/Roblox/Versions"),
        "auth_token": os.getenv("ROBLOX_TOKEN", ""),
        "retry_limit": 3,
        "timeout": 30,
        "headless": False
    }

    @classmethod
    def get(cls, key: str) -> Any:
        return cls.DEFAULT_SETTINGS.get(key)

    @classmethod
    def update(cls, key: str, value: Any) -> None:
        cls.DEFAULT_SETTINGS[key] = value

def load_environment() -> None:
    """Initializes environment variables for automation tool"""
    required_vars = ["ROBLOX_TOKEN"]
    for var in required_vars:
        if not os.getenv(var):
            print(f"Warning: {var} is not set")

if __name__ == "__main__":
    load_environment()