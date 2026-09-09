import logging
from typing import Any, Dict, List

# Configure logger for tracking execution state
logger = logging.getLogger("automation-tool.core")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class RobloxAutomationProcessor:
    """Processes and executes validated automation tasks for Roblox operations."""

    VALID_ACTIONS = {"update_price", "configure_shout", "upload_decal"}

    def __init__(self) -> None:
        self.processed_count = 0

    def validate_task(self, task: Dict[str, Any]) -> bool:
        """Performs strict input validation on incoming Roblox tasks before execution."""
        if not isinstance(task, dict):
            logger.warning("Task rejected: Must be a dictionary.")
            return False

        action = task.get("action")
        if action not in self.VALID_ACTIONS:
            logger.warning(f"Task rejected: Invalid or unsupported action '{action}'.")
            return False

        # Action-specific parameter validation
        if action == "update_price":
            asset_id = task.get("asset_id")
            price = task.get("price")
            if not isinstance(asset_id, int) or asset_id <= 0:
                logger.warning(f"Validation failed: Invalid Roblox asset_id '{asset_id}'.")
                return False
            if not isinstance(price, int) or price < 0:
                logger.warning(f"Validation failed: Robux price '{price}' must be non-negative.")
                return False

        elif action == "configure_shout":
            group_id = task.get("group_id")
            message = task.get("message")
            if not isinstance(group_id, int) or group_id <= 0:
                logger.warning(f"Validation failed: Invalid Roblox group_id '{group_id}'.")
                return False
            if not isinstance(message, str) or len(message.strip()) > 255:
                logger.warning("Validation failed: Group shout message must be a string <= 255 chars.")
                return False

        elif action == "upload_decal":
            file_path = task.get("file_path")
            if not isinstance(file_path, str) or not file_path.strip():
                logger.warning("Validation failed: Missing or invalid file path for decal upload.")
                return False

        return True

    def process_queue(self, task_queue: List[Dict[str, Any]]) -> int:
        """Iterates over incoming tasks, skipping those that fail validation."""
        self.processed_count = 0
        logger.info(f"Processing batch of {len(task_queue)} Roblox automation tasks...")

        for index, task in enumerate(task_queue):
            if not self.validate_task(task):
                logger.error(f"Task rejected at index {index} due to validation errors.")
                continue

            # Execute validated commands
            action = task["action"]
            if action == "update_price":
                logger.info(f"Successfully updated asset {task['asset_id']} price to {task['price']} Robux.")
            elif action == "configure_shout":
                logger.info(f"Successfully configured group {task['group_id']} shout to: '{task['message']}'.")
            elif action == "upload_decal":
                logger.info(f"Successfully processed decal upload from: '{task['file_path']}'.")

            self.processed_count += 1

        logger.info(f"Completed processing loop. Successfully executed {self.processed_count} tasks.")
        return self.processed_count