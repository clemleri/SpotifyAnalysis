# saved_album.py
from pydantic import BaseModel
from models.album import Album

class SavedAlbum(BaseModel):
    added_at: datetime
    album: Album

    @validator('added_at')
    def added_at_not_in_future(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError('added_at doit être timezone-aware')
        if v > datetime.now(timezone.utc):
            raise ValueError('added_at ne peut être dans le futur')
        return v