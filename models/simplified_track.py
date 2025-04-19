from pydantic import BaseModel
from typing import List, Optional
from models.simplified_artist import SimplifiedArtist
from models.external_urls import ExternalUrls
from models.linked_from import LinkedFrom
from models.restrictions import Restrictions

class SimplifiedTrack(BaseModel):
    artists : List[SimplifiedArtist]
    available_markets : List[str]
    disc_number : int
    duration_ms : float
    explicit : bool
    external_urls : ExternalUrls
    href : str
    id : str
    is_playable : bool 
    linked_from : Optional[LinkedFrom] = None
    restrictions : Optional[Restrictions] = None
    name : str
    track_number : int
    type : str
    uri : str
    is_local : bool
    preview_url: Optional[str] = None