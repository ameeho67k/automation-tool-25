import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for roblox automation validation errors."""
    pass

def validate_roblox_id(asset_id: str) -> int:
    """Verifies asset ID format and type."""
    try:
        if not asset_id:
            raise ValidationError("Asset ID cannot be empty")
        
        parsed_id = int(asset_id)
        if parsed_id <= 0:
            raise ValidationError("Asset ID must be positive")
        return parsed_id
    except ValueError:
        logger.error(f"Invalid asset ID format provided: {asset_id}")
        raise ValidationError("Asset ID must be a numeric string")

def validate_session_data(data: dict) -> bool:
    """Checks session configuration integrity."""
    required_keys = ['cookie', 'user_id']
    
    for key in required_keys:
        if key not in data:
            logger.warning(f"Missing session configuration key: {key}")
            return False
            
    if not data['cookie'].startswith('_|WARNING:-DO-NOT-SHARE-THIS'):
        logger.warning("Suspicious or malformed roblox cookie detected")
        return False
        
    return True

def safe_execute(func, *args, **kwargs):
    """Wrapper for handling routine execution failures."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.critical(f"Execution failure in {func.__name__}: {str(e)}")
        return None