import os

# Roblox API and Automation Constants
ROBLOX_BASE_URL = "https://roblox.com"
ROBLOX_API_URL = "https://apis.roblox.com"

# Default headers for automation requests
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Retry policy configuration
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2

# File paths and directory constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Roblox-specific status codes
STATUS_SUCCESS = 200
STATUS_UNAUTHORIZED = 401
STATUS_TOO_MANY_REQUESTS = 429

# Performance throttling settings
REQUEST_TIMEOUT_SECONDS = 10
RATE_LIMIT_COOLDOWN = 60