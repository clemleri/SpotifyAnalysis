'use client'
import Image from 'next/image'

export default function UserAvatar({ username, language, followers, avatarUrl, onLogout }) {
  return (
    <div className="bg-white dark:bg-[#141414] border dark:border-[#212121] border-[#b5b5b5] rounded-xl shadow-md p-6 flex items-center gap-5 w-full max-w-md">
      {/* Avatar */}
      <div className="relative w-16 h-16 rounded-full overflow-hidden border dark:border-zinc-700 border-gray-300">
        <Image
          src={avatarUrl}
          alt={`${username}'s avatar`}
          fill
          className="object-cover"
        />
      </div>

      {/* Info */}
      <div className="flex-1">
        <h3 className="text-lg font-semibold">{username}</h3>
        <p className="text-sm text-gray-500 dark:text-gray-400">{language}</p>
        <p className="text-sm text-gray-500 dark:text-gray-400">{followers} followers</p>
      </div>

      {/* Logout */}
      <button
        onClick={onLogout}
        className="text-sm font-medium px-4 py-2 rounded-lg border border-red-500 text-red-500 hover:bg-red-500 hover:text-white transition"
        >
        Logout
      </button>

    </div>
  )
}
