from typing import List, Dict

class RobloxHandler:
    def __init__(self, username: str, password: str) -> None:
        """Initialize the RobloxHandler with username and password."""
        self.username = username
        self.password = password

    def login(self) -> bool:
        """Logs in to the Roblox account.
        Returns True if login is successful, otherwise False."""  
        # Simulating a login process
        print(f"Logging in as {self.username}...")
        return self.username == 'valid_user' and self.password == 'secure_password'

    def fetch_game_data(self, game_id: int) -> Dict[str, str]:
        """Fetches game data for the given game ID.
        Returns a dictionary containing game data."""  
        # Simulating fetching game data
        print(f"Fetching data for game ID: {game_id}")
        return {
            'name': 'Example Game',
            'description': 'This is an example game.',
            'owner': self.username
        }

    def get_friends_list(self) -> List[str]:
        """Retrieves a list of friends for the logged-in user."""
        # Simulating fetching friends list
        print(f"Retrieving friends list for {self.username}...")
        return ['Friend1', 'Friend2', 'Friend3']

# Example usage:
if __name__ == '__main__':
    handler = RobloxHandler('valid_user', 'secure_password')
    if handler.login():
        print(handler.fetch_game_data(12345))
        print(handler.get_friends_list())