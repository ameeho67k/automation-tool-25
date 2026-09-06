import functools
import time
import logging
from typing import Callable, Any

# Configure logger for performance metrics
logger = logging.getLogger('automation-tool-25')

def memoize_with_ttl(ttl_seconds: int = 300):
    """Cache function results with time-to-live to reduce overhead."""
    def decorator(func: Callable):
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

def batch_process_entities(data: list, batch_size: int = 50):
    """Generator to process large roblox entity batches efficiently."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def performance_timer(func: Callable):
    """Decorator to log execution duration of core methods."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 0.1:
            logger.debug(f"Method {func.__name__} took {duration:.4f}s")
        return result
    return wrapper