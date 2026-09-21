import re

# Validation logic for roblox-specific identifiers
def validate_roblox_input(user_input: str) -> bool:
    """Validates roblox game IDs and user IDs format."""
    if not isinstance(user_input, str):
        return False
    
    # Roblox IDs consist of digits, typical range 1 to 15 digits
    pattern = r'^\d{1,15}$'
    return bool(re.match(pattern, user_input))

def sanitize_input(user_input: str) -> str:
    """Removes non-numeric characters for system safety."""
    return re.sub(r'\D', '', user_input)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass