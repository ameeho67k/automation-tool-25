import re
from typing import Optional

def validate_roblox_user_id(user_id: str) -> bool:
    """
    Validates that a Roblox User ID is a numeric string of 1-12 digits.

    :param user_id: The string ID to validate.
    :return: True if valid, False otherwise.
    """
    return bool(re.fullmatch(r'\d{1,12}', user_id))

def validate_game_place_id(place_id: int) -> bool:
    """
    Validates that a Roblox Place ID is a positive integer.

    :param place_id: The integer ID to check.
    :return: True if positive, False otherwise.
    """
    return isinstance(place_id, int) and place_id > 0

def sanitize_script_name(name: str) -> Optional[str]:
    """
    Removes illegal characters from a script file name.

    :param name: Raw script name.
    :return: Sanitized string or None if empty.
    """
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '', name)
    return sanitized if sanitized else None

def validate_auth_token(token: str) -> bool:
    """
    Checks format of a ROBLOSECURITY token string.

    :param token: The auth token string.
    :return: True if pattern matches expected cookie format.
    """
    pattern = r'_[A-Fa-f0-9]{128,}'
    return bool(re.match(pattern, token))