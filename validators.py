import re

class InputValidator:
    """Utility class for validating Roblox-related automation inputs."""

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        """Checks if the user_id is a valid numeric string."""
        return bool(re.fullmatch(r'\d{5,12}', str(user_id)))

    @staticmethod
    def validate_place_id(place_id: str) -> bool:
        """Checks if the place_id is a valid numeric string."""
        return bool(re.fullmatch(r'\d{7,15}', str(place_id)))

    @staticmethod
    def validate_configuration(config: dict) -> bool:
        """Validates the core automation configuration dictionary."""
        required_keys = ['user_id', 'place_id', 'delay']
        if not all(key in config for key in required_keys):
            return False
        
        if not InputValidator.validate_user_id(config['user_id']):
            return False
            
        if not InputValidator.validate_place_id(config['place_id']):
            return False
            
        if not isinstance(config['delay'], (int, float)) or config['delay'] < 0:
            return False
            
        return True
