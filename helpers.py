import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple
import requests

logger = logging.getLogger("roblox_automation")

RETRYABLE_STATUS_CODES: Tuple[int, ...] = (429, 500, 502, 503, 504)

def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    retryable_status_codes: Tuple[int, ...] = RETRYABLE_STATUS_CODES
) -> Callable:
    """
    Decorator to retry failed Roblox HTTP requests with exponential backoff
    and automatic handling of rate limits (429 status).
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            delay = 1.0

            while True:
                try:
                    response = func(*args, **kwargs)
                    if isinstance(response, requests.Response):
                        if response.status_code in retryable_status_codes:
                            response.raise_for_status()
                    return response
                except (requests.RequestException, requests.HTTPError) as exc:
                    retries += 1
                    if retries > max_retries:
                        logger.error(f"Roblox API operation '{func.__name__}' failed after {max_retries} retries: {exc}")
                        raise exc

                    current_delay = delay
                    # Check for Roblox rate-limit Retry-After header
                    if hasattr(exc, 'response') and exc.response is not None:
                        retry_after = exc.response.headers.get("Retry-After")
                        if retry_after and retry_after.isdigit():
                            current_delay = float(retry_after)

                    logger.warning(
                        f"Network issue in '{func.__name__}': {exc}. Retrying in {current_delay:.2f}s (Attempt {retries}/{max_retries})"
                    )
                    time.sleep(current_delay)
                    delay *= backoff_factor

        return wrapper
    return decorator