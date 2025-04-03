import os
import requests
import urllib.parse
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'spotify_secret_key'

CLIENT_ID = "9bf2c0b082f847baa3d7bc2110eed0a4"
CLIENT_SECRET = "16e18a5a0c0e4e01a64069a8c2a89de7"
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-read-private user-read-email user-top-read"

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

STYLE = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        body {
            background-color: #121212;
            color: white;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
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
        nav {
            background-color: #181818;
            padding: 10px 30px;
            display: flex;
            justify-content: center;
            gap: 30px;
            position: sticky;
            top: 0;
            z-index: 999;
        }
        nav a {
            color: #1DB954;
            font-size: 16px;
            text-decoration: none;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .content {
            padding: 40px;
        }
        h2 {
            font-size: 26px;
            margin-bottom: 4px;
        }
        .subtitle {
            font-size: 15px;
            color: #b3b3b3;
            margin-bottom: 20px;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 10px;
        }
        .card {
            background-color: transparent;
            text-align: center;
            padding: 10px;
        }
        .card img {
            width: 100%;
            border-radius: 8px;
            transition: transform 0.2s;
        }
        .card img:hover {
            transform: scale(1.05);
        }
        .circle-img {
            border-radius: 50%;
        }
        .title {
            font-weight: 600;
            margin-top: 10px;
            font-size: 16px;
        }
        .subtitle-small {
            font-size: 13px;
            color: #b3b3b3;
        }
    </style>
    <header><h1>Lyra</h1></header>
    <nav>
        <a href="/">Login</a>
        <a href="/profile">Profile</a>
        <a href="/topTracks">Top Tracks</a>
        <a href="/topArtists">Top Artists</a>
    </nav>
    <div class='content'>
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
    return STYLE + f'<a href="{auth_redirect_url}">Click here to authorize with Spotify</a></div>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return STYLE + "<p>Error: Authorization code not found.</p></div>"

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
        return STYLE + '<a href="/topTracks">View Top Tracks</a></div>'
    else:
        return STYLE + f"<p>Error fetching token: {token_info}</p></div>"

@app.route("/profile")
def user_profile():
    access_token = session.get('access_token')
    if not access_token:
        return STYLE + "<p>Access token not found. Please <a href='/'>login</a> again.</p></div>"

    headers = {"Authorization": f"Bearer {access_token}"}
    user_resp = requests.get("https://api.spotify.com/v1/me", headers=headers)

    if user_resp.status_code != 200:
        return STYLE + f"<p>Error fetching user profile: {user_resp.json()}</p></div>"

    user = user_resp.json()
    image_url = user['images'][0]['url'] if user.get('images') else ""

    html = f"""
    <h2>Your Spotify Profile</h2>
    <img src="{image_url}" width="150" class="circle-img">
    <p><strong>Name:</strong> {user['display_name']}</p>
    <p><strong>Email:</strong> {user['email']}</p>
    <p><strong>Country:</strong> {user['country']}</p>
    <p><strong>Followers:</strong> {user['followers']['total']}</p>
    """
    return STYLE + html + "</div>"

@app.route("/topTracks")
def get_top_tracks():
    access_token = session.get('access_token')
    if not access_token:
        return STYLE + "<p>Access token not found. Please <a href='/'>login</a> again.</p></div>"

    headers = {"Authorization": f"Bearer {access_token}"}
    tracks_resp = requests.get("https://api.spotify.com/v1/me/top/tracks", headers=headers)

    if tracks_resp.status_code != 200:
        return STYLE + f"<p>Error fetching data: {tracks_resp.json()}</p></div>"

    tracks_data = tracks_resp.json()['items']

    html = "<h2>Top tracks</h2><div class='subtitle'>Your top tracks from the past 4 weeks</div><div class='grid-container'>"
    for i, track in enumerate(tracks_data, start=1):
        image_url = track['album']['images'][0]['url'] if track['album']['images'] else ""
        html += f"""
        <div class='card'>
            <img src="{image_url}" alt="{track['name']}">
            <div class='title'>{i}. {track['name']}</div>
            <div class='subtitle-small'>{track['artists'][0]['name']}</div>
        </div>
        """
    html += "</div>"
    return STYLE + html + "</div>"

@app.route("/topArtists")
def get_top_artists():
    access_token = session.get('access_token')
    if not access_token:
        return STYLE + "<p>Access token not found. Please <a href='/'>login</a> again.</p></div>"

    headers = {"Authorization": f"Bearer {access_token}"}
    artists_resp = requests.get("https://api.spotify.com/v1/me/top/artists", headers=headers)

    if artists_resp.status_code != 200:
        return STYLE + f"<p>Error fetching top artists: {artists_resp.json()}</p></div>"

    artists_data = artists_resp.json()['items']

    html = "<h2>Top artists</h2><div class='subtitle'>Your top artists from the past 4 weeks</div><div class='grid-container'>"
    for i, artist in enumerate(artists_data, start=1):
        image_url = artist['images'][0]['url'] if artist['images'] else ""
        html += f"""
        <div class='card'>
            <img src="{image_url}" class="circle-img" alt="{artist['name']}">
            <div class='title'>{i}. {artist['name']}</div>
            <div class='subtitle-small'>{', '.join(artist['genres'])}</div>
        </div>
        """
    html += "</div>"
    return STYLE + html + "</div>"

if __name__ == "__main__":
    app.run(port=8080)
