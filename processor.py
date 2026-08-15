import json
import requests
from requests.exceptions import RequestException

class RobloxProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint):
        url = f'{self.api_url}/{endpoint}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except RequestException as e:
            print(f'Error fetching data from {url}: {e}')  
            return None
        except json.JSONDecodeError:
            print(f'Error decoding JSON response from {url}')
            return None

    def process_data(self, data):
        if not data:
            print('No data to process.')
            return
        # Assuming data needs to be a dictionary
        if not isinstance(data, dict):
            print('Expected data to be a dictionary.')
            return
        # Process the data
        print(f'Processing data: {data}')

    def run(self, endpoint):
        data = self.fetch_data(endpoint)
        self.process_data(data)

if __name__ == '__main__':
    processor = RobloxProcessor('https://api.example.com')
    processor.run('dummy_endpoint')