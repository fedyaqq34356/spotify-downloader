import sys
from spotify_url import ContentType, SpotifyUrl, parse_choice
from output import print_header
from core import download
from logger import get_logger


logger = get_logger()


def ask_content_type() -> ContentType:
    print("\nWhat do you want to download?")
    print("  1  Track")
    print("  2  Album")
    print("  3  Playlist")

    while True:
        choice = input("\nChoice (1-3): ").strip()
        try:
            content_type = parse_choice(choice)
            logger.debug(f"User selected: {content_type}")
            return content_type
        except ValueError:
            logger.warning("Invalid choice entered")
            print("Please enter 1, 2 or 3")


def ask_url(expected_type: ContentType) -> SpotifyUrl:
    print("\nPaste Spotify URL:")
    raw_url = input().strip()

    url = SpotifyUrl(raw_url)
    logger.debug(f"User provided URL: {raw_url}")

    if not url.is_valid():
        logger.error("Invalid Spotify URL")
        print("Error: URL does not contain spotify.com")
        sys.exit(1)

    if not url.matches_expected(expected_type):
        actual = url.get_type()
        logger.warning(f"Type mismatch: expected {expected_type}, got {actual}")
        print(f"Warning: URL appears to be {actual}, but you selected {expected_type}")
        
        if input("Continue anyway? [y/N] ").strip().lower() != "y":
            logger.info("User aborted due to type mismatch")
            print("Aborted")
            sys.exit(0)

    return url


def run_interactive() -> None:
    print_header()
    content_type = ask_content_type()
    url = ask_url(content_type)
    download(url)