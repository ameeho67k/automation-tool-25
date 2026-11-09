import time
import functools
import requests
from typing import Callable, Any

def with_retry(max_attempts: int = 3, delay: float = 2.0):
    """
    Decorator to retry network requests on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
                        continue
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1.0)
def fetch_roblox_api(url: str, session: requests.Session) -> dict:
    """
    Fetches data from roblox api with built-in retry logic.
    """
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()