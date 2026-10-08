import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class RobloxAutomationError(Exception):
    """Base exception for automation-tool-25"""
    pass

def safe_execute(func, *args, **kwargs) -> Optional[Any]:
    """Wraps execution to handle Roblox API and network edge cases"""
    try:
        return func(*args, **kwargs)
    except ConnectionError as e:
        logger.error(f"Network connectivity lost: {e}")
    except TimeoutError:
        logger.warning("Roblox service request timed out")
    except ValueError as e:
        logger.error(f"Invalid data structure returned from API: {e}")
    except Exception as e:
        logger.critical(f"Unexpected automation failure: {e}")
    return None

def validate_response(data: dict) -> bool:
    """Checks if response contains expected Roblox schema keys"""
    required_keys = {"success", "data"}
    if not isinstance(data, dict):
        return False
    return required_keys.issubset(data.keys())

def retry_operation(func, retries: int = 3, *args, **kwargs):
    """Simple retry loop for transient automation errors"""
    attempt = 0
    while attempt < retries:
        result = safe_execute(func, *args, **kwargs)
        if result is not None:
            return result
        attempt += 1
        logger.info(f"Retrying operation, attempt {attempt}/{retries}")
    return None