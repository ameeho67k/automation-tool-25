import time
import functools
import requests
from typing import Callable, Any

def retry_operation(retries: int = 3, delay: float = 2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    time.sleep(delay * (attempt + 1))
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
def fetch_roblox_data(url: str):
    """Fetches resource data from roblox api endpoints."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        data = fetch_roblox_data("https://thumbnails.roblox.com/v1/batch")
        print("data retrieval successful")
    except Exception as err:
        print(f"operation failed after retries: {err}")