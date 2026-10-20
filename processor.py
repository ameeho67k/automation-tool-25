import time
import logging

# Roblox automation processing logic
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures incoming data matches expected Roblox automation schema."""
    if not isinstance(data, dict):
        return False
    if "action_id" not in data or not isinstance(data.get("action_id"), int):
        return False
    if "payload" not in data or not isinstance(data.get("payload"), str):
        return False
    return True

def process_loop(queue):
    """Main processing loop for incoming task payloads."""
    logger.info("Starting main processing loop")
    
    while True:
        try:
            task = queue.get(timeout=1)
            
            # Input validation block
            if not validate_input(task):
                logger.warning(f"Invalid task data received: {task}")
                continue
            
            # Processing logic for verified data
            action_id = task["action_id"]
            payload = task["payload"]
            
            logger.info(f"Executing action {action_id} with data: {payload}")
            time.sleep(0.1)
            
        except Exception as e:
            logger.error(f"Unexpected error in processing loop: {e}")
            time.sleep(5)
