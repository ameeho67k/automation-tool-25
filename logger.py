import os
import sys
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "roblox_automation", log_dir: str = "logs", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a logger instance with rotating file handlers."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if setup is called multiple times
    if logger.handlers:
        return logger

    # Format structure for output
    log_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output for terminal display
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Rotating file handler (5 MB max size, keeps 3 backups)
    log_file_path = os.path.join(log_dir, "bot_activity.log")
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    logger.info("Logger initialized for Roblox automation operations")
    return logger

# Initialize default logger instance
bot_logger = setup_logger()