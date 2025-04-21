# constants/tests.py
from typing import Final
from models.track import Track
from models.simplified_track import SimplifiedTrack
from models.album import Album
from models.simplified_album import SimplifiedAlbum
from models.artist import Artist
from models.simplified_artist import SimplifiedArtist
from models.saved_track import SavedTrack
from models.saved_tracks import SavedTracks
from models.saved_album import SavedAlbum
from models.playlist_track import PlaylistTrack
from models.play_history import PlayHistory
from models.paginated_response import PaginatedResponse
from models.linked_from import LinkedFrom
from models.image import Image
from models.followers import Followers
from models.external_urls import ExternalUrls
from models.external_ids import ExternalIds
from models.cursors import Cursors
from models.copyright import Copyright
from models.context import Context
from models.restrictions import Restrictions

# constantes file_name tests/unit/models
TRACK_FILE_NAME: Final[str] = "track.json"
SIMPLIFIED_TRACK_FILE_NAME: Final[str] = "simplified_track.json"
ARTIST_FILE_NAME : Final[str] = "artist.json"
SIMPLIFIED_ARTIST_FILE_NAME : Final[str] = "simplified_artist.json"
ALBUM_FILE_NAME: Final[str] = "album.json"
SIMPLIFIED_ALBUM_FILE_NAME: Final[str] = "simplified_album.json"


# constantes type tests/unit/models
TRACK_TYPE: Final[type] = Track
TRACKS_TYPE: Final[type] = Track  # à ajuster si vous avez un wrapper spécifique
SIMPLIFIED_TRACK_TYPE: Final[type] = SimplifiedTrack
ALBUM_TYPE: Final[type] = Album
SIMPLIFIED_ALBUM_TYPE: Final[type] = SimplifiedAlbum
ARTIST_TYPE: Final[type] = Artist
SIMPLIFIED_ARTIST_TYPE: Final[type] = SimplifiedArtist
SAVED_TRACK_TYPE: Final[type] = SavedTrack
SAVED_TRACKS_TYPE: Final[type] = SavedTracks
SAVED_ALBUM_TYPE: Final[type] = SavedAlbum
PLAYLIST_TRACK_TYPE: Final[type] = PlaylistTrack
PLAY_HISTORY_TYPE: Final[type] = PlayHistory
PAGINATED_RESPONSE_TYPE: Final[type] = PaginatedResponse
LINKED_FROM_TYPE: Final[type] = LinkedFrom
IMAGE_TYPE: Final[type] = Image
FOLLOWERS_TYPE: Final[type] = Followers
EXTERNAL_URLS_TYPE: Final[type] = ExternalUrls
EXTERNAL_IDS_TYPE: Final[type] = ExternalIds
CURSORS_TYPE: Final[type] = Cursors
COPYRIGHT_TYPE: Final[type] = Copyright
CONTEXT_TYPE: Final[type] = Context
RESTRICTIONS_TYPE: Final[type] = Restrictions