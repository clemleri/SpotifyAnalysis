from pydantic import BaseModel
from models.track import Track

class PlayHistory(BaseModel):
    track : Track
    played_at : str
    context : Context