const API_BASE_URL = "http://localhost:8080";

function getToken() {
  return localStorage.getItem("spotify_token");
}

function getAuthHeaders() {
  const token = getToken();
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {})
  };
}

// 👤 Récupère les infos utilisateur Spotify
export async function getSpotifyUser() {
  const response = await fetch(`${API_BASE_URL}/api/user`, {
    method: "GET",
    headers: getAuthHeaders()
  });

  if (!response.ok) throw new Error("Impossible de récupérer l'utilisateur Spotify");
  return await response.json();
}

// 🎧 Récupère les top tracks
export async function getTopTracks(timeRange = "medium_term") {
  const response = await fetch(`${API_BASE_URL}/api/top-tracks?time_range=${timeRange}`, {
    method: "GET",
    headers: getAuthHeaders()
  });

  if (!response.ok) throw new Error("Erreur lors de la récupération des top tracks");
  return await response.json();
}

// 🎤 Récupère les top artists
export async function getTopArtists(timeRange = "medium_term") {
  const response = await fetch(`${API_BASE_URL}/api/top-artists?time_range=${timeRange}`, {
    method: "GET",
    headers: getAuthHeaders()
  });

  if (!response.ok) throw new Error("Erreur lors de la récupération des top artists");
  return await response.json();
}

// ⏪ Récupère les morceaux récemment joués
export async function getRecentlyPlayed() {
  const response = await fetch(`${API_BASE_URL}/api/recently-played`, {
    method: "GET",
    headers: getAuthHeaders()
  });

  if (!response.ok) throw new Error("Erreur lors de la récupération des écoutes récentes");
  return await response.json();
}

export function logout() {
  localStorage.removeItem("spotify_token");
  localStorage.removeItem("spotify_user");
  // Supprime aussi d'autres services si besoin, ex: Strava

  // Redirige vers la page d’accueil
  window.location.href = "/";
}
