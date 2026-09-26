import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-25', log_file='automation.log'):
    """Initializes a rotating file logger for Roblox automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        os.path.join(log_dir, log_file),
        maxBytes=5*1024*1024,
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        logger.addHandler(handler)
        
    # Add stream handler for console visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger