"use client"
import { useEffect, useState } from "react"
import Navbar from "../components/Navbar"
import LayoutWithSidebar from "../components/LayoutWithSidebar"
import Breadcrumb from "../components/Breadcrumb"
import DashboardSection from "../components/sections/DashboardSection"
import TopTracksSection from "../components/sections/TopTracksSection"
import TopArtistsSection from "../components/sections/TopArtistsSection"
import RecentTracksSection from "../components/sections/RecentTracksSection"
import SportStatsSection from "../components/sections/SportStatsSection"
import SpotifyLoginButton from "../components/SpotifyLoginButton"
import { getTopTracks, getTopArtists, getRecentlyPlayed } from "../api/spotifyApi"
import {
  HomeIcon, ChartBarIcon, UsersIcon, InboxIcon, Squares2X2Icon, HeartIcon,
} from "@heroicons/react/24/outline"
import { useRouter } from "next/navigation"
import LoadingProgressBar from "../components/LoadingProgressBar"
import { AnimatePresence, motion } from "framer-motion"
import BottomNav from "../components/BottomNav"
import TopTabs from "../components/TopTabs"

export default function Tops() {
  const [hash, setHash] = useState(null)
  const [topTracks, setTopTracks] = useState([])
  const [topArtists, setTopArtists] = useState([])
  const [recentTracks, setRecentTracks] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [hasLoaded, setHasLoaded] = useState(false)

  const router = useRouter()

  const token = typeof window !== "undefined" ? localStorage.getItem("spotify_token") : null
  const isConnected = Boolean(token)

  useEffect(() => {
    const updateHash = () => {
      setHash(window.location.hash || "#dashboard")
    }

    updateHash()
    window.addEventListener("hashchange", updateHash)
    return () => window.removeEventListener("hashchange", updateHash)
  }, [router])

  useEffect(() => {
    async function fetchData() {
      if (!token) {
        setIsLoading(false)
        return
      }

      try {
        const [tracks, artists, recent] = await Promise.all([
          getTopTracks(),
          getTopArtists(),
          getRecentlyPlayed()
        ])
        setTopTracks(tracks.items || [])
        setTopArtists(artists.items || [])
        setRecentTracks(recent.items || [])
      } catch (e) {
        console.error("Erreur lors du chargement des données Spotify", e)
      } finally {
        setIsLoading(false)
      }
    }

    fetchData()
  }, [])

  // ✅ Déclenche l’animation d’apparition une fois le fetch terminé
  useEffect(() => {
    if (!isLoading) {
      const timeout = setTimeout(() => setHasLoaded(true), 100)
      return () => clearTimeout(timeout)
    }
  }, [isLoading])

  const labelMap = {
    "#dashboard": { label: "Dashboard", icon: ChartBarIcon },
    "#topsTracks": { label: "Top Tracks", icon: Squares2X2Icon },
    "#topsArtists": { label: "Top Artists", icon: UsersIcon },
    "#recentTracks": { label: "Recent Tracks", icon: InboxIcon },
    "#sportStats": { label: "Sport Stats", icon: HeartIcon },
  }

  const current = labelMap[hash] || { label: "Dashboard", icon: ChartBarIcon }

  const breadcrumbItems = [
    { label: "Home", href: "/", icon: HomeIcon },
    { label: "Tops", href: "/tops#dashboard", icon: ChartBarIcon },
    { label: current.label }
  ]

  if (hash === null) return null

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <BottomNav/>
      <TopTabs />
      <LayoutWithSidebar>
        <div className="px-4 pt-4 ml-16 mt-1 lg:ml-0 lg:mt-0">
          <Breadcrumb items={breadcrumbItems} />
        </div>

        {isLoading ? (
          <div className="flex flex-col items-center justify-center min-h-[60vh]">
            <LoadingProgressBar />
          </div>
        ) : (
          <motion.div
            initial={{ opacity: 0 }}
            animate={hasLoaded ? { opacity: 1 } : {}}
            transition={{ duration: 0.6 }}
            className="w-full"
          >
            <div className="w-full h-full mt-[-3rem] md:mt-[-4rem] gap-6 flex-col md:flex-row flex justify-center items-center">
              <AnimatePresence mode="wait">
                <motion.div
                  key={hash}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  transition={{ duration: 0.2 }}
                  className="w-full"
                >
                  {!isConnected ? (
                    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center gap-4">
                      <p className="text-sm text-gray-500 dark:text-gray-300">
                        Connectez votre compte Spotify pour accéder à cette section.
                      </p>
                      <SpotifyLoginButton isConnected={false} />
                    </div>
                  ) : (
                    <>
                      {hash === "#dashboard" && (
                        <DashboardSection
                          topTracks={topTracks}
                          topArtists={topArtists}
                          recentTracks={recentTracks}
                        />
                      )}
                      {hash === "#topsTracks" && <TopTracksSection tracks={topTracks} />}
                      {hash === "#topsArtists" && <TopArtistsSection artists={topArtists} />}
                      {hash === "#recentTracks" && <RecentTracksSection recent={recentTracks} />}
                      {hash === "#sportStats" && <SportStatsSection />}
                    </>
                  )}
                </motion.div>
              </AnimatePresence>
            </div>
          </motion.div>
        )}
      </LayoutWithSidebar>
    </main>
  )
}
