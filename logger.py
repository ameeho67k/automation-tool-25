import logging

# Configuring the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('roblox_data.log'),
        logging.StreamHandler()
    ]
)

# Utility functions for logging

def log_info(message: str) -> None:
    """Logs an info message."""
    logging.info(message)


def log_warning(message: str) -> None:
    """Logs a warning message."""
    logging.warning(message)


def log_error(message: str) -> None:
    """Logs an error message."""
    logging.error(message)


def log_debug(message: str) -> None:
    """Logs a debug message."""
    logging.debug(message)


def log_exception(exc: Exception) -> None:
    """Logs an exception with traceback."""
    logging.exception(exc)