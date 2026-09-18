import json
import base64

def decode_roblox_data(encoded_payload: str) -> dict:
    """Decodes base64 encoded Roblox JSON strings."""
    try:
        decoded_bytes = base64.b64decode(encoded_payload)
        return json.loads(decoded_bytes.decode('utf-8'))
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return {"error": "decoding_failed", "details": str(e)}

def format_roblox_timestamp(timestamp: float) -> str:
    """Converts roblox epoch to human readable format."""
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def sanitize_robux_value(value: any) -> int:
    """Ensures currency data is treated as integer."""
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0

def process_player_stats(data: dict) -> dict:
    """Transforms raw player stat dictionaries."""
    return {
        "id": data.get("UserId", 0),
        "balance": sanitize_robux_value(data.get("AccountBalance", 0)),
        "active": data.get("IsOnline", False)
    }