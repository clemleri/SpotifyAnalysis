import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_constr_regex_field,
    assert_literal
)
from constants.tests import CONTEXT_TYPE, CONTEXT_FILE_NAME


@pytest.mark.parametrize("data", [CONTEXT_FILE_NAME], indirect=True)
def test_context_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "type",
        "href",
        "external_urls",
        "uri"
    ]
    optional = []
    model_factory(CONTEXT_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [CONTEXT_FILE_NAME], indirect=True)
def test_context_uri_field(data):
    model_cls = CONTEXT_TYPE
    field = "uri"

    # suffixe de 22 caractères alphanumériques
    suffix = "1234567890abcdefABCDEF"  # longueur = 22

    # Préfixes valides pour chaque type
    valid_prefixes = [
        "spotify:artist:",
        "spotify:album:",
        "spotify:track:",
        "spotify:playlist:",
        "spotify:show:",
        "spotify:episode:"
    ]
    # Cas valides : toutes combinaisons de prefix + suffix
    valid_values = [p + suffix for p in valid_prefixes]

    # Cas invalides :
    invalid_values = []
    # mauvaise casse, absence de 'spotify:'
    invalid_values += ["Spotify:artist:" + suffix, "spotify-artist:" + suffix, suffix]
    # type invalide
    invalid_values += ["spotify:user:" + suffix, "spotify:albumx:" + suffix]
    # suffixe trop court ou trop long
    invalid_values += [valid_prefixes[0] + suffix[:-1], valid_prefixes[0] + suffix + "XYZ"]
    # caractères invalides dans le suffixe
    bad_suffix = suffix[:-3] + "!@#"
    invalid_values += [valid_prefixes[0] + bad_suffix]

    assert_constr_regex_field(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=valid_values,
        invalid_values=invalid_values
    )
    
@pytest.mark.parametrize("data", [CONTEXT_FILE_NAME], indirect=True)
def test_context_type_field(data):
    model_cls = CONTEXT_TYPE
    field = "type"
    # Valeurs valides selon le Literal
    valid_values = ["artist", "album", "track", "playlist", "show", "episode"]
    # Valeurs invalides variées
    invalid_values = ["", "Artist", "user", "spotify:track:123", None]

    assert_literal(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=valid_values,
        invalid_values=invalid_values
    )

