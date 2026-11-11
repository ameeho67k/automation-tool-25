class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxSessionError(AutomationError):
    """Raised when session state is invalid or disconnected."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when Roblox API limits are hit."""
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(f"API rate limit exceeded. Retry after {retry_after}s")

class ScriptInjectionError(AutomationError):
    """Raised when script execution fails within the environment."""
    pass

class MemoryThresholdError(AutomationError):
    """Raised when local memory usage exceeds safe limits."""
    pass

def handle_critical_failure(error: Exception):
    """Logs and re-raises core automation exceptions."""
    if isinstance(error, AutomationError):
        print(f"[CRITICAL] {error.__class__.__name__}: {str(error)}")
    raise error