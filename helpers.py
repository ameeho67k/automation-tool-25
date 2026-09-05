import json
from typing import Any, Dict, Optional

def encode_roblox_data(data: Dict[str, Any]) -> str:
    """Encodes dictionary to a minified JSON string for Roblox endpoints."""
    return json.dumps(data, separators=(',', ':'))

def decode_roblox_response(response_text: str) -> Optional[Dict[str, Any]]:
    """Parses JSON response from Roblox API with basic error handling."""
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return None

def format_roblox_timestamp(timestamp: str) -> str:
    """Converts ISO 8601 Roblox timestamps to standard format."""
    return timestamp.replace('T', ' ').replace('Z', '')

def validate_universe_id(universe_id: Any) -> bool:
    """Checks if provided ID is a valid positive integer."""
    try:
        val = int(universe_id)
        return val > 0
    except (ValueError, TypeError):
        return False