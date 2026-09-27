import os
from pathlib import Path

# Base directory for automation-tool-25 workspace
BASE_DIR = Path(__file__).resolve().parent

# Roblox-specific configuration constants
ROBLOX_API_BASE = "https://api.roblox.com"
MAX_RETRIES = 3
TIMEOUT = 30

# Environment setup
SESSION_TOKEN = os.getenv("ROBLOX_SESSION_ID", "anonymous")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

def get_config_dict():
    """Returns current runtime configuration settings."""
    return {
        "base_dir": str(BASE_DIR),
        "api_base": ROBLOX_API_BASE,
        "max_retries": MAX_RETRIES,
        "timeout": TIMEOUT,
        "log_level": LOG_LEVEL
    }

if __name__ == "__main__":
    # Validation of environment paths
    if not BASE_DIR.exists():
        raise FileNotFoundError("Base directory mapping failed")
    print(f"Configuration loaded for session: {SESSION_TOKEN[:5]}***")