import json
from typing import Any, Dict, Optional

def encode_roblox_data(data: Dict[str, Any]) -> str:
    """Converts python dictionary to a standardized JSON string for roblox API"""
    return json.dumps(data, separators=(',', ':'))

def decode_roblox_data(payload: str) -> Optional[Dict[str, Any]]:
    """Safely parses roblox response payloads with basic error handling"""
    try:
        return json.loads(payload)
    except (json.JSONDecodeError, TypeError):
        return None

def format_player_data(user_id: int, stats: Dict[str, Any]) -> Dict[str, Any]:
    """Structure player stat payloads for consistency"""
    return {
        "userId": user_id,
        "stats": stats,
        "version": "1.0.0",
        "timestamp": None  # Server should inject epoch here
    }

def sanitize_input(value: Any) -> Any:
    """Filter raw input data to prevent injection during API requests"""
    if isinstance(value, str):
        return value.replace("\"", "\'").strip()
    return value