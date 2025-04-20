# simplified_artist.py
from pydantic import BaseModel
from models.external_urls import ExternalUrls
from pydantic import BaseModel, conlist, constr, conint, PositiveInt, HttpUrl

class SimplifiedArtist(BaseModel):
    external_urls : ExternalUrls
    href : HttpUrl
    id : constr(regex=r'^[A-Za-z0-9]{22}$')
    name : constr(min_length=1)
    type : Literal['artist']
    uri : constr(regex=r'^spotify:artist:[A-Za-z0-9]{22}$')