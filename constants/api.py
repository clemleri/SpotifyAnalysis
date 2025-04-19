# constants/api.py
from typing import Final

# Spotify API base
SPOTIFY_API_BASE_URL: Final[str] = "https://api.spotify.com/v1"

# Endpoints tracks
SPOTIFY_TRACKS_URL: Final[str] = f"{SPOTIFY_API_BASE_URL}/tracks"
SPOTIFY_SAVED_TRACKS_URL: Final[str] = f"{SPOTIFY_API_BASE_URL}/me/tracks"
SPOTIFY_TRACK_IS_SAVED_URL: Final[str] = f"{SPOTIFY_API_BASE_URL}/me/tracks/contains"

# Endpoints player
SPOTIFY_RECENT_PLAY_HISTORY_URL: Final[str] = f"{SPOTIFY_API_BASE_URL}/me/player/recently-played"
SPOTIFY_TOP_TRACKS_URL: Final[str] = f"{SPOTIFY_API_BASE_URL}/me/top/tracks"

# Pour playlist tracks : on utilisera le .format() ou f-string au moment de l'appel
SPOTIFY_PLAYLIST_TRACKS_URL_TEMPLATE: Final[str] = f"{SPOTIFY_API_BASE_URL}/playlists/{{playlist_id}}/tracks"
