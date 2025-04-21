"""dao/album_fetch_dao.py

Contient le DAO (Data Access Object) pour toutes les opérations liées aux albums Spotify.
Chaque méthode correspond à un endpoint REST de l'API Spotify renvoyant des albums ou leurs tracks.
"""
from typing import Any, Dict, List, Optional
import requests

from models.album import Album
from models.saved_album import SavedAlbum
from models.track import Track
from constants.api import (
    SPOTIFY_ALBUMS_URL,
    SPOTIFY_ALBUM_TRACKS_URL_TEMPLATE,
    SPOTIFY_SAVED_ALBUMS_URL,
    SPOTIFY_CHECK_SAVED_ALBUMS_URL,
)


class AlbumDAO:
    """
    Data Access Object pour les albums Spotify.
    Regroupe les méthodes de récupération d'un album, de plusieurs albums,
    des tracks d'un album, des albums sauvegardés et de la vérification des sauvegardes.
    """
    def __init__(self):
        # Endpoints configurés depuis constants/api.py
        self.url = SPOTIFY_ALBUMS_URL
        self.url_album_tracks = SPOTIFY_ALBUM_TRACKS_URL_TEMPLATE
        self.url_saved_albums = SPOTIFY_SAVED_ALBUMS_URL
        self.url_check_saved = SPOTIFY_CHECK_SAVED_ALBUMS_URL

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

    def fetch_album(
        self,
        access_token: str,
        album_id: str
    ) -> Album:
        """Récupère un album par son ID."""
        data = self._request(f"{self.url}/{album_id}", access_token)
        return Album.model_validate(data)

    def fetch_albums(
        self,
        access_token: str,
        album_ids: List[str]
    ) -> List[Album]:
        """Récupère plusieurs albums par leurs IDs conjoints."""
        query = ",".join(album_ids)
        data = self._request(f"{self.url}?ids={query}", access_token)
        return [Album.model_validate(item) for item in data.get("albums", [])]

    def fetch_album_tracks(
        self,
        access_token: str,
        album_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> List[Track]:
        """Récupère les tracks d'un album donné."""
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        url = self.url_album_tracks.format(album_id=album_id)
        data = self._request(url, access_token, params)
        return [Track.model_validate(item) for item in data.get("items", [])]

    def fetch_saved_albums(
        self,
        access_token: str,
        limit: int = 20,
        offset: int = 0
    ) -> List[SavedAlbum]:
        """Récupère les albums sauvegardés de l'utilisateur."""
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        data_albums = self._request(self.url_saved_albums, access_token, params)
        return [SavedAlbum.model_validate(data_album) for data_album in data_albums]

    def fetch_check_album_is_saved(
        self,
        access_token: str,
        album_ids: List[str]
    ) -> List[bool]:
        """Vérifie si les albums spécifiés sont sauvegardés."""
        query = ",".join(album_ids)
        data = self._request(f"{self.url_check_saved}?ids={query}", access_token)
        return data
