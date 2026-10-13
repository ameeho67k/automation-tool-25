from typing import List, Optional, Dict

class RobloxAutomationEngine:
    """Core engine for handling automated Roblox tasks."""

    def __init__(self, bot_token: str, max_instances: int = 5) -> None:
        self.bot_token: str = bot_token
        self.max_instances: int = max_instances
        self.active_tasks: Dict[str, bool] = {}

    def launch_session(self, place_id: int) -> bool:
        """Initializes a new automation session for a specific game."""
        if len(self.active_tasks) >= self.max_instances:
            return False
        
        session_id: str = f"session_{place_id}"
        self.active_tasks[session_id] = True
        return True

    def get_status(self) -> List[str]:
        """Retrieves a list of currently running instance IDs."""
        return list(self.active_tasks.keys())

    def terminate_session(self, session_id: str) -> None:
        """Stops a running automation session by ID."""
        if session_id in self.active_tasks:
            del self.active_tasks[session_id]

def initialize_engine(token: str, instances: int) -> RobloxAutomationEngine:
    """Factory function to create a new automation instance."""
    return RobloxAutomationEngine(token, instances)