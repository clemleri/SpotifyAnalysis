import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_constr_regex_field,
    assert_literal
)
from constants.tests import LINKED_FROM_TYPE, LINKED_FROM_FILE_NAME


@pytest.mark.parametrize("data", [LINKED_FROM_FILE_NAME], indirect=True)
def test_linked_from_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "external_urls",
        "href",
        "id",
        "type",
        "uri"
    ]
    optional = []
    model_factory(LINKED_FROM_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [LINKED_FROM_FILE_NAME], indirect=True)
def test_linked_from_id_field(data):
    model_cls = LINKED_FROM_TYPE
    field = "id"

    # Cas valide : 22 caractères alphanumériques
    good = "1UnPDzVRkrTBflEQ9MJUhX"

    # Variantes invalides
    bad_length_small = good[:-5]           # trop court (17 caractères)
    bad_length_long  = good + "ABCD"       # trop long  (26 caractères + 4)
    bad_characters   = "1U#PDzVRkrT*flEQ9M^UhX"  # présence de #, *, ^

    invalid_values = [
        bad_length_small,
        bad_length_long,
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
    
@pytest.mark.parametrize("data", [LINKED_FROM_FILE_NAME], indirect=True)
def test_linked_from_uri_field(data):
    model_cls = LINKED_FROM_TYPE
    field = "uri"

    # Préfixe et suffixe valides
    valid_prefix = "spotify:track:"
    valid_suffix = "1UnPDzVRkrTBflEQ9MJUhX"
    valid_uri = valid_prefix + valid_suffix

    # Variantes de prefixes invalides
    bad_prefixes = [
        "",                             # absence de prefixe
        "spotify-track:",               # mauvais séparateur
        "Spotify:Track:",               # casse incorrecte
        "spotify:track",                # sans les deux-points finaux
        "spotify:/track:",              # slash en trop
    ]

    # Variantes de suffixes invalides
    bad_suffixes = [
        valid_suffix[:-4],              # trop court
        valid_suffix + "ABCD",          # trop long
        "1U#PDzVRkrT*flEQ9M^UhX",       # caractères non alphanumériques
        "",                             # suffixe vide
    ]

    # Assemblage des cas invalides :
    #   - mauvais prefixe + suffixe valide
    #   - prefixe valide + mauvais suffixe
    #   - mauvais prefixe + mauvais suffixe
    invalid_uris = []
    invalid_uris += [p + valid_suffix for p in bad_prefixes]
    invalid_uris += [valid_prefix + s for s in bad_suffixes]
    invalid_uris += [p + s for p in bad_prefixes for s in bad_suffixes]
    # cas extrêmes
    invalid_uris += ["", valid_prefix, valid_suffix]

    # Lancement des assertions
    assert_constr_regex_field(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=[valid_uri],
        invalid_values=invalid_uris
    )
    
@pytest.mark.parametrize("data", [LINKED_FROM_FILE_NAME], indirect=True)
def test_context_type_field(data):
    model_cls = LINKED_FROM_TYPE
    field = "type"
    # Valeurs valides selon le Literal
    valid_values = ["track"]
    # Valeurs invalides variées
    invalid_values = ["", "Artist", "user", "spotify:track:123", None]

    assert_literal(
        model_cls=model_cls,
        data=data,
        field=field,
        valid_values=valid_values,
        invalid_values=invalid_values
    )