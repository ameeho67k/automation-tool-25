import time
import random
import logging
from typing import Callable, Any, Tuple
import requests

logger = logging.getLogger("automation-tool.helpers")

def retry_on_failure(
    max_retries: int = 5,
    backoff_factor: float = 2.0,
    status_to_retry: Tuple[int, ...] = (429, 500, 502, 503, 504)
) -> Callable:
    """
    Decorator to retry Roblox API calls on transient errors or rate limits (HTTP 429).
    Includes exponential backoff with randomized jitter.
    """
    def decorator(func: Callable[..., requests.Response]) -> Callable[..., requests.Response]:
        def wrapper(*args: Any, **kwargs: Any) -> requests.Response:
            retries = 0
            while True:
                try:
                    response = func(*args, **kwargs)
                    
                    # Check if status code matches retryable conditions
                    if response.status_code in status_to_retry:
                        # Handle rate limiting dynamically if the header is available
                        if response.status_code == 429:
                            retry_after = response.headers.get("Retry-After")
                            if retry_after and retry_after.isdigit():
                                wait_time = float(retry_after) + random.uniform(0.5, 1.5)
                                logger.warning(f"Roblox rate limit hit. Waiting {wait_time:.2f}s based on response header.")
                                time.sleep(wait_time)
                                continue
                        
                        raise requests.exceptions.HTTPError(
                            f"Transient error {response.status_code}", 
                            response=response
                        )
                        
                    return response
                except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as err:
                    retries += 1
                    if retries > max_retries:
                        logger.error(f"Roblox API request failed permanently after {max_retries} attempts.")
                        raise err

                    # Compute exponential backoff with random jitter
                    sleep_time = (backoff_factor ** retries) + random.uniform(0.1, 1.0)
                    logger.warning(
                        f"Network operational delay ({err}). Retrying in {sleep_time:.2f} seconds... "
                        f"(Attempt {retries}/{max_retries})"
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator
