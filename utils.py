import re
from typing import Dict, Any, Optional, Union


def extract_asset_id(url_or_id: Union[str, int]) -> Optional[int]:
    """Extract a Roblox asset or place ID from a URL or raw ID string.

    Args:
        url_or_id: Roblox URL or raw ID string/integer.

    Returns:
        The integer asset ID if valid, or None if extraction fails.
    """
    if isinstance(url_or_id, int):
        return url_or_id if url_or_id > 0 else None

    cleaned = str(url_or_id).strip()
    if cleaned.isdigit():
        return int(cleaned)

    match = re.search(r"/(?:games|catalog|library)/(\d+)", cleaned, re.IGNORECASE)
    if match:
        return int(match.group(1))

    return None


def format_roblox_cookie(cookie_str: str) -> str:
    """Sanitize and format a Roblox security cookie for HTTP headers.

    Args:
        cookie_str: Raw .ROBLOSECURITY cookie value or string.

    Returns:
        Standardized cookie string with valid key-value prefix.
    """
    prefix = ".ROBLOSECURITY="
    token = cookie_str.strip()
    if not token.startswith(prefix):
        return f"{prefix}{token}"
    return token


def extract_csrf_token(headers: Dict[str, Any]) -> Optional[str]:
    """Locate X-CSRF-TOKEN header case-insensitively from HTTP response headers.

    Args:
        headers: Header map returned by network requests.

    Returns:
        The token string if found, otherwise None.
    """
    for key, value in headers.items():
        if key.lower() == "x-csrf-token":
            return str(value)
    return None
