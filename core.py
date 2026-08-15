import time
from typing import List, Dict

class PerformanceOptimized:
    def __init__(self):
        self.data_cache: Dict[str, str] = {}

    def fetch_data(self, key: str) -> str:
        if key in self.data_cache:
            return self.data_cache[key]  # Return cached data
        
        # Simulate fetching data (e.g., from an API or database)
        result = self._simulate_data_fetch(key)
        self.data_cache[key] = result  # Cache the result
        return result

    def _simulate_data_fetch(self, key: str) -> str:
        time.sleep(1)  # Simulate a delay
        return f'Data for {key}'

    def batch_fetch_data(self, keys: List[str]) -> List[str]:
        results = []
        for key in keys:
            results.append(self.fetch_data(key))
        return results

# Example usage
if __name__ == '__main__':
    optimizer = PerformanceOptimized()
    keys_to_fetch = ['key1', 'key2', 'key1']  # 'key1' will be fetched from cache
    print(optimizer.batch_fetch_data(keys_to_fetch))
