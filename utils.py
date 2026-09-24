import time
import logging
from typing import Optional, List, Union

logger = logging.getLogger('automation-tool-25')

def format_roblox_id(id_val: Union[str, int]) -> Optional[int]:
    """Converts varied input types to a validated Roblox ID integer."""
    try:
        return int(id_val)
    except (ValueError, TypeError):
        logger.error(f"Invalid ID format provided: {id_val}")
        return None

def retry_request(func: callable, retries: int = 3, delay: float = 1.0) -> Optional[dict]:
    """Retries a network operation for Roblox API endpoints."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    return None

def sanitize_input(data: List[str]) -> List[str]:
    """Cleans raw input lists by removing whitespace and empty entries."""
    return [item.strip() for item in data if item and item.strip()]

def log_task_completion(task_name: str, status: bool = True) -> None:
    """Records status of automation tasks to the console."""
    state = "success" if status else "failure"
    logger.info(f"Task {task_name} completed with status: {state}")