# models/simplified_artist.py
from models.external_urls import ExternalUrls
from pydantic import BaseModel, constr, HttpUrl
from typing import Literal
from models.spotify_id import SpotifyID

class SimplifiedArtist(BaseModel):
    external_urls : ExternalUrls
    href : HttpUrl
    id : SpotifyID
    name : constr(min_length=1)
    type : Literal['artist']
    uri : constr(pattern=r'^spotify:artist:[A-Za-z0-9]{22}$')