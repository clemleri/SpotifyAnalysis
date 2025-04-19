from pydantic import BaseModel
from typing import List, Optional
from models.external_urls import ExternalUrls
from models.simplified_artist import SimplifiedArtist
from models.image import Image
from models.tracks import Tracks 
from models.restrictions import Restrictions
from models.external_ids import ExternalIds
from models.tracks import Tracks
from models.copyright import Copyright

class Album(BaseModel):
    album_type: str         
    total_tracks: int
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    release_date: str               
    release_date_precision: str     
    restrictions : Restrictions | None
    type: str       
    uri: str
    artists: List[SimplifiedArtist] 
    tracks : Optional[Tracks] = None
    copyrights : List[Copyright]
    external_ids : ExternalIds
    genres : List[str] = []
    labels : str
    popularity : int
    images: List[Image]