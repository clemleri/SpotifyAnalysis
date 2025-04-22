import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_conint_between,
    assert_positive_int
)
from constants.tests import FOLLOWERS_TYPE, FOLLOWERS_FILE_NAME


@pytest.mark.parametrize("data", [FOLLOWERS_FILE_NAME], indirect=True)
def test_followers_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "total"
    ]
    optional = [
        "href"
    ]
    model_factory(FOLLOWERS_TYPE, data, required, optional)
    
    
@pytest.mark.parametrize("data", [FOLLOWERS_FILE_NAME], indirect=True)
def test_followers_total_field(data):
    assert_positive_int(FOLLOWERS_TYPE, data, "total")
