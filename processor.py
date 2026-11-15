import logging
from typing import Dict, List, Any

logger = logging.getLogger("automation.processor")

class AssetProcessingError(Exception):
    """Raised when asset data fails standard processing rules."""
    pass

class AssetProcessor:
    """Processes Roblox asset responses and normalizes data for automation tasks."""

    def __init__(self, max_retries: int = 3, retry_delay: float = 1.0):
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def parse_asset_item(self, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extracts essential asset fields with strict edge case validation."""
        if not isinstance(item_data, dict):
            raise AssetProcessingError("Payload item must be a dictionary")

        asset_id = item_data.get("id") or item_data.get("assetId")
        if not asset_id or not str(asset_id).isdigit():
            raise AssetProcessingError(f"Invalid or missing asset ID: {asset_id}")

        # Handle non-standard price representations and null values
        price = item_data.get("price")
        if price is None or not isinstance(price, (int, float)) or price < 0:
            logger.warning(f"Asset {asset_id} has invalid price '{price}'. Defaulting to 0.")
            price = 0

        creator_info = item_data.get("creator") or {}
        creator_id = creator_info.get("id", 0) if isinstance(creator_info, dict) else 0

        return {
            "asset_id": int(asset_id),
            "name": str(item_data.get("name", "Unknown Asset")).strip(),
            "price": int(price),
            "is_purchasable": bool(item_data.get("isPurchasable", False)) and not bool(item_data.get("isOffSale", False)),
            "creator_id": int(creator_id)
        }

    def batch_process(self, raw_assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Processes a list of raw asset records, skipping invalid items safely."""
        if not isinstance(raw_assets, list):
            logger.error("Expected list for raw_assets batch processing")
            return []

        processed = []
        for item in raw_assets:
            try:
                result = self.parse_asset_item(item)
                processed.append(result)
            except AssetProcessingError as err:
                logger.warning(f"Skipping invalid asset payload: {err}")
            except Exception as err:
                logger.error(f"Unexpected error processing asset payload: {err}")
        return processed