import json
import os
import logging

# Roblox automation tool configuration management
DEFAULT_CONFIG = {
    "place_id": 0,
    "auth_token": "",
    "retry_limit": 3,
    "timeout": 30
}

def load_config(filepath: str) -> dict:
    """Loads and validates configuration from a JSON file."""
    if not os.path.exists(filepath):
        logging.warning(f"Config file {filepath} not found. Using defaults.")
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
            
        # Validate presence of required keys
        if not isinstance(config, dict):
            raise ValueError("Invalid config format: expected dictionary")
            
        # Ensure basic schema consistency
        for key in DEFAULT_CONFIG:
            if key not in config:
                config[key] = DEFAULT_CONFIG[key]
        
        return config

    except (json.JSONDecodeError, IOError, ValueError) as e:
        logging.error(f"Failed to load config: {e}. Falling back to defaults.")
        return DEFAULT_CONFIG

def save_config(filepath: str, data: dict) -> bool:
    """Saves configuration securely to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        logging.error(f"Critical failure saving config: {e}")
        return False