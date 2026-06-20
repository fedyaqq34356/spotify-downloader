import logging
import sys
from pathlib import Path


LOG_FILE = Path("spotify-downloader.log")
FORMAT = "%(asctime)s  %(levelname)-7s  %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging() -> None:
    logging.root.setLevel(logging.DEBUG)

    formatter = logging.Formatter(FORMAT, datefmt=DATE_FORMAT)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logging.root.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logging.root.addHandler(console_handler)


def get_logger(name: str = "spotify_downloader") -> logging.Logger:
    return logging.getLogger(name)