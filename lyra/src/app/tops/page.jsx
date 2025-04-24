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
import { getTopTracks, getTopArtists, getRecentlyPlayed } from "../api/spotifyApi"
import {
  HomeIcon, ChartBarIcon, UsersIcon, InboxIcon, Squares2X2Icon, HeartIcon,
} from "@heroicons/react/24/outline"
import { useRouter } from "next/navigation"
import { usePathname, useSearchParams } from 'next/navigation'

export default function Tops() {
  const [hash, setHash] = useState(null)
  const [topTracks, setTopTracks] = useState([])
  const [topArtists, setTopArtists] = useState([])
  const [recentTracks, setRecentTracks] = useState([])

  const router = useRouter()

  useEffect(() => {
    const updateHash = () => {
      setHash(window.location.hash || "#dashboard")
    }

    updateHash()
    window.addEventListener("hashchange", updateHash)
    return () => window.removeEventListener("hashchange", updateHash)
  }, [router]) // 🔁 on force update à chaque navigation
  

  useEffect(() => {
    getTopTracks().then(data => setTopTracks(data.items || []))
    getTopArtists().then(data => setTopArtists(data.items || []))
    getRecentlyPlayed().then(data => setRecentTracks(data.items || []))
  }, [])

  if (hash === null) return null

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

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <LayoutWithSidebar>
        <div className="px-4 pt-4 ml-16 mt-1 md:ml-0 md:mt-0">
          <Breadcrumb items={breadcrumbItems} />
        </div>

        <div className="w-full h-full mt-[-4rem] gap-6 flex-col md:flex-row flex justify-center items-center">
          {hash === "#dashboard" && <DashboardSection topTracks = {topTracks} topArtists = {topArtists} recentTracks = {recentTracks}/>}
          {hash === "#topsTracks" && <TopTracksSection tracks={topTracks} />}
          {hash === "#topsArtists" && <TopArtistsSection artists={topArtists} />}
          {hash === "#recentTracks" && <RecentTracksSection recent={recentTracks} />}
          {hash === "#sportStats" && <SportStatsSection />}
        </div>
      </LayoutWithSidebar>
    </main>
  )
}
