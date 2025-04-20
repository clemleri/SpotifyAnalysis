# linked_from.py
from pydantic import BaseModel, HttpUrl, constr
from typing import Literal
from models.external_urls import ExternalUrls

class LinkedFrom(BaseModel):
    external_urls: ExternalUrls
    href: HttpUrl
    id: constr(regex=r'^[A-Za-z0-9]{22}$')  # Spotify IDs font 22 caractères
    type: Literal['track']
    uri: constr(regex=r'^spotify:track:[A-Za-z0-9]{22}$')