import logging
import os
from datetime import datetime

class RobloxAutomationLogger:
    """Centralized logging handler for automation-tool-25."""
    
    def __init__(self, name: str = "automation_tool"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Ensure log directory exists
        log_dir = "logs"
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
            except OSError as e:
                print(f"Critical: Failed to create log directory: {e}")
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(f"{log_dir}/app_{datetime.now().strftime('%Y%m%d')}.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_error(self, message: str, exc: Exception = None):
        """Handles edge cases for unexpected runtime exceptions."""
        context = f" | Exception: {type(exc).__name__}: {str(exc)}" if exc else ""
        self.logger.error(f"{message}{context}")

    def log_event(self, message: str):
        """Standard event tracking for roblox automation tasks."""
        self.logger.info(message)

# Instantiate singleton instance
app_logger = RobloxAutomationLogger()