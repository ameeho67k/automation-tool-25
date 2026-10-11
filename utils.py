import logging
from typing import Any, Callable, Optional

logger = logging.getLogger('automation-tool-25')

class RobloxAutomationError(Exception):
    """Base exception for roblox automation tasks."""
    pass

def execute_with_retry(func: Callable, retries: int = 3, *args, **kwargs) -> Any:
    """Executes a given function with simple retry logic for network stability."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
        except Exception as e:
            logger.error(f"Critical failure during execution: {e}")
            raise RobloxAutomationError(f"Operation failed after {attempt + 1} attempts") from e
            
    raise RobloxAutomationError(f"Max retries exceeded: {last_exception}")

def validate_response(data: Optional[dict], keys: list) -> bool:
    """Checks if required keys exist in the roblox API response."""
    if not data:
        logger.error("Received empty or null data from API")
        return False
        
    missing = [key for key in keys if key not in data]
    if missing:
        logger.error(f"Response missing keys: {missing}")
        return False
        
    return True