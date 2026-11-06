import time
import requests

class RobloxSessionError(Exception):
    """Base exception for Roblox session errors."""
    pass

class InvalidCookieError(RobloxSessionError):
    """Raised when the provided ROBLOSECURITY cookie is invalid or expired."""
    pass

class RateLimitError(RobloxSessionError):
    """Raised when hitting Roblox API rate limits."""
    pass

class RobloxClient:
    """Core client for interacting with Roblox APIs with edge-case handling."""

    def __init__(self, roblosecurity_token: str):
        if not roblosecurity_token or not roblosecurity_token.startswith("_|WARNING:-DO-NOT-SHARE-THIS"):
            raise InvalidCookieError("Cookie format appears invalid or unformatted.")
        
        self.session = requests.Session()
        self.session.cookies[".ROBLOSECURITY"] = roblosecurity_token
        self.csrf_token = None

    def fetch_csrf_token(self) -> str:
        """Fetches or refreshes the X-CSRF-TOKEN required for write operations."""
        response = self.session.post("https://auth.roblox.com/v2/logout")
        if response.status_code == 403 and "x-csrf-token" in response.headers:
            self.csrf_token = response.headers["x-csrf-token"]
            return self.csrf_token
        elif response.status_code == 401:
            raise InvalidCookieError("Session cookie is unauthorized or expired.")
        raise RobloxSessionError(f"Failed to fetch CSRF token. Status: {response.status_code}")

    def request(self, method: str, url: str, **kwargs) -> dict:
        """Executes API requests with automated CSRF retry and rate-limit handling."""
        headers = kwargs.pop("headers", {})
        if self.csrf_token:
            headers["X-CSRF-TOKEN"] = self.csrf_token

        try:
            response = self.session.request(method, url, headers=headers, timeout=15, **kwargs)

            # Handle expired CSRF token edge case
            if response.status_code == 403 and response.headers.get("x-csrf-token"):
                self.csrf_token = response.headers["x-csrf-token"]
                headers["X-CSRF-TOKEN"] = self.csrf_token
                response = self.session.request(method, url, headers=headers, timeout=15, **kwargs)

            # Handle rate limiting edge case
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 5))
                raise RateLimitError(f"Rate limited by Roblox API. Retry after {retry_after}s.")

            # Handle revoked session edge case
            if response.status_code == 401:
                raise InvalidCookieError("Roblox session expired during request execution.")

            response.raise_for_status()
            return response.json()

        except requests.RequestException as exc:
            raise RobloxSessionError(f"Network error during request: {exc}") from exc
