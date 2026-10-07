import time
import random
import logging

# Roblox automation helper utilities

def get_random_delay(min_ms=500, max_ms=2000):
    """Generates a human-like delay between actions."""
    delay = random.uniform(min_ms, max_ms) / 1000
    time.sleep(delay)
    return delay

def format_roblox_timestamp(timestamp=None):
    """Formats unix epoch for roblox api logs."""
    if timestamp is None:
        timestamp = time.time()
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(timestamp))

def validate_game_id(game_id):
    """Checks if provided string is a valid numeric ID."""
    return str(game_id).isdigit() and len(str(game_id)) >= 8

def retry_operation(func, retries=3, delay=2):
    """Generic retry wrapper for unstable network requests."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logging.warning(f"Attempt {i+1} failed: {e}")
            if i == retries - 1:
                raise
            time.sleep(delay * (i + 1))

def chunk_list(data, size=50):
    """Splits large player lists into manageable chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]