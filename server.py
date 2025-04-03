import os
import requests
import urllib.parse
import pandas as pd
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'spotify_secret_key'  # For session storage

CLIENT_ID = "9bf2c0b082f847baa3d7bc2110eed0a4"
CLIENT_SECRET = "16e18a5a0c0e4e01a64069a8c2a89de7"
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-read-private user-read-email user-top-read"

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

STYLE = """
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #1DB954;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            color: black;
            margin: 0;
        }
        h2 {
            color: #1DB954;
        }
        a {
            color: #1DB954;
            font-size: 18px;
            text-decoration: none;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            background-color: #181818;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }
        .card img {
            width: 100%;
            border-radius: 6px;
            cursor: pointer;
        }
        .card .title {
            font-weight: bold;
            margin-top: 10px;
        }
        .card .subtitle {
            font-size: 0.9em;
            color: #b3b3b3;
        }
    </style>
    <header><h1>Lyra</h1></header>
"""

@app.route("/")
def login():
    query_params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": SCOPE,
        "redirect_uri": REDIRECT_URI,
    }
    url_args = urllib.parse.urlencode(query_params)
    auth_redirect_url = f"{auth_url}?{url_args}"
    return STYLE + f'<a href="{auth_redirect_url}">Click here to authorize with Spotify</a>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return STYLE + "<p>Error: Authorization code not found.</p>"

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(token_url, data=data, headers=headers)
    token_info = response.json()

    if "access_token" in token_info:
        session['access_token'] = token_info['access_token']
        return STYLE + '<a href="/topTracks">View Top Tracks</a>'
    else:
        return STYLE + f"<p>Error fetching token: {token_info}</p>"

@app.route("/topTracks")
def get_top_tracks():
    access_token = session.get('access_token')
    if not access_token:
        return STYLE + "<p>Access token not found. Please <a href='/'>login</a> again.</p>"

    headers = {"Authorization": f"Bearer {access_token}"}

    tracks_resp = requests.get("https://api.spotify.com/v1/me/top/tracks", headers=headers)

    if tracks_resp.status_code != 200:
        return STYLE + f"<p>Error fetching data: {tracks_resp.json()}</p>"

    tracks_data = tracks_resp.json()['items']

    track_cards = "<h2>Top Tracks</h2><div class='grid-container'>"
    for i, track in enumerate(tracks_data, start=1):
        image_url = track['album']['images'][0]['url'] if track['album']['images'] else ""
        track_cards += f"""
        <div class='card'>
            <a href='/track/{track['id']}'><img src='{image_url}' alt='Album cover'></a>
            <div class='title'>{i}. {track['name']}</div>
            <div class='subtitle'>{track['artists'][0]['name']}</div>
        </div>
        """
    track_cards += "</div>"

    return STYLE + track_cards

@app.route("/track/<track_id>")
def show_track_details(track_id):
    access_token = session.get('access_token')
    if not access_token:
        return STYLE + "<p>Access token not found. Please <a href='/'>login</a> again.</p>"

    headers = {"Authorization": f"Bearer {access_token}"}

    track_resp = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}?market=FR", headers=headers)
    if track_resp.status_code != 200:
        return STYLE + f"<p>Error fetching track info. Status code: {track_resp.status_code}</p>"

    track = track_resp.json()

    # Only request audio features if not a local track
    features = {}
    if not track.get('is_local', False):
        audio_resp = requests.get(f"https://api.spotify.com/v1/audio-features/{track_id}", headers=headers)
        if audio_resp.status_code == 200:
            features = audio_resp.json()

    html = f"""
    <h2>{track['name']} by {track['artists'][0]['name']}</h2>
    <img src='{track['album']['images'][0]['url']}' width='300' style='border-radius:10px'>
    <p><strong>Album:</strong> {track['album']['name']}</p>
    <p><strong>Popularity:</strong> {track['popularity']}</p>
    <p><strong>Duration:</strong> {round(track['duration_ms'] / 60000, 2)} minutes</p>
    """

    if features:
        html += """
        <h3>Audio Features</h3>
        <ul>
            <li><strong>Danceability:</strong> {danceability}</li>
            <li><strong>Energy:</strong> {energy}</li>
            <li><strong>Tempo:</strong> {tempo}</li>
            <li><strong>Valence:</strong> {valence}</li>
            <li><strong>Acousticness:</strong> {acousticness}</li>
            <li><strong>Instrumentalness:</strong> {instrumentalness}</li>
        </ul>
        """.format(
            danceability=features.get('danceability', 'N/A'),
            energy=features.get('energy', 'N/A'),
            tempo=features.get('tempo', 'N/A'),
            valence=features.get('valence', 'N/A'),
            acousticness=features.get('acousticness', 'N/A'),
            instrumentalness=features.get('instrumentalness', 'N/A')
        )
    else:
        html += "<p><em>No audio features available for local tracks.</em></p>"

    return STYLE + html

if __name__ == "__main__":
    app.run(port=8080)
