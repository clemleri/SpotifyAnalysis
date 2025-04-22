import pytest
from pydantic import ValidationError
from tests.helpers.models.constraints import (
    assert_constr_regex_field,
    assert_non_empty_str_field,
    assert_literal
)
from constants.tests import PLAYLIST_TYPE, PLAYLIST_FILE_NAME


@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "collaborative",
        "external_urls",
        "href",
        "id",
        "images",
        "name",
        "owner",
        "public",
        "snapshot_id",
        "tracks",
        "type",
        "uri",
    ]
    optional = [
        "description"
    ]
    model_factory(PLAYLIST_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_id_field(data):
    model_cls = PLAYLIST_TYPE
    field = "id"

    # Cas valide : 22 caractères alphanumériques
    good = "1UnPDzVRkrTBflEQ9MJUhXZEKJFBZEFKNZ654"

    # Variantes invalides
    bad_length_small = good[:-20]           # trop court (17 caractères)
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
    
@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_name_field(data):
    assert_non_empty_str_field(PLAYLIST_TYPE, data, "name")
    

@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_snapshot_id_field(data):
    model_cls = PLAYLIST_TYPE
    field = "id"

    # Cas valide : 22 caractères alphanumériques
    good = "1UnPDzVRkrTBflEQ9MJUhXZEKJFBZEFKNZ654"

    # Variantes invalides
    bad_characters   = "1U#PDzVRkrT*flEQ9M^UhX"  # présence de #, *, ^

    invalid_values = [
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
    
@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_type_field(data):
    valid_values=['playlist']
    invalid_values=['album', 'artist', 'episode', 'track']
    assert_literal(PLAYLIST_TYPE, data, "type", valid_values, invalid_values)

@pytest.mark.parametrize("data", [PLAYLIST_FILE_NAME], indirect=True)
def test_playlist_uri_field(data):
    model_cls = PLAYLIST_TYPE
    field = "uri"

    # Préfixe et suffixe valides
    valid_prefix = "spotify:playlist:"
    valid_suffix = "1UnPDzVRkrTBflEQ9MJUhX"
    valid_uri = valid_prefix + valid_suffix

    # Variantes de prefixes invalides
    bad_prefixes = [
        "",                             # absence de prefixe
        "spotify-playlist:",               # mauvais séparateur
        "Spotify:Playlist:",               # casse incorrecte
        "spotify:playlist",                # sans les deux-points finaux
        "spotify:/playlist:"              # slash en trop
    ]

    # Variantes de suffixes invalides
    bad_suffixes = [
        valid_suffix[:-4],              # trop court
        "1U#PDzVRkrT*flEQ9M^UhX",       # caractères non alphanumériques
        ""                             # suffixe vide
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