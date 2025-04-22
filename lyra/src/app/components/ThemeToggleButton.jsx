'use client'

import { useEffect, useState } from 'react'
import { MoonIcon, SunIcon } from '@heroicons/react/24/outline'
import { useClient } from '../hooks/useClient'

export default function ThemeToggleButton({ mobile = false }) {
  const [darkMode, setDarkMode] = useState(false)
  const isClient = useClient()

  // Lecture initiale du thème
  useEffect(() => {
    if (!isClient) return
    const savedTheme = localStorage.getItem('theme')
    const initial = (savedTheme === 'dark')
    setDarkMode(initial)
  }, [isClient])

  // Applique le thème quand `darkMode` change
  useEffect(() => {
    if (!isClient) return
    if (darkMode) {
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  }, [darkMode, isClient])

  if (!isClient) return null

  return (
    <button
      onClick={() => setDarkMode(!darkMode)}
      className={`p-2 rounded-full transition ${
        mobile ? 'flex items-center gap-2 hover:bg-gray-300 dark:hover:bg-zinc-700' : 'hover:bg-gray-100 dark:hover:bg-zinc-700'
      }`}
      aria-label="Toggle Theme"
    >
      {darkMode ? (
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
