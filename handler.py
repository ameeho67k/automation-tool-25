import json
import base64

def decode_roblox_data(payload: str) -> dict:
    """Decodes base64 encoded roblox game data payload."""
    try:
        decoded_bytes = base64.b64decode(payload)
        return json.loads(decoded_bytes.decode('utf-8'))
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        return {"error": "invalid_payload", "details": str(e)}

def format_data_for_roblox(data: dict) -> str:
    """Serializes dictionary to compact JSON string."""
    return json.dumps(data, separators=(',', ':'))

def validate_game_payload(data: dict) -> bool:
    """Checks if dictionary contains core roblox keys."""
    required_keys = ['PlayerID', 'Timestamp', 'ActionID']
    return all(key in data for key in required_keys)

def process_roblox_packet(raw_packet: str) -> dict:
    """Pipeline for decoding and validating roblox packets."""
    data = decode_roblox_data(raw_packet)
    if "error" in data or not validate_game_payload(data):
        return {"status": "failed", "payload": data}
    return {"status": "success", "data": data}