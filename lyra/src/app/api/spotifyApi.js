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

async function refreshAccessToken() {
  const refreshToken = localStorage.getItem("spotify_refresh_token");
  if (!refreshToken) return null;

  try {
    const response = await fetch(`${API_BASE_URL}/api/refresh-token`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ refresh_token: refreshToken })
    });

    if (!response.ok) return null;

    const data = await response.json();

    localStorage.setItem("spotify_token", data.access_token);
    if (data.expires_in) {
      const expiresAt = Date.now() + data.expires_in * 1000;
      localStorage.setItem("spotify_token_expires_at", expiresAt.toString());
    }

    return data.access_token;
  } catch (err) {
    console.error("Erreur lors du refresh_token :", err);
    return null;
  }
}

export async function handleResponse(response, originalRequestFn) {
  if (response.status === 401) {
    console.warn("⚠️ Token expiré : tentative de rafraîchissement...");
    const success = await refreshAccessToken();

    if (success) {
      console.log("🔁 Token rafraîchi, re-tentative de la requête...");
      return originalRequestFn(); // ⬅️ on rejoue la requête
    } else {
      throw new Error("Token expiré et non renouvelable");
    }
  }

  if (!response.ok) {
    throw new Error(`Erreur API Spotify : ${response.status}`);
  }

  return await response.json();
}

// 👤 Infos utilisateur Spotify
export async function getSpotifyUser() {
  const originalRequest = () =>
    fetch(`${API_BASE_URL}/api/user`, {
      method: "GET",
      headers: getAuthHeaders()
    });

  const response = await originalRequest();
  return handleResponse(response, getSpotifyUser);
}

// 🎧 Top tracks
export async function getTopTracks(timeRange = "medium_term") {
  const originalRequest = () =>
    fetch(`${API_BASE_URL}/api/top-tracks?time_range=${timeRange}`, {
      method: "GET",
      headers: getAuthHeaders()
    });

  const response = await originalRequest();
  return handleResponse(response, () => getTopTracks(timeRange));
}

// 🎤 Top artists
export async function getTopArtists(timeRange = "medium_term") {
  const originalRequest = () =>
    fetch(`${API_BASE_URL}/api/top-artists?time_range=${timeRange}`, {
      method: "GET",
      headers: getAuthHeaders()
    });

  const response = await originalRequest();
  return handleResponse(response, () => getTopArtists(timeRange));
}

// ⏪ Récents
export async function getRecentlyPlayed() {
  const originalRequest = () =>
    fetch(`${API_BASE_URL}/api/recently-played`, {
      method: "GET",
      headers: getAuthHeaders()
    });

  const response = await originalRequest();
  return handleResponse(response, getRecentlyPlayed);
}

// 🚪 Déconnexion
export function logout() {
  localStorage.removeItem("spotify_token");
  localStorage.removeItem("spotify_refresh_token");
  localStorage.removeItem("spotify_token_expires_at");
  localStorage.removeItem("spotify_user");
  window.location.href = "/";
}

// ⏳ Token expiré ?
export function isTokenExpired() {
  const expiresAt = parseInt(localStorage.getItem("spotify_token_expires_at") || "0");
  return Date.now() > expiresAt;
}
