class AutomationError(Exception):
    """Base exception for automation-tool-25"""
    pass

class RobloxSessionError(AutomationError):
    """Raised when the Roblox session is invalid or expired"""
    pass

class DataParsingError(AutomationError):
    """Raised when JSON or API response schema is unexpected"""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when hitting Roblox API rate limits"""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds")

class AssetAccessError(AutomationError):
    """Raised when restricted or private assets are accessed"""
    pass

def handle_roblox_error(error: Exception):
    """Utility for logging and categorizing automation errors"""
    if isinstance(error, RateLimitExceeded):
        print(f"[!] Throttled by Roblox: {error}")
    elif isinstance(error, RobloxSessionError):
        print("[!] Session expired. Re-authentication required.")
    else:
        print(f"[!] Unexpected automation failure: {error}")
    raise error