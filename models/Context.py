# context.py
from pydantic import BaseModel, HttpUrl, constr
from typing import Literal
from models.external_urls import ExternalUrls

class Context(BaseModel):
    type: Literal['artist', 'album', 'track', 'playlist', 'show', 'episode']
    href: HttpUrl                              # lien vers le contexte
    external_urls: ExternalUrls                # URLs externes liées
    uri: constr(regex=r'^spotify:(?:artist|album|track|playlist|show|episode):[A-Za-z0-9]{22}$')  # URI Spotify
