import json
import base64
from typing import Any, Dict, Optional

def decode_roblox_datastore(raw_payload: str) -> Optional[Dict[str, Any]]:
    """Decodes base64 encoded Roblox DataStore strings."""
    try:
        decoded_bytes = base64.b64decode(raw_payload)
        return json.loads(decoded_bytes.decode('utf-8'))
    except (ValueError, KeyError, json.JSONDecodeError):
        return None

def serialize_roblox_data(data: Dict[str, Any]) -> str:
    """Serializes Python dicts for DataStore upload."""
    return json.dumps(data, separators=(',', ':'))

def sanitize_roblox_value(value: Any) -> Any:
    """Enforces strict type compatibility for Roblox API."""
    if isinstance(value, (int, float, str, bool)):
        return value
    if isinstance(value, list):
        return [sanitize_roblox_value(v) for v in value]
    if isinstance(value, dict):
        return {str(k): sanitize_roblox_value(v) for k, v in value.items()}
    return str(value)