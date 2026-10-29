import re
from typing import Optional, Union

ROBLOX_TAX_RATE = 0.30


def extract_asset_id(url_or_string: str) -> Optional[int]:
    """Extracts a numeric Roblox asset or place ID from a string or URL."""
    match = re.search(r'(?:catalog/|library/|games/|assets/)?(\d+)', str(url_or_string))
    if match:
        return int(match.group(1))
    return None


def calculate_net_robux(gross_amount: int) -> int:
    """Calculates net Robux after deducting Roblox\'s 30% marketplace fee."""
    if gross_amount < 0:
        raise ValueError("Gross amount must be non-negative")
    return max(0, int(gross_amount * (1.0 - ROBLOX_TAX_RATE)))


def calculate_gross_price(target_net: int) -> int:
    """Calculates required list price to receive a target net Robux amount."""
    if target_net < 0:
        raise ValueError("Target net must be non-negative")
    if target_net == 0:
        return 0
    return max(1, int(target_net / (1.0 - ROBLOX_TAX_RATE)))


def format_robux(amount: Union[int, float]) -> str:
    """Formats Robux numbers into compact readable strings (e.g., 10.5K, 2M)."""
    value = float(amount)
    if value >= 1_000_000_000:
        formatted = f"{value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        formatted = f"{value / 1_000_000:.1f}M"
    elif value >= 1_000:
        formatted = f"{value / 1_000:.1f}K"
    else:
        return str(int(value))
    return formatted.replace(".0", "")


def is_valid_username(username: str) -> bool:
    """Validates if a string adheres to standard Roblox username requirements."""
    if not (3 <= len(username) <= 20):
        return False
    if username.startswith("_") or username.endswith("_"):
        return False
    return bool(re.match(r"^[a-zA-Z0-9_]+$", username))
