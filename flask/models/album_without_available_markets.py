from models.simplified_album import SimplifiedAlbum
from pydantic import conlist, constr

class AlbumWithoutAvailableMarkets(SimplifiedAlbum):
    available_markets: conlist(
        constr(pattern=r'^[A-Z]{2}$'),
    )