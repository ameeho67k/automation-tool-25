import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "roblox_automation",
    log_dir: str = "logs",
    log_file: str = "bot.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5
) -> logging.Logger:
    """
    Configures and returns a logger instance with console and rotating file handlers.
    Designed for multi-threaded Roblox automation scripts.
    """
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        filename=file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    return logger


def get_session_logger(account_id: Optional[str] = None) -> logging.Logger:
    """Helper to retrieve logger scoped for specific Roblox account sessions."""
    logger_name = f"roblox_session.{account_id}" if account_id else "roblox_session"
    return setup_logger(name=logger_name, log_file="session_activity.log")
