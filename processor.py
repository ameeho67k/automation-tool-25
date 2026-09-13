import asyncio
import time
from typing import List, Any, Callable, Optional


class BatchProcessor:
    """Optimizes API and data processing by grouping items into dynamic batches."""

    def __init__(self, batch_size: int = 50, flush_interval: float = 0.2):
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.queue: asyncio.Queue = asyncio.Queue()
        self._worker_task: Optional[asyncio.Task] = None

    async def start(self, process_callback: Callable[[List[Any]], Any]):
        """Starts the background worker task to process queued items."""
        self._worker_task = asyncio.create_task(self._worker(process_callback))

    async def add_item(self, item: Any):
        """Adds a single item to the queue for batch processing."""
        await self.queue.put(item)

    async def _worker(self, process_callback: Callable[[List[Any]], Any]):
        while True:
            batch = []
            start_time = time.time()

            while len(batch) < self.batch_size:
                elapsed = time.time() - start_time
                remaining_time = self.flush_interval - elapsed
                if remaining_time <= 0:
                    break
                try:
                    item = await asyncio.wait_for(self.queue.get(), timeout=max(remaining_time, 0.001))
                    batch.append(item)
                    self.queue.task_done()
                except asyncio.TimeoutError:
                    break

            if batch:
                try:
                    await process_callback(batch)
                except Exception as err:
                    print(f"Batch processing error: {err}")

    async def stop(self):
        """Gracefully flushes remaining items and stops the background worker."""
        if self._worker_task:
            await self.queue.join()
            self._worker_task.cancel()