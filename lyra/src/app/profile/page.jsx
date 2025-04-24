'use client'

import { useEffect, useState } from "react"
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import UserAvatar from "../components/UserAvatar"
import SpotifyLoginButton from "../components/SpotifyLoginButton"
import { getSpotifyUser, logout } from "../api/spotifyApi"
import LoadingProgressBar from "../components/LoadingProgressBar"

export default function Profile() {
  const token = localStorage.getItem("spotify_token");
  const isConnected = Boolean(token);

  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isConnected) {
      setLoading(false); // ✅ on arrête le chargement si pas connecté
      return;
    }
    
    if (isConnected) {
      const cached = localStorage.getItem("spotify_user");
      if (cached) {
        setUserData(JSON.parse(cached));
        setLoading(false);
      } else {
        getSpotifyUser()
          .then(data => {
            const user = {
              username: data.display_name,
              language: data.country,
              followers: data.followers?.total || 0,
              avatarUrl: data.images?.[0]?.url || 'https://i.pravatar.cc/150'
            };
            setUserData(user);
            localStorage.setItem("spotify_user", JSON.stringify(user)); // 🧠 cache
          })
          .catch(err => {
            console.error("Erreur récupération utilisateur :", err);
          })
          .finally(() => setLoading(false));
      }
    }
  }, [isConnected]);
  

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <div className="mt-[-4rem] flex items-center justify-center min-h-screen px-4">
        {loading ? (
          <div className="flex flex-col items-center justify-center min-h-[60vh]">
            <LoadingProgressBar />
          </div>
        ) : isConnected && userData ? (
          <UserAvatar
            username={userData.username}
            language={userData.language}
            followers={userData.followers}
            avatarUrl={userData.avatarUrl}
            onLogout={logout}
          />
        ) : (
          <div className="flex flex-col items-center justify-center gap-4">
            <p className="text-sm text-gray-500 dark:text-gray-300">
              Connectez votre compte Spotify pour accéder à votre profil.
            </p>
            <SpotifyLoginButton isConnected={isConnected} />
          </div>
        )}
      </div>
      <Footer extend={false} />
    </main>
  )
}
