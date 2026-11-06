import logging
from typing import Dict, List, Any, Tuple

logger = logging.getLogger("roblox_automation")

ALLOWED_ACTIONS = {"purchase_asset", "send_trade", "update_place", "verify_ownership"}

class ProcessingEngine:
    """Handles execution and validation of incoming Roblox automation payloads."""

    def __init__(self, max_batch_size: int = 50):
        self.max_batch_size = max_batch_size
        self.processed_count = 0

    def validate_payload(self, payload: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate structure and required fields of an individual task payload."""
        if not isinstance(payload, dict):
            return False, "Payload must be a valid dictionary"

        task_id = payload.get("task_id")
        if not isinstance(task_id, str) or not task_id.strip():
            return False, "Invalid or missing 'task_id'"

        asset_id = payload.get("asset_id")
        if not isinstance(asset_id, int) or asset_id <= 0:
            return False, "Field 'asset_id' must be a positive integer"

        action = payload.get("action")
        if action not in ALLOWED_ACTIONS:
            return False, f"Action '{action}' is not supported"

        user_id = payload.get("target_user_id")
        if user_id is not None and (not isinstance(user_id, int) or user_id <= 0):
            return False, "Field 'target_user_id' must be a positive integer"

        return True, "Valid"

    def run_processing_loop(self, raw_tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a batch of Roblox automation tasks with input validation."""
        results = []
        if len(raw_tasks) > self.max_batch_size:
            logger.warning("Batch size exceeds limit of %d items", self.max_batch_size)
            raw_tasks = raw_tasks[:self.max_batch_size]

        for index, task in enumerate(raw_tasks):
            is_valid, reason = self.validate_payload(task)
            if not is_valid:
                logger.error("Skipping task at index %d: %s", index, reason)
                continue

            task_id = task["task_id"]
            action = task["action"]
            asset_id = task["asset_id"]

            logger.info("Executing '%s' for asset %d (Task: %s)", action, asset_id, task_id)

            results.append({
                "task_id": task_id,
                "status": "completed",
                "action": action,
                "asset_id": asset_id
            })
            self.processed_count += 1

        return results