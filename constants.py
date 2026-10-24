from typing import Final, Dict, List

# Roblox API endpoints
API_BASE_URL: Final[str] = "https://apis.roblox.com"
AUTH_HEADER: Final[str] = "Roblox-API-Key"

# Tool settings
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Roblox place settings
SUPPORTED_PLATFORMS: List[str] = ["PC", "Mobile", "Console"]

# Error messages for automation workflows
ERROR_MESSAGES: Dict[str, str] = {
    "auth_failed": "Authentication token invalid or expired.",
    "timeout": "Request timed out while connecting to Roblox API.",
    "rate_limited": "Too many requests; backing off."
}

def get_retry_delay(attempt: int) -> float:
    """
    Calculate exponential backoff delay based on attempt number.

    Args:
        attempt: Current retry count index.

    Returns:
        Calculated delay in seconds.
    """
    return float(2 ** attempt)
