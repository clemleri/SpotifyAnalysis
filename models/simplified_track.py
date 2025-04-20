# simplified_track.py
from typing import List, Optional, Literal
from pydantic import BaseModel, conlist, constr, conint, PositiveInt, HttpUrl
from models.simplified_artist import SimplifiedArtist
from models.external_urls import ExternalUrls
from models.linked_from import LinkedFrom
from models.restrictions import Restrictions

class SimplifiedTrack(BaseModel):
    artists: conlist(SimplifiedArtist, min_items=1)  # au moins un artiste
    available_markets: conlist(
        constr(regex=r'^[A-Z]{2}$'),  # codes ISO 3166‑1 alpha‑2
        min_items=1
    )
    disc_number: conint(ge=1)             # >= 1
    duration_ms: PositiveInt              # > 0
    explicit: bool
    external_urls: ExternalUrls
    href: HttpUrl                         # URL valide
    id: constr(regex=r'^[A-Za-z0-9]{22}$')  # ID Spotify (22 chars)
    is_playable: bool
    linked_from: Optional[LinkedFrom] = None
    restrictions: Optional[Restrictions] = None
    name: constr(min_length=1)            # nom non vide
    track_number: conint(ge=1)           # >= 1
    type: Literal['track']               # toujours "track"
    uri: constr(regex=r'^spotify:track:[A-Za-z0-9]{22}$')
    is_local: bool
    preview_url: Optional[HttpUrl] = None