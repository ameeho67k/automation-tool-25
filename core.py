import asyncio
from typing import Dict, List, Any, Optional
import aiohttp

class RobloxBatchProcessor:
    """Optimized processor for handling concurrent Roblox API requests with caching."""
    
    def __init__(self, concurrency_limit: int = 10, cache_ttl: int = 60):
        self.semaphore = asyncio.Semaphore(concurrency_limit)
        self.cache: Dict[str, tuple] = {}  # Format: {url: (data, timestamp)}
        self.cache_ttl = cache_ttl

    async def _fetch_url(self, session: aiohttp.ClientSession, url: str) -> Optional[Dict[str, Any]]:
        # Check cache and TTL before making network calls
        current_time = asyncio.get_event_loop().time()
        if url in self.cache:
            cached_data, timestamp = self.cache[url]
            if current_time - timestamp < self.cache_ttl:
                return cached_data

        async with self.semaphore:
            try:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        self.cache[url] = (data, asyncio.get_event_loop().time())
                        return data
            except Exception:
                # Gracefully handle network exceptions to avoid process termination
                pass
        return None

    async def fetch_users_data(self, user_ids: List[int]) -> List[Optional[Dict[str, Any]]]:
        """Concurrently fetches user profile details from Roblox API."""
        if not user_ids:
            return []

        urls = [f"https://users.roblox.com/v1/users/{user_id}" for user_id in user_ids]
        
        async with aiohttp.ClientSession() as session:
            tasks = [self._fetch_url(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    def clear_expired_cache(self) -> None:
        """Prunes expired entries from the in-memory cache to manage memory footprint."""
        current_time = asyncio.get_event_loop().time()
        expired_keys = [
            url for url, (_, timestamp) in self.cache.items()
            if current_time - timestamp >= self.cache_ttl
        ]
        for url in expired_keys:
            del self.cache[url]