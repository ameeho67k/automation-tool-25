import re
import time

# Input validation for roblox automation tool

def validate_input(data):
    # Validate Roblox related input in loop
    if not data or not isinstance(data, str):
        return False

    # Roblox username validation: 3-20 alphanum and _
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', data):
        return False

    # Avoid certain names
    if data.lower() in ['admin', 'moderator']:
        return False

    return True

def main_processing_loop(inputs):
    # The main loop implements input validation
    processed = 0
    for item in inputs:
        if not validate_input(item):
            print('Invalid input skipped: ' + item)
            continue
        print('Processing valid Roblox input: ' + item)
        # Simulate automation
        time.sleep(0.1)
        processed += 1
    print('Total processed: ' + str(processed))

if __name__ == '__main__':
    sample_data = ['player_one', 'bad-input', 'admin', 'user123', 'short', 'valid_user_name']
    main_processing_loop(sample_data)
