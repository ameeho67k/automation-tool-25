import functools
import json
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Optional

DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 1.5


def retry_network_op(
    max_retries: int = DEFAULT_MAX_RETRIES,
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
):
    """Decorator to retry network requests with exponential backoff for Roblox API calls."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                    retries += 1
                    if retries > max_retries:
                        raise RuntimeError(
                            f"Network operation failed after {max_retries} retries: {e}"
                        ) from e
                    sleep_time = backoff_factor ** retries
                    time.sleep(sleep_time)
        return wrapper
    return decorator


class RobloxApiClient:
    """Client for interacting with Roblox endpoints with built-in retry resilience."""

    def __init__(self, cookie: Optional[str] = None):
        self.cookie = cookie
        self.headers = {"User-Agent": "AutomationTool25/1.0"}
        if self.cookie:
            self.headers["Cookie"] = f".ROBLOSECURITY={self.cookie}"

    @retry_network_op(max_retries=3, backoff_factor=2.0)
    def fetch_user_details(self, user_id: int) -> Dict[str, Any]:
        """Fetch Roblox user details given a target user ID."""
        url = f"https://users.roblox.com/v1/users/{user_id}"
        req = urllib.request.Request(url, headers=self.headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
