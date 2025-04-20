# track.py
from typing import Optional
from pydantic import conint
from models.simplified_track import SimplifiedTrack
from models.simplified_album import SimplifiedAlbum
from models.external_ids import ExternalIds

class Track(SimplifiedTrack):
    album: SimplifiedAlbum
    external_ids: ExternalIds
    popularity: conint(ge=0, le=100)      # 0 ≤ popularity ≤ 100