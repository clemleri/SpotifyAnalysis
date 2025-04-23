'use client'
import { useConnection } from '../../context/ConnectionContext'
import SpotifyLoginButton from '../SpotifyLoginButton'
import StravaLoginButton from '../StravaLoginButton'

export default function SportStatsSection() {
  const { spotifyConnected, stravaConnected } = useConnection()
  const notConnected = !spotifyConnected || !stravaConnected

  return (
    <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
      {notConnected ? (
        <>
          <p className="text-sm text-gray-500 dark:text-gray-300">
            Connectez vos comptes Spotify et Strava pour voir vos stats sportives.
          </p>
          <SpotifyLoginButton isConnected={spotifyConnected} />
          <StravaLoginButton isConnected={stravaConnected} />
        </>
      ) : (
        <p className="text-lg font-medium text-green-600 dark:text-green-400">
          ✅ Statistiques sportives prêtes à être consultées !
        </p>
      )}
    </div>
  )
}
