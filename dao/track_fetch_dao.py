"""dao/track_dao.py

Contient le DAO (Data Access Object) pour toutes les opérations liées aux tracks Spotify.
Chaque méthode correspond à un endpoint REST de l'API Spotify renvoyant des tracks ou des informations associées.
"""
from models.track import Track
from models.saved_tracks import SavedTracks
from models.play_history import PlayHistory
from models.playlist_track import PlaylistTrack
import requests
import json
from typing import Any, Dict, List, Optional

from constants.api import (
    SPOTIFY_TRACKS_URL,
    SPOTIFY_SAVED_TRACKS_URL,
    SPOTIFY_TRACK_IS_SAVED_URL,
    SPOTIFY_RECENT_PLAY_HISTORY_URL,
    SPOTIFY_TOP_TRACKS_URL,
    SPOTIFY_PLAYLIST_TRACKS_URL_TEMPLATE,
)


class TrackDAO:
    """
    Data Access Object pour les tracks Spotify.
    Regroupe les méthodes de récupération de tracks, saved tracks, historique de lecture,
    top tracks et items de playlist via l'API Spotify.
    """
    def __init__(self):
        # Endpoints configurés depuis constants/api.py
        self.url = SPOTIFY_TRACKS_URL
        self.url_saved_tracks = SPOTIFY_SAVED_TRACKS_URL
        self.url_track_is_saved = SPOTIFY_TRACK_IS_SAVED_URL
        self.url_play_history = SPOTIFY_RECENT_PLAY_HISTORY_URL
        self.url_top_tracks = SPOTIFY_TOP_TRACKS_URL
        self.url_playlist_tracks = SPOTIFY_PLAYLIST_TRACKS_URL_TEMPLATE

    def _request(
        self,
        url: str,
        access_token: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Méthode privée pour exécuter une requête GET sur l'API Spotify,
        gérer les headers, la validation et le parsing JSON.
        """
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def fetch_track(
        self,
        access_token: str,
        track_id: str
    ) -> Track:
        """Récupère un track par son ID."""
        data = self._request(f"{self.url}/{track_id}", access_token)
        return Track.parse_obj(data)

    def fetch_tracks(
        self,
        access_token: str,
        track_ids: List[str]
    ) -> List[Track]:
        """Récupère plusieurs tracks par leurs IDs conjoints."""
        query = ",".join(track_ids)
        data = self._request(f"{self.url}?ids={query}", access_token)
        json.dumps(data, indent=2)
        return [Track.parse_obj(item) for item in data.get("tracks", [])]

    def fetch_saved_tracks(
        self,
        access_token: str,
        market: Optional[str] = None,
        limit: int = 20,
        offset: int = 0
    ) -> SavedTracks:
        """Récupère les tracks sauvegardés de l'utilisateur."""
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if market:
            params["market"] = market
        data = self._request(self.url_saved_tracks, access_token, params)
        return SavedTracks.parse_obj(data)

    def fetch_check_track_is_saved(
        self,
        access_token: str,
        track_ids: List[str]
    ) -> List[bool]:
        """Vérifie si les tracks spécifiés sont sauvegardés."""
        query = ",".join(track_ids)
        data = self._request(f"{self.url_track_is_saved}?ids={query}", access_token)
        return data

    def fetch_play_history(
        self,
        access_token: str,
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None
    ) -> List[PlayHistory]:
        """Récupère l'historique de lecture de l'utilisateur."""
        params: Dict[str, Any] = {"limit": limit}
        if after:
            params["after"] = after
        elif before:
            params["before"] = before
        data = self._request(self.url_play_history, access_token, params)
        return [PlayHistory.parse_obj(item) for item in data]

    def fetch_top_tracks(
        self,
        access_token: str,
        time_range: str = "medium_term",
        limit: int = 20
    ) -> List[Track]:
        """Récupère les top tracks de l'utilisateur selon une plage temporelle."""
        params: Dict[str, Any] = {"time_range": time_range, "limit": limit}
        data = self._request(self.url_top_tracks, access_token, params)
        return [Track.parse_obj(item) for item in data]

    def fetch_playlist_item(
        self,
        access_token: str,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
        additional_types: str = 'track'
    ) -> List[PlaylistTrack]:
        """Récupère les items d'une playlist donnée."""
        params: Dict[str, Any] = {"limit": limit, "offset": offset, "additional_types": additional_types}
        if market:
            params["market"] = market
        if fields:
            params["fields"] = fields
        url = self.url_playlist_tracks.format(playlist_id=playlist_id)
        data = self._request(url, access_token, params)
        return [PlaylistTrack.parse_obj(item) for item in data]
