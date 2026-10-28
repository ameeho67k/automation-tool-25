import os

# Roblox API configuration
BASE_URL = "https://apis.roblox.com"
API_KEY_HEADER = "X-API-KEY"

# Retry configuration for stability
MAX_RETRIES = 3
RETRY_DELAY = 2.0

# Directory and file paths for automation
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Default request timeout in seconds
REQUEST_TIMEOUT = 30

# User agent for identification
USER_AGENT = "RobloxAutomationTool/2.5.0"

# Supported job categories
JOB_TYPES = {
    "ASSET_UPLOAD": "asset_upload",
    "GROUP_MANAGER": "group_manager",
    "PLAYER_ANALYTICS": "player_analytics"
}

# Status codes for internal processes
STATUS_SUCCESS = 0
STATUS_RETRY = 1
STATUS_FATAL = 2