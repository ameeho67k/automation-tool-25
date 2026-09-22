import re
from typing import Dict, Optional

ROBLOX_BASE_URL = "https://www.roblox.com"
USERS_API_URL = "https://users.roblox.com"
GAMES_API_URL = "https://games.roblox.com"


def build_roblox_headers(cookie: Optional[str] = None, csrf_token: Optional[str] = None) -> Dict[str, str]:
    """Construct standard HTTP headers required for Roblox web requests."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
    }
    if cookie:
        headers["Cookie"] = f".ROBLOSECURITY={cookie}"
    if csrf_token:
        headers["X-CSRF-TOKEN"] = csrf_token
    return headers


def parse_place_id(input_str: str) -> Optional[int]:
    """Extract a numeric Roblox place ID from a raw ID or game URL."""
    input_str = input_str.strip()
    if input_str.isdigit():
        return int(input_str)
    
    match = re.search(r"games/(\d+)", input_str)
    if match:
        return int(match.group(1))
    return None


def format_user_profile_url(user_id: int) -> str:
    """Generate standard web profile URL for a given user ID."""
    return f"{ROBLOX_BASE_URL}/users/{user_id}/profile"


def extract_csrf_token(response_headers: Dict[str, str]) -> Optional[str]:
    """Case-insensitive extraction of X-CSRF-TOKEN from response headers."""
    for key, value in response_headers.items():
        if key.lower() == "x-csrf-token":
            return value
    return None


def build_endpoint(service: str, path: str) -> str:
    """Build clean request endpoint for Roblox microservices."""
    subdomains = {
        "users": USERS_API_URL,
        "games": GAMES_API_URL,
    }
    base_url = subdomains.get(service.lower(), ROBLOX_BASE_URL)
    return f"{base_url}/{path.lstrip('/')}"
