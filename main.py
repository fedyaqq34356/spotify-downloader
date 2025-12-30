import sys
from cli import run_interactive
from logger import setup_logging, get_logger


logger = get_logger()


def main() -> None:
    setup_logging()
    logger.info("Starting Spotify Downloader")

    try:
        run_interactive()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        logger.info("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.exception("Unexpected error occurred")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
