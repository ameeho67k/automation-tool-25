import logging

logger = logging.getLogger('automation-tool-25')

# Input validation rules for roblox automation
VALID_ACTION_TYPES = ['click', 'press', 'wait', 'type']

def validate_payload(data: dict) -> bool:
    """Ensures incoming instructions meet schema requirements."""
    if not isinstance(data, dict):
        return False
    if data.get('action') not in VALID_ACTION_TYPES:
        return False
    if not isinstance(data.get('duration', 0), (int, float)):
        return False
    return True

def process_instruction_queue(queue):
    """Main processing loop with integrated input validation."""
    for entry in queue:
        try:
            if not validate_payload(entry):
                logger.warning(f"Invalid payload detected: {entry}")
                continue
            
            action = entry['action']
            value = entry.get('value', '')
            
            logger.info(f"Executing {action} with parameter {value}")
            # Execution logic placeholder for roblox engine
            
        except KeyError as e:
            logger.error(f"Missing key in payload: {e}")
        except Exception as e:
            logger.error(f"Unexpected error processing step: {e}")