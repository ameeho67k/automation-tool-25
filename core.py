import json
import base64
from typing import Any, Dict, Optional

def encode_roblox_data(data: Dict[str, Any]) -> str:
    """Serializes dictionary to base64 encoded JSON string."""
    raw_json = json.dumps(data, separators=(',', ':'))
    return base64.b64encode(raw_json.encode('utf-8')).decode('utf-8')

def decode_roblox_data(encoded_data: str) -> Optional[Dict[str, Any]]:
    """Decodes base64 string back into Python dictionary."""
    try:
        decoded = base64.b64decode(encoded_data).decode('utf-8')
        return json.loads(decoded)
    except (ValueError, TypeError, json.JSONDecodeError):
        return None

def validate_datastore_key(key: str) -> bool:
    """Checks if key follows standard Roblox naming conventions."""
    if not key or len(key) > 50:
        return False
    return key.isalnum() or '_' in key

def process_player_payload(payload: str) -> Dict[str, Any]:
    """Entry point for incoming Roblox network payloads."""
    data = decode_roblox_data(payload)
    if data is None:
        return {"status": "error", "message": "invalid encoding"}
    return {"status": "success", "data": data}