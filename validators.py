import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network-bound operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt {attempt + 1} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3)
def validate_roblox_api_connection(url: str) -> bool:
    """
    Simple check for endpoint availability using standard request patterns.
    """
    import requests
    response = requests.get(url, timeout=5)
    return response.status_code == 200