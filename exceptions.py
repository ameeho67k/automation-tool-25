class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxSessionError(AutomationError):
    """Raised when authentication or session heartbeat fails."""
    pass

class DataParsingError(AutomationError):
    """Raised when API response format is unexpected."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when too many requests are sent to Roblox API."""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Wait {retry_after} seconds.")

class GameProcessError(AutomationError):
    """Raised when the target Roblox instance is unresponsive."""
    pass

class ValidationError(AutomationError):
    """Raised when configuration or inputs fail validation."""
    pass