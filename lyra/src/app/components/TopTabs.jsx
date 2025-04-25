'use client'

import { useEffect, useState } from 'react'
import {
  ChartBarIcon,
  Squares2X2Icon,
  UsersIcon,
  InboxIcon,
  HeartIcon,
} from '@heroicons/react/24/outline'

export default function TopTabs() {
  const [activeHash, setActiveHash] = useState("#dashboard")

  const links = [
    { name: 'Dashboard', href: '#dashboard', icon: ChartBarIcon },
    { name: 'Tops Tracks', href: '#topsTracks', icon: Squares2X2Icon },
    { name: 'Tops Artists', href: '#topsArtists', icon: UsersIcon },
    { name: 'Recent', href: '#recentTracks', icon: InboxIcon },
    { name: 'Sport', href: '#sportStats', icon: HeartIcon },
  ]

  useEffect(() => {
    const updateHash = () => {
      setActiveHash(window.location.hash || '#dashboard')
    }

    updateHash()
    window.addEventListener('hashchange', updateHash)
    return () => window.removeEventListener('hashchange', updateHash)
  }, [])

  return (
    <div className="md:hidden fixed top-0 z-40 w-full bg-white dark:bg-[#0f0f0f] border-b border-gray-200 dark:border-zinc-800 flex justify-between">
      {links.map((link) => {
        const isActive = activeHash === link.href
        const Icon = link.icon
        return (
          <a
            key={link.name}
            href={link.href}
            className={`flex-1 flex flex-col items-center py-2 text-xs font-medium transition ${
              isActive ? 'text-primary border-b-2 border-primary' : 'text-gray-600 dark:text-gray-400'
            }`}
          >
            <Icon className={`w-5 h-5 my-2 ${isActive ? 'text-primary' : ''}`} />
            <p className='hidden xs:block'>
            {link.name}
            </p>
            
          </a>
        )
      })}
    </div>
  )
}
