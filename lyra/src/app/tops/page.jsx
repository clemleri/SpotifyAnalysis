  "use client"
  import { useEffect, useState } from "react"
  import Navbar from "../components/Navbar"
  import LayoutWithSidebar from "../components/LayoutWithSidebar"
  import SpotifyLoginButton from "../components/SpotifyLoginButton"
  import StravaLoginButton from "../components/StravaLoginButton"
  import { useConnection } from "../context/ConnectionContext"
  import Breadcrumb from "../components/Breadcrumb"
  import {
  HomeIcon,
  ChartBarIcon,
  UsersIcon,
  InboxIcon,
  Squares2X2Icon,
  HeartIcon,
} from "@heroicons/react/24/outline"
import DashboardSection from "../components/sections/DashboardSection"
import TopTracksSection from "../components/sections/TopTracksSection"
import TopArtistsSection from "../components/sections/TopArtistsSection"
import RecentTracksSection from "../components/sections/RecentTracksSection"
import SportStatsSection from "../components/sections/SportStatsSection"

  export default function Tops() {
    const [hash, setHash] = useState(null)
    const { spotifyConnected, stravaConnected } = useConnection()

    useEffect(() => {
      const currentHash = window.location.hash
      setHash(currentHash)

      const onHashChange = () => {
        setHash(window.location.hash)
      }

      window.addEventListener("hashchange", onHashChange)
      return () => window.removeEventListener("hashchange", onHashChange)
    }, [])

    if (hash === null) {
      // ⏳ Attend que le hash soit lu
      return null
    }

    const isSportPage = hash === "#sportStats"

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
      { label: current.label }, // page active
    ]

    return (
      <main className="text-black dark:text-white min-h-screen">
        <Navbar />
        <LayoutWithSidebar>
          <div className="px-4 pt-4 ml-16 mt-1 sm:ml-0">
            <Breadcrumb items={breadcrumbItems} />
          </div>
          
          <div className="w-full h-[100vh] mt-[-4rem] gap-6 flex-col md:flex-row flex justify-center items-center">
            {hash === "#dashboard" && <DashboardSection />}
            {hash === "#topsTracks" && <TopTracksSection />}
            {hash === "#topsArtists" && <TopArtistsSection />}
            {hash === "#recentTracks" && <RecentTracksSection />}
            {hash === "#sportStats" && <SportStatsSection />}
          </div>
        </LayoutWithSidebar>
      </main>
    )
  }
