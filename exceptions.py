import time
import functools
import logging

logger = logging.getLogger(__name__)

class NetworkRetryError(Exception):
    """Custom exception for network operation failures."""
    pass

def with_retry(max_attempts=3, delay=2):
    """Decorator to retry network functions on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts.")
            raise NetworkRetryError(f"Failed after {max_attempts} attempts: {last_exception}")
        return wrapper
    return decorator