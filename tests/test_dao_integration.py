# tests/test_dao_integration.py
import pytest
import requests
from dao.track_fetch_dao import TrackDAO
from dao.artist_fetch_dao import ArtistDAO
from dao.album_fetch_dao import AlbumDAO
from models.track import Track
from models.artist import Artist
from models.album import Album

class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._json

@pytest.fixture(autouse=True)
def disable_network(monkeypatch):
    """Empêche toute vraie requête HTTP pendant les tests."""
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("Network disabled")))

# -------------------------
# TrackDAO Integration tests
# -------------------------

def test_fetch_track_parses_full_response(monkeypatch):
    sample = {
        "album": {"id": "alb1", "album_type": "album", "artists": [], "available_markets": [],
                  "external_urls": {"spotify": "url"}, "href": "href", "name": "Album", "release_date": "2020-01-01",
                  "release_date_precision": "day", "total_tracks": 1, "type": "album", "uri": "uri"},
        "artists": [{"id": "art1", "name": "Artist", "external_urls": {"spotify": "url"}, "href": "href", "type": "artist", "uri": "uri"}],
        "available_markets": ["US"], "disc_number": 1, "duration_ms": 200000, "explicit": False,
        "external_ids": {"isrc": "123"}, "external_urls": {"spotify": "url"}, "href": "href",
        "id": "tr1", "name": "Track", "popularity": 50.0, "preview_url": None,
        "track_number": 1, "type": "track", "uri": "uri", "is_local": False
    }
    # Monkeypatch requests.get to return our sample
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(sample))
    dao = TrackDAO()
    track = dao.fetch_track('token', 'tr1')
    assert isinstance(track, Track)
    assert track.id == 'tr1'
    assert track.album.id == 'alb1'
    assert track.artists[0].id == 'art1'
    assert track.duration_ms == 200000

# -------------------------
# ArtistDAO Integration tests
# -------------------------

def test_fetch_artist_parses_full_response(monkeypatch):
    sample = {
        "id": "art1", "name": "Artist", "genres": ["pop"], "popularity": 10,
        "external_urls": {"spotify": "url"}, "followers": {"total": 100}, "images": [], "type": "artist", "uri": "uri"
    }
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(sample))
    dao = ArtistDAO()
    artist = dao.fetch_artist('token', 'art1')
    assert isinstance(artist, Artist)
    assert artist.id == 'art1'
    assert artist.name == 'Artist'
    assert artist.followers.total == 100

# -------------------------
# AlbumDAO Integration tests
# -------------------------

def test_fetch_album_parses_full_response(monkeypatch):
    sample = {
        "id": "alb1", "name": "Album", "album_type": "single", "total_tracks": 2,
        "available_markets": ["US"], "external_urls": {"spotify": "url"}, "href": "href",
        "release_date": "2021-05-01", "release_date_precision": "day", "type": "album", "uri": "uri",
        "artists": [{"id": "art1", "name": "Artist", "external_urls": {"spotify": "url"}, "href": "href", "type": "artist", "uri": "uri"}],
        "copyrights": [], "external_ids": {"ean": "123"}, "genres": [], "labels": "Label",
        "popularity": 20, "images": [], "tracks": {"items": []}
    }
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(sample))
    dao = AlbumDAO()
    album = dao.fetch_album('token', 'alb1')
    assert isinstance(album, Album)
    assert album.id == 'alb1'
    assert album.name == 'Album'
    assert album.total_tracks == 2
