def validate_user_input(user_input):
    """
    Validates the user input from Roblox platform.
    Ensures that the input meets the required criteria.
    """
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string")
    if len(user_input) < 3 or len(user_input) > 20:
        raise ValueError("Input length must be between 3 and 20 characters")
    if not user_input.isalnum():
        raise ValueError("Input must only contain alphanumeric characters")
    return True


def validate_game_id(game_id):
    """
    Validates the game ID to ensure it's a valid format.
    """
    if not isinstance(game_id, int):
        raise ValueError("Game ID must be an integer")
    if game_id <= 0:
        raise ValueError("Game ID must be a positive integer")
    return True


def validate_username(username):
    """
    Validates the username against Roblox standards.
    """
    if not isinstance(username, str):
        raise ValueError("Username must be a string")
    if len(username) < 3 or len(username) > 20:
        raise ValueError("Username length must be between 3 and 20 characters")
    if not username[0].isalpha():
        raise ValueError("Username must start with a letter")
    return True
