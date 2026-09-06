import time
import random

def get_roblox_headers(csrf_token: str = ""):
    """Constructs standard headers for Roblox API requests."""
    return {
        "User-Agent": "Roblox/WinInet",
        "X-CSRF-TOKEN": csrf_token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def simulate_human_delay(min_ms: int = 500, max_ms: int = 2000):
    """Sleeps for a random duration to mimic organic behavior."""
    time.sleep(random.uniform(min_ms, max_ms) / 1000)

def format_place_id(place_id: int) -> str:
    """Converts raw ID to string format for URL endpoints."""
    return str(place_id)

def validate_response_status(status_code: int) -> bool:
    """Checks if a Roblox API response status is successful."""
    return 200 <= status_code < 300

def batch_process_ids(id_list: list, chunk_size: int = 50):
    """Splits large ID lists for batch endpoint requests."""
    for i in range(0, len(id_list), chunk_size):
        yield id_list[i:i + chunk_size]