import sys

# Roblox automation performance configuration
# Pre-computed constants to minimize runtime calculations

# Frame-rate throttling targets
TARGET_FPS = 60
FRAME_INTERVAL = 1.0 / TARGET_FPS

# Memory management thresholds for long-running sessions
MAX_MEMORY_MB = 1024
CACHE_CLEANUP_INTERVAL = 300

# API request rate-limiting (Roblox-specific constraints)
MAX_REQUESTS_PER_SECOND = 10
REQUEST_TIMEOUT_SECONDS = 5.0

# Optimization toggles for CPU-bound tasks
ENABLE_MULTI_THREADING = True
BATCH_PROCESSING_SIZE = 50

# Static coordinate mapping for fast lookup
UI_ELEMENT_OFFSETS = {
    "main_menu": (0, 0),
    "play_button": (150, 200),
    "settings_tab": (300, 50)
}

# Byte-level packet structure headers
PACKET_HEADER_SIZE = 8
BUFFER_SIZE = 4096

def get_performance_mode():
    """Returns high-performance settings based on system load."""
    return {
        "fps": TARGET_FPS,
        "batch": BATCH_PROCESSING_SIZE,
        "threads": ENABLE_MULTI_THREADING
    }