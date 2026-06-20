import sys
import subprocess
from pathlib import Path
from spotify_url import SpotifyUrl
from logger import get_logger


logger = get_logger()


def get_music_directory() -> Path:
    music_dir = Path.cwd() / "downloads"
    
    if not music_dir.exists():
        logger.info(f"Creating directory: {music_dir}")
        music_dir.mkdir(parents=True, exist_ok=True)
    
    return music_dir


def build_command(url: SpotifyUrl) -> list[str]:
    output_dir = get_music_directory()
    output_template = output_dir / "{album}" / "{artist} - {title}.{output-ext}"

    return [
        "spotdl",
        url.raw,
        "--format", "mp3",
        "--bitrate", "320k",
        "--output", str(output_template),
        "--preload",
        "--threads", "3",
    ]


def download(url: SpotifyUrl) -> None:
    output_dir = get_music_directory()
    command = build_command(url)

    logger.info(f"Download directory: {output_dir}")
    logger.info(f"Running: spotdl {url.raw[:50]}...")
    logger.debug(f"Command: {' '.join(command)}")

    try:
        subprocess.run(command, check=True, capture_output=False)
        logger.info("Download completed successfully")
        logger.info(f"Files saved to: {output_dir}")
    except FileNotFoundError:
        logger.error("Command 'spotdl' not found")
        logger.error("Install it: pip install spotdl")
        sys.exit(127)
    except subprocess.CalledProcessError as e:
        logger.error(f"spotdl exited with code {e.returncode}")
        sys.exit(e.returncode)