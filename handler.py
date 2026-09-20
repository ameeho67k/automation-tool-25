import logging
from validators import validate_roblox_id, validate_action_type

logger = logging.getLogger(__name__)

def main_processing_loop(task_queue):
    """Processes automation tasks with input validation."""
    while True:
        task = task_queue.get()
        if task is None:
            break

        try:
            user_id = task.get("user_id")
            action = task.get("action")

            # Validate Roblox-specific inputs before processing
            if not validate_roblox_id(user_id):
                logger.warning(f"Invalid user_id detected: {user_id}")
                continue

            if not validate_action_type(action):
                logger.warning(f"Unsupported action requested: {action}")
                continue

            # Proceed with safe execution
            execute_task(user_id, action)

        except Exception as e:
            logger.error(f"Unexpected error in processing loop: {e}")
        finally:
            task_queue.task_done()

def execute_task(user_id, action):
    """Mock execution logic for automation tool."""
    logger.info(f"Executing {action} for user {user_id}")
    # Business logic for Roblox automation goes here