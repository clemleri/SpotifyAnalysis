from pydantic import BaseModel
from typing import List, Optional
from models.external_urls import ExternalUrls
from models.followers import Followers
from models.image import Image

class Artist(BaseModel):
    external_urls: ExternalUrls
    followers: Followers
    genres: List[str]
    href: Optional[str] = None
    id: str
    images: List[Image]
    name: str
    popularity: int
    type: str
    uri: str