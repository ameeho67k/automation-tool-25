import json
import os

DEFAULT_CONFIG = {
    'username': 'Player',
    'server': 'localhost',
    'port': 5432,
    'game_mode': 'casual',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config = {**DEFAULT_CONFIG, **user_config}

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

# Example usage: 
# loader = ConfigLoader()
# print(loader.get('username'))
# loader.set('username', 'NewPlayer')
