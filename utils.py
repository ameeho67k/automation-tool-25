import re
from typing import Dict, Any, Optional


def extract_asset_id(url_or_string: str) -> Optional[int]:
    """
    Extracts a Roblox asset or place ID from a given URL or raw string.

    Args:
        url_or_string: The string containing the Roblox asset reference.

    Returns:
        The extracted integer ID if found, otherwise None.
    """
    match = re.search(r'(?:catalog|library|games)/(\d+)', url_or_string)
    if match:
        return int(match.group(1))
    
    digits_match = re.search(r'^\d+$', url_or_string.strip())
    if digits_match:
        return int(digits_match.group(0))
        
    return None


def format_cookie(raw_cookie: str) -> str:
    """
    Ensures a Roblox security cookie is properly formatted.

    Args:
        raw_cookie: The raw .ROBLOSECURITY string or value.

    Returns:
        A clean, formatted cookie string with the warning prefix.
    """
    cleaned = raw_cookie.strip()
    prefix = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-to-your-account-and-steal-your-ROBUX-and-items.|_"
    if not cleaned.startswith("_|WARNING"):
        return f"{prefix}{cleaned}"
    return cleaned


def parse_place_launch_args(place_id: int, job_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Generates standard protocol parameters for launching a Roblox place.

    Args:
        place_id: The ID of the Roblox place to join.
        job_id: Optional server instance job ID.

    Returns:
        Dictionary containing formatted protocol parameters.
    """
    params: Dict[str, Any] = {
        "place_id": place_id,
        "launch_time": 0,
        "protocol": "roblox-player"
    }
    if job_id:
        params["game_instance_id"] = job_id
        
    return params
