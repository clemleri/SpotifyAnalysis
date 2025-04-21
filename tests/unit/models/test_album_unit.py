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
    assert_literal,
    assert_constr_depending_literal
)
from constants.tests import ALBUM_TYPE, ALBUM_FILE_NAME


@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_model(data, model_factory):
    """
    Teste le modèle Track via model_factory pour :
      1. parsing valide -> OK
      2. champs manquants -> ValidationError
      3. optionnels manquants -> OK
      4. mauvais type -> ValidationError
      5. tous optionnels présents -> OK
    """
    required = [
        "album_type",
        "artists",
        "available_markets",
        "external_urls",
        "href",
        "id",
        "images",
        "name",
        "release_date",
        "release_date_precision",
        "total_tracks",
        "type",
        "uri",
        "tracks",
        "copyrights",
        "external_ids",
        "label",
        "popularity"
    ]
    optional = [
        "restrictions",
        "genres"
    ]
    model_factory(ALBUM_TYPE, data, required, optional)
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_album_type_field(data):
    valid_values=['album', 'single', 'compilation', 'appears_on']
    invalid_values=['track', 'artist', 'episode', 'playlist']
    assert_literal(ALBUM_TYPE, data, "album_type", valid_values, invalid_values)


@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_artists_non_empty(data):
    assert_non_empty_list_field(ALBUM_TYPE, data, "artists")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_albumm_available_markets_non_empty(data):
    assert_non_empty_list_field(ALBUM_TYPE, data, "available_markets")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_available_markets_field(data):
    model_cls = ALBUM_TYPE
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
        [],             # liste vide (déjà couvert, mais redondant)
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
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_id_field(data):
    model_cls = ALBUM_TYPE
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
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_images_non_empty(data):
    assert_non_empty_list_field(ALBUM_TYPE, data, "images")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_name_non_empty(data):
    assert_non_empty_str_field(ALBUM_TYPE, data, "name")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_release_date_field(data):
    # valeur invalides
    valid_values = [
        # → cas valides
        ("2025",       "year"),
        ("2025-04",    "month"),
        ("2025-04-21", "day"),
    ]
    # valeurs valides 
    invalid_values = [
        # → precision 'year' mais format non-YYYY
        ("2025-04",    "year"),
        ("2025-04-21", "year"),
        # → precision 'month' mais format non-YYYY-MM
        ("2025",       "month"),
        ("2025-04-21", "month"),
        # → precision 'day' mais format non-YYYY-MM-DD
        ("2025",       "day"),
        ("2025-04",    "day"),
        # → cas complètement hors format
        ("abcd-ef-gh", "year"),
        ("20250230",   "day"),
        ("2025-04", ""),
        ("",   "day"),
    ]
    assert_constr_depending_literal(
        model_cls=ALBUM_TYPE,
        data=data,
        constr_field="release_date",
        literal_field="release_date_precision",
        valid_values=valid_values,
        invalid_values=invalid_values
    )

@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_total_tracks_field(data):
    assert_conint_ge(ALBUM_TYPE, data, "total_tracks", 1)

@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_field(data):
    valid_values=['album']
    invalid_values=['track', 'artist', 'episode', 'playlist', ""]
    assert_literal(ALBUM_TYPE, data, "type", valid_values, invalid_values)
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_uri_field(data):
    model_cls = ALBUM_TYPE
    field = "uri"

    # Préfixe et suffixe valides
    valid_prefix = "spotify:album:"
    valid_suffix = "1UnPDzVRkrTBflEQ9MJUhX"
    valid_uri = valid_prefix + valid_suffix

    # Variantes de prefixes invalides
    bad_prefixes = [
        "",                             # absence de prefixe
        "spotify-album:",               # mauvais séparateur
        "Spotify:Album:",               # casse incorrecte
        "spotify:album",                # sans les deux-points finaux
        "spotify:/album:",              # slash en trop
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
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_copyrights_non_empty(data):
    assert_non_empty_list_field(ALBUM_TYPE, data, "copyrights")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_label_non_empty(data):
    assert_non_empty_str_field(ALBUM_TYPE, data, "label")
    
@pytest.mark.parametrize("data", [ALBUM_FILE_NAME], indirect=True)
def test_album_popularity_field(data):
    assert_conint_between(ALBUM_TYPE, data, "popularity", 0, 100)