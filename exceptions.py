class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxConnectionError(AutomationError):
    """Raised when the connection to Roblox API fails."""
    pass

class ValidationError(AutomationError):
    """Raised when input parameters fail schema validation."""
    pass

class SessionExpiredError(AutomationError):
    """Raised when the auth session cookie is invalid."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when exceeding API request quotas."""
    def __init__(self, retry_after=60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit hit. Retry after {retry_after} seconds")

class AssetProcessingError(AutomationError):
    """Raised during failure to parse or upload assets."""
    pass