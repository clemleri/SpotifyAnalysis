import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_conint_between,
    assert_constr_regex_field,
    assert_conint_between,
    assert_non_empty_list_field,
    assert_non_empty_str_field,
    assert_conint_ge,
    assert_positive_int,
    assert_literal
)
from constants.tests import ARTIST_TYPE, ARTIST_FILE_NAME


@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_model(data, model_factory):
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
        "name",
        "type",
        "uri",
    ]
    optional = []
    model_factory(ARTIST_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_id_field(data):
    model_cls = ARTIST_TYPE
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

@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_name_field(data):
    assert_non_empty_str_field(ARTIST_TYPE, data, "name")
    
@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_type_field(data):
    valid_values=['artist']
    invalid_values=['album', 'track', 'episode', 'playlist']
    assert_literal(ARTIST_TYPE, data, "type", valid_values, invalid_values)
    
@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_uri_field(data):
    model_cls = ARTIST_TYPE
    field = "uri"

    # Préfixe et suffixe valides
    valid_prefix = "spotify:artist:"
    valid_suffix = "1UnPDzVRkrTBflEQ9MJUhX"
    valid_uri = valid_prefix + valid_suffix

    # Variantes de prefixes invalides
    bad_prefixes = [
        "",                             # absence de prefixe
        "spotify-artist:",               # mauvais séparateur
        "Spotify:artist:",               # casse incorrecte
        "spotify:artist",                # sans les deux-points finaux
        "spotify:/artist:",              # slash en trop
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

@pytest.mark.parametrize("data", [ARTIST_FILE_NAME], indirect=True)
def test_artist_popularity_field(data):
    assert_conint_between(ARTIST_TYPE, data, "popularity", 0, 100)