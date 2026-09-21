import time
import logging
from typing import Any, Optional

# Configure logger for automation-tool-25
logger = logging.getLogger("roblox_automation")

def retry_operation(func, max_attempts: int = 3, delay: float = 1.0) -> Any:
    """Execute function with simple retry logic for network stability."""
    last_exception = None
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay * (attempt + 1))
    raise last_exception

def validate_roblox_id(roblox_id: Any) -> bool:
    """Ensure provided ID is a valid numeric Roblox format."""
    try:
        return isinstance(int(roblox_id), int) and int(roblox_id) > 0
    except (ValueError, TypeError):
        return False

def format_timestamp() -> str:
    """Standardized logging format for tool processes."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())