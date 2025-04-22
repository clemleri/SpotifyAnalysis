# models/playlist.py
from pydantic import BaseModel, HttpUrl, constr, conlist
from typing import Literal, Optional, List
from models.external_urls import ExternalUrls
from models.tracks import Tracks
from models.owner import Owner
from models.image import Image
from models.spotify_id import SpotifyID

class Playlist(BaseModel):
    collaborative : bool
    description : Optional[str] = None
    external_urls : ExternalUrls
    href : HttpUrl
    id: constr(min_length=22, pattern=r'^[A-Za-z0-9]+$')  # ID Spotify ( > 22 chars)
    images : List[Image]
    name : constr(min_length=1)
    owner : Owner
    public : bool
    snapshot_id : SpotifyID
    tracks : Tracks
    type : Literal['playlist']
    uri: constr(pattern=r'^spotify:playlist:[A-Za-z0-9]+$', min_length=39) # len("spotify:playlist:") = 17 donc 22 + 17 = 39
