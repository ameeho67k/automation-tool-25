import asyncio
from typing import List, Dict, Any
import aiohttp

class RobloxAssetProcessor:
    """Optimized batch processor for Roblox asset metadata queries."""

    ASSET_API_URL = "https://economy.roblox.com/v2/assets"

    def __init__(self, max_connections: int = 20):
        # Limit concurrent connections to avoid rate-limiting issues
        self.semaphore = asyncio.Semaphore(max_connections)

    async def fetch_asset_details(self, session: aiohttp.ClientSession, asset_id: int) -> Dict[str, Any]:
        """Fetches details for a single Roblox asset with strict concurrency limits."""
        url = f"{self.ASSET_API_URL}/{asset_id}/details"
        async with self.semaphore:
            try:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        return await response.json()
                    return {"assetId": asset_id, "success": False, "status": response.status}
            except asyncio.TimeoutError:
                return {"assetId": asset_id, "success": False, "error": "timeout"}
            except Exception as err:
                return {"assetId": asset_id, "success": False, "error": str(err)}

    async def process_batch(self, asset_ids: List[int]) -> List[Dict[str, Any]]:
        """Concurrently retrieves metadata for a batch of Roblox assets."""
        connector = aiohttp.TCPConnector(limit_per_host=10)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [
                self.fetch_asset_details(session, asset_id)
                for asset_id in asset_ids
            ]
            return await asyncio.gather(*tasks)