import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger("automation_tool.handler")


class RobloxAPIError(Exception):
    """Base exception for Roblox API response errors."""
    pass


class RateLimitExceededError(RobloxAPIError):
    """Raised when API rate limit is hit."""

    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit hit. Retry after {retry_after}s.")


class MalformedPayloadError(RobloxAPIError):
    """Raised when response payload cannot be parsed."""
    pass


class ResponseHandler:
    """Handles and normalizes Roblox API responses with edge case support."""

    def process_response(
        self, status_code: int, raw_body: str, headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        headers = {k.lower(): v for k, v in (headers or {}).items()}

        if status_code == 429:
            retry_header = headers.get("retry-after", "60")
            try:
                retry_after = int(retry_header)
            except ValueError:
                retry_after = 60
            logger.warning("Roblox API rate limit exceeded.")
            raise RateLimitExceededError(retry_after)

        if not raw_body.strip():
            if 200 <= status_code < 300:
                return {"success": True, "data": {}}
            raise RobloxAPIError(f"HTTP {status_code}: Empty response received.")

        try:
            data = json.loads(raw_body)
        except json.JSONDecodeError as err:
            logger.error("Non-JSON response returned from Roblox endpoints.")
            raise MalformedPayloadError(
                f"HTTP {status_code}: Unparseable payload '{raw_body[:50]}...'"
            ) from err

        if status_code >= 400:
            errors = data.get("errors") if isinstance(data, dict) else None
            if errors and isinstance(errors, list) and len(errors) > 0:
                code = errors[0].get("code", "UNKNOWN")
                msg = errors[0].get("message", "No detailed message")
                raise RobloxAPIError(f"Roblox Error Code {code}: {msg}")

            msg = data.get("message", "Unknown error") if isinstance(data, dict) else "Unexpected payload format"
            raise RobloxAPIError(f"HTTP {status_code}: {msg}")

        return data if isinstance(data, dict) else {"data": data}
