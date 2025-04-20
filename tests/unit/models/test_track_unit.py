import pytest
from pydantic import ValidationError
from models.track import Track
from models.simplified_album import SimplifiedAlbum
from models.simplified_artist import SimplifiedArtist
from models.external_ids import ExternalIds
from models.external_urls import ExternalUrls

# Fixture minimale pour un Track valide
def valid_track_data():
    return {
        "album": {
            "album_type": "single",
            "artists": [{
                "external_urls": {"spotify": "url_artist"},
                "href": "href_artist",
                "id": "id_artist",
                "name": "name_artist",
                "type": "artist",
                "uri": "uri_artist"
            }],
            "available_markets": ["US", "FR"],
            "external_urls": {"spotify": "url_album"},
            "href": "href_album",
            "id": "id_album",
            "images": [],
            "name": "AlbumName",
            "release_date": "2021-01-01",
            "release_date_precision": "day",
            "total_tracks": 1,
            "type": "album",
            "uri": "uri_album"
        },
        "artists": [{
            "external_urls": {"spotify": "url_artist"},
            "href": "href_artist",
            "id": "id_artist",
            "name": "name_artist",
            "type": "artist",
            "uri": "uri_artist"
        }],
        "available_markets": ["US", "FR"],
        "disc_number": 1,
        "duration_ms": 123456,
        "explicit": False,
        "external_ids": {"isrc": "CODE123"},
        "external_urls": {"spotify": "url_track"},
        "href": "href_track",
        "id": "id_track",
        "name": "TrackName",
        "popularity": 50,
        "preview_url": None,
        "track_number": 1,
        "type": "track",
        "uri": "uri_track",
        "is_local": False
    }


def test_valid_track_parses_without_errors():
    data = valid_track_data()
    track = Track.parse_obj(data)
    assert track.id == "id_track"
    assert isinstance(track.album, SimplifiedAlbum)
    assert isinstance(track.artists, list)


def test_missing_required_field_raises():
    data = valid_track_data()
    del data['id']
    with pytest.raises(ValidationError):
        Track.parse_obj(data)


def test_wrong_type_field_raises():
    data = valid_track_data()
    data['duration_ms'] = 'not_a_number'
    with pytest.raises(ValidationError):
        Track.parse_obj(data)
        
def test_optional_fields_default_to_none():
    data = valid_track_data()
    data.pop("is_playable", None)
    data.pop("linked_from", None)
    data.pop("restrictions", None)
    data.pop("preview_url", None)
    track = Track.parse_obj(data)
    assert track.is_playable is None
    assert track.linked_from is None
    assert track.restrictions is None
    assert track.preview_url is None

def test_optional_fields_parsed_when_present():
    data = valid_track_data()
    data["is_playable"] = True
    data["preview_url"] = "http://exemple"
    # Fournir un dummy minimal pour linked_from et restrictions
    data["linked_from"] = {"uri": "uri_from", "href": "href_from", "id": "id_from"}
    data["restrictions"] = {"reason": "market"}
    track = Track.parse_obj(data)
    assert track.is_playable is True
    assert track.preview_url == "http://exemple"
    assert track.linked_from.id == "id_from"
    assert track.restrictions.reason == "market"
