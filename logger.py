import logging
import time
from functools import wraps

# Configure the logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Retry decorator for handling network operations

def retry(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logger.warning(f'Attempt {attempts} failed with error: {e}')
                    if attempts >= max_retries:
                        logger.error('Max retries reached. Operation failed.')
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Example function that could fail due to network issues
@retry(max_retries=5, delay=3)
def fetch_data_from_api(url):
    # Simulating a network operation
    if url == 'http://fail.com':
        raise ConnectionError('Failed to connect')
    return {'data': 'success'}
