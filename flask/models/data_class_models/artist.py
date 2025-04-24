# models/artist.py
from pydantic import BaseModel, conint
from models.simplified_artist import SimplifiedArtist
from typing import List, Optional
from models.external_urls import ExternalUrls
from models.followers import Followers
from models.image import Image

class Artist(SimplifiedArtist):
    followers: Followers
    genres: List[str]
    images: List[Image]
    popularity: conint(ge=0, le=100)    # 0 ≤ popularity ≤ 100
