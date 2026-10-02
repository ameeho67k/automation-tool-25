import re
from typing import Union

USERNAME_REGEX = re.compile(r"^(?!_)(?!.*__)[a-zA-Z0-9_]{3,20}(?<!_)$")


def validate_roblox_username(username: str) -> bool:
    """Validates if a string conforms to Roblox username rules."""
    if not isinstance(username, str):
        return False
    return bool(USERNAME_REGEX.match(username))


def validate_roblox_id(identifier: Union[int, str]) -> bool:
    """Validates if a Roblox ID (User ID or Asset ID) is a valid positive integer."""
    if isinstance(identifier, int):
        return identifier > 0
    if isinstance(identifier, str):
        if not identifier.isdigit():
            return False
        if identifier.startswith("0") and len(identifier) > 1:
            return False
        try:
            return int(identifier) > 0
        except ValueError:
            return False
    return False


def validate_cookie_format(cookie: str) -> bool:
    """Checks if a string resembles a typical Roblox .ROBLOSECURITY cookie format."""
    if not isinstance(cookie, str):
        return False
    # Roblox security cookies almost always contain this warning prefix
    warning_prefix = "_|WARNING:-DO-NOT-SHARE-THIS."
    return warning_prefix in cookie
