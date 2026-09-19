import logging
import time
from typing import Any, Optional

# Roblox automation helper utilities

logger = logging.getLogger('automation-tool-25')

def validate_roblox_session(session_data: dict) -> bool:
    """Ensures session integrity before execution."""
    required_keys = ['cookie', 'user_id']
    return all(key in session_data for key in required_keys)

def format_log_entry(level: str, message: str) -> str:
    """Standardizes log formatting for system monitoring."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return f"[{timestamp}] [{level.upper()}] {message}"

def retry_operation(func: Any, retries: int = 3, delay: int = 2) -> Optional[Any]:
    """Generic execution wrapper for unstable API endpoints."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return None

def clean_workspace(temp_dir: str = "./temp") -> None:
    """Purges ephemeral files to prevent build bloating."""
    import shutil
    import os
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        logger.info("Workspace cleanup completed successfully")