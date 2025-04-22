# tests/test_daos.py
import pytest
import requests

from models.track import Track
from models.saved_tracks import SavedTracks
from models.play_history import PlayHistory
from models.playlist_track import PlaylistTrack
from models.artist import Artist
from models.simplified_artist import SimplifiedArtist
from models.saved_album import SavedAlbum
from models.album import Album

from dao.track_fetch_dao import TrackDAO
from dao.artist_fetch_dao import ArtistDAO
from dao.album_fetch_dao import AlbumDAO

class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._json


# TrackDAO tests

def test_fetch_track(monkeypatch):
    data = {'id': 't1'}
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    monkeypatch.setattr(Track, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_track('token', 't1') == data


def test_fetch_tracks(monkeypatch):
    items = [{'id': 't1'}, {'id': 't2'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse({'tracks': items}))
    monkeypatch.setattr(Track, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_tracks('token', ['t1', 't2']) == items


def test_fetch_saved_tracks(monkeypatch):
    data = {'saved': True}
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    monkeypatch.setattr(SavedTracks, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_saved_tracks('token') == data


def test_fetch_check_track_is_saved(monkeypatch):
    bools = [True, False]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(bools))
    dao = TrackDAO()
    assert dao.fetch_check_track_is_saved('token', ['t1', 't2']) == bools


def test_fetch_play_history(monkeypatch):
    items = [{'id': 'p1'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(items))
    monkeypatch.setattr(PlayHistory, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_play_history('token') == items


def test_fetch_top_tracks(monkeypatch):
    items = [{'id': 't1'}, {'id': 't2'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(items))
    monkeypatch.setattr(Track, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_top_tracks('token') == items


def test_fetch_playlist_item(monkeypatch):
    items = [{'id': 'pt1'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(items))
    monkeypatch.setattr(PlaylistTrack, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = TrackDAO()
    assert dao.fetch_playlist_item('token', 'pl1') == items


# ArtistDAO tests

def test_fetch_artist(monkeypatch):
    data = {'id': 'a1'}
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    monkeypatch.setattr(Artist, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = ArtistDAO()
    assert dao.fetch_artist('token', 'a1') == data


def test_fetch_artists(monkeypatch):
    items = [{'id': 'a1'}, {'id': 'a2'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse({'artists': items}))
    monkeypatch.setattr(Artist, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = ArtistDAO()
    assert dao.fetch_artists('token', ['a1', 'a2']) == items


def test_fetch_top_artists(monkeypatch):
    items = [{'id': 'sa1'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse({'items': items}))
    monkeypatch.setattr(SimplifiedArtist, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = ArtistDAO()
    assert dao.fetch_top_artists('token') == items


def test_fetch_followed_artists(monkeypatch):
    data = {'artists': ['a1']}
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    dao = ArtistDAO()
    assert dao.fetch_followed_artists('token') == data


def test_fetch_check_user_follows_artists(monkeypatch):
    bools = [True, False]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(bools))
    dao = ArtistDAO()
    assert dao.fetch_check_user_follows_artists('token', ['a1', 'a2']) == bools


# AlbumDAO tests

def test_fetch_album(monkeypatch):
    data = {'id': 'alb1'}
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    monkeypatch.setattr(Album, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = AlbumDAO()
    assert dao.fetch_album('token', 'alb1') == data


def test_fetch_albums(monkeypatch):
    items = [{'id': 'alb1'}, {'id': 'alb2'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse({'albums': items}))
    monkeypatch.setattr(Album, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = AlbumDAO()
    assert dao.fetch_albums('token', ['alb1', 'alb2']) == items


def test_fetch_album_tracks(monkeypatch):
    items = [{'id': 't1'}]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse({'items': items}))
    monkeypatch.setattr(Track, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = AlbumDAO()
    assert dao.fetch_album_tracks('token', 'alb1') == items


def test_fetch_saved_albums(monkeypatch):
    data = ["saved"]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(data))
    monkeypatch.setattr(SavedAlbum, 'model_validate', classmethod(lambda cls, obj: obj))
    dao = AlbumDAO()
    assert dao.fetch_saved_albums('token') == data


def test_fetch_check_album_is_saved(monkeypatch):
    bools = [True]
    monkeypatch.setattr(requests, 'get', lambda url, headers=None, params=None: FakeResponse(bools))
    dao = AlbumDAO()
    assert dao.fetch_check_album_is_saved('token', ['alb1']) == bools
