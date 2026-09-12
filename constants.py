import sys

# performance-optimized constants for roblox automation
# cached lookups and pre-allocated memory structures

CACHE_EXPIRATION_SECONDS = 300
MAX_RETRY_ATTEMPTS = 3
ROBLOX_API_BASE = "https://api.roblox.com"

# pre-computed bitwise masks for performance
READ_ACCESS_MASK = 0b00000001
WRITE_ACCESS_MASK = 0b00000010
EXECUTE_ACCESS_MASK = 0b00000100

# memory-efficient lookup for object types
OBJECT_TYPE_MAP = {
    0: "Workspace",
    1: "Players",
    2: "Lighting",
    3: "ReplicatedStorage",
    4: "ServerScriptService"
}

# optimized buffer sizes for network transmission
CHUNK_SIZE = 4096
BUFFER_THRESHOLD = 1024 * 64

# session timeout configuration
TIMEOUT_CONFIG = {
    "connect": 5.0,
    "read": 15.0,
    "write": 10.0
}

def get_system_platform():
    """returns platform identifier for hardware optimization"""
    return sys.platform

# platform specific thread optimization constants
THREAD_COUNT = 4 if sys.platform == "win32" else 8

__all__ = [
    "CACHE_EXPIRATION_SECONDS",
    "MAX_RETRY_ATTEMPTS",
    "OBJECT_TYPE_MAP",
    "CHUNK_SIZE",
    "THREAD_COUNT"
]