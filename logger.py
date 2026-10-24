import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation-tool-25', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the automation tool."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs at 5MB, keep 3 historical backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)

        # Console output for visibility during development
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate standard logger instance for the tool
logger = setup_logger()