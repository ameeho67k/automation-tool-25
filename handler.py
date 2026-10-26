import json
from typing import Any, Dict, Optional

class RobloxDataHandler:
    """Utility for formatting and validating Roblox API data structures."""

    @staticmethod
    def sanitize_metadata(data: Dict[str, Any]) -> Dict[str, Any]:
        """Removes sensitive or unnecessary keys from API payloads."""
        ignored_keys = {'cookie', 'csrf_token', 'internal_id'}
        return {k: v for k, v in data.items() if k not in ignored_keys}

    @staticmethod
    def parse_roblox_json(raw_string: str) -> Optional[Dict[str, Any]]:
        """Safe parsing of Roblox endpoint JSON responses."""
        try:
            data = json.loads(raw_string)
            if 'errors' in data:
                return None
            return data
        except (json.JSONDecodeError, TypeError):
            return None

    @staticmethod
    def format_player_payload(user_id: int, place_id: int) -> str:
        """Creates a standard payload for Roblox join requests."""
        payload = {
            "userId": user_id,
            "placeId": place_id,
            "settings": {
                "isTeleport": True,
                "joinSource": "automation-tool-25"
            }
        }
        return json.dumps(payload)