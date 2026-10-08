import json
from typing import Any, Dict, Optional

class RobloxDataHandler:
    """Utility for processing Roblox Datastore JSON payloads."""

    @staticmethod
    def serialize(data: Any) -> str:
        """Encodes python objects to Roblox-compatible JSON strings."""
        try:
            return json.dumps(data, separators=(',', ':'))
        except (TypeError, ValueError) as e:
            raise ValueError(f"failed to serialize data: {e}")

    @staticmethod
    def deserialize(payload: str) -> Optional[Dict[str, Any]]:
        """Parses incoming Roblox Datastore JSON responses."""
        if not payload:
            return None
        return json.loads(payload)

    @staticmethod
    def sanitize_key(key: str) -> str:
        """Ensures datastore keys meet Roblox naming constraints."""
        return "".join(char for char in key if char.isalnum() or char in "-_/")

    @classmethod
    def format_datastore_payload(cls, data: Dict[str, Any], key: str) -> Dict[str, Any]:
        """Structures data for web API transmission."""
        return {
            "target": cls.sanitize_key(key),
            "body": cls.serialize(data),
            "timestamp": "auto"
        }