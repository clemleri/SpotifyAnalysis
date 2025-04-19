from pydantic import BaseModel
from typing import List
from models.simplified_track import SimplifiedTrack
from models.paginated_response import PaginatedResponse

class Tracks(PaginatedResponse):
    items : List[SimplifiedTrack]