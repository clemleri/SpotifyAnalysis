'use client'
import { useConnection } from '../../context/ConnectionContext'
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function RecentTracksSection() {
  const { spotifyConnected } = useConnection()
  const notConnected = !spotifyConnected

  return (
    <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
      {notConnected ? (
        <>
          <p className="text-sm text-gray-500 dark:text-gray-300">
            Connectez votre compte Spotify pour voir vos titres écoutés récemment.
          </p>
          <SpotifyLoginButton isConnected={spotifyConnected} />
        </>
      ) : (
        <p className="text-lg font-medium text-green-600 dark:text-green-400">
          ✅ Derniers titres disponibles !
        </p>
      )}
    </div>
  )
}
