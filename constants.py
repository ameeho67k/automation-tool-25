import os

# Roblox API and service endpoints
BASE_API_URL = "https://apis.roblox.com"
AUTH_TOKEN_HEADER = "RBX-AUTHENTICATION-TOKEN"

# Configuration for automation cycles
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
POLLING_INTERVAL_SECONDS = 5

# Environment pathing for automation-tool-25
DATA_DIR = os.path.join(os.getcwd(), "data")
LOGS_DIR = os.path.join(os.getcwd(), "logs")
CACHE_DIR = os.path.join(DATA_DIR, "cache")

# File patterns for automation tasks
TARGET_FILE_EXTENSIONS = (".rbxl", ".rbxm")
IGNORE_DIRS = {"__pycache__", ".git", ".venv", "tests"}

# Security and connection constants
USER_AGENT = "RobloxAutomationTool/1.0.0 (Internal Utility)"
SESSION_LIMIT = 5

# Status codes for internal handlers
STATUS_SUCCESS = 0
STATUS_RETRYABLE_ERROR = 1
STATUS_FATAL_ERROR = 2