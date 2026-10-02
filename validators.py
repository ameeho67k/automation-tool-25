from typing import Optional, Dict, Any

def validate_roblox_id(asset_id: Any) -> bool:
    """Verify that the provided asset ID is a positive integer.

    Args:
        asset_id: The ID to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        val = int(asset_id)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_config_schema(config: Dict[str, Any]) -> bool:
    """Ensure the configuration dictionary contains required automation keys.

    Args:
        config: The automation settings dictionary.

    Returns:
        bool: True if configuration is structurally valid.
    """
    required_keys = {'api_key', 'workspace_id', 'retries'}
    return all(key in config for key in required_keys)

def sanitize_input_string(raw_data: Optional[str]) -> str:
    """Clean strings for safe usage in Roblox API requests.

    Args:
        raw_data: The input string to clean.

    Returns:
        str: Sanitized alphanumeric string.
    """
    if not raw_data:
        return ""
    return "".join(char for char in raw_data if char.isalnum())
