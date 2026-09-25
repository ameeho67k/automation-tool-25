import time
import random
import logging

def get_random_delay(min_sec=1.5, max_sec=3.5):
    """Generates a randomized delay to mimic human behavior."""
    return random.uniform(min_sec, max_sec)

def sleep_random(min_sec=1.5, max_sec=3.5):
    """Pauses execution for a randomized duration."""
    time.sleep(get_random_delay(min_sec, max_sec))

def validate_roblox_user_id(user_id):
    """Ensures the user ID format is a positive integer."""
    try:
        val = int(user_id)
        return val > 0
    except (ValueError, TypeError):
        return False

def format_log_message(module_name, message):
    """Standardizes log output for tool components."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return f"[{timestamp}] [{module_name}] {message}"

def retry_operation(func, retries=3, delay=1.0):
    """Retries a function call on failure with exponential backoff."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            time.sleep(delay * (2 ** attempt))
    logging.error(f"Operation failed after {retries} attempts: {last_exception}")
    return None