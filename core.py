import time
from functools import lru_cache
from typing import Dict, Any, List, Optional
import requests


class RobloxSessionManager:
    """Manages optimized HTTP requests and cached data for Roblox APIs."""

    def __init__(self, cookie: Optional[str] = None, timeout: float = 5.0):
        self.session = requests.Session()
        self.timeout = timeout
        if cookie:
            self.session.cookies[".ROBLOSECURITY"] = cookie
            self.session.headers.update({"User-Agent": "AutomationTool25/1.0"})

    @lru_cache(maxsize=512)
    def get_asset_info(self, asset_id: int) -> Optional[Dict[str, Any]]:
        """Fetch asset details with memory caching to reduce redundant network calls."""
        url = f"https://economy.roblox.com/v2/assets/{asset_id}/details"
        try:
            response = self.session.get(url, timeout=self.timeout)
            if response.status_code == 200:
                return response.json()
        except requests.RequestException:
            pass
        return None

    def batch_fetch_user_presences(self, user_ids: List[int]) -> Dict[int, Dict[str, Any]]:
        """Efficiently fetch multiple user presences in batched chunk requests."""
        if not user_ids:
            return {}

        chunk_size = 100
        results = {}
        url = "https://presence.roblox.com/v1/presence/users"

        for i in range(0, len(user_ids), chunk_size):
            chunk = user_ids[i:i + chunk_size]
            try:
                res = self.session.post(url, json={"userIds": chunk}, timeout=self.timeout)
                if res.status_code == 200:
                    data = res.json().get("userPresences", [])
                    for item in data:
                        results[item["userId"]] = item
            except requests.RequestException:
                continue

        return results

    def clear_cache(self) -> None:
        """Clear memory cache for asset responses."""
        self.get_asset_info.cache_clear()
