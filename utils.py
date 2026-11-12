import time
import functools
import logging

logger = logging.getLogger('automation-tool-25')

def retry_network_operation(max_retries=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=1)
def fetch_roblox_data(endpoint):
    """Example network call wrapper for roblox endpoints."""
    # Simulating actual network logic
    pass