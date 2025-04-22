import pytest
from pydantic import ValidationError, BaseModel
from tests.helpers.models.constraints import (
    assert_constr_regex_field
)
from constants.tests import SPOTIFY_ID_TYPE, SPOTIFY_ID_FILE_NAME
from datetime import datetime, timezone

class DummyModel(BaseModel):
    """Modèle factice pour tester AvailableMarkets."""
    id: SPOTIFY_ID_TYPE
    
@pytest.mark.parametrize("data", [SPOTIFY_ID_FILE_NAME], indirect=True)
def test_tracks_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "id"
    ]
    optional = []
    model_factory(DummyModel, data, required, optional)
    

@pytest.mark.parametrize("data", [SPOTIFY_ID_FILE_NAME], indirect=True)
def test_spotify_id_id_field(data):
    model_cls = DummyModel
    field = "id"

    # Cas valide : 22 caractères alphanumériques
    good = "1UnPDzVRkrTBflEQ9MJUhX"

    # Variantes invalides
    bad_length_small = good[:-5]           # trop court (17 caractères)
    bad_characters   = "1U#PDzVRkrT*flEQ9M^UhX"  # présence de #, *, ^

    invalid_values = [
        bad_length_small,
        bad_characters,
        "",             # chaîne vide
        "123456789012345678901!",  # 22 chars mais dernier non alphanum
    ]

    assert_constr_regex_field(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=[good],
        invalid_values=invalid_values
    )