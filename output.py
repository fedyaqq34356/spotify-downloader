import shutil


def get_terminal_width() -> int:
    return shutil.get_terminal_size(fallback=(80, 24)).columns


def print_header() -> None:
    width = get_terminal_width()
    print("=" * width)
    print("Spotify Downloader".center(width))
    print("=" * width)