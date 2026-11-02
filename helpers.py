import re
import random
from typing import List, Generator, Any, Optional


def extract_asset_id(input_str: str) -> Optional[int]:
    """
    Extracts a numeric Roblox ID from a raw string, URL, or integer.
    Returns None if no valid ID is found.
    """
    if isinstance(input_str, int):
        return input_str
    
    # Match standard Roblox URL patterns
    match = re.search(r'(?:games|catalog|library|users|badges|game-passes)/(\d+)', str(input_str))
    if match:
        return int(match.group(1))
    
    # Fallback to direct digits check
    cleaned = str(input_str).strip()
    if cleaned.isdigit():
        return int(cleaned)
    
    return None


def format_robux(amount: int) -> str:
    """Formats an integer amount into a readable Robux string (e.g., R$1,234,567)."""
    if not isinstance(amount, (int, float)):
        return "R$0"
    return f"R${int(amount):,}"


def calculate_backoff_delay(attempt: int, base_delay: float = 1.0, max_delay: float = 30.0) -> float:
    """
    Calculates exponential backoff delay with full jitter for rate-limited Roblox endpoints.
    """
    temp = min(max_delay, base_delay * (2 ** attempt))
    return random.uniform(0, temp)


def batch_items(items: List[Any], batch_size: int) -> Generator[List[Any], None, None]:
    """Yield successive batch_size chunks from items list for batch API calls."""
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than 0")
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]
