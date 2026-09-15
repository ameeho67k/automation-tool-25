import logging
import sys
from typing import Optional

class RobloxLogger:
    """Handles standardized logging for automation-tool-25."""
    
    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Logs error events and optional tracebacks."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Logs warning events for process monitoring."""
        self.logger.warning(message)

def get_logger(name: str) -> RobloxLogger:
    """Factory function for creating module-specific loggers."""
    return RobloxLogger(name)