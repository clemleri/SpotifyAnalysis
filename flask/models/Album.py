# album.py
from pydantic import BaseModel, conlist, constr, conint, HttpUrl, root_validator
from typing import List, Optional
from models.restrictions import Restrictions
from models.external_ids import ExternalIds
from models.tracks import Tracks
from models.copyright import Copyright
from models.simplified_album import SimplifiedAlbum


class Album(SimplifiedAlbum):
    restrictions : Optional[Restrictions] = None
    tracks : Tracks
    copyrights : conlist(Copyright, min_length=1)
    external_ids : ExternalIds
    genres : Optional[List[str]] = []
    label : constr(min_length=1)
    popularity: conint(ge=0, le=100)    # 0 ≤ popularity ≤ 100
