import re

class AutomationValidator:
    """Handles input sanitization for Roblox automation routines."""

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        """Checks if Roblox user ID is numeric and non-empty."""
        return bool(re.fullmatch(r'\d+', str(user_id)))

    @staticmethod
    def validate_place_id(place_id: str) -> bool:
        """Checks if place ID is a valid numeric format."""
        return bool(re.fullmatch(r'\d+', str(place_id)))

    @staticmethod
    def validate_config_key(key: str) -> bool:
        """Ensures configuration keys follow snake_case convention."""
        return bool(re.fullmatch(r'[a-z_][a-z0-9_]*', key))

    @classmethod
    def validate_payload(cls, data: dict) -> bool:
        """Validates dictionary payloads for processing."""
        required = ['user_id', 'place_id']
        if not all(k in data for k in required):
            return False
        
        return (
            cls.validate_user_id(str(data['user_id'])) and
            cls.validate_place_id(str(data['place_id']))
        )

    @staticmethod
    def sanitize_input(value: str) -> str:
        """Strips illegal characters from raw input strings."""
        return re.sub(r'[^a-zA-Z0-9_\-\s]', '', value).strip()