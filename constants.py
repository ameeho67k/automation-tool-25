from typing import Final, Dict, List

# Configuration constants for automation-tool-25
# Target endpoints for Roblox web API interactions

ROBLOX_BASE_URL: Final[str] = "https://roblox.com"
API_BASE_URL: Final[str] = "https://apis.roblox.com"

DEFAULT_TIMEOUT: Final[float] = 30.0
RETRY_ATTEMPTS: Final[int] = 3

# Header templates for session authentication
DEFAULT_HEADERS: Final[Dict[str, str]] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RobloxAutomation/1.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Status codes for internal handler state tracking
SUCCESS_CODE: Final[int] = 200
RATE_LIMITED_CODE: Final[int] = 429
UNAUTHORIZED_CODE: Final[int] = 401

# Supported job categories for automation processing
JOB_TYPES: Final[List[str]] = [
    "asset_upload",
    "group_management",
    "inventory_scan",
    "profile_sync"
]

def get_timeout_settings() -> float:
    """Return the default timeout duration for requests."""
    return DEFAULT_TIMEOUT

def get_api_base() -> str:
    """Return the base URL used for Roblox API calls."""
    return API_BASE_URL