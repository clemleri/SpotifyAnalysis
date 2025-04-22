# linked_from.py
from pydantic import BaseModel, HttpUrl, constr
from typing import Literal
from models.external_urls import ExternalUrls

class LinkedFrom(BaseModel):
    external_urls: ExternalUrls
    href: HttpUrl
    id: constr(pattern=r'^[A-Za-z0-9]{22,28}$')  # Spotify IDs font 22 caractères pour Track, Album, Artist, plus pour les User
    type: Literal['track', 'user']
    uri: constr(pattern=r'^spotify:(?:user|track):[A-Za-z0-9]{22,28}$')
    
