import json
import base64
from typing import Any, Dict, Optional

class RobloxDataHandler:
    """Utility for processing and encoding Roblox game data structures."""

    @staticmethod
    def serialize_data(data: Dict[str, Any]) -> str:
        """Converts dictionary to JSON and encodes for transport."""
        json_string = json.dumps(data)
        return base64.b64encode(json_string.encode('utf-8')).decode('utf-8')

    @staticmethod
    def deserialize_data(encoded_data: str) -> Optional[Dict[str, Any]]:
        """Decodes base64 string back into a Python dictionary."""
        try:
            decoded_bytes = base64.b64decode(encoded_data)
            return json.loads(decoded_bytes.decode('utf-8'))
        except (ValueError, TypeError, json.JSONDecodeError):
            return None

    def format_player_payload(user_id: int, assets: list) -> Dict[str, Any]:
        """Constructs standardized payload for Roblox API interaction."""
        return {
            "target_user": user_id,
            "asset_list": assets,
            "version": "1.0.0",
            "timestamp": "auto"
        }