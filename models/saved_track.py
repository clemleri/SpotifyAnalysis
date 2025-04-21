# saved_track.py
from datetime import datetime, timezone
from pydantic import BaseModel, field_validator
from models.track import Track

class SavedTrack(BaseModel):
    added_at: datetime
    track: Track

    @field_validator('added_at', mode='before')
    def added_at_not_in_future(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError('added_at doit être timezone-aware')
        if v > datetime.now(timezone.utc):
            raise ValueError('added_at ne peut être dans le futur')
        return v
