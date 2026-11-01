import logging

logger = logging.getLogger(__name__)

class RobloxAutomationError(Exception):
    """Base exception for automation-tool-25"""
    pass

def validate_game_id(game_id):
    """Ensures game_id is a valid integer string or numeric type."""
    try:
        parsed_id = int(game_id)
        if parsed_id <= 0:
            raise ValueError("ID must be a positive integer")
        return parsed_id
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid Roblox Game ID: {game_id}. Error: {e}")
        raise RobloxAutomationError(f"Invalid game format: {game_id}")

def validate_auth_cookie(cookie):
    """Checks basic cookie structure to prevent malformed requests."""
    if not cookie or not isinstance(cookie, str):
        raise RobloxAutomationError("Authentication cookie is missing or invalid type")
    
    if not cookie.startswith('_|WARNING:-DO-NOT-SHARE-THIS'):
        logger.warning("Cookie format suspicious; missing expected warning header.")
    return cookie.strip()

def safe_execute(func, *args, **kwargs):
    """Wrapper to catch execution edge cases during automation tasks."""
    try:
        return func(*args, **kwargs)
    except ConnectionError:
        logger.critical("Network connection lost during operation")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in {func.__name__}: {str(e)}")
        return None