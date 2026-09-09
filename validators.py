import functools
from typing import Any, Callable, Dict

# cache for validated roblox asset IDs to prevent redundant checks
_validation_cache: Dict[str, bool] = {}

def memoize_validation(func: Callable) -> Callable:
    """decorator to reduce CPU overhead on recurring lookups"""
    @functools.wraps(func)
    def wrapper(asset_id: str, *args: Any, **kwargs: Any) -> bool:
        if asset_id not in _validation_cache:
            _validation_cache[asset_id] = func(asset_id, *args, **kwargs)
        return _validation_cache[asset_id]
    return wrapper

@memoize_validation
def validate_asset_id(asset_id: str) -> bool:
    """verifies roblox asset string structure for API calls"""
    if not isinstance(asset_id, str):
        return False
    return asset_id.isdigit() and 1_000_000 <= int(asset_id) <= 9_999_999_999

def clear_cache() -> None:
    """resets validation registry to free memory"""
    _validation_cache.clear()

# pre-compile common regex patterns if needed for string parsing
# placeholder for batch processing logic if performance degrades further
