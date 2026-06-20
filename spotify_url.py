from dataclasses import dataclass
from typing import Literal


ContentType = Literal["track", "album", "playlist"]


@dataclass(frozen=True)
class SpotifyUrl:
    raw: str

    def is_valid(self) -> bool:
        return "spotify.com" in self.raw.lower()

    def get_type(self) -> ContentType | None:
        url_lower = self.raw.lower()
        if "/track/" in url_lower:
            return "track"
        if "/album/" in url_lower:
            return "album"
        if "/playlist/" in url_lower:
            return "playlist"
        return None

    def matches_expected(self, expected: ContentType) -> bool:
        actual = self.get_type()
        return actual is None or actual == expected


def parse_choice(choice: str) -> ContentType:
    mapping = {"1": "track", "2": "album", "3": "playlist"}
    if choice.strip() in mapping:
        return mapping[choice.strip()]
    raise ValueError("Invalid choice")