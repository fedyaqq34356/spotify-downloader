# Spotify Downloader

Spotify Downloader is a simple utility for downloading tracks, albums, and playlists from Spotify.

## Features

* Download individual tracks
* Download complete albums
* Download entire playlists
* MP3 output at 320kbps
* Organized file structure by album

## Requirements

```
Python 3.10+
spotdl
```

## Installation

```
git clone https://github.com/yourusername/spotify-downloader.git
cd spotify-downloader
pip install spotdl
```

## Usage

```
python main.py
```

Steps:
1. Run the program
2. Select content type (track/album/playlist)
3. Paste Spotify URL
4. Files download to `downloads/` directory

## Output Structure

```
downloads/
├── Album Name/
│   ├── Artist - Track 1.mp3
│   └── Artist - Track 2.mp3
└── Another Album/
    └── Artist - Track 3.mp3
```

## Project Structure

```
spotify-downloader/
├── main.py              # Entry point
├── cli.py               # Interactive interface
├── core.py              # Download logic
├── spotify_url.py       # URL parsing
├── output.py            # Terminal output
├── logger.py            # Logging setup
└── README.md
```

## Configuration

Downloads are saved to `downloads/` in the current directory. Output format is `{album}/{artist} - {title}.mp3` at 320kbps bitrate.

## Logging

All operations are logged to `spotify-downloader.log` for debugging and tracking downloads.

## Notes

The tool validates URLs before downloading. If URL type doesn't match your selection, you'll be prompted to confirm or abort.

## License

GNU General Public License v3.0

This project is free software. You can redistribute it and/or modify it under the terms of the GPL v3 or any later version.

This software is provided without any warranty.

## Contributing

Pull requests are welcome. Keep changes minimal and focused.

## Author

Built with Python and spotdl.