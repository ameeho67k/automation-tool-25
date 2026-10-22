import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_operation(retries: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

def validate_roblox_id(asset_id: Any) -> bool:
    """Check if the provided asset ID is valid integer format."""
    try:
        return int(asset_id) > 0
    except (ValueError, TypeError):
        return False