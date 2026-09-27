import time
import random

def click_element(coords: tuple[int, int], delay: float = 0.5):
    """Simulates a mouse click at specific screen coordinates."""
    x, y = coords
    print(f"[Automation] Clicking at: {x}, {y}")
    time.sleep(delay)

def find_game_instance(process_name: str = "RobloxPlayerBeta.exe") -> bool:
    """Verifies if a specific Roblox process is currently running."""
    import psutil
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def random_jitter(base_val: int, intensity: float = 0.1) -> int:
    """Adds pseudo-random jitter to integer values for anti-cheat avoidance."""
    variation = int(base_val * intensity)
    return base_val + random.randint(-variation, variation)

def wait_for_load(seconds: int = 10):
    """Pauses execution flow to allow game assets to render."""
    jittered_time = random_jitter(seconds, 0.2)
    print(f"[Automation] Waiting for {jittered_time} seconds")
    time.sleep(jittered_time)