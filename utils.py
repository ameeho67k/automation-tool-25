import os
import json
import logging

def load_config(filepath: str) -> dict:
    """Loads configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def sanitize_path(path: str) -> str:
    """Ensures paths are absolute and normalized."""
    return os.path.normpath(os.path.abspath(path))

def setup_logger(name: str) -> logging.Logger:
    """Configures standard automation tool logging."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def validate_roblox_path(path: str) -> bool:
    """Checks if provided path contains roblox binaries."""
    return os.path.exists(os.path.join(path, 'RobloxPlayerBeta.exe'))

def get_app_data_path() -> str:
    """Retrieves user profile path for storage."""
    return os.path.join(os.environ['LOCALAPPDATA'], 'automation-tool-25')