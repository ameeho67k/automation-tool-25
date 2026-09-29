import time
from functools import lru_cache

class RobloxEventProcessor:
    """Handles Roblox API event processing with caching."""

    def __init__(self, cache_size=128):
        self.cache_size = cache_size
        self._stats = {'processed': 0, 'hits': 0}

    @lru_cache(maxsize=128)
    def fetch_player_data(self, user_id: int):
        """Simulates expensive network request for user profile."""
        # Mock latency
        time.sleep(0.05)
        return {"id": user_id, "status": "online", "timestamp": time.time()}

    def batch_process(self, user_ids: list):
        """Processes list of user IDs with performance optimization."""
        results = []
        for uid in user_ids:
            data = self.fetch_player_data(uid)
            results.append(data)
            self._stats['processed'] += 1
        return results

    def clear_cache(self):
        """Resets the memoization storage."""
        self.fetch_player_data.cache_clear()

    def get_metrics(self):
        """Returns current processing performance metrics."""
        info = self.fetch_player_data.cache_info()
        return {
            "processed_count": self._stats['processed'],
            "cache_hits": info.hits,
            "cache_misses": info.misses
        }