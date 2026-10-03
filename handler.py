import json
from typing import Any, Dict, Optional

class RobloxDataHandler:
    """Utility for parsing and sanitizing Roblox API data packets."""
    
    @staticmethod
    def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
        """Removes null fields and cleans key names for processing."""
        return {k: v for k, v in payload.items() if v is not None}

    @staticmethod
    def parse_roblox_json(raw_data: str) -> Optional[Dict[str, Any]]:
        """Parses raw response strings into structured dictionaries."""
        try:
            data = json.loads(raw_data)
            return data if isinstance(data, dict) else None
        except json.JSONDecodeError:
            return None

    def format_datastore_entry(key: str, value: Any, scope: str = 'global') -> str:
        """Constructs JSON strings for Roblox DataStore service."""
        structure = {
            "key": key,
            "value": value,
            "scope": scope,
            "timestamp": "server_optimized"
        }
        return json.dumps(structure)