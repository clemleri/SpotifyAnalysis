from pydantic import BaseModel
from models.linked_from import LinkedFrom
from models.track import Track

class PlaylistTrack(BaseModel):
    added_at : str
    added_by : LinkedFrom
    is_local : bool
    track : Track