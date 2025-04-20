# playlist_track.py
from datetime import datetime, timezone
from pydantic import BaseModel, validator
from models.linked_from import LinkedFrom
from models.track import Track

class PlaylistTrack(BaseModel):
    added_at: datetime
    added_by: LinkedFrom
    is_local: bool
    track: Track

    @validator('added_at')
    def added_at_not_in_future(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError('added_at doit être timezone-aware')
        if v > datetime.now(timezone.utc):
            raise ValueError('added_at ne peut être dans le futur')
        return v