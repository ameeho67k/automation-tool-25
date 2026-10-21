from typing import Union, Optional

def validate_game_id(game_id: Union[int, str]) -> bool:
    """Checks if the provided game identifier is a valid positive integer."""
    try:
        return int(game_id) > 0
    except (ValueError, TypeError):
        return False

def validate_place_version(version: Optional[int]) -> bool:
    """Ensures place version is either None or a non-negative integer."""
    if version is None:
        return True
    return isinstance(version, int) and version >= 0

def sanitize_username(username: str) -> str:
    """Removes illegal characters from Roblox usernames for API requests."""
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    return "".join(c for c in username if c in allowed_chars)

def check_rate_limit_status(status_code: int) -> bool:
    """Verifies if a specific HTTP status indicates rate limiting."""
    return status_code == 429

def validate_asset_type(asset_type: str) -> bool:
    """Confirms asset type belongs to the permitted Roblox categories."""
    permitted = {"Model", "Decal", "Audio", "MeshPart", "Place"}
    return asset_type in permitted