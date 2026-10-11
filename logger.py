import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log', level=logging.INFO):
    """Initializes a rotating file logger for automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    
    # Optional console output
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

# Instantiate default logger for automation-tool-25
logger = setup_logger('roblox_bot')