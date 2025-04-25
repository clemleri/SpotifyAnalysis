'use client'

import { useState, useEffect } from 'react'
import {
  ChartBarIcon as ChartBarOutline,
  Squares2X2Icon as SquaresOutline,
  InboxIcon as InboxOutline,
  UsersIcon as UsersOutline,
  HeartIcon as HeartOutline,
} from '@heroicons/react/24/outline'

import {
  ChartBarIcon as ChartBarSolid,
  Squares2X2Icon as SquaresSolid,
  InboxIcon as InboxSolid,
  UsersIcon as UsersSolid,
  HeartIcon as HeartSolid,
} from '@heroicons/react/24/solid'

export default function Sidebar() {
  const [open, setOpen] = useState(false)
  const [activeHash, setActiveHash] = useState("#dashboard")

  const links = [
    {
      name: 'Dashboard',
      href: '#dashboard',
      iconOutline: ChartBarOutline,
      iconSolid: ChartBarSolid
    },
    {
      name: 'Tops Tracks',
      href: '#topsTracks',
      iconOutline: SquaresOutline,
      iconSolid: SquaresSolid
    },
    {
      name: 'Tops Artists',
      href: '#topsArtists',
      iconOutline: UsersOutline,
      iconSolid: UsersSolid
    },
    {
      name: 'Recent Tracks',
      href: '#recentTracks',
      iconOutline: InboxOutline,
      iconSolid: InboxSolid
    },
    {
      name: 'Sport Stats',
      href: '#sportStats',
      iconOutline: HeartOutline,
      iconSolid: HeartSolid
    },
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
    <>
      <button
        onClick={() => setOpen(!open)}
        className=" hidden sm:inline-flex fixed items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
      >
        <span className="sr-only">Open sidebar</span>
        <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
          <path
            clipRule="evenodd"
            fillRule="evenodd"
            d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
          />
        </svg>
      </button>

      <aside
        className={`fixed top-0 left-0 z-40 w-64 h-screen transition-transform bg-white dark:bg-[#0f0f0f] ${
          open ? 'translate-x-0' : '-translate-x-full'
        } lg:translate-x-0`}
      >
        <div className="h-full border-r dark:border-zinc-700 border-gray-300 px-3 py-4 overflow-y-auto mt-[4.5rem]">
          <ul className="space-y-2 font-medium">
            {links.map((link) => {
              const isActive = activeHash === link.href
              const Icon = isActive ? link.iconSolid : link.iconOutline
              return (
                <li key={link.name}>
                  <a
                    href={link.href}
                    onClick={() => {
                      setOpen(false)
                    }}
                    className={`flex items-center p-2 rounded-lg group ${
                      isActive
                        ? 'bg-primary-200 dark:bg-primary-darkDeep text-primary-900 dark:text-white'
                        : 'text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-zinc-800'
                    }`}
                  >
                    <Icon className={`w-5 h-5 ${
                      isActive
                        ? 'text-black dark:text-white'
                        : 'text-zinc-600 dark:text-zinc-400 group-hover:text-zinc-900 dark:group-hover:text-white'
                    }`} />
                    <span className="ms-3 flex-1 whitespace-nowrap">{link.name}</span>
                  </a>
                </li>
              )
            })}
          </ul>
        </div>
      </aside>
    </>
  )
}
