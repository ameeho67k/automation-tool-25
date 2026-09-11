import time
import functools
from typing import Callable, Any

# cache for roblox api request results
_cache = {}

def memoize_request(ttl: int = 300):
    """decorator for caching api calls to reduce latency"""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{kwargs}"
            now = time.time()
            if key in _cache:
                data, timestamp = _cache[key]
                if now - timestamp < ttl:
                    return data
            
            result = func(*args, **kwargs)
            _cache[key] = (result, now)
            return result
        return wrapper
    return decorator

class RobloxHandler:
    def __init__(self, session_id: str):
        self.session_id = session_id

    @memoize_request(ttl=60)
    def get_player_data(self, user_id: int) -> dict:
        """fetch player metadata with local caching"""
        # simulate network request delay
        time.sleep(0.1)
        return {"id": user_id, "status": "online", "place": "lobby"}

    def batch_process_users(self, user_ids: list[int]) -> list[dict]:
        """optimized batch processing for player data"""
        results = []
        for uid in user_ids:
            results.append(self.get_player_data(uid))
        return results