import re
from typing import Dict, Optional, Any


def extract_csrf_token(response_headers: Dict[str, str]) -> Optional[str]:
    """Extract X-CSRF-TOKEN from Roblox API response headers."""
    for key, value in response_headers.items():
        if key.lower() == "x-csrf-token":
            return value
    return None


def sanitize_cookie(cookie: str) -> str:
    """Clean and format standard Roblox security cookie string."""
    cleaned = cookie.strip()
    if cleaned.startswith(".ROBLOSECURITY="):
        cleaned = cleaned[15:]
    return cleaned.strip('"\'')


def get_default_headers(cookie: str, csrf_token: Optional[str] = None) -> Dict[str, str]:
    """Generate standard request headers required for Roblox endpoints."""
    clean_cookie = sanitize_cookie(cookie)
    headers = {
        "User-Agent": "RobloxAutomationTool/1.0",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": f".ROBLOSECURITY={clean_cookie}",
    }
    if csrf_token:
        headers["X-CSRF-TOKEN"] = csrf_token
    return headers


def parse_place_id(url_or_id: Any) -> Optional[int]:
    """Extract a numeric Place ID from a Roblox game URL or raw ID input."""
    if isinstance(url_or_id, int):
        return url_or_id if url_or_id > 0 else None
    
    val_str = str(url_or_id).strip()
    if val_str.isdigit():
        return int(val_str)
    
    match = re.search(r"games/(\d+)", val_str)
    if match:
        return int(match.group(1))
    
    return None
