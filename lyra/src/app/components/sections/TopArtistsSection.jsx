'use client'
import PodiumCarousel from '../PodiumCarousel';
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function TopArtistsSection({ artists = [] }) {
  const isConnected = Boolean(localStorage.getItem("spotify_token"));
  const notConnected = !isConnected;

  const medals = [
    { border: 'border-yellow-400', glow: 'shadow-yellow-400', emoji: '🥇', pulseClass: 'animate-glow-gold' },
    { border: 'border-gray-400', glow: 'shadow-gray-400', emoji: '🥈', pulseClass: 'animate-glow-silver' },
    { border: 'border-orange-500', glow: 'shadow-orange-500', emoji: '🥉', pulseClass: 'animate-glow-bronze' }
  ];

  if (notConnected) {
    return (
      <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
        <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
          Connectez votre compte Spotify pour voir vos artistes préférés.
        </p>
        <SpotifyLoginButton isConnected={isConnected} />
      </div>
    );
  }

  if (artists.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <p className="text-sm text-gray-500">Aucun artiste trouvé.</p>
      </div>
    );
  }

  return (
    <div className="px-4 py-8 w-full max-w-6xl mx-auto mt-24">
      {/* Podium */}
      <div className="sm:hidden mb-16">
        <PodiumCarousel items={artists.slice(0, 3)} isArtist />
      </div>
      <div className="hidden sm:flex justify-center items-end gap-6 mb-20">
        {artists.slice(0, 3).map((artist, index) => {
          const style = medals[index] || {};

          return (
            <div key={artist.id} className="flex flex-col items-center gap-2 relative">
              <div className={`absolute z-0 w-36 h-36 rounded-full blur-2xl opacity-50 ${style.pulseClass}`}></div>
              <span className="absolute -top-3 -left-3 text-xl z-10">{style.emoji}</span>

              <div className={`relative z-10 border-4 ${style.border} ${style.glow} rounded-full p-1 bg-white dark:bg-zinc-800`}>
                <img
                  src={artist.images[0]?.url}
                  alt={artist.name}
                  className="w-32 h-32 object-cover rounded-full"
                />
              </div>

              <p className="w-32 text-sm font-medium text-center break-words line-clamp-2 z-10">{artist.name}</p>
            </div>
          );
        })}
      </div>

      {/* Reste des artistes */}
      <h3 className="text-sm uppercase font-semibold text-gray-500 mb-4">Autres artistes écoutés</h3>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6">
      
        {artists.slice(3).map((artist, index) => (
          <div
            key={artist.id}
            className="flex flex-col items-center p-4 bg-gray-200 dark:bg-zinc-800 rounded-2xl  transition hover:scale-[1.02]"
          >
            <span className="text-xs font-bold dark:text-gray-400 text-gray-600 mb-2">{index + 4}</span>

            <img
              src={artist.images[0]?.url}
              alt={artist.name}
              className="w-24 h-24 rounded-full mb-2 shadow"
            />
            <p className="text-center font-medium text-sm">{artist.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
