from models.track import Track
from dao.track_dao import TrackDAO
from typing import List
import json

if __name__ == "__main__":
    ACCESS_TOKEN = "BQAcOpqrM1pi0s6Jz52sw6sCjDkHMo1Z9wkTC56d5oqOHyPuz85vo-C7rJGFuBsmzPLjAebAFag8vOcCI6R4in5gUuwXXj9pAnSohUHW4Eq-YXOu9OfFNFSz1YywT6qi12nF9X34CPDYTdtyK9giFffQnKcJeSqduF3w8rh5Q2sHdoyW7bcNrFqfaxefawN6ujYujoOcdZ-fQV6DB1xgJwvGZdFa9Bealneb_DAqJfZwPu9yJuNGMAMj3LE_w20XHd8umsJTj2e5FD4G"
    trackDAO = TrackDAO()
    saved_tracks = trackDAO.fetch_saved_tracks(ACCESS_TOKEN)
    for saved_track in saved_tracks.items:
        print(f"track_name : {saved_track.track.name}, added_at : {saved_track.added_at}")