# tracks.py
from pydantic import BaseModel, conlist
from typing import List
from models.simplified_track import SimplifiedTrack
from models.paginated_response import PaginatedResponse

class Tracks(PaginatedResponse):
    items : conlist(SimplifiedTrack, min_length=1)