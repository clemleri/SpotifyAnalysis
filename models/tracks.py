from pydantic import BaseModel
from typing import List
from models.simplified_track import SimplifiedTrack

class Tracks(BaseModel):
    href : str
    limit : int
    next : str
    offset : int 
    previous : str 
    total : int
    items : List[SimplifiedTrack]