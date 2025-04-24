from flask import Flask, request, jsonify
import requests, urllib.parse
from flask_cors import CORS
from flask import render_template_string

app = Flask(__name__)
CORS(app, supports_credentials=True)


# Configuration Spotify
CLIENT_ID = "9bf2c0b082f847baa3d7bc2110eed0a4"
CLIENT_SECRET = "16e18a5a0c0e4e01a64069a8c2a89de7"
REDIRECT_URI = "http://localhost:8080/callback"
SCOPE = "user-read-private user-read-email user-top-read user-read-recently-played user-library-read"

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"


# ▶️ Génère l'URL d'autorisation Spotify
@app.route("/api/login-url")
def login_url():
    query_params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": SCOPE,
        "redirect_uri": REDIRECT_URI,
    }
    url_args = urllib.parse.urlencode(query_params)
    return jsonify({"url": f"{AUTH_URL}?{url_args}"})



@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Code manquant", 400

    # 🔧 Données à envoyer à Spotify pour récupérer un token
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = { "Content-Type": "application/x-www-form-urlencoded" }

    # ✅ Envoie de la requête POST vers l'API Spotify
    response = requests.post(TOKEN_URL, data=data, headers=headers)
    token_info = response.json()

    # ✅ Envoie le token au front via postMessage depuis une page HTML temporaire
    if "access_token" in token_info:
        return render_template_string("""
            <html><body>
            <script>
              window.opener.postMessage({
                access_token: "{{ access_token }}",
                refresh_token: "{{ refresh_token }}",
                expires_in: "{{ expires_in }}"
              }, "http://localhost:3000");
              window.close();
            </script>
            </body></html>
        """,
        access_token=token_info["access_token"],
        refresh_token=token_info.get("refresh_token", ""),
        expires_in=token_info.get("expires_in", 3600))
    else:
        return f"Erreur token : {token_info}", 400


# 👤 Récupère les infos utilisateur
@app.route("/api/user")
def get_user():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        return jsonify({"error": "Token manquant"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get("https://api.spotify.com/v1/me", headers=headers)
    return jsonify(resp.json()), resp.status_code


# 🎧 Top Tracks
@app.route("/api/top-tracks")
def top_tracks():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    time_range = request.args.get("time_range", "medium_term")

    if not token:
        return jsonify({"error": "Token manquant"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"https://api.spotify.com/v1/me/top/tracks?limit=50&time_range={time_range}", headers=headers)
    return jsonify(resp.json()), resp.status_code


# 🎤 Top Artists
@app.route("/api/top-artists")
def top_artists():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    time_range = request.args.get("time_range", "medium_term")

    if not token:
        return jsonify({"error": "Token manquant"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"https://api.spotify.com/v1/me/top/artists?limit=50&time_range={time_range}", headers=headers)
    return jsonify(resp.json()), resp.status_code


# ⏪ Tracks récemment écoutés
@app.route("/api/recently-played")
def recently_played():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if not token:
        return jsonify({"error": "Token manquant"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=20", headers=headers)
    return jsonify(resp.json()), resp.status_code

@app.route("/api/refresh-token", methods=["POST"])
def refresh_token():
    refresh_token = request.json.get("refresh_token")

    if not refresh_token:
        return jsonify({"error": "Refresh token manquant"}), 400

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(TOKEN_URL, data=data, headers=headers)

    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Échec du refresh"}), 400


# 🔧 Lancer le serveur
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
