import pytest
from pydantic import ValidationError, BaseModel
from tests.helpers.models.constraints import (
    assert_constr_regex_field
)
from constants.tests import AVAILABLE_MARKETS_TYPE, AVAILABLE_MARKETS_FILE_NAME
from datetime import datetime, timezone


class DummyModel(BaseModel):
    """Modèle factice pour tester AvailableMarkets."""
    available_markets: AVAILABLE_MARKETS_TYPE


@pytest.mark.parametrize("data", [AVAILABLE_MARKETS_FILE_NAME], indirect=True)
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
        "available_markets"
    ]
    optional = []
    model_factory(DummyModel, data, required, optional)
    
@pytest.mark.parametrize("data", [AVAILABLE_MARKETS_FILE_NAME], indirect=True)
def test_available_markets_available_markets_field(data):
    model_cls = DummyModel
    field = "available_markets"
    # Cas valides : un ou plusieurs codes ISO 3166‑1 alpha‑2
    valid_lists = [
        ["FR"],
        ["US", "DE", "GB"],
    ]
    
    # Cas invalides : 
    #   - codes trop courts ou longs
    #   - lowercase
    #   - caractères non alphabétiques
    invalid_lists = [
        ["F"],          # trop court
        ["USA"],        # trop long
        ["fr"],         # lowercase
        ["1A"],         # chiffre + lettre
        ["?!"],         # caractères spéciaux
    ]
    assert_constr_regex_field(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=valid_lists,
        invalid_values=invalid_lists
    )