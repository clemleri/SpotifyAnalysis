'use client'
import { useEffect, useState } from 'react'

export default function LoadingProgressBar() {
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval)
          return 100
        }
        return prev + Math.random() * 70 // valeur randomisée pour un effet + naturel
      })
    }, 300)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="w-full max-w-md px-6">
      <div className="w-full bg-gray-200 dark:bg-zinc-700 h-2 rounded-full overflow-hidden">
        <div
          className="h-full bg-primary transition-all duration-300 rounded-full"
          style={{ width: `${progress}%` }}
        ></div>
      </div>
      <p className="mt-4 text-sm text-center text-gray-500 dark:text-gray-300">
        Chargement de vos données Spotify...
      </p>
    </div>
  )
}
