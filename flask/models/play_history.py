# play_history.py
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, field_validator
from models.track import Track
from models.context import Context

class PlayHistory(BaseModel):
    track: Track
    played_at: datetime
    context: Context

    @field_validator('played_at', mode='before')
    def played_at_timezone_and_not_future(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError('played_at doit être timezone-aware')
        if v > datetime.now(timezone.utc):
            raise ValueError('played_at ne peut être dans le futur')
        return v