import json
import base64
from typing import Any, Dict, Optional

def decode_roblox_json(payload: str) -> Optional[Dict[str, Any]]:
    """Decodes standard Roblox API JSON strings with error handling."""
    try:
        data = json.loads(payload)
        return data
    except (json.JSONDecodeError, TypeError):
        return None

def format_player_data(user_id: int, username: str, rank: int) -> Dict[str, Any]:
    """Structures raw player attributes for internal processing."""
    return {
        "id": user_id,
        "name": username,
        "rank": rank,
        "is_premium": rank > 0
    }

def encode_session_token(data: Dict[str, Any]) -> str:
    """Serializes dictionary data into a base64 encoded string."""
    raw_json = json.dumps(data)
    return base64.b64encode(raw_json.encode('utf-8')).decode('utf-8')

def validate_universe_id(universe_id: Any) -> bool:
    """Checks if provided ID meets Roblox numeric requirements."""
    if not isinstance(universe_id, int):
        return False
    return universe_id > 0
