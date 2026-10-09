import re

class RobloxInputValidator:
    """Utility to validate Roblox-specific inputs."""

    ROBLOX_ID_PATTERN = re.compile(r'^\d+$')
    ASSET_NAME_PATTERN = re.compile(r'^[a-zA-Z0-9_\s]{3,50}$')

    @staticmethod
    def validate_id(roblox_id: str) -> bool:
        """Checks if provided string is a valid numeric ID."""
        return bool(RobloxInputValidator.ROBLOX_ID_PATTERN.match(str(roblox_id)))

    @staticmethod
    def validate_asset_name(name: str) -> bool:
        """Validates asset naming conventions for safety."""
        return bool(RobloxInputValidator.ASSET_NAME_PATTERN.match(name))

    @classmethod
    def sanitize_input(cls, user_input: str) -> str:
        """Strips dangerous characters from user input."""
        return re.sub(r'[^a-zA-Z0-9_\s]', '', user_input).strip()

def validate_payload(data: dict) -> bool:
    """Batch validation logic for tool configurations."""
    required_fields = ['asset_id', 'script_name']
    for field in required_fields:
        if field not in data:
            return False
    
    return (
        RobloxInputValidator.validate_id(data['asset_id']) and
        RobloxInputValidator.validate_asset_name(data['script_name'])
    )