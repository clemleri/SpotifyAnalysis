'use client'

import { createContext, useContext, useState } from 'react'

const ConnectionContext = createContext()

export function ConnectionProvider({ children }) {
  const [spotifyConnected, setSpotifyConnected] = useState(false)
  const [stravaConnected, setStravaConnected] = useState(false)

  return (
    <ConnectionContext.Provider value={{
      spotifyConnected,
      stravaConnected,
      setSpotifyConnected,
      setStravaConnected
    }}>
      {children}
    </ConnectionContext.Provider>
  )
}

export function useConnection() {
  const context = useContext(ConnectionContext)
  if (!context) {
    throw new Error('useConnection must be used within a ConnectionProvider')
  }
  return context
}
