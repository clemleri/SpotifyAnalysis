import { format } from 'date-fns'
import { fr } from 'date-fns/locale'

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
    <div className="px-4 py-8 w-[100vw] max-w-lg xl:max-w-2xl mx-auto mt-24 space-y-4">
      <h3 className="flex sm:hidden text-sm uppercase font-semibold text-gray-500 dark:text-gray-200 mb-8 text-left">⏪ Écoutes Récentes</h3>

      {recent.map((item, index) => {
        const track = item.track;
        const date = new Date(item.played_at);
        const formatted = format(date, "dd MMM yyyy 'à' HH:mm", { locale: fr });

        return (
          <div
            key={`${track.id}-${index}`}
            className="flex items-center gap-4 p-3 bg-gray-200 dark:bg-zinc-800 rounded-xl"
          >
            <img
              src={track.album.images[0]?.url}
              alt={track.name}
              className="w-16 h-16 object-cover rounded-md shadow"
            />
            <div className="flex flex-col">
              <p className="text-sm font-medium">{track.name}</p>
              <p className="text-xs text-gray-800 dark:text-gray-300">{track.artists.map(a => a.name).join(', ')}</p>
              <p className="text-xs text-gray-600 dark:text-gray-400 mt-1">{formatted}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}
