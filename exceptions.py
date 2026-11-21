from typing import Optional

class RobloxAutomationError(Exception):
    """Base exception class for all automation-tool-25 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class AuthenticationError(RobloxAutomationError):
    """Raised when Roblox session authentication fails."""
    pass

class NetworkTimeoutError(RobloxAutomationError):
    """Raised when a request to Roblox API times out."""
    pass

class RateLimitError(RobloxAutomationError):
    """Raised when the tool hits Roblox API rate limits."""
    def __init__(self, retry_after: int) -> None:
        super().__init__(f"Rate limit exceeded, retry after {retry_after} seconds", code=429)
        self.retry_after = retry_after

class InstanceNotFoundError(RobloxAutomationError):
    """Raised when a specific Roblox instance or ID is not found."""
    pass

class ValidationError(RobloxAutomationError):
    """Raised when configuration or input parameters are invalid."""
    pass