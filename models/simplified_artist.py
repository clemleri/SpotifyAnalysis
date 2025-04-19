from pydantic import BaseModel
from models.external_urls import ExternalUrls

class SimplifiedArtist(BaseModel):
    external_urls : ExternalUrls
    href : str
    id : str
    name : str
    type : str
    uri : str