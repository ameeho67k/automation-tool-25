import time

class PerformanceOptimized:
    def __init__(self):
        self.data_cache = {}

    def compute_heavy_task(self, input_data):
        if input_data in self.data_cache:
            return self.data_cache[input_data]

        # Simulate a heavy computation
        time.sleep(2)  # Simulate time-consuming task
        result = sum(input_data)  # Example computation
        self.data_cache[input_data] = result  # Cache result
        return result

    def clear_cache(self):
        self.data_cache.clear()

# Example usage
if __name__ == '__main__':
    perf_opt = PerformanceOptimized()
    result = perf_opt.compute_heavy_task((1, 2, 3, 4))  # First call, computes
    print(result)
    result = perf_opt.compute_heavy_task((1, 2, 3, 4))  # Second call, retrieves from cache
    print(result)