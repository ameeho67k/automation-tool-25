"""Custom exceptions for Roblox API and data handling in automation-tool-25."""

class RobloxAutomationError(Exception):
    """Base exception class for automation-tool-25 errors."""
    def __init__(self, message: str = "An unknown error occurred during Roblox automation"):
        self.message = message
        super().__init__(self.message)


class CookieInvalidError(RobloxAutomationError):
    """Raised when the provided .ROBLOSECURITY cookie is invalid or expired."""
    def __init__(self, message: str = "Provided Roblox security cookie is invalid or expired"):
        super().__init__(message)


class RateLimitError(RobloxAutomationError):
    """Raised when Roblox API rate limit is hit."""
    def __init__(self, retry_after: int = 60, endpoint: str = ""):
        self.retry_after = retry_after
        self.endpoint = endpoint
        msg = f"Rate limit reached for '{endpoint}'. Retry after {retry_after}s" if endpoint else f"Rate limit reached. Retry after {retry_after}s"
        super().__init__(msg)


class AssetNotFoundError(RobloxAutomationError):
    """Raised when a requested Roblox asset or place cannot be found."""
    def __init__(self, asset_id: int):
        self.asset_id = asset_id
        super().__init__(f"Roblox asset or entity with ID '{asset_id}' was not found")


class DataValidationError(RobloxAutomationError):
    """Raised when parsed Roblox JSON payload fails field validation."""
    def __init__(self, field_name: str, expected_type: str, actual_type: str):
        self.field_name = field_name
        self.expected_type = expected_type
        self.actual_type = actual_type
        super().__init__(
            f"Data validation failed for field '{field_name}': expected {expected_type}, got {actual_type}"
        )
