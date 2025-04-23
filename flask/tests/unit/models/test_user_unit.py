import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_constr_regex_field
)
from constants.tests import USER_TYPE, USER_FILE_NAME
from datetime import datetime, timezone


@pytest.mark.parametrize("data", [USER_FILE_NAME], indirect=True)
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
        "country",
        "display_name",
        "email",
        "explicit_content",
        "external_urls",
        "followers",
        "href",
        "id",
        "images",
        "product",
        "type",
        "uri"
    ]
    optional = []
    model_factory(USER_TYPE, data, required, optional)
    

