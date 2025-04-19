from pydantic import BaseModel
from models.track import Track
from models.context import Context

class PlayHistory(BaseModel):
    track : Track
    played_at : str
    context : Context