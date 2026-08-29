import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation_tool_25", log_file: str = "automation.log", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if called multiple times
    if logger.hasHandlers():
        return logger

    # Ensure logs directory exists
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    # RotatingFileHandler for log rotation
    # maxBytes=1MB, backupCount=5
    file_handler = RotatingFileHandler(
        log_path, maxBytes=1024*1024, backupCount=5
    )

    file_handler.setLevel(level)

    # StreamHandler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Standard formatter
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Test if run directly
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger setup complete with rotation enabled")
    logger.debug("Debug message for testing")
    logger.warning("Sample warning log")

    # Generate logs to demonstrate rotation
    for i in range(50):
        logger.info("Test log entry number %d for rotation demo", i)
