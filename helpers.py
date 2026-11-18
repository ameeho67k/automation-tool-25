import os
import time
import logging
from typing import List, Optional

logger = logging.getLogger('automation-tool-25')

def validate_roblox_path(path: str) -> bool:
    """Verify Roblox executable existence and path integrity."""
    return os.path.exists(path) and path.endswith('.exe')

def retry_operation(func, retries: int = 3, delay: int = 2):
    """Generic execution wrapper for unstable Roblox API calls."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return None

def format_session_data(raw_data: dict) -> dict:
    """Standardize raw roblox session telemetry data."""
    return {
        'user_id': raw_data.get('id'),
        'is_active': raw_data.get('status') == 'online',
        'timestamp': time.time()
    }

def cleanup_temp_files(directory: str, extension: str = '.tmp') -> None:
    """Purge orphaned temporary workspace assets."""
    if not os.path.exists(directory):
        return
    
    for file in os.listdir(directory):
        if file.endswith(extension):
            try:
                os.remove(os.path.join(directory, file))
            except OSError as e:
                logger.error(f"Cleanup failure: {e}")