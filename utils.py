import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-25')

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying unstable network requests."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_roblox_data(url: str):
    """Example function for roblox api interactions."""
    # Placeholder for actual request logic
    return {"status": "success"}