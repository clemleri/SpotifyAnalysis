import pytest
from pydantic import ValidationError
from models.simplified_artist import SimplifiedArtist
from models.external_urls import ExternalUrls


def valid_artist_data():
    return {
        "external_urls": {"spotify": "url_artist"},
        "href": "href_artist",
        "id": "id_artist",
        "name": "name_artist",
        "type": "artist",
        "uri": "uri_artist"
    }


def test_valid_artist_parses():
    art = SimplifiedArtist.parse_obj(valid_artist_data())
    assert art.id == "id_artist"
    assert isinstance(art.external_urls, ExternalUrls)


def test_missing_field_raises():
    data = valid_artist_data()
    del data['name']
    with pytest.raises(ValidationError):
        SimplifiedArtist.parse_obj(data)