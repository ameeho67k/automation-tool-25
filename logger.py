import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "roblox_automation",
    log_file: str = "logs/automation.log",
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configures and returns a logger with rotating file and console handlers
    tailored for roblox automation tasks.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Default logger instance for quick import
logger = setup_logger()
