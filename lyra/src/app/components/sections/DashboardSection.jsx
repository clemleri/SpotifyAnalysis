'use client'
import { useConnection } from '../../context/ConnectionContext'
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function DashboardSection() {
  const isConnected = Boolean(localStorage.getItem("spotify_token"));

  const notConnected = !isConnected

  return (
    <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
      {notConnected ? (
        <>
          <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
            Connectez votre compte Spotify pour afficher votre dashboard.
          </p>
          <SpotifyLoginButton isConnected={isConnected} />
        </>
      ) : (
        <p className="text-lg font-medium text-green-600 dark:text-green-400">
          ✅ Dashboard personnalisé disponible !
        </p>
      )}
    </div>
  )
}
