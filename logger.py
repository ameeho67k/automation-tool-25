import logging
import sys
from typing import Optional

class RobloxAutomationLogger:
    """Handles standardized logging for automation-tool-25."""
    
    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages for tool execution."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Logs critical tool failures or errors."""
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message: str) -> None:
        """Logs granular details for troubleshooting automation scripts."""
        self.logger.debug(message)

    @staticmethod
    def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
        """Factory method to retrieve a configured logger instance."""
        instance = RobloxAutomationLogger(name, level)
        return instance.logger