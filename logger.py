import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Default log settings for roblox automation bot
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB per log file
BACKUP_COUNT = 3  # Keep up to 3 old log files
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str = "roblox_automation") -> logging.Logger:
    """Initializes and returns a standard logger with stdout and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent adding handlers repeatedly if already configured
    if logger.hasHandlers():
        return logger

    # Ensure logs directory exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console handler for realtime stdout feedback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler for session logging
    log_path = os.path.join(LOG_DIR, "automation.log")
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Pre-configured logger instance
bot_logger = get_logger()
