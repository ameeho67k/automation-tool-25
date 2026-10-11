import os

# Roblox automation configurations and system constants
ROBLOX_PROCESS_NAME = "RobloxPlayerBeta.exe"
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2.0

# API endpoints and memory addresses
API_BASE_URL = "https://apis.roblox.com"
MEMORY_OFFSET_BASE = 0x400000

# Error handling constants
TIMEOUT_THRESHOLD = 30.0
POLL_RATE_HZ = 10

# Path validations
EXECUTABLE_PATH = os.getenv("ROBLOX_PATH", "C:\\Program Files (x86)\\Roblox\\Versions")

class AutomationConstants:
    """Static configuration class for environment and system parameters."""
    @classmethod
    def get_retry_config(cls):
        return {
            "max_retries": MAX_RETRIES,
            "delay": RETRY_DELAY_SECONDS,
            "timeout": TIMEOUT_THRESHOLD
        }

# Standard error messages for edge cases
ERROR_MESSAGES = {
    "PROCESS_NOT_FOUND": "Target Roblox process could not be identified",
    "MEMORY_ACCESS_DENIED": "Insufficient permissions for memory manipulation",
    "CONNECTION_LOST": "Network connectivity to Roblox services interrupted",
    "TIMEOUT_EXCEEDED": "Operation timed out after reaching threshold"
}