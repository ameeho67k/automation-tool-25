import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-25', log_file='automation.log', level=logging.INFO):
    """Configures a rotating file logger for Roblox automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # Format: timestamp - name - level - message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # File handler: 5MB max, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Global logger instance
logger = setup_logger()