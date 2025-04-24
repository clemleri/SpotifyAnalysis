'use client'
import PodiumCarousel from '../PodiumCarousel';
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function TopTracksSection({ tracks = [] }) {
  const isConnected = Boolean(localStorage.getItem("spotify_token"));
  const notConnected = !isConnected;

  if (notConnected) {
    return (
      <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
        <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
          Connectez votre compte Spotify pour voir vos titres les plus écoutés.
        </p>
        <SpotifyLoginButton isConnected={isConnected} />
      </div>
    );
  }

  if (tracks.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <p className="text-sm text-gray-500">Aucun titre trouvé.</p>
      </div>
    );
  }

  return (
    <div className="px-4 py-8 w-full max-w-6xl mx-auto mt-24 space-y-12">

      {/* 🏆 Podium Top 3 */}
      <div>
        <div className="sm:hidden mb-16">
          <PodiumCarousel items={tracks.slice(0, 3)} />
        </div>
        <div className="hidden sm:flex justify-center gap-8">
          {tracks.slice(0, 3).map((track, index) => {
            const medals = [
              { emoji: '🥇', pulseClass: 'animate-glow-gold' },
              { emoji: '🥈', pulseClass: 'animate-glow-silver' },
              { emoji: '🥉', pulseClass: 'animate-glow-bronze' },
            ];
            const style = medals[index] || {};

            return (
              <div key={track.id} className="relative flex flex-col items-center p-2">
                <div className={`absolute z-0 w-36 h-36 rounded-full blur-2xl opacity-50 ${style.pulseClass}`}></div>
                <span className="absolute -top-3 -left-3 text-xl z-10">{style.emoji}</span>
                <img
                  src={track.album.images[0]?.url}
                  alt={track.name}
                  className="w-32 h-32 object-cover rounded-md shadow relative z-10"
                />
                <p className="w-32 text-sm font-medium text-center mt-2 z-10 break-words">{track.name}</p>
                <p className="text-xs text-gray-500 text-center z-10">{track.artists.map(a => a.name).join(', ')}</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* 🎶 Autres titres */}
      <div>
        <h3 className="text-sm uppercase font-semibold text-gray-500 mb-4">Autres titres écoutés</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {tracks.slice(3).map((track, index) => (
            <div
              key={track.id}
              className="flex flex-col items-center p-4 bg-gray-200 dark:bg-zinc-800 rounded-2xl transition hover:scale-[1.02]"
            >
              <span className="text-xs text-gray-400 mb-1">#{index + 4}</span>
              <img
                src={track.album.images[0]?.url}
                alt={track.name}
                className="w-24 h-24 rounded-lg mb-2 shadow"
              />
              <p className="text-center font-medium  text-sm">{track.name}</p>
              <p className="text-xs text-gray-500 text-center">{track.artists.map(a => a.name).join(', ')}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
