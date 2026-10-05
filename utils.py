import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation-tool.utils")

def retry_on_failure(
    retries: int = 3,
    backoff_in_seconds: float = 1.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a function on failure with exponential backoff and jitter.
    Useful for Roblox API requests that may rate-limit or fail transiently.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            current_delay = backoff_in_seconds
            
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise e
                    
                    # Exponential backoff with jitter to prevent thundering herd
                    jitter = random.uniform(0.5, 1.5)
                    sleep_time = current_delay * jitter
                    logger.warning(
                        f"Attempt {attempt} failed for {func.__name__}: {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    current_delay *= 2
            
            return func(*args, **kwargs)
        return wrapper
    return decorator