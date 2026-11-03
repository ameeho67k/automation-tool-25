from typing import Union, Optional

def validate_game_id(game_id: Union[int, str]) -> bool:
    """
    Validates that the provided Roblox game ID is a positive integer.

    :param game_id: The ID of the Roblox place or universe.
    :return: True if valid, False otherwise.
    """
    try:
        return int(game_id) > 0
    except (ValueError, TypeError):
        return False

def validate_cookie(cookie: str) -> bool:
    """
    Checks if the Roblox security cookie follows the expected format.

    :param cookie: The .ROBLOSECURITY string.
    :return: Boolean status of cookie structural integrity.
    """
    if not isinstance(cookie, str) or len(cookie) < 500:
        return False
    return cookie.startswith('_|WARNING:-DO-NOT-SHARE-THIS')

def sanitize_username(username: str) -> Optional[str]:
    """
    Cleans user input to ensure it meets Roblox username requirements.

    :param username: The raw username string.
    :return: Sanitized string or None if invalid.
    """
    if not username or not (3 <= len(username) <= 20):
        return None
    
    # Roblox usernames allow alphanumeric and single underscores
    if not username.replace('_', '').isalnum():
        return None
    
    return username.strip()

def check_rate_limit_status(status_code: int) -> bool:
    """
    Determines if a request was throttled by Roblox API.

    :param status_code: HTTP response status code.
    :return: True if 429 encountered, False otherwise.
    """
    return status_code == 429