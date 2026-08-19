import time
from typing import List

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            self.execution_times.append(elapsed_time)
            print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
            return result
        return wrapper

    @time_function
    def process_data(self, data: List[int]) -> List[int]:
        # Simulating data processing with a simple operation
        return [x * 2 for x in data]

    def get_average_time(self) -> float:
        if not self.execution_times:
            return 0.0
        return sum(self.execution_times) / len(self.execution_times)

# Example usage
optimizer = PerformanceOptimizer()
data = list(range(1000))
processed_data = optimizer.process_data(data)
average_time = optimizer.get_average_time()
print(f"Average execution time: {average_time:.4f} seconds")