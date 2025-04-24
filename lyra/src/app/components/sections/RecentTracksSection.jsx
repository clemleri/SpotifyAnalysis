'use client'
import SpotifyLoginButton from '../SpotifyLoginButton'

export default function RecentTracksSection({ recent = [] }) {
  const isConnected = Boolean(localStorage.getItem("spotify_token"));
  const notConnected = !isConnected;

  if (notConnected) {
    return (
      <div className="flex flex-col items-center justify-center gap-4 min-h-[60vh]">
        <p className="text-sm text-gray-500 dark:text-gray-300 text-center">
          Connectez votre compte Spotify pour voir vos titres écoutés récemment.
        </p>
        <SpotifyLoginButton isConnected={isConnected} />
      </div>
    );
  }

  if (recent.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <p className="text-sm text-gray-500">Aucune écoute récente trouvée.</p>
      </div>
    );
  }

  return (
    <div className="px-4 py-8 w-full max-w-3xl mx-auto mt-24 space-y-4">
      {recent.map((item, index) => {
        const track = item.track;
        return (
          <div
            key={`${track.id}-${index}`}
            className="flex items-center gap-4 p-3 bg-gray-200 dark:bg-zinc-800 rounded-xl "
          >
            <img
              src={track.album.images[0]?.url}
              alt={track.name}
              className="w-16 h-16 object-cover rounded-md shadow"
            />
            <div className="flex flex-col">
              <p className="text-sm font-medium">{track.name}</p>
              <p className="text-xs text-gray-500">
                {track.artists.map((a) => a.name).join(', ')}
              </p>
            </div>
          </div>
        );
      })}
    </div>
  );
}
