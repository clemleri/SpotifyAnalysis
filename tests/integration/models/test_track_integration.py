import json
import pytest
from pathlib import Path
from models.track import Track
from helpers.compare_models import assert_models_equal
from models.simplified_album import SimplifiedAlbum
from models.simplified_artist import SimplifiedArtist
from models.external_ids import ExternalIds
from models.external_urls import ExternalUrls

FIXTURE_PATH = Path(__file__).parent / 'data' / 'track.json'


def expected_track_oracle():
    # Créez ici un objet Track identique au JSON
    return Track.parse_obj(json.loads(FIXTURE_PATH.read_text()))


def test_track_integration_parse_from_json(tmp_path):
    raw = FIXTURE_PATH.read_text(encoding='utf-8')
    track = Track.parse_obj(json.loads(raw))
    oracle = expected_track_oracle()
    assert_models_equal(track, oracle)