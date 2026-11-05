import time
import random
from typing import Any, Callable

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute function with simple linear retry logic."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if i == retries - 1:
                raise e
            time.sleep(delay * (2 ** i))
    return None

def get_random_user_agent() -> str:
    """Generate randomized browser identifiers for requests."""
    versions = ["115.0.0.0", "116.0.0.0", "117.0.0.0"]
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(versions)} Safari/537.36"

def sanitize_input(text: str) -> str:
    """Remove non-ascii characters from string input."""
    return text.encode('ascii', 'ignore').decode('ascii').strip()

def format_timestamp() -> str:
    """Human readable string for log entries."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())