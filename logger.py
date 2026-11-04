import os
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "roblox_automation.log"

def setup_logger(name="roblox_bot", log_level=logging.INFO, max_bytes=5_000_000, backup_count=5):
    """Configure and return a logger instance with rotating file and console output."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)

    log_path = os.path.join(LOG_DIR, LOG_FILE)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if function is called multiple times
    if logger.hasHandlers():
        return logger

    # Output format tailored for automation debugging
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotating file handler to prevent giant log files during extended bot runs
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)

    # Console handler for real-time output monitoring
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Main logger instance for global import
bot_logger = setup_logger()
