class AutomationError(Exception):
    """Base exception for automation-tool-25"""
    pass

class RobloxSessionError(AutomationError):
    """Raised when the Roblox session is invalid or expired"""
    pass

class RateLimitError(AutomationError):
    """Raised when API requests exceed threshold"""
    def __init__(self, retry_after=60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry in {retry_after} seconds")

class ElementNotFoundError(AutomationError):
    """Raised when a specific UI element is not found"""
    pass

class NetworkTimeoutError(AutomationError):
    """Raised when a connection to Roblox servers times out"""
    pass

def raise_if_not_valid(condition: bool, message: str):
    """Helper to enforce state conditions"""
    if not condition:
        raise AutomationError(message)

def handle_automation_exception(e: Exception):
    """Unified logging interface for custom exceptions"""
    if isinstance(e, AutomationError):
        print(f"[Automation Error]: {e}")
    else:
        print(f"[Critical System Error]: {type(e).__name__} - {e}")