class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxConnectionError(AutomationError):
    """Raised when the Roblox API is unreachable."""
    pass

class ScriptExecutionError(AutomationError):
    """Raised when a remote script fails to run."""
    pass

class ValidationError(AutomationError):
    """Raised when input data fails internal validation."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when API request thresholds are hit."""
    pass

def handle_automation_exception(e: Exception) -> str:
    """Format exception messages for logging purposes."""
    if isinstance(e, AutomationError):
        return f"[Automation Error] {e.__class__.__name__}: {str(e)}"
    return f"[Unexpected Error] {type(e).__name__}: {str(e)}"