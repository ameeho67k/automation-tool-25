import time
import functools
from typing import Callable, Any

# Cache for roblox api request results
_CACHE = {}

def memoize_request(ttl: int = 30):
    """Performance decorator for rate-limited API calls."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, str(args), str(kwargs))
            now = time.time()
            if key in _CACHE and (now - _CACHE[key]['time'] < ttl):
                return _CACHE[key]['data']
            result = func(*args, **kwargs)
            _CACHE[key] = {'data': result, 'time': now}
            return result
        return wrapper
    return decorator

class RobloxAutomationCore:
    def __init__(self):
        self.batch_size = 50

    @memoize_request(ttl=60)
    def fetch_user_data(self, user_id: int) -> dict:
        """Simulated core fetch operation with cached response."""
        # Simulating external network latency
        time.sleep(0.5)
        return {"id": user_id, "status": "active"}

    def process_batch(self, user_ids: list[int]) -> list[dict]:
        """Optimized batch processing using list comprehension."""
        return [self.fetch_user_data(uid) for uid in user_ids[:self.batch_size]]