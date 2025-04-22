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
from constants.tests import TRACK_TYPE, TRACK_FILE_NAME


@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
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
        "album",
        "external_ids",
        "popularity"
    ]
    optional = [
        "is_playable",
        "linked_from",
        "restrictions",
        "preview_url"
    ]
    model_factory(TRACK_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_popularity_field(data):
    assert_conint_between(TRACK_TYPE, data, "popularity", 0, 100)

@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_artists_non_empty(data):
    assert_non_empty_list_field(TRACK_TYPE, data, "artists")
    
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_disc_number_field(data):
    assert_conint_ge(TRACK_TYPE, data, "disc_number", 1)
    
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_duration_ms_field(data):
    assert_positive_int(TRACK_TYPE, data, "duration_ms")
        
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_name_field(data):
    assert_non_empty_str_field(TRACK_TYPE, data, "name")
    
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_track_number_field(data):
    assert_conint_ge(TRACK_TYPE, data, "track_number", 1)
    
@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_type_field(data):
    valid_values=['track']
    invalid_values=['album', 'artist', 'episode', 'playlist']
    assert_literal(TRACK_TYPE, data, "type", valid_values, invalid_values)

@pytest.mark.parametrize("data", [TRACK_FILE_NAME], indirect=True)
def test_track_uri_field(data):
    model_cls = TRACK_TYPE
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



    


    
