import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_conint_between,
    assert_conint_ge,
)
from constants.tests import PAGINATED_RESPONSE_TYPE, PAGINATED_RESPONSE_FILE_NAME


@pytest.mark.parametrize("data", [PAGINATED_RESPONSE_FILE_NAME], indirect=True)
def test_paginated_response_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "href",
        "limit",
        "offset",
        "total",
    ]
    optional = [
        "next",
        "cursors",
        "previous",
    ]
    model_factory(PAGINATED_RESPONSE_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [PAGINATED_RESPONSE_FILE_NAME], indirect=True)
def test_paginated_response_limit_field(data):
    assert_conint_between(PAGINATED_RESPONSE_TYPE, data, "limit", 1, 50)
    
@pytest.mark.parametrize("data", [PAGINATED_RESPONSE_FILE_NAME], indirect=True)
def test_paginated_response_offset_field(data):
    assert_conint_ge(PAGINATED_RESPONSE_TYPE, data, "offset", 0)
    
@pytest.mark.parametrize("data", [PAGINATED_RESPONSE_FILE_NAME], indirect=True)
def test_paginated_response_total_field(data):
    assert_conint_ge(PAGINATED_RESPONSE_TYPE, data, "total", 0)