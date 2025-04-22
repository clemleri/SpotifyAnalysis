'use client'

import { useState, useEffect } from 'react'
import {
  Dialog,
  DialogPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
} from '@headlessui/react'
import {
  Bars3Icon,
  XMarkIcon,
  ChevronDownIcon,
  UserIcon,
  MoonIcon,
  SunIcon,
  StarIcon,
  MusicalNoteIcon,
} from '@heroicons/react/24/outline'
import Link from 'next/link'

const topsMenu = [
  { name: 'Top Tracks', href: '/tops', icon: MusicalNoteIcon },
  { name: 'Top Artists', href: '/tops', icon: StarIcon },
]
export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('theme') === 'dark'
    }
    return false
  })  
  
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  }, [darkMode])
  

  return (
    <header className="bg-white dark:bg-[#0f0f0f] border-b dark:border-zinc-700 border-gray-300 sticky top-0 z-50">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4">
        {/* Logo */}
        <div className="flex lg:flex-1">
          <Link href="/" className="flex items-center gap-2">
            <img
              src="/assets/Lyre_black.png"
              alt="Lyra Logo Light"
              width={30}
              height={30}
              className="block dark:hidden"
            />
            <img
              src="/assets/Lyre_white.png"
              alt="Lyra Logo Dark"
              width={30}
              height={30}
              className="hidden dark:block"
            />
            <span className="text-xl font-bold">Lyra</span>
          </Link>
        </div>

        {/* Mobile menu toggle */}
        <div className="flex lg:hidden">
          <button
            onClick={() => setMobileMenuOpen(true)}
            className="p-2 text-gray-700 dark:text-white"
          >
            <Bars3Icon className="w-6 h-6" />
          </button>
        </div>

        {/* Desktop Nav */}
        <PopoverGroup className="hidden lg:flex lg:items-center lg:gap-x-8">
          <Popover className="relative">
            <PopoverButton className="flex items-center gap-x-1 font-semibold text-sm text-gray-900 dark:text-white">
              Tops
              <ChevronDownIcon className="w-5 h-5 text-gray-400 dark:text-gray-500" />
            </PopoverButton>
            <PopoverPanel className="absolute top-full z-10 mt-2 w-56 rounded-xl bg-white dark:bg-zinc-800 shadow-lg ring-1 ring-gray-200 dark:ring-zinc-600">
              <div className="p-2">
                {topsMenu.map((item) => (
                  <Link
                    key={item.name}
                    href={item.href}
                    className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-zinc-700 text-sm text-gray-800 dark:text-white"
                  >
                    <item.icon className="w-5 h-5 text-primary" />
                    {item.name}
                  </Link>
                ))}
              </div>
            </PopoverPanel>
          </Popover>

          <Link href="/profile" className="text-sm font-semibold text-primary border border-primary px-4 py-2 rounded-xl hover:bg-primary hover:text-white transition">
            Profile
          </Link>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded hover:bg-gray-100 dark:hover:bg-zinc-700 transition"
            aria-label="Toggle Theme"
          >
            {darkMode ? (
              <SunIcon className="w-5 h-5 text-yellow-400" />
            ) : (
              <MoonIcon className="w-5 h-5 text-gray-700 dark:text-gray-300" />
            )}
          </button>
        </PopoverGroup>
      </nav>

      {/* Mobile Nav */}
      <Dialog open={mobileMenuOpen} onClose={setMobileMenuOpen} className="lg:hidden">
        <div className="fixed inset-0 z-40 bg-black/30" aria-hidden="true" />
        <DialogPanel className="fixed top-0 right-0 z-50 h-full w-72 bg-white dark:bg-[#0f0f0f] p-6 shadow-lg">
          <div className="flex justify-between items-center mb-6">
            <a href="/" className="flex items-center gap-2">
              <img
                src="/assets/Lyre_black.png"
                alt="Lyra Logo Light"
                width={30}
                height={30}
                className="block dark:hidden"
              />
              <img
                src="/assets/Lyre_white.png"
                alt="Lyra Logo Dark"
                width={30}
                height={30}
                className="hidden dark:block"
              />
              <span className="text-xl font-bold">Lyra</span>
            </a>
            <button onClick={() => setMobileMenuOpen(false)} className="p-2">
              <XMarkIcon className="w-6 h-6 text-gray-700 dark:text-white" />
            </button>
          </div>

          <Disclosure as="div" className="mb-4">
            <DisclosureButton className="w-full flex items-center justify-between rounded py-2 text-left font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-zinc-700 px-2">
              Tops
              <ChevronDownIcon className="w-5 h-5 text-gray-400" />
            </DisclosureButton>
            <DisclosurePanel className="pl-4">
              {topsMenu.map((item) => (
                <a
                  key={item.name}
                  href={item.href}
                  className="block py-2 text-sm text-gray-700 dark:text-gray-300 hover:underline"
                >
                  {item.name}
                </a>
              ))}
            </DisclosurePanel>
          </Disclosure>

          <a href="/profile" className="block py-2 text-sm text-primary font-medium">
            Profile
          </a>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="mt-4 flex items-center gap-2 p-2 rounded hover:bg-gray-100 dark:hover:bg-zinc-700 transition"
          >
            {darkMode ? (
              <>
                <SunIcon className="w-5 h-5 text-yellow-400" />
                <span className="text-sm text-gray-900 dark:text-white">Light Mode</span>
              </>
            ) : (
              <>
                <MoonIcon className="w-5 h-5 text-gray-700 dark:text-gray-300" />
                <span className="text-sm text-gray-900 dark:text-white">Dark Mode</span>
              </>
            )}
          </button>
        </DialogPanel>
      </Dialog>
    </header>
  )
}
