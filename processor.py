import time
import random
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(retries=3, backoff_factor=1.0):
    """Decorator to implement exponential backoff for network requests."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Max retries reached for {func.__name__}")
                        raise e
                    
                    sleep_time = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 1)
                    logger.warning(f"Retry {attempt}/{retries} after error: {e}. Sleeping {sleep_time:.2f}s")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry_network_operation(retries=3)
def fetch_roblox_api_data(url):
    """Simulated network call to Roblox API endpoints."""
    # Logic for request would go here
    print(f"Attempting fetch from {url}")
    # raise ConnectionError("API unavailable")
    return {"status": "success"}