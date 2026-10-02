"""Custom exceptions for the Roblox automation tool.

This module defines specific exceptions raised during Roblox API interaction, 
authentication, and asset data parsing.
"""

class RobloxAutomationError(Exception):
    """Base exception for all errors within automation-tool-25."""
    def __init__(self, message: str = "An unknown Roblox automation error occurred."):
        super().__init__(message)
        self.message = message


class RobloxAPIError(RobloxAutomationError):
    """Raised when a Roblox API request returns a non-200 status code."""
    def __init__(self, status_code: int, endpoint: str, response_text: str):
        self.status_code = status_code
        self.endpoint = endpoint
        self.response_text = response_text
        detailed_message = f"HTTP {status_code} on {endpoint}: {response_text[:100]}"
        super().__init__(detailed_message)


class InvalidCookieError(RobloxAutomationError):
    """Raised when the provided .ROBLOSECURITY token is invalid or expired."""
    def __init__(self, message: str = "The provided Roblox cookie is expired or unauthorized."):
        super().__init__(message)


class RateLimitExceededError(RobloxAPIError):
    """Raised when Roblox API returns HTTP 429 (Too Many Requests)."""
    def __init__(self, endpoint: str, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(status_code=429, endpoint=endpoint, response_text=f"Rate limit reached. Retry after {retry_after}s.")


class AssetHandlingError(RobloxAutomationError):
    """Raised when reading, downloading, or writing Roblox asset data fails."""
    def __init__(self, asset_id: int, reason: str):
        self.asset_id = asset_id
        super().__init__(f"Failed processing asset {asset_id}: {reason}")
