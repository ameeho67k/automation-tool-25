import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-25')

def retry_on_failure(retries: int = 3, delay: float = 1.5) -> Callable:
    """Decorator to retry network functions on exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            
            logger.error(f"Final attempt failed for {func.__name__} after {retries} retries")
            raise last_exception
        return wrapper
    return decorator