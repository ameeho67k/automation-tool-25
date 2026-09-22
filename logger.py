import logging
import logging.handlers
import os

LOG_FILE = "automation-tool-25.log"

def setup_logger(name: str = "roblox-automation") -> logging.Logger:
    """
    Configures a rotating file logger for the automation tool.
    Keeps 5 files of 5MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # Rotating file handler: max 5MB per file, keep 5 backups
        handler = logging.handlers.RotatingFileHandler(
            LOG_FILE, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=5
        )
        
        # Standard formatting with timestamps for roblox sessions
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Console output for real-time monitoring
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Instance for global application usage
logger = setup_logger()