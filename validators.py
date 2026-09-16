import re

class InputValidator:
    """
    Validates incoming roblox asset identifiers and user inputs
    to prevent malformed processing in automation-tool-25.
    """
    
    ROBLOX_ID_PATTERN = re.compile(r'^\d+$')
    MAX_NAME_LENGTH = 50

    @staticmethod
    def validate_asset_id(asset_id: str) -> bool:
        """Ensure asset_id is a positive integer string."""
        if not asset_id or not InputValidator.ROBLOX_ID_PATTERN.match(asset_id):
            return False
        return int(asset_id) > 0

    @staticmethod
    def validate_task_name(name: str) -> bool:
        """Verify task name meets naming convention requirements."""
        if not name or len(name) > InputValidator.MAX_NAME_LENGTH:
            return False
        return name.isalnum() or '_' in name

    @classmethod
    def process_input(cls, asset_id: str, task_name: str):
        """Main validation gate for processing logic."""
        if not cls.validate_asset_id(asset_id):
            raise ValueError(f"Invalid Roblox Asset ID: {asset_id}")
            
        if not cls.validate_task_name(task_name):
            raise ValueError(f"Invalid task name format: {task_name}")
            
        return True