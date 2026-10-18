import logging

# Configure logging for automation-tool-25
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('processor')

def validate_input(data: dict) -> bool:
    """Validates incoming Roblox payload structure."""
    required_keys = {'user_id', 'action', 'timestamp'}
    if not all(k in data for k in required_keys):
        logger.warning(f"Missing keys in payload: {data}")
        return False
    if not isinstance(data.get('user_id'), int):
        logger.error("Invalid user_id type; expected integer")
        return False
    return True

def run_processing_loop(queue: list):
    """Main loop for processing automation tasks."""
    logger.info("Starting main processing loop...")
    
    while queue:
        task = queue.pop(0)
        
        # Input validation gate
        if not validate_input(task):
            logger.error("Task skipped due to validation failure")
            continue
            
        try:
            # Simulate automation execution
            logger.info(f"Processing task for user: {task['user_id']}")
            # Execution logic would go here
        except Exception as e:
            logger.error(f"Task execution error: {e}")

if __name__ == '__main__':
    mock_queue = [{'user_id': 12345, 'action': 'login', 'timestamp': 1625000000}]
    run_processing_loop(mock_queue)