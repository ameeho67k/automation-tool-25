import time
from typing import List, Any

class DataProcessor:
    def __init__(self, data: List[Any]):
        self.data = data

    def process_data(self) -> List[Any]:
        start_time = time.time()
        optimized_data = self._optimize_data(self.data)
        end_time = time.time()
        print(f"Data processed in {{end_time - start_time}} seconds")
        return optimized_data

    def _optimize_data(self, data: List[Any]) -> List[Any]:
        return list(set(data))  # Removes duplicates

# Example usage
if __name__ == '__main__':
    processor = DataProcessor([1, 2, 2, 3, 4, 4, 5])
    result = processor.process_data()
    print(result)  # Output: [1, 2, 3, 4, 5]