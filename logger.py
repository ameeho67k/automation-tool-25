import logging

# Setting up the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to log messages

def log_message(message):
    if not isinstance(message, str):
        raise ValueError('Message must be a string')
    logger.info(message)

# Main processing loop

def main_process(data_list):
    for data in data_list:
        try:
            if not isinstance(data, dict):
                raise ValueError('Each item must be a dictionary')
            log_message(f'Processed data: {data}')
        except ValueError as ve:
            logger.error(f'ValueError: {ve}')
        except Exception as e:
            logger.error(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    sample_data = [{'key1': 'value1'}, {'key2': 'value2'}, 'invalid']  # Invalid entry for demonstration
    main_process(sample_data)