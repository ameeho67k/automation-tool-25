class ValidationError(Exception):
    """Custom exception for automation data issues."""
    pass

def validate_roblox_input(data: dict):
    """
    Validates input schema for automation processing.
    Ensures required fields exist and types are correct.
    """
    required_fields = {'user_id', 'action_type', 'delay'}
    
    # Check for missing keys
    if not all(field in data for field in required_fields):
        raise ValidationError(f"Missing required fields: {required_fields}")

    # Validate user_id format
    if not isinstance(data['user_id'], int) or data['user_id'] <= 0:
        raise ValidationError("Invalid user_id: must be a positive integer")

    # Validate action_type against allowed list
    allowed_actions = {'trade', 'friend', 'purchase'}
    if data['action_type'] not in allowed_actions:
        raise ValidationError(f"Unsupported action: {data['action_type']}")

    # Validate delay constraints
    if not isinstance(data['delay'], (int, float)) or data['delay'] < 0:
        raise ValidationError("Invalid delay: must be a non-negative number")

    return True

def process_safe(data: dict):
    """
    Wrapper for processing validated inputs.
    """
    try:
        if validate_roblox_input(data):
            return True
    except ValidationError as e:
        return False
    return False