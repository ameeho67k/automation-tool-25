import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-25', log_file='automation.log', level=logging.INFO):
    """Configures a rotating file logger for Roblox automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        return logger

    # Rotation settings: 5MB per file, keep 3 backups
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

    # Add stream handler for console output
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger