class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxSessionError(AutomationError):
    """Raised when the Roblox API session is invalid."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when hitting Roblox server rate limits."""
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after}s")

class ExecutionTimeoutError(AutomationError):
    """Raised when a script execution exceeds threshold."""
    pass

class ResourceValidationError(AutomationError):
    """Raised when input parameters fail validation."""
    pass

# Performance optimized exception hierarchy for logging
def get_error_context(e: Exception) -> dict:
    """Returns structured diagnostic data for exceptions."""
    return {
        "error_type": type(e).__name__,
        "message": str(e),
        "retry_delay": getattr(e, "retry_after", 0)
    }