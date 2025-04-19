# dao/track_dao.py
from models.track import Track
import json
import requests

class TrackDAO:
    def __init__(self):
        """
        Injecte le service responsable des appels à l'API Spotify.
        """
        self.url = "https://api.spotify.com/v1/tracks/"

    def fetch_track(self, access_token : str, track_id : str) -> Track:
        headers = {"Authorization": f"Bearer {access_token}"}
        res = requests.get(self.url+track_id, headers=headers)
        track_data_json = res.json()
        print(json.dumps(track_data_json, indent=2))
        return Track.parse_obj(track_data_json)

    def fetch_top_tracks(self, 
    access_token : str,
    time_range : str,
    limit : int
    ) : list(Track)


