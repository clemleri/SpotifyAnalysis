from pydantic import BaseModel
from models.external_urls import ExternalUrls

class Context(BaseModel):
    type : str
    href : str
    external_urls : ExternalUrls
    uri : str