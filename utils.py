import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("roblox_automation")


def network_retry(
    max_retries: int = 4,
    backoff_factor: float = 2.0,
    retry_exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator to retry Roblox API network requests using exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            delay = 1.0

            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except retry_exceptions as err:
                    retries += 1
                    if retries > max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} retries. Error: {err}"
                        )
                        raise err

                    logger.warning(
                        f"Roblox API request '{func.__name__}' hit error: {err}. "
                        f"Retrying in {delay:.1f}s ({retries}/{max_retries})..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor

            return None

        return wrapper

    return decorator
