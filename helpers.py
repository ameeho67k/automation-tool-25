import re
import time
from typing import Optional, Dict, Any


def extract_place_id(url_or_id: str) -> Optional[int]:
    """Extracts a Roblox Place ID from a game URL or string representation."""
    if not url_or_id:
        return None
    
    # Direct integer string
    if str(url_or_id).isdigit():
        return int(url_or_id)
    
    # Pattern for standard games URL
    match = re.search(r'roblox\.com/games/(\d+)', str(url_or_id))
    if match:
        return int(match.group(1))
    
    return None


def format_asset_url(asset_id: int) -> str:
    """Constructs the CDN delivery URL for a given asset ID."""
    return f"https://assetdelivery.roblox.com/v1/asset/?id={asset_id}"


def sanitize_cookie(cookie_str: str) -> str:
    """Formats and cleans a .ROBLOSECURITY cookie string."""
    cookie = cookie_str.strip()
    prefix = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-to-your-account-with-it.-ROBLOSECURITY="
    
    if cookie.startswith("_|WARNING:"):
        return cookie
    return f"{prefix}{cookie}"


def calculate_backoff(attempt: int, base_delay: float = 1.0, max_delay: float = 60.0) -> float:
    """Calculates exponential backoff duration for API rate limiting."""
    delay = base_delay * (2 ** (attempt - 1))
    return min(delay, max_delay)
