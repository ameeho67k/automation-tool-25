import functools
import time
import logging
from typing import Callable, Any

# Logger setup for automation-tool-25
logger = logging.getLogger(__name__)

def memoize_with_ttl(ttl_seconds: int = 300):
    """Cache function results to optimize repeated roblox API calls"""
    def decorator(func: Callable):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 50):
    """Generator to process large object lists in manageable chunks"""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def throttle_execution(interval: float):
    """Rate limiting decorator to prevent roblox API rate limits"""
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                time.sleep(interval - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator