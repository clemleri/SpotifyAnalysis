from models.track import Track
from models.album_without_available_markets import AlbumWithoutAvailableMarkets
from pydantic import conlist, constr

class TrackWithoutAvailableMarkets(Track):
    album: AlbumWithoutAvailableMarkets
    available_markets: conlist(
        constr(pattern=r'^[A-Z]{2}$')
)