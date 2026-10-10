import json
import base64
from typing import Any, Dict, Optional

def decode_roblox_data(raw_data: str) -> Optional[Dict[str, Any]]:
    """Decodes base64 encoded Roblox JSON payloads."""
    try:
        # Strip potential padding or formatting issues
        decoded = base64.b64decode(raw_data).decode('utf-8')
        return json.loads(decoded)
    except (json.JSONDecodeError, ValueError, TypeError) as e:
        print(f"Data decoding failure: {e}")
        return None

def format_roblox_payload(data: Dict[str, Any]) -> str:
    """Serializes data into standard Roblox compatible JSON."""
    try:
        return json.dumps(data, separators=(',', ':'))
    except TypeError as e:
        print(f"Payload serialization error: {e}")
        return "{}"

def validate_datastore_key(key: str) -> bool:
    """Checks if a key meets Roblox naming constraints."""
    # Keys must be strings and within character limits
    if not isinstance(key, str) or len(key) > 50:
        return False
    return key.isalnum() or '_' in key