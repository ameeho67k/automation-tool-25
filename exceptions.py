import time
import requests

class NetworkError(Exception):
    """Custom exception for network-related errors."""
    pass

def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Makes a network request with retry logic.
    Retries the request if a network error occurs.
    Args:
        url (str): The URL to fetch.
        max_retries (int): Maximum number of retry attempts.
        backoff_factor (int): Factor by which to increase wait time after each failure.
    Returns:
        Response: The response object if successful.
    Raises:
        NetworkError: Exception raised if all retries fail.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = backoff_factor * (2 ** attempt)
                time.sleep(wait_time)  # Wait before next attempt
            else:
                raise NetworkError(f'Failed to fetch {url} after {max_retries} attempts') from e
