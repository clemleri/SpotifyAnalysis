'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import {
  HomeIcon,
  ChartBarIcon,
  BoltIcon,
  UserGroupIcon,
  HeartIcon,
  UserCircleIcon
} from '@heroicons/react/24/outline'

const navItems = [
  { href: '/', label: 'Accueil', icon: HomeIcon },
  { href: '/tops', label: 'Tops', icon: ChartBarIcon },
  { href: '/stats', label: 'Stats', icon: BoltIcon },
  { href: '/social', label: 'Social', icon: UserGroupIcon },
  { href: '/profile', label: 'Profil', icon: UserCircleIcon },
]

export default function BottomNav() {
  const pathname = usePathname()

  return (
    <nav className="sm:hidden fixed bottom-0 left-0 w-full bg-white dark:bg-zinc-900 border-t border-gray-200 dark:border-zinc-700 z-50">
      <ul className="flex justify-around items-center py-2">
        {navItems.map((item) => {
          const active = pathname === item.href
          return (
            <li key={item.href}>
              <Link href={item.href} className="flex flex-col items-center text-xs text-gray-600 dark:text-gray-300">
                <item.icon className={`w-6 h-6 mb-1 ${active ? 'text-primary' : ''}`} />
                <span className={`${active ? 'text-primary font-semibold' : ''}`}>{item.label}</span>
              </Link>
            </li>
          )
        })}
      </ul>
    </nav>
  )
}
