import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = "automation.log", level: int = logging.INFO):
    """Configures a rotating file logger for Roblox automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure logs directory exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    file_path = os.path.join("logs", log_file)

    # Rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        file_path, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )

    # Set formatting for console and file
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )
    handler.setFormatter(formatter)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        logger.addHandler(handler)
        
        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger