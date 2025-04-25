"use client"

import { useEffect, useState } from "react"
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import UserAvatar from "../components/UserAvatar"
import SpotifyLoginButton from "../components/SpotifyLoginButton"
import { getSpotifyUser, logout } from "../api/spotifyApi"
import LoadingProgressBar from "../components/LoadingProgressBar"
import { motion, AnimatePresence } from "framer-motion"
import BottomNav from "../components/BottomNav"

export default function Profile() {
  const token = typeof window !== "undefined" ? localStorage.getItem("spotify_token") : null
  const isConnected = Boolean(token)

  const [userData, setUserData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!isConnected) {
      setLoading(false)
      return
    }

    const cached = localStorage.getItem("spotify_user")
    if (cached) {
      setUserData(JSON.parse(cached))
      setLoading(false)
    } else {
      getSpotifyUser()
        .then(data => {
          const user = {
            username: data.display_name,
            language: data.country,
            followers: data.followers?.total || 0,
            avatarUrl: data.images?.[0]?.url || 'https://i.pravatar.cc/150'
          }
          setUserData(user)
          localStorage.setItem("spotify_user", JSON.stringify(user))
        })
        .catch(err => {
          console.error("Erreur récupération utilisateur :", err)
        })
        .finally(() => setLoading(false))
    }
  }, [isConnected])

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <BottomNav/>
      
      <div className="mt-[-4rem] flex items-center justify-center min-h-screen px-4">
        {loading ? (
          <div className="flex flex-col items-center justify-center min-h-[60vh]">
            <LoadingProgressBar />
          </div>
        ) : (
          <AnimatePresence mode="wait">
            <motion.div
              key={isConnected ? "connected" : "disconnected"}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.3 }}
              className="w-full flex flex-col items-center justify-center gap-4"
            >
              {isConnected && userData ? (
                <UserAvatar
                  username={userData.username}
                  language={userData.language}
                  followers={userData.followers}
                  avatarUrl={userData.avatarUrl}
                  onLogout={logout}
                />
              ) : (
                <>
                  <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
                    Connectez votre compte Spotify pour accéder à votre profil.
                  </p>
                  <SpotifyLoginButton isConnected={isConnected} />
                </>
              )}
            </motion.div>
          </AnimatePresence>
        )}
      </div>
      <Footer extend={false} />
    </main>
  )
}
