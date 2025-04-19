from pydantic import BaseModel
from datetime import datetime
from models.track import Track

class SavedTrack(BaseModel):
    added_at: datetime       
    track: Track
