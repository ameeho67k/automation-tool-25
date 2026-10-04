import os
import json
import logging

def load_config(path: str) -> dict:
    """Loads and validates configuration for roblox automation."""
    default_config = {
        "retry_limit": 3,
        "timeout": 30,
        "webhook_url": None
    }

    if not os.path.exists(path):
        logging.warning("Config file missing, applying defaults")
        return default_config

    try:
        with open(path, 'r') as f:
            data = json.load(f)
            # Edge case validation for critical fields
            if not isinstance(data.get('retry_limit'), int):
                data['retry_limit'] = default_config['retry_limit']
            return data
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Config corruption detected: {e}")
        return default_config

def validate_env_vars() -> bool:
    """Checks for existence of mandatory environment secrets."""
    required = ['ROBLOSECURITY', 'API_KEY']
    missing = [var for var in required if not os.getenv(var)]
    
    if missing:
        logging.critical(f"Missing environment variables: {', '.join(missing)}")
        return False
    return True