import logging
import sys
import os
from datetime import datetime

def setup_logger(name: str, log_dir: str = 'logs') -> logging.Logger:
    """Configures a robust logger with file system edge case handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    try:
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
    except (PermissionError, OSError) as e:
        # Fallback to stderr if directory creation fails due to permissions
        print(f"Critical: Could not create log directory {log_dir}: {e}", file=sys.stderr)
        return logger

    log_path = os.path.join(log_dir, f"automation_{datetime.now().strftime('%Y-%m-%d')}.log")
    
    try:
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    except (IOError, OSError) as e:
        # Fallback if specific file is inaccessible or disk is full
        stream_handler = logging.StreamHandler(sys.stderr)
        logger.addHandler(stream_handler)
        logger.error(f"Logging file failure: {e}. Falling back to console output.")

    return logger