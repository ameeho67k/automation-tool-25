import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("roblox_automation")

def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    allowed_exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    Designed for Roblox API requests to handle rate limits and temporary drops.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed permanently after "
                            f"{max_retries} attempts. Final error: {err}"
                        )
                        raise err
                    
                    logger.warning(
                        f"Network operation '{func.__name__}' attempt {attempt}/{max_retries} "
                        f"failed: {err}. Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator
