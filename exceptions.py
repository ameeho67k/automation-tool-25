class AutomationError(Exception):
    """Base exception for all automation-tool-25 errors."""
    pass

class RobloxSessionError(AutomationError):
    """Raised when the Roblox session is invalid or expired."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when API requests exceed threshold."""
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after}s")

class MemoryOptimizationError(AutomationError):
    """Raised when process memory exceeds safe bounds."""
    pass

class ProcessInterruptError(AutomationError):
    """Raised when an automation process is forcefully halted."""
    pass

def raise_if_memory_critical(current_usage: float, threshold: float) -> None:
    """Performance guard to prevent OOM crashes in core module."""
    if current_usage > threshold:
        raise MemoryOptimizationError(f"Memory usage {current_usage}MB above threshold {threshold}MB")

def handle_roblox_error(status_code: int) -> None:
    """Maps network status codes to custom performance-aware exceptions."""
    if status_code == 429:
        raise RateLimitExceeded(retry_after=60)
    if status_code >= 500:
        raise RobloxSessionError("Server-side error encountered")