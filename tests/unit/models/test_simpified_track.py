import pytest
from pydantic import ValidationError
from models.simplified_track import SimplifiedTrack

@pytest.mark.parametrize("data", ["simplified_track.json"], indirect=True)
def test_track_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "artists",
        "available_markets",
        "disc_number",
        "duration_ms",
        "explicit",
        "external_urls",
        "href",
        "id",
        "name",
        "track_number",
        "type",
        "uri",
        "is_local",
    ]
    optional = [
        "is_playable",
        "linked_from",
        "restrictions",
        "preview_url"
    ]
    model_factory(SimplifiedTrack, data, required, optional)
