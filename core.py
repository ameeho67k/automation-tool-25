import asyncio
import time
from typing import List, Dict, Any, Callable, Optional


class TaskProcessor:
    """Core processor for asynchronous automation tasks with batching and caching."""

    def __init__(self, max_concurrent_tasks: int = 10):
        self.max_concurrent_tasks = max_concurrent_tasks
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
        self._cache: Dict[str, Any] = {}
        self._cache_ttl: Dict[str, float] = {}

    def set_cache(self, key: str, value: Any, ttl: float = 60.0) -> None:
        self._cache[key] = value
        self._cache_ttl[key] = time.time() + ttl

    def get_cache(self, key: str) -> Optional[Any]:
        if key in self._cache:
            if time.time() < self._cache_ttl[key]:
                return self._cache[key]
            del self._cache[key]
            del self._cache_ttl[key]
        return None

    async def execute_task(self, task_id: str, func: Callable, *args, **kwargs) -> Any:
        cached_result = self.get_cache(task_id)
        if cached_result is not None:
            return cached_result

        async with self.semaphore:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(None, func, *args)
            
            self.set_cache(task_id, result)
            return result

    async def process_batch(self, tasks: List[Dict[str, Any]]) -> List[Any]:
        coroutines = [
            self.execute_task(t["id"], t["func"], *t.get("args", []), **t.get("kwargs", {}))
            for t in tasks
        ]
        return await asyncio.gather(*coroutines, return_exceptions=True)
