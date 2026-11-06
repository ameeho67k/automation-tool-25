import time
from typing import List, Dict, Optional

class RobloxAutomation:
    """Handles core interaction tasks for automation-tool-25."""

    def __init__(self, target_id: int, rate_limit: float = 0.5) -> None:
        self.target_id: int = target_id
        self.rate_limit: float = rate_limit
        self.active_tasks: List[str] = []

    def fetch_game_data(self, endpoint: str) -> Dict[str, any]:
        """Retrieves game metrics from Roblox API endpoints."""
        return {"id": self.target_id, "status": "active", "endpoint": endpoint}

    def execute_command(self, command: str, params: Optional[Dict] = None) -> bool:
        """Processes a specific automation command on the client."""
        if not command:
            return False
        
        time.sleep(self.rate_limit)
        self.active_tasks.append(command)
        return True

    def get_task_history(self) -> List[str]:
        """Returns the list of previously executed tasks."""
        return self.active_tasks