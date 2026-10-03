import os

# Roblox API and Environment Constants
ROBLOX_API_BASE = "https://apis.roblox.com"
AUTH_HEADER_KEY = "X-CSRF-TOKEN"
USER_AGENT = "automation-tool-25/1.0.0 (Roblox Automation)"

# Retry Configuration
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2

# File System Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Automation Thresholds
MIN_SLEEP_INTERVAL = 0.5
MAX_SLEEP_INTERVAL = 2.5
BATCH_SIZE = 50

# Supported Error Codes
ERR_RATE_LIMITED = 429
ERR_UNAUTHORIZED = 401
ERR_FORBIDDEN = 403

# Initialization check
def validate_paths():
    """Ensures internal directories exist for application runtime."""
    for directory in [LOG_DIR, DATA_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)

validate_paths()