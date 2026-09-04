import time
import random
import pyautogui

def sleep_random(min_sec: float = 1.0, max_sec: float = 3.0):
    """Pauses execution for a random duration to mimic human behavior."""
    time.sleep(random.uniform(min_sec, max_sec))

def click_at_element(x: int, y: int, confidence: float = 0.9):
    """Performs a mouse click at specific coordinates."""
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()

def get_screen_center():
    """Calculates screen center for game interactions."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def type_chat_message(message: str):
    """Types and sends a message in the Roblox chat."""
    pyautogui.press('/')
    sleep_random(0.1, 0.2)
    pyautogui.write(message, interval=0.05)
    pyautogui.press('enter')

def ensure_window_focus(window_title: str = "Roblox"):
    """Brings the specified application window to the foreground."""
    import pygetwindow as gw
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].activate()