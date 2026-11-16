import logging

logger = logging.getLogger('automation-tool-25')

def validate_roblox_input(data: dict) -> bool:
    """
    Validates input structure for roblox automation tasks.
    Checks for presence of required keys and data types.
    """
    required_fields = {
        'place_id': int,
        'job_id': str,
        'action': str
    }

    try:
        for field, expected_type in required_fields.items():
            if field not in data:
                logger.warning(f"missing required field: {field}")
                return False
            
            if not isinstance(data[field], expected_type):
                logger.warning(f"invalid type for {field}: expected {expected_type.__name__}")
                return False

        if data['action'] not in ['join', 'leave', 'teleport']:
            logger.warning(f"unsupported action type: {data['action']}")
            return False
            
        return True
        
    except Exception as e:
        logger.error(f"validation error: {str(e)}")
        return False

def process_loop_input(raw_input: dict):
    """Main loop entry for input validation checks."""
    if not validate_roblox_input(raw_input):
        return None
    return raw_input