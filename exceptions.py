class AutomationError(Exception):
    """Base exception for automation-tool-25."""
    pass

class RobloxSessionError(AutomationError):
    """Raised when session state is invalid."""
    pass

class RobloxRateLimitError(AutomationError):
    """Raised when API requests exceed threshold."""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limited. Retry after {retry_after} seconds.")

class RobloxAuthError(AutomationError):
    """Raised when authentication fails."""
    pass

class RobloxElementNotFoundError(AutomationError):
    """Raised when a UI element cannot be located."""
    pass

def handle_roblox_exception(e: Exception) -> str:
    """Standardizes exception logging output for the tool."""
    if isinstance(e, RobloxRateLimitError):
        return f"[RateLimit] Wait {e.retry_after}s before retrying."
    if isinstance(e, RobloxAuthError):
        return "[Auth] Login credentials expired or invalid."
    return f"[Error] Unexpected failure: {str(e)}"