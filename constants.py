import os

# Roblox API endpoint configuration
ROBLOX_BASE_URL = "https://apis.roblox.com"
ROBLOX_AUTH_HEADER = "RBX-Authentication-Token"

# Operational thresholds and safety limits
MAX_RETRIES = 3
REQUEST_TIMEOUT = 10.0
RATE_LIMIT_DELAY = 1.5

# Error code mappings for roblox-specific edge cases
ERR_UNAUTHORIZED = 401
ERR_FORBIDDEN = 403
ERR_RATE_LIMITED = 429
ERR_SERVER_ERROR = 500

# Environment setup with fallback validation
def get_api_key():
    """Fetches and validates the required roblox session cookie."""
    api_key = os.getenv("ROBLOX_SESSION_COOKIE")
    if not api_key:
        raise EnvironmentError("missing required environment variable: ROBLOX_SESSION_COOKIE")
    if len(api_key) < 50:
        raise ValueError("invalid roblox cookie format detected")
    return api_key

# Default pathing for automation artifacts
LOG_DIR = "./logs"
DATA_DIR = "./data"

# Configuration settings for robust error handling
RETRY_BACKOFF_FACTOR = 2.0
HTTP_SUCCESS_STATUS = 200