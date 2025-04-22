import pytest
from pydantic import ValidationError
from constants.tests import SAVED_TRACK_TYPE, SAVED_TRACK_FILENAME 
from datetime import datetime, timezone


@pytest.mark.parametrize("data", [SAVED_TRACK_FILENAME], indirect=True)
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
        "added_at",
        "track"
    ]
    optional = []
    model_factory(SAVED_TRACK_TYPE, data, required, optional)
    
    
@pytest.mark.parametrize("data", [SAVED_TRACK_FILENAME], indirect=True)
def test_saved_track_added_at_valid(data):
    """
    Vérifie que 'added_at' accepte un timestamp ISO timezone-aware dans le passé.
    """
    model_cls = SAVED_TRACK_TYPE
    d = data.copy()
    # Cas valide : date passée et timezone-aware
    valid_ts = "2025-04-20T15:30:00+00:00"
    d["added_at"] = valid_ts
    obj = model_cls.model_validate(d)
    # Type et timezone
    assert isinstance(obj.added_at, datetime)
    assert obj.added_at.tzinfo is not None
    # Ne dépasse pas le moment présent
    assert obj.added_at <= datetime.now(timezone.utc)

@pytest.mark.parametrize("data", [SAVED_TRACK_FILENAME], indirect=True)
def test_saved_track_added_at_naive_error(data):
    """
    Vérifie qu'une date naive (sans timezone) lève une ValidationError.
    """
    model_cls = SAVED_TRACK_TYPE
    d = data.copy()
    naive_ts = "2025-04-20T15:30:00"   # sans suffixe '+00:00'
    d["added_at"] = naive_ts
    with pytest.raises(ValidationError, match="added_at doit être timezone-aware"):
        model_cls.model_validate(d)

@pytest.mark.parametrize("data", [SAVED_TRACK_FILENAME], indirect=True)
def test_saved_track_added_at_future_error(data):
    """
    Vérifie qu'une date dans le futur lève une ValidationError.
    """
    model_cls = SAVED_TRACK_TYPE
    d = data.copy()
    future_ts = "2999-01-01T00:00:00+00:00"  # clairement dans le futur
    d["added_at"] = future_ts
    with pytest.raises(ValidationError, match="added_at ne peut être dans le futur"):
        model_cls.model_validate(d)