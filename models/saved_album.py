from pydantic import BaseModel
from models.album import Album

class SavedAlbum(BaseModel):
    added_at : str
    album : Album