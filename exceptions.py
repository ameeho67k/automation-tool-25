import time
import functools
import logging

# Configure logger for automation-tool-25
logger = logging.getLogger('automation-tool-25')

def retry_on_failure(max_attempts=3, delay=2, backoff=2):
    """
    Decorator to implement exponential backoff for network operations.
    
    Args:
        max_attempts: Maximum number of retries.
        delay: Initial delay in seconds.
        backoff: Multiplier for the delay after each failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_attempts - 1:
                        logger.error(f'Failed after {max_attempts} attempts: {e}')
                        raise
                    
                    logger.warning(f'Attempt {attempt + 1} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkException(Exception):
    """Custom base exception for network-related failures in Roblox API."""
    pass