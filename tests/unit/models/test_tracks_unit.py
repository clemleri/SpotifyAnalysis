import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_non_empty_list_field
)
from constants.tests import TRACKS_TYPE, TRACKS_FILE_NAME


@pytest.mark.parametrize("data", [TRACKS_FILE_NAME], indirect=True)
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
        "items"
    ]
    optional = []
    model_factory(TRACKS_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [TRACKS_FILE_NAME], indirect=True)
def test_tracks_items_field(data):
    assert_non_empty_list_field(TRACKS_TYPE, data, "items")