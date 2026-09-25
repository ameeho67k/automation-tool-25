import logging
import requests
from requests.exceptions import RequestException

logger = logging.getLogger('automation-tool-25')

def fetch_roblox_asset(asset_id: int, retries: int = 3) -> dict:
    """Fetches metadata for a specific Roblox asset with retry logic."""
    url = f"https://economy.roblox.com/v2/assets/{asset_id}/details"
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for asset {asset_id}: {e}")
            if attempt == retries - 1:
                logger.error(f"Critical failure fetching asset {asset_id} after {retries} attempts")
                return {}
    return {}

def validate_roblox_username(username: str) -> bool:
    """Checks if a username string conforms to standard API expectations."""
    if not isinstance(username, str) or len(username) < 3 or len(username) > 20:
        return False
    return username.isalnum() or '_' in username

def parse_game_id(input_value: any) -> int:
    """Sanitizes and converts input to a valid integer game ID."""
    try:
        return int(input_value)
    except (ValueError, TypeError):
        logger.error(f"Invalid game ID provided: {input_value}")
        return 0