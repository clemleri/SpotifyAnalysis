"""dao/artist_dao.py

Contient le DAO (Data Access Object) pour toutes les opérations liées aux artistes Spotify.
Chaque méthode correspond à un endpoint REST de l'API Spotify renvoyant des informations sur les artistes.
"""
from typing import Any, Dict, List, Optional
import requests

from models.artist import Artist
from models.simplified_artist import SimplifiedArtist
from constants.api import (
    SPOTIFY_ARTISTS_URL,
    SPOTIFY_TOP_ARTISTS_URL,
    SPOTIFY_FOLLOWED_ARTISTS_URL,
    SPOTIFY_CHECK_FOLLOWED_ARTISTS_URL_TEMPLATE,
)


class ArtistDAO:
    """
    Data Access Object pour les artistes Spotify.
    Regroupe les méthodes de récupération d'un artiste, de plusieurs artistes,
    des top artists de l'utilisateur et de la vérification des follows.
    """
    def __init__(self):
        # Endpoints configurés depuis constants/api.py
        self.url = SPOTIFY_ARTISTS_URL
        self.url_top_artists = SPOTIFY_TOP_ARTISTS_URL
        self.url_followed_artists = SPOTIFY_FOLLOWED_ARTISTS_URL
        self.url_check_followed = SPOTIFY_CHECK_FOLLOWED_ARTISTS_URL_TEMPLATE

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

    def fetch_artist(
        self,
        access_token: str,
        artist_id: str
    ) -> Artist:
        """Récupère un artiste par son ID."""
        data = self._request(f"{self.url}/{artist_id}", access_token)
        return Artist.parse_obj(data)

    def fetch_artists(
        self,
        access_token: str,
        artist_ids: List[str]
    ) -> List[Artist]:
        """Récupère plusieurs artistes par leurs IDs conjoints."""
        query = ",".join(artist_ids)
        data = self._request(f"{self.url}?ids={query}", access_token)
        return [Artist.parse_obj(item) for item in data.get("artists", [])]

    def fetch_top_artists(
        self,
        access_token: str,
        time_range: str = "medium_term",
        limit: int = 20
    ) -> List[SimplifiedArtist]:
        """Récupère les top artists de l'utilisateur selon une plage temporelle."""
        params: Dict[str, Any] = {"time_range": time_range, "limit": limit}
        data = self._request(self.url_top_artists, access_token, params)
        items = data.get("items", [])
        return [SimplifiedArtist.parse_obj(item) for item in items]

    def fetch_followed_artists(
        self,
        access_token: str,
        limit: int = 20,
        after: Optional[str] = None
    ) -> Any:
        """Récupère la liste paginée des artistes suivis par l'utilisateur."""
        params: Dict[str, Any] = {"type": "artist", "limit": limit}
        if after:
            params["after"] = after
        return self._request(self.url_followed_artists, access_token, params)

    def fetch_check_user_follows_artists(
        self,
        access_token: str,
        artist_ids: List[str]
    ) -> List[bool]:
        """Vérifie si les artistes spécifiés sont suivis par l'utilisateur."""
        query = ",".join(artist_ids)
        url = f"{self.url_check_followed}?ids={query}"
        return self._request(url, access_token)
