import logging
import sys
from pathlib import Path
from typing import Any, Optional

class SafeRobloxLogger:
    """Logger wrapper providing edge-case handling for Roblox automation tasks."""

    def __init__(self, name: str = "RobloxAuto", log_file: Optional[str] = "logs/automation.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.log_file = log_file
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Standard console handler as primary output/fallback
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if not self.log_file:
            return

        # Edge case: handle non-existent directories and permission errors
        try:
            log_path = Path(self.log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(log_path, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except (PermissionError, OSError) as err:
            self.logger.warning(
                f"Could not create log file at '{self.log_file}': {err}. Using console only."
            )

    def log_safely(self, level: str, message: Any) -> None:
        """Safely logs arbitrary data types, handling invalid levels and format errors."""
        # Edge case: sanitize non-string or corrupted log payloads
        try:
            formatted_msg = str(message) if not isinstance(message, str) else message
        except Exception as str_err:
            formatted_msg = f"[Unstringifiable payload: {type(message).__name__}] (err: {str_err})"

        # Edge case: fallback for invalid/unrecognized log levels
        numeric_level = getattr(logging, str(level).upper(), None)
        if not isinstance(numeric_level, int):
            numeric_level = logging.INFO
            formatted_msg = f"[Invalid Level '{level}'] {formatted_msg}"

        try:
            self.logger.log(numeric_level, formatted_msg)
        except Exception as err:
            sys.stderr.write(f"Logger failure while recording event: {err}\n")
