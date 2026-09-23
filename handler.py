import json
import base64
from typing import Any, Dict, Optional

def encode_roblox_data(data: Dict[str, Any]) -> str:
    """Serializes dictionary to base64 encoded JSON string."""
    json_str = json.dumps(data)
    return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

def decode_roblox_data(encoded_str: str) -> Optional[Dict[str, Any]]:
    """Decodes base64 string back into a dictionary."""
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        return json.loads(decoded_bytes.decode('utf-8'))
    except (ValueError, TypeError, json.JSONDecodeError):
        return None

def validate_roblox_key(key: str) -> bool:
    """Checks if key follows standard Roblox data store format."""
    return bool(key and 1 <= len(key) <= 50 and key.isalnum())

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively removes null values for cleaner data transmission."""
    return {k: v for k, v in payload.items() if v is not None}

if __name__ == "__main__":
    sample = {"player_id": 12345, "score": 100, "items": None}
    sanitized = sanitize_payload(sample)
    encoded = encode_roblox_data(sanitized)
    print(f"Processed data: {encoded}")