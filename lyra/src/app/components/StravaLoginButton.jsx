"use client"
import { CheckCircleIcon } from '@heroicons/react/24/outline';

const StravaLoginButton = ({ isConnected }) => {
  const CLIENT_ID = "VOTRE_STRAVA_CLIENT_ID";
  const REDIRECT_URI = "http://localhost:3000/auth/strava/callback";
  const SCOPES = "read,activity:read_all";

  const handleLogin = () => {
    if (isConnected) return;
    const authUrl = `https://www.strava.com/oauth/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&scope=${encodeURIComponent(SCOPES)}`;
    window.location.href = authUrl;
  };

  return (
    <button
      onClick={handleLogin}
      disabled={isConnected}
      className={`flex items-center gap-2 px-8 py-4 rounded-2xl text-sm font-medium transition
        ${isConnected ? "bg-orange-200 text-orange-800 cursor-default" : "bg-orange-600/80 border-2 border-orange-600 hover:bg-orange-600"}`}
    >
      {isConnected ? (
        <>
          <CheckCircleIcon className="h-5 w-5" />
          <span>Connecté</span>
        </>
      ) : (
        <>
          <img src="/assets/strava_icon.png" alt="Strava" className="h-5 w-5 dark:invert" />
          <span>Connexion</span>
        </>
      )}
    </button>
  );
};

export default StravaLoginButton;
