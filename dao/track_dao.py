# dao/track_dao.py
from models.track import Track
from models.saved_tracks import SavedTracks
import json
import requests
from typing import List

class TrackDAO:
    def __init__(self):
        self.url = "https://api.spotify.com/v1/tracks"
        self.url_saved_tracks = "https://api.spotify.com/v1/me/tracks"

    def fetch_track(
        self, 
        access_token : str, 
        track_id : str
    ) -> Track:
        headers = {"Authorization": f"Bearer {access_token}"}
        res = requests.get(self.url+f"/{track_id}", headers=headers)
        res.raise_for_status()
        return Track.parse_obj(res.json())
    
    def fetch_tracks(
        self,
        access_token : str, 
        track_ids : List[str]
    ) -> List[Track]:
        headers = {"Authorization": f"Bearer {access_token}"}
        res = requests.get(self.url+f"?ids={",".join(track_ids)}", headers=headers)
        res.raise_for_status()
        json_tracks_data = (res.json())["tracks"]
        return [Track.parse_obj(json_track_data) for json_track_data in json_tracks_data]

    def fetch_saved_tracks(
        self,
        access_token: str,
        market: str | None = None,
        limit: int = 20,
        offset: int = 0
    ) -> SavedTracks:
        headers = {"Authorization": f"Bearer {access_token}"}
        params: dict[str, int | str] = {
            "limit": limit,
            "offset": offset
        }
        if market is not None:
            params["market"] = market
        res = requests.get(self.url_saved_tracks, headers=headers, params=params)
        res.raise_for_status()
        return SavedTracks.parse_obj(res.json())


    def fetch_top_tracks(self, 
    access_token : str,
    time_range : str,
    limit : int
    ) : list(Track)


