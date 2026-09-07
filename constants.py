import os

# Configuration for automation-tool-25
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30
ROBLOX_API_BASE = "https://economy.roblox.com/v1/"

# Path validations
DATA_DIR = os.getenv("ROBLOX_DATA_PATH", "./data")
LOG_FILE = os.path.join(DATA_DIR, "automation.log")

# Error handling status codes
HTTP_RATE_LIMITED = 429
HTTP_UNAUTHORIZED = 401
HTTP_INTERNAL_ERROR = 500

# Default operation timeouts
TASK_SLEEP_INTERVAL = 2.5
CONNECTION_RETRY_DELAY = 5

# Allowed environment identifiers
SUPPORTED_ENVIRONMENTS = {"production", "staging", "development"}

# Validation constraints
MIN_USER_ID = 1
MAX_USER_ID = 999999999

def get_timeout(env: str) -> int:
    """Determines timeout based on environment context."""
    if env == "production":
        return REQUEST_TIMEOUT
    return 10