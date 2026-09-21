"""Roblox automation constants and configuration defaults."""

from enum import Enum, IntEnum


class RobloxAPIEndpoint(str, Enum):
    """Base endpoints for Roblox Web APIs."""
    USERS = "https://users.roblox.com"
    PRESENCE = "https://presence.roblox.com"
    GROUPS = "https://groups.roblox.com"
    ECONOMY = "https://economy.roblox.com"
    ASSETS = "https://assetdelivery.roblox.com"
    GAMES = "https://games.roblox.com"


class AssetType(IntEnum):
    """Common Roblox asset type IDs."""
    IMAGE = 1
    AUDIO = 3
    MESH = 4
    LUA = 5
    HAT = 8
    PLACE = 9
    MODEL = 10
    SHIRT = 11
    PANTS = 12
    ANIMATION = 24


# Request limits and timeouts
DEFAULT_TIMEOUT_SECONDS: int = 15
MAX_RETRIES: int = 3
RATE_LIMIT_COOLDOWN_SECONDS: float = 2.5

# Default HTTP Headers for bot requests
DEFAULT_HEADERS: dict[str, str] = {
    "User-Agent": "RobloxAutomationTool/2.5",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Roblox Cookie key name
ROBLOSECURITY_COOKIE_NAME: str = ".ROBLOSECURITY"
