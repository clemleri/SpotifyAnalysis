# models/tracks.py
from typing import Union, List
from pydantic import model_validator, ConfigDict
from models.simplified_track import SimplifiedTrack
from models.paginated_response import PaginatedResponse
from models.playlist_track import PlaylistTrack

class Tracks(PaginatedResponse):
    # items peut contenir soit des PlaylistTrack, soit des SimplifiedTrack
    items: List[Union[PlaylistTrack, SimplifiedTrack]]
    # override de limit pour lever dynamiquement une erreur selon le type d'items
    limit: int

    # configuration Pydantic v2
    model_config = ConfigDict()

    @model_validator(mode='after')
    def check_limit_based_on_item_type(cls, result):
        """
        Après création du modèle :
        - si le premier item est un PlaylistTrack, limit ≤ 100
        - sinon (SimplifiedTrack), limit ≤ 50
        """
        if result.items:
            first_item = result.items[0]
            if isinstance(first_item, PlaylistTrack):
                max_limit = 100
                context = 'PlaylistTrack'
            else:
                max_limit = 50
                context = 'SimplifiedTrack'
            if result.limit > max_limit:
                raise ValueError(
                    f'Pour {context}, limit doit être ≤ {max_limit}, got {result.limit}'
                )
        return result

                
    
    