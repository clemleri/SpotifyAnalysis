import os
import requests
import urllib.parse
from flask import Flask, request, session, render_template
import json

app = Flask(__name__)
app.secret_key = 'spotify_secret_key'

CLIENT_ID = "9bf2c0b082f847baa3d7bc2110eed0a4"
CLIENT_SECRET = "16e18a5a0c0e4e01a64069a8c2a89de7"
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-read-private user-read-email user-top-read"

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    query_params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": SCOPE,
        "redirect_uri": REDIRECT_URI,
    }
    url_args = urllib.parse.urlencode(query_params)
    auth_redirect_url = f"{auth_url}?{url_args}"
    return f'<a href="{auth_redirect_url}">Click here to authorize with Spotify</a>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "<p>Error: Authorization code not found.</p>"

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
        return '<a href="/topTracks">View Top Tracks</a>'
    else:
        return f"<p>Error fetching token: {token_info}</p>"

@app.route("/profile")
def user_profile():
    access_token = session.get('access_token')
    if not access_token:
        return "<p>Access token not found. Please <a href='/'>login</a> again.</p>"

    headers = {"Authorization": f"Bearer {access_token}"}
    user_resp = requests.get("https://api.spotify.com/v1/me", headers=headers)

    if user_resp.status_code != 200:
        return f"<p>Error fetching user profile: {user_resp.json()}</p>"

    user = user_resp.json()
    
    return render_template('displayProfile.html', posts=user)

@app.route("/topTracks")
def get_top_tracks(index = 0):
    access_token = session.get('access_token')
    if not access_token:
        return "<p>Access token not found. Please <a href='/'>login</a> again.</p>"

    headers = {"Authorization": f"Bearer {access_token}"}
    tracks_resp = requests.get("https://api.spotify.com/v1/me/top/tracks?limit=50", headers=headers)

    if tracks_resp.status_code != 200:
        return f"<p>Error fetching data: {tracks_resp.json()}</p>"

    tracks_data = tracks_resp.json()['items']

    with open("data.json", "w") as data:
        json.dump(tracks_data, data)

    chunksOfTrackData = [tracks_data[i:i+6] for i in range(0, len(tracks_data), 6)]
    
    return render_template('displayTracks.html', topTracks=chunksOfTrackData)

@app.route("/topArtists")
def get_top_artists():
    access_token = session.get('access_token')
    if not access_token:
        return "<p>Access token not found. Please <a href='/'>login</a> again.</p>"

    headers = {"Authorization": f"Bearer {access_token}"}
    artists_resp = requests.get("https://api.spotify.com/v1/me/top/artists?limit=50", headers=headers)

    if artists_resp.status_code != 200:
        return f"<p>Error fetching top artists: {artists_resp.json()}</p>"

    artists_data = artists_resp.json()['items']

    return render_template('displayArtists.html', posts=artists_data)

@app.route("/topArtists/getNext/<lastId>")
@app.route("/topTracks/getNext/<lastId>")
def get_six_next(lastId):
    with open("data.json", "r") as data:
        jsonData = json.load(data)
    for i in range(len(jsonData)):
        if jsonData[i]['id'] == lastId:
            if "topArtists" in request.path:
                return render_template('displayArtist.html', posts=jsonData[i+1:i+7])
            else:
                return render_template('displayTracks.html', posts=jsonData[i+1:i+7])

@app.route("/topArtists/getPrevious/<lastId>")
@app.route("/topTracks/getPrevious/<lastId>")
def get_six_previous(lastId):
    with open("data.json", "r") as data:
        jsonData = json.load(data)
    for i in range(len(jsonData)):
        if jsonData[i]['id'] == lastId:
            if "topArtists" in request.path:
                return render_template('displayArtist.html', posts=jsonData[i-6:i])
            else:
                return render_template('displayTracks.html', posts=jsonData[i-6:i])
    

if __name__ == "__main__":
    app.run(port=8080)
