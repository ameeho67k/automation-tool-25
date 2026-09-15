import logging
import sys
from functools import lru_cache

@lru_cache(maxsize=128)
def get_logger(name: str) -> logging.Logger:
    """Creates and configures a cached logger instance."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_performance(func):
    """Decorator to track execution duration for optimization."""
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 0.1:
            get_logger('perf').warning(f'{func.__name__} took {duration:.4f}s')
        return result
    return wrapper