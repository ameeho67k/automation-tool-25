import re
from typing import Dict, Any, List


class TaskValidationError(Exception):
    """Raised when a Roblox automation task fails input validation."""
    pass


def validate_roblox_task(task: Dict[str, Any]) -> bool:
    """Validate input data structure for Roblox automation jobs."""
    if not isinstance(task, dict):
        raise TaskValidationError("Task payload must be a dictionary")

    task_type = task.get("type")
    valid_types = ("asset_upload", "place_update", "group_payout")
    if task_type not in valid_types:
        raise TaskValidationError(f"Invalid task type '{task_type}'. Must be one of {valid_types}")

    # Roblox IDs must be positive non-zero integers
    target_id = task.get("target_id")
    if not isinstance(target_id, int) or target_id <= 0:
        raise TaskValidationError("target_id must be a positive integer")

    # Optional payload check
    payload = task.get("payload", {})
    if not isinstance(payload, dict):
        raise TaskValidationError("payload must be a dictionary object")

    return True


def process_automation_queue(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Main processing loop with input validation for batch automation tasks."""
    processed = []
    errors = []

    for index, task in enumerate(tasks):
        try:
            # Validate input schema prior to execution
            validate_roblox_task(task)
            
            # Execution stub for validated Roblox action
            task_id = task["target_id"]
            task_type = task["type"]
            processed.append({
                "queue_index": index,
                "target_id": task_id,
                "status": f"Executed {task_type}"
            })
        except TaskValidationError as err:
            errors.append({
                "queue_index": index,
                "error": str(err),
                "raw_task": task
            })

    return {"successful_count": len(processed), "failures": errors, "results": processed}
