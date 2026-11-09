import re
import random
from typing import Dict, Optional


def extract_csrf_token(headers: Dict[str, str]) -> Optional[str]:
    """Extract x-csrf-token from response headers (case-insensitive)."""
    for key, value in headers.items():
        if key.lower() == "x-csrf-token":
            return value
    return None


def format_asset_url(asset_id: int) -> str:
    """Construct standard Roblox asset delivery URL."""
    if not isinstance(asset_id, int) or asset_id <= 0:
        raise ValueError("Asset ID must be a positive integer.")
    return f"https://assetdelivery.roblox.com/v1/asset/?id={asset_id}"


def calculate_backoff(attempt: int, base_delay: float = 1.0, max_delay: float = 60.0) -> float:
    """Calculate exponential backoff delay with full jitter for rate limits."""
    temp = min(max_delay, base_delay * (2 ** attempt))
    return random.uniform(0, temp)


def sanitize_cookie(raw_cookie: str) -> str:
    """Clean and validate Roblox security cookie string."""
    cleaned = raw_cookie.strip()
    prefix = "_|WARNING:-DO-NOT-SHARE-THIS."
    if not cleaned.startswith(prefix):
        if len(cleaned) > 100:
            return f"{prefix}--Sharing-this-will-allow-someone-to-log-into-your-account-with-all-your-ROBUX-and-items.|_{cleaned}"
        raise ValueError("Invalid Roblox security cookie format.")
    return cleaned


def parse_place_id(url: str) -> Optional[int]:
    """Extract place ID from standard Roblox game URLs."""
    match = re.search(r"roblox\.com/games/(\d+)", url)
    if match:
        return int(match.group(1))
    return None
