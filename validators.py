def validate_input(user_input):
    """
    Validates user input for the automation tool.
    Checks if the input is a non-empty string and contains only allowed characters.
    """
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if any(char not in allowed_characters for char in user_input):
        raise ValueError('Input contains invalid characters.')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter the command: ')
        try:
            validate_input(user_input)
            # Further processing of validated input
            print(f'Processing command: {user_input}')
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main_processing_loop()