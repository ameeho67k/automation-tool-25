import logging
import sys
from functools import lru_cache

# Configure optimized logger for roblox automation throughput
logger = logging.getLogger('automation-tool-25')

@lru_cache(maxsize=128)
def get_logger(name: str) -> logging.Logger:
    """Cache logger instances to minimize memory overhead"""
    instance = logging.getLogger(name)
    instance.setLevel(logging.INFO)
    return instance

def setup_logging(level: int = logging.INFO):
    """Initialize handler with non-blocking stream access"""
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(level)

class PerformanceLogger:
    """Static utility for high-frequency event logging"""
    @staticmethod
    def log_event(message: str):
        """Writes log directly to output buffer"""
        if logger.isEnabledFor(logging.INFO):
            logger.info(message)

# Instantiate core logger
setup_logging()