import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "roblox_bot", log_dir: str = "logs", level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance with stdout and rotating file handlers.
    
    Args:
        name: Logger module identifier.
        log_dir: Path to directory where log files are stored.
        level: Minimum severity level to log.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Ensure output log directory exists
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "automation.log")

    # Standard format for Roblox automation tracking
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotate logs at 5MB, keep up to 5 historical log backups
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Console handler for real-time task output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize primary logger instance for Roblox automation
bot_logger = setup_logger()
