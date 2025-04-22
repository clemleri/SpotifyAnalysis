# simplified_artist.py
from models.external_urls import ExternalUrls
from pydantic import BaseModel, constr, HttpUrl
from typing import Literal

class SimplifiedArtist(BaseModel):
    external_urls : ExternalUrls
    href : HttpUrl
    id : constr(pattern=r'^[A-Za-z0-9]{22}$')
    name : constr(min_length=1)
    type : Literal['artist']
    uri : constr(pattern=r'^spotify:artist:[A-Za-z0-9]{22}$')