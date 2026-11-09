import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = "automation.log", level=logging.INFO):
    """Configures a rotating file logger for roblox automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # Ensure logs directory exists
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # File rotation: 5MB per file, keep 3 backups
        handler = RotatingFileHandler(
            os.path.join(log_dir, log_file),
            maxBytes=5*1024*1024,
            backupCount=3
        )

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger