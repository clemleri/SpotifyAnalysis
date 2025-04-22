'use client'

import { useState } from 'react'
import {
  ChartBarIcon,
  Squares2X2Icon,
  InboxIcon,
  UsersIcon,
  ShoppingBagIcon,
  HeartIcon,
} from '@heroicons/react/24/outline'


export default function Sidebar() {
  const [open, setOpen] = useState(false)

  const links = [
    { name: 'Dashboard', href: '#dashboard', icon: ChartBarIcon },
    { name: 'Tops Tracks', href: '#topsTracks', icon: Squares2X2Icon, },
    { name: 'Tops Artists', href: '#topsArtists', icon: UsersIcon, },
    { name: 'Recent Tracks', href: '#recentTracks', icon: InboxIcon },
    { name: 'Sport Stats', href: '#sportStats', icon: HeartIcon },
  ]

  return (
    <>
      <button
        onClick={() => setOpen(!open)}
        className="inline-flex fixed items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
      >
        <span className="sr-only">Open sidebar</span>
        <svg
          className="w-6 h-6"
          aria-hidden="true"
          fill="currentColor"
          viewBox="0 0 20 20"
        >
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
        } sm:translate-x-0`}
      >
        <div className="h-full  border-r dark:border-zinc-700 border-gray-300 px-3 py-4 overflow-y-auto mt-[4.5rem]">
          <ul className="space-y-2 font-medium">
            {links.map((link) => (
              <li key={link.name}>
                <a
                  href={link.href}
                  onClick={() => {
                    if (window.innerWidth < 640) setOpen(false)
                  }}
                  className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-zinc-800 group"
                >
                  <link.icon className="w-5 h-5 text-gray-500 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
                  <span className="ms-3 flex-1 whitespace-nowrap">{link.name}</span>

                  {typeof link.badge === 'string' ? (
                    <span className="inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                      {link.badge}
                    </span>
                  ) : typeof link.badge === 'number' ? (
                    <span className="inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">
                      {link.badge}
                    </span>
                  ) : null}
                </a>
              </li>
            ))}
          </ul>
        </div>
      </aside>
    </>
  )
}
