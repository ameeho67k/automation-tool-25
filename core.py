import logging
import time
from typing import Optional

class RobloxAutomationError(Exception):
    """Custom exception for roblox automation errors."""
    pass

def execute_task(task_id: str, retries: int = 3) -> Optional[dict]:
    """Executes automation task with retry logic and error handling."""
    logger = logging.getLogger('automation-tool-25')
    
    for attempt in range(retries):
        try:
            if not task_id:
                raise ValueError("Task ID cannot be empty")
            
            # Simulate task execution
            result = {"id": task_id, "status": "success"}
            logger.info(f"Task {task_id} completed successfully.")
            return result
            
        except ValueError as ve:
            logger.error(f"Invalid configuration error: {ve}")
            break
            
        except ConnectionError as ce:
            logger.warning(f"Connection attempt {attempt + 1} failed: {ce}")
            time.sleep(2 ** attempt)
            
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")
            break
            
    return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    execute_task("RBX_123")