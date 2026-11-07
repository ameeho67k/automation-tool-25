import time
import requests
from typing import Dict, Any, Optional


class RobloxRequestHandler:
    """Handles HTTP requests to Roblox Web APIs with automatic retry and rate-limit handling."""

    BASE_USERS_URL = "https://users.roblox.com/v1"
    BASE_ECONOMY_URL = "https://economy.roblox.com/v1"

    def __init__(self, cookie: Optional[str] = None, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout
        if cookie:
            self.session.cookies[".ROBLOSECURITY"] = cookie

    def get_user_info(self, user_id: int) -> Dict[str, Any]:
        """Fetch profile information for a specific Roblox user ID."""
        url = f"{self.BASE_USERS_URL}/users/{user_id}"
        response = self.safe_request("GET", url)
        return response.json() if response else {}

    def get_asset_details(self, asset_id: int) -> Dict[str, Any]:
        """Retrieve item marketplace details by asset ID."""
        url = f"{self.BASE_ECONOMY_URL}/assets/{asset_id}/details"
        response = self.safe_request("GET", url)
        return response.json() if response else {}

    def safe_request(
        self, method: str, url: str, retries: int = 3, backoff: float = 1.5, **kwargs
    ) -> Optional[requests.Response]:
        """Execute HTTP request with retry logic for rate limits and network errors."""
        for attempt in range(retries):
            try:
                resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
                if resp.status_code == 429:
                    time.sleep(backoff * (attempt + 1))
                    continue
                resp.raise_for_status()
                return resp
            except requests.RequestException:
                if attempt == retries - 1:
                    raise
                time.sleep(backoff * (attempt + 1))
        return None
