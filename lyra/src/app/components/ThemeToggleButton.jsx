'use client'

import { useTheme } from 'next-themes'
import { useEffect, useState } from 'react'
import { MoonIcon, SunIcon, ArrowPathIcon } from '@heroicons/react/24/outline'

export default function ThemeToggleButton({ mobile = false }) {
  const { setTheme, resolvedTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  // Fix le problème d'hydratation avec next-themes
  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) return (
    <button
      onClick={() => setTheme(isDark ? 'light' : 'dark')}
      className={`p-2 rounded-full transition ${
        mobile
          ? 'flex items-center gap-2 hover:bg-gray-300 dark:hover:bg-zinc-700'
          : 'hover:bg-gray-100 dark:hover:bg-zinc-700'
      }`}
      aria-label="Toggle Theme"
    >
        <ArrowPathIcon className="w-5 h-5 animate-spin" />
        {mobile && <span className="text-sm text-gray-900 dark:text-white">Loading...</span>}
    </button>
  )

  const isDark = resolvedTheme === 'dark'

  return (
    <button
      onClick={() => setTheme(isDark ? 'light' : 'dark')}
      className={`p-2 rounded-full transition ${
        mobile
          ? 'flex items-center gap-2 hover:bg-gray-300 dark:hover:bg-zinc-700'
          : 'hover:bg-gray-100 dark:hover:bg-zinc-700'
      }`}
      aria-label="Toggle Theme"
    >
      {isDark ? (
        <>
          <SunIcon className="w-5 h-5 text-yellow-400" />
          {mobile && <span className="text-sm text-gray-900 dark:text-white">Light Mode</span>}
        </>
      ) : (
        <>
          <MoonIcon className="w-5 h-5 text-gray-700 dark:text-gray-300" />
          {mobile && <span className="text-sm text-gray-900 dark:text-white">Dark Mode</span>}
        </>
      )}
    </button>
  )
}
