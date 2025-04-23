'use client'

import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import UserAvatar from "../components/UserAvatar"
import SpotifyLoginButton from "../components/SpotifyLoginButton"
import { useConnection } from "../context/ConnectionContext"

const userData = {
  username: 'Driss Baritaud',
  language: 'French 🇫🇷',
  followers: 258,
  avatarUrl: 'https://i.pravatar.cc/150?img=32',
}

export default function Profile() {
  const { spotifyConnected } = useConnection()

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <div className="mt-[-4rem] flex items-center justify-center min-h-screen px-4">
        {spotifyConnected ? (
          <UserAvatar
            username={userData.username}
            language={userData.language}
            followers={userData.followers}
            avatarUrl={userData.avatarUrl}
            onLogout={() => alert('Déconnecté !')}
          />
        ) : (
          <div className="flex flex-col items-center justify-center gap-4">
            <p className="text-sm text-gray-500 dark:text-gray-300">
              Connectez votre compte Spotify pour accéder à votre profil.
            </p>
            <SpotifyLoginButton isConnected={false} />
          </div>
        )}
      </div>
      <Footer extend={false} />
    </main>
  )
}
