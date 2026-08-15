import json
import re

# Function to validate user input

def validate_input(user_input):
    # Check if input is a valid Roblox username (alphanumeric and underscores)
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    if not re.match(pattern, user_input):
        return False, 'Invalid username'
    return True, 'Valid username'

# Main processing loop

def main_loop():
    while True:
        user_input = input('Enter Roblox username (type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break
        is_valid, message = validate_input(user_input)
        if is_valid:
            print(f'Proceeding with valid input: {user_input}')
            # Further processing of the input
        else:
            print(message)

if __name__ == '__main__':
    main_loop()