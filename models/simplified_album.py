from typing import List
from pydantic import BaseModel
from models.external_urls import ExternalUrls
from models.image import Image
from models.simplified_artist import SimplifiedArtist

class SimplifiedAlbum(BaseModel):
    album_type: str                 
    artists: List[SimplifiedArtist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str              
    release_date_precision: str     
    total_tracks: int
    type: str                       
    uri: str
