# tests/test_dao_integration.py
import pytest
import requests
import sys
import json
from typing import List
from typing_inspect import get_parameters, get_origin
from dao.track_fetch_dao import TrackDAO
from dao.artist_fetch_dao import ArtistDAO
from dao.album_fetch_dao import AlbumDAO
from models.simplified_album import SimplifiedAlbum
from models.simplified_artist import SimplifiedArtist
from models.external_urls import ExternalUrls
from models.external_ids import ExternalIds
from models.track import Track
from models.artist import Artist
from models.album import Album
from models.image import Image

class FakeResponse:
    def __init__(self, raw_json_str, status_code=200):
        self._raw = raw_json_str
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")
          
    def raise_value_error(self, tested_value, oracle_value):
      """
        Affiche un message d'erreur du type :
        
        <tested_value>
        should be equal to :
        <oracle_value>
      """
      message = f"{tested_value}\nshould be equal to :\n{oracle_value}"
      raise ValueError(message)
    
    def json(self):
        # On parse la chaîne JSON ici, comme requests le fait en interne
        return json.loads(self._raw)

@pytest.fixture(autouse=True)
def disable_network(monkeypatch):
    """Empêche toute vraie requête HTTP pendant les tests."""
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("Network disabled")))

# -------------------------
# TrackDAO Integration tests
# -------------------------

def test_fetch_track_parses_full_response(monkeypatch):
    # Lecture du JSON brute
    with open("tests/data_test_integration/data_track.json", "r", encoding="utf-8") as f:
        sample_str = f.read()
    # Instanciation d’une seule FakeResponse que l’on réutilise
    fake_resp = FakeResponse(sample_str)

    # Monkeypatch requests.get pour toujours renvoyer fake_resp
    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: fake_resp
    )

    # Oracles
    available_markets_track_oracle = [
      "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE", "EC", "EE", "SV", "FI",
      "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA",
      "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP",
      "TH", "VN", "RO", "IL", "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY",
      "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR", "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG",
      "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS",
      "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW", "PG", "PR", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN",
      "LC", "VC", "SR", "TL", "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG",
      "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ",
      "LY", "TJ", "VE", "ET", "XK"]
    simplified_artists_oracle = [
        SimplifiedArtist(
          external_urls=ExternalUrls(spotify="https://open.spotify.com/artist/1ZZOH5sVtg6KLXJydOm43Q"),
          href="https://api.spotify.com/v1/artists/1ZZOH5sVtg6KLXJydOm43Q",
          id="1ZZOH5sVtg6KLXJydOm43Q",
          name="NoAki",
          type="artist",
          uri="spotify:artist:1ZZOH5sVtg6KLXJydOm43Q"
        )
    ]
    simplified_album_oracle = SimplifiedAlbum(
      album_type="single",
      total_tracks=2,
      available_markets= [
        "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE",
        "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU",
        "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES",
        "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL",
        "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY",
        "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR", "BD", "PK", "LK", "GH", "KE",
        "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM",
        "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR",
        "NE", "PW", "PG", "PR", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL",
        "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG",
        "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ",
        "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE", "ET", "XK"
      ],
      external_urls=ExternalUrls(spotify="https://open.spotify.com/album/7su6cRkbhOA6WpGbXMyNhF"),
      href="https://api.spotify.com/v1/albums/7su6cRkbhOA6WpGbXMyNhF",
      id="7su6cRkbhOA6WpGbXMyNhF",
      images=[
        Image(url="https://i.scdn.co/image/ab67616d0000b27357db3b359e020bad955a5bc8",height=640,width=640),
        Image(url="https://i.scdn.co/image/ab67616d00001e0257db3b359e020bad955a5bc8",height=300,width=300),
        Image(url="https://i.scdn.co/image/ab67616d0000485157db3b359e020bad955a5bc8",height=64,width=64)
      ],
      name="Igokochi",
      release_date="2025-02-14",
      release_date_precision="day",
      type="album",
      uri="spotify:album:7su6cRkbhOA6WpGbXMyNhF",
      artists=simplified_artists_oracle
    )


    # Exécution
    dao = TrackDAO()
    track = dao.fetch_track('token', '6xvbIzPvmDvk1B0QDdsoEr')

    # Assertions Track attributes types
    assert isinstance(track.album, SimplifiedAlbum)
    assert isinstance(track.artists, list)
    assert all(isinstance(artist, SimplifiedArtist) for artist in track.artists)
    assert isinstance(track.available_markets, list)
    assert all(isinstance(m, str) for m in track.available_markets)
    assert isinstance(track.disc_number, int)
    assert isinstance(track.duration_ms, float)
    assert isinstance(track.explicit, bool)
    assert isinstance(track.external_ids, ExternalIds)
    assert isinstance(track.external_urls, ExternalUrls)
    assert isinstance(track.href, str)
    assert isinstance(track.id, str)
    assert isinstance(track.name, str)
    assert track.preview_url is None or isinstance(track.preview_url, str)
    assert isinstance(track.track_number, int)
    assert isinstance(track.type, str)
    assert isinstance(track.uri, str)
    assert isinstance(track.is_local, bool)

    # Assertions Track attributes values, en utilisant fake_resp.raise_value_error
    if track.album != simplified_album_oracle:
        fake_resp.raise_value_error(track.album, simplified_album_oracle)
    if track.artists != simplified_artists_oracle:
        fake_resp.raise_value_error(track.artists, simplified_artists_oracle)
    if track.id != '6xvbIzPvmDvk1B0QDdsoEr':
        fake_resp.raise_value_error(track.id, '6xvbIzPvmDvk1B0QDdsoEr')
    if track.name != 'Igokochi':
        fake_resp.raise_value_error(track.name, 'Igokochi')
    if track.available_markets != available_markets_track_oracle:
        fake_resp.raise_value_error(track.available_markets, available_markets_track_oracle)
    if track.disc_number != 1:
        fake_resp.raise_value_error(track.disc_number, 1)
    if track.duration_ms != 94193:
        fake_resp.raise_value_error(track.duration_ms, 94193)
    if track.explicit is not False:
        fake_resp.raise_value_error(track.explicit, False)
    if track.external_ids != ExternalIds(isrc="GB8KE2503919"):
        fake_resp.raise_value_error(track.external_ids, ExternalIds(isrc="GB8KE2503919"))
    if track.external_urls != ExternalUrls(spotify="https://open.spotify.com/track/6xvbIzPvmDvk1B0QDdsoEr"):
        fake_resp.raise_value_error(track.external_urls, ExternalUrls(spotify="https://open.spotify.com/track/6xvbIzPvmDvk1B0QDdsoEr"))
    if track.href != "https://api.spotify.com/v1/tracks/6xvbIzPvmDvk1B0QDdsoEr":
        fake_resp.raise_value_error(track.href, "https://api.spotify.com/v1/tracks/6xvbIzPvmDvk1B0QDdsoEr")
    if track.popularity != 35:
        fake_resp.raise_value_error(track.popularity, 35)
    if track.preview_url is not None:
        fake_resp.raise_value_error(track.preview_url, None)
    if track.track_number != 1:
        fake_resp.raise_value_error(track.track_number, 1)
    if track.type != "track":
        fake_resp.raise_value_error(track.type, "track")
    if track.uri != "spotify:track:6xvbIzPvmDvk1B0QDdsoEr":
        fake_resp.raise_value_error(track.uri, "spotify:track:6xvbIzPvmDvk1B0QDdsoEr")
    if track.is_local is not False:
        fake_resp.raise_value_error(track.is_local, False)