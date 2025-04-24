"use client";
import { useEffect, useState } from "react";
import { CheckCircleIcon } from "@heroicons/react/24/outline";
import { useConnection } from "../context/ConnectionContext";

const SpotifyLoginButton = ({ isConnected, onTokenReceived }) => {
  const [loading, setLoading] = useState(false);
  const { spotifyConnected, setSpotifyConnected } = useConnection();

  useEffect(() => {
    // Écoute une seule fois après montage
    const handleMessage = (event) => {
      if (event.origin !== "http://localhost:8080") return;
      const { access_token, refresh_token, expires_in } = event.data;


      if (access_token) {
        localStorage.setItem("spotify_token", access_token);
        setSpotifyConnected(true); // 🟢 MAJ du contexte global
        console.log("🎉 Token Save ");

        // ✅ Stockage supplémentaire pour la reconnexion automatique :
        if (refresh_token) {
          localStorage.setItem("spotify_refresh_token", refresh_token);
          console.log("🎉 Refresh Token Save ");
        }
        if (expires_in) {
          const expiresAt = Date.now() + expires_in * 1000;
          localStorage.setItem("spotify_token_expires_at", expiresAt.toString());
          console.log("🎉 Expire Time Save ");
        }

      }
      
      if (onTokenReceived) onTokenReceived(access_token);

      // Tu peux aussi stocker refresh_token, expires_in si tu veux les gérer
    };

    window.addEventListener("message", handleMessage);
    return () => window.removeEventListener("message", handleMessage);
  }, [onTokenReceived]);

  const handleLogin = async () => {
    if (isConnected || loading) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8080/api/login-url");
      const data = await res.json();

      if (data.url) {
        // Ouvre la popup au lieu de rediriger
        window.open(data.url, "_blank", "width=500,height=700");
      } else {
        console.error("Erreur : URL de connexion non reçue");
      }
    } catch (err) {
      console.error("Erreur lors de la récupération de l'URL de login Spotify", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <button
      onClick={handleLogin}
      disabled={isConnected || loading}
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
          <span>{loading ? "Connexion..." : "Connexion"}</span>
        </>
      )}
    </button>
  );
};

export default SpotifyLoginButton;
