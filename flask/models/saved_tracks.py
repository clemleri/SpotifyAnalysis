# models/saved_tracks.py
from typing import List
from models.paginated_response import PaginatedResponse
from models.saved_track import SavedTrack

class SavedTracks(PaginatedResponse):
    items: List[SavedTrack]
