import time
import functools
import requests
from typing import Callable, Any

def retry_request(max_retries: int = 3, delay: float = 2.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
                        continue
            raise last_exception
        return wrapper
    return decorator

@retry_request(max_retries=3, delay=1.0)
def fetch_roblox_api(url: str, session: requests.Session):
    """Fetches data from Roblox API endpoints with retry support."""
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()