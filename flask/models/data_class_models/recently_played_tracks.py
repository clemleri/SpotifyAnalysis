# models/recently_played_tracks.py
from pydantic import BaseModel
from models.paginated_response import PaginatedResponse
from models import PlayHistory
from typing import List

class RecentlyPlayedTracks(PaginatedResponse):
    items : List[PlayHistory]