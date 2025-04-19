from typing import List, Dict, Optional
from pydantic import BaseModel
from models.simplified_artist import SimplifiedArtist
from models.simplified_album import SimplifiedAlbum
from models.restrictions import Restrictions
from models.external_ids import ExternalIds
from models.external_urls import ExternalUrls
from models.linked_from import LinkedFrom


class Track(BaseModel):
    album: SimplifiedAlbum
    artists: List[SimplifiedArtist]
    available_markets: List[str]
    disc_number: int
    duration_ms: float
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href: str
    id: str
    is_playable: Optional[bool] = None
    linked_from: Optional[LinkedFrom] = None
    restrictions: Optional[Restrictions] = None
    name: str
    popularity: float
    preview_url: Optional[str] = None
    track_number: int
    type: str
    uri: str
    is_local: bool
