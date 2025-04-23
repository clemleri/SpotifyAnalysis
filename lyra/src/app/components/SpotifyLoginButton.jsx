"use client"
import { CheckCircleIcon } from '@heroicons/react/24/outline';

const SpotifyLoginButton = ({ isConnected }) => {
  const CLIENT_ID = "VOTRE_SPOTIFY_CLIENT_ID";
  const REDIRECT_URI = "http://localhost:3000/auth/spotify/callback";
  const SCOPES = [
    "user-read-email",
    "user-read-private",
    "user-top-read",
    "user-read-recently-played"
  ];

  const handleLogin = () => {
    if (isConnected) return;
    const authUrl = `https://accounts.spotify.com/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&scope=${encodeURIComponent(SCOPES.join(" "))}`;
    window.location.href = authUrl;
  };

  return (
    <button
      onClick={handleLogin}
      disabled={isConnected}
      className={`flex items-center gap-2 px-8 py-4 rounded-2xl text-sm font-medium transition
        ${isConnected ? "bg-green-200 text-green-800 cursor-default" : "bg-green-600/80 border-2 border-green-600 hover:bg-green-600 "}`}
    >
      {isConnected ? (
        <>
          <CheckCircleIcon className="h-5 w-5" />
          <span>Connecté</span>
        </>
      ) : (
        <>
          <img src="/assets/spotify_icon.png" alt="Spotify" className="h-5 w-5 dark:invert" />
          <span>Connexion</span>
        </>
      )}
    </button>
  );
};

export default SpotifyLoginButton;
