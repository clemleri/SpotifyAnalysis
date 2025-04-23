from pydantic import BaseModel, constr, HttpUrl
from typing import Literal, List
from models.explicit_content import ExplicitContent
from models.spotify_id import SpotifyID
from models.image import Image
from models.followers import Followers
from models.external_urls import ExternalUrls


class User(BaseModel):
    country : constr(pattern=r'^[A-Z]{2}$')
    display_name : constr(min_length=1)
    email : constr(pattern=r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$') # Note : ce mail n'est pas vérifié
    explicit_content : ExplicitContent
    external_urls : ExternalUrls
    followers : Followers
    href : HttpUrl
    id : SpotifyID
    images : List[Image]
    product : Literal["premium","free","open"]
    type : Literal['user']
    uri: constr(pattern=r'^spotify:user:[A-Za-z0-9]+$', min_length=35)
    

    
    