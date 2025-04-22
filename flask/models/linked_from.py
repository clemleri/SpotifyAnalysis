# models/linked_from.py
from pydantic import BaseModel, HttpUrl, constr
from typing import Literal
from models.external_urls import ExternalUrls
from models.spotify_id import SpotifyID

class LinkedFrom(BaseModel):
    external_urls: ExternalUrls
    href: HttpUrl
    id: SpotifyID  # Spotify IDs font 22 caractères pour Track, Album, Artist, plus pour les User
    type: str
    uri: str
    
class LinkedFromUser(LinkedFrom):
    uri : constr(pattern=r'^spotify:user:[A-Za-z0-9]+$', min_length=35)
    type : Literal['user']
    
class LinkedFromTrack(LinkedFrom):
    uri : constr(pattern=r'^spotify:track:[A-Za-z0-9]+$', min_length=36)
    type : Literal['track']