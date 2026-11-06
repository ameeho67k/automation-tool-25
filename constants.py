import os

# Configuration paths and default values
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_DIRECTORY = os.path.join(BASE_PATH, 'logs')

# Roblox process identification constants
ROBLOX_PROCESS_NAMES = ('RobloxPlayerBeta.exe', 'RobloxPlayerLauncher.exe')

# Network and timeout settings
DEFAULT_TIMEOUT = 30
RETRY_ATTEMPTS = 3
REQUEST_DELAY = 1.5

# Automation state constants
STATUS_IDLE = 'IDLE'
STATUS_RUNNING = 'RUNNING'
STATUS_ERROR = 'ERROR'

# Keybindings and interaction defaults
INTERACTION_KEY = 'e'
SCAN_INTERVAL = 0.5

# API endpoints
AUTH_ENDPOINT = 'https://auth.roblox.com/v1'
USER_ENDPOINT = 'https://users.roblox.com/v1'

# Supported environment flags
DEBUG_MODE = os.getenv('ROBLOX_DEBUG', 'False') == 'True'
HEADLESS_MODE = os.getenv('ROBLOX_HEADLESS', 'False') == 'True'