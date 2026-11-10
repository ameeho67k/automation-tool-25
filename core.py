import time
import subprocess
from typing import Optional

def get_roblox_process_id() -> Optional[int]:
    """Finds the running Roblox process ID."""
    cmd = 'tasklist /FI "imagename eq RobloxPlayerBeta.exe" /NH'
    output = subprocess.check_output(cmd, shell=True).decode()
    parts = output.split()
    return int(parts[1]) if len(parts) > 1 else None

def inject_script(script_content: str, pid: int) -> bool:
    """Simulates script injection into the target PID."""
    try:
        print(f"Injecting into process {pid}...")
        # Placeholder for actual memory manipulation logic
        time.sleep(0.5)
        return True
    except Exception:
        return False

def wait_for_game(timeout: int = 30) -> bool:
    """Blocks until Roblox is detected or timeout reached."""
    start = time.time()
    while time.time() - start < timeout:
        if get_roblox_process_id():
            return True
        time.sleep(1)
    return False

def execute_task(task_name: str, delay: float = 1.0):
    """Standardizes delay between automation steps."""
    print(f"Executing: {task_name}")
    time.sleep(delay)