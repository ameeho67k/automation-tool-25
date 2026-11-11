import logging
from typing import Dict, Any

class RobloxHandler:
    """Manages interaction logic for automation-tool-25."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.logger = logging.getLogger(__name__)

    def process_request(self, payload: Dict[str, Any]) -> bool:
        """Validates and executes task based on payload."""
        if not self._validate_payload(payload):
            self.logger.error("Invalid payload structure")
            return False

        return self._execute_task(payload)

    def _validate_payload(self, payload: Dict[str, Any]) -> bool:
        required_fields = ['task_id', 'action_type']
        return all(field in payload for field in required_fields)

    def _execute_task(self, payload: Dict[str, Any]) -> bool:
        task_id = payload.get('task_id')
        try:
            self.logger.info(f"Executing task {task_id} for session {self.session_id}")
            return True
        except Exception as e:
            self.logger.error(f"Task execution failed: {e}")
            return False

def get_handler(session_id: str) -> RobloxHandler:
    """Factory function for handler instantiation."""
    return RobloxHandler(session_id)