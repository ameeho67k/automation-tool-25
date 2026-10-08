import os
import shutil
import logging
from typing import List

# Configure logger for automation-tool-25
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-25')

def clean_temp_directories(directories: List[str]) -> None:
    """Removes temporary artifact directories to maintain workspace."""
    for path in directories:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                logger.info(f"Successfully cleaned: {path}")
            except OSError as e:
                logger.error(f"Error deleting {path}: {e}")

def organize_workspace(root: str, extensions: List[str]) -> None:
    """Reorganizes files by extension into subdirectory folders."""
    if not os.path.exists(root):
        return
    
    for item in os.listdir(root):
        ext = os.path.splitext(item)[1].lower()
        if ext in extensions:
            target_dir = os.path.join(root, ext[1:] or 'no_ext')
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(root, item), os.path.join(target_dir, item))

def validate_roblox_path(path: str) -> bool:
    """Verifies existence and accessibility of roblox directory."""
    return os.path.isdir(path) and os.access(path, os.W_OK)