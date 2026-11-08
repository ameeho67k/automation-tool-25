import logging
import time
from typing import Any, Callable, Optional

logger = logging.getLogger('automation-tool-25')

class RobloxAutomationError(Exception):
    """Base exception for automation operations."""
    pass

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Executes a roblox interaction with backoff logic."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            time.sleep(delay * (2 ** attempt))
        except Exception as e:
            logger.error(f"Unrecoverable error in {func.__name__}: {e}")
            raise RobloxAutomationError(f"Failed to execute {func.__name__}") from e
            
    raise RobloxAutomationError(f"Max retries reached for {func.__name__}") from last_exception

def validate_roblox_session(session_data: Optional[dict]) -> bool:
    """Checks validity of session configuration."""
    if not session_data or 'cookie' not in session_data:
        logger.error("Invalid session structure detected")
        return False
    return True