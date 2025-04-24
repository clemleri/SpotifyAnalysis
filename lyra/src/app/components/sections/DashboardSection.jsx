'use client'
import PodiumCarousel from '../PodiumCarousel'
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function DashboardSection({ topTracks = [], topArtists = [], recentTracks = [] }) {
  const isConnected = Boolean(localStorage.getItem("spotify_token"))
  const notConnected = !isConnected

  return (
    <div className="flex flex-col items-center justify-center gap-8 min-h-[60vh] mt-16 px-4 text-center">
      {notConnected ? (
        <>
          <p className="text-sm text-gray-500 dark:text-gray-300">
            Connectez votre compte Spotify pour afficher votre dashboard.
          </p>
          <SpotifyLoginButton isConnected={isConnected} />
        </>
      ) : (
        <div className="w-full max-w-6xl mx-auto mt-16 px-4">
          <div className="grid grid-cols-1 2xl:grid-cols-2 gap-24">

            {/* 📊 Podium : Top Tracks + Top Artists */}
            <div className="flex flex-col gap-8">
              {/* 🎧 Top Tracks */}
              
              <div>
                <h3 className="hidden sm:flex text-sm uppercase font-semibold text-gray-500 mb-4 text-left">🎧 Top Tracks</h3>
                <div className="sm:hidden">
                  <PodiumCarousel items={topTracks.slice(0, 3)} />
                </div>
                <div className="hidden sm:flex gap-6 justify-center">
                  {topTracks.slice(0, 3).map((track, index) => {
                    const medals = [
                      { emoji: '🥇', pulseClass: 'animate-glow-gold' },
                      { emoji: '🥈', pulseClass: 'animate-glow-silver' },
                      { emoji: '🥉', pulseClass: 'animate-glow-bronze' }
                    ]
                    const style = medals[index] || {}

                    return (
                      <div key={track.id} className="relative flex flex-col items-center p-2">
                        <div className={`absolute z-0 w-36 h-36 rounded-full blur-2xl opacity-50 ${style.pulseClass}`}></div>
                        <span className="absolute -top-3 -left-3 text-xl z-10">{style.emoji}</span>
                        <img
                          src={track.album.images[0]?.url}
                          alt={track.name}
                          className="w-32 h-32 object-cover rounded-md shadow relative z-10"
                        />
                        <p className="text-sm font-medium line-clamp-2 text-center mt-2 z-10 w-32">{track.name}</p>
                        <p className="text-xs text-gray-500 text-center z-10 w-32">{track.artists.map(a => a.name).join(', ')}</p>
                      </div>
                    )
                  })}
                </div>
              </div>

              {/* 🧑‍🎤 Top Artists */}
              {/* Mobile version */}
              
              <div>
                <h3 className="text-sm uppercase font-semibold text-gray-500 mb-4 text-left">🧑‍🎤 Top Artists</h3>
                <div className="sm:hidden">
                  <PodiumCarousel items={topArtists.slice(0, 3)} isArtist />
                </div>
                <div className="hidden sm:flex gap-6 justify-center">
                  {topArtists.slice(0, 3).map((artist, index) => {
                    const medals = [
                      { emoji: '🥇', pulseClass: 'animate-glow-gold' },
                      { emoji: '🥈', pulseClass: 'animate-glow-silver' },
                      { emoji: '🥉', pulseClass: 'animate-glow-bronze' }
                    ]
                    const style = medals[index] || {}

                    return (
                      <div key={artist.id} className="relative flex flex-col items-center p-2">
                        <div className={`absolute z-0 w-36 h-36 rounded-full blur-2xl opacity-50 ${style.pulseClass}`}></div>
                        <span className="absolute -top-3 -left-3 text-xl z-10">{style.emoji}</span>
                        <img
                          src={artist.images[0]?.url}
                          alt={artist.name}
                          className="w-32 h-32 object-cover rounded-full shadow relative z-10"
                        />
                        <p className="text-sm font-medium text-center mt-2 z-10 w-32">{artist.name}</p>
                      </div>
                    )
                  })}
                </div>
              </div>
            </div>

            {/* ⏪ Écoutes Récentes */}
            <div>
              <h3 className="text-sm uppercase font-semibold text-gray-500 mb-4 text-left">⏪ Écoutes Récentes</h3>
              <ul className="flex flex-col gap-4">
                {recentTracks.slice(0, 5).map((item, i) => (
                  <li
                    key={`${item.track.id}-${i}`}
                    className="flex items-center gap-4 bg-gray-200 dark:bg-zinc-800 p-3 rounded-lg shadow"
                  >
                    <img
                      src={item.track.album.images[0]?.url}
                      alt={item.track.name}
                      className="w-14 h-14 rounded shadow"
                    />
                    <div className="text-left">
                      <p className="font-medium text-sm">{item.track.name}</p>
                      <p className="text-xs text-gray-500">{item.track.artists.map(a => a.name).join(', ')}</p>
                    </div>
                  </li>
                ))}
              </ul>
            </div>

          </div>
        </div>
      )}
    </div>
  )
}
