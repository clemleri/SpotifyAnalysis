'use client'

import { Fragment, useState } from 'react'
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
  Transition,
} from '@headlessui/react'
import {
  Bars3Icon,
  XMarkIcon,
  ChevronDownIcon,
  ChartBarIcon,
  Squares2X2Icon,
  UsersIcon,
} from '@heroicons/react/24/outline'
import Link from 'next/link'
import ThemeToggleButton from './ThemeToggleButton'
import { usePathname } from 'next/navigation'

const topsMenu = [
  { name: 'Dashboard', href: '/tops#dashboard', icon: ChartBarIcon },
  { name: 'Tops Tracks', href: '/tops#topsTracks', icon: Squares2X2Icon },
  { name: 'Tops Artists', href: '/tops#topsArtists', icon: UsersIcon },
]

export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const pathname = usePathname()
  const isOnTopsPage = pathname === '/tops'

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
            <span className="text-xl font-bold">lyra</span>
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
                {topsMenu.map((item) =>
                  isOnTopsPage ? (
                    <a
                      key={item.name}
                      href={item.href}
                      className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-zinc-700 text-sm text-gray-800 dark:text-white"
                    >
                      <item.icon className="w-5 h-5 text-primary" />
                      {item.name}
                    </a>
                  ) : (
                    <Link
                      key={item.name}
                      href={item.href}
                      className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-zinc-700 text-sm text-gray-800 dark:text-white"
                    >
                      <item.icon className="w-5 h-5 text-primary" />
                      {item.name}
                    </Link>
                  )
                )}
              </div>
            </PopoverPanel>
          </Popover>

          <Link
            href="/profile"
            className="text-sm font-semibold text-primary border border-primary px-4 py-2 rounded-xl hover:bg-primary hover:text-white transition"
          >
            Profile
          </Link>

          <ThemeToggleButton />
        </PopoverGroup>
      </nav>

      {/* Mobile Nav */}
      <Transition show={mobileMenuOpen} as={Fragment}>
        <Dialog as="div" className="lg:hidden relative z-50" onClose={setMobileMenuOpen}>
          <Transition.Child
            as={Fragment}
            enter="transition-opacity ease-in duration-200"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="transition-opacity ease-out duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black/30" />
          </Transition.Child>

          <Transition.Child
            as={Fragment}
            enter="transition-transform duration-300 ease-in-out"
            enterFrom="translate-x-full"
            enterTo="translate-x-0"
            leave="transition-transform duration-300 ease-in-out"
            leaveFrom="translate-x-0"
            leaveTo="translate-x-full"
          >
            <DialogPanel className="fixed inset-y-0 right-0 w-full md:w-[50vw] bg-white dark:bg-[#0f0f0f] p-6 shadow-lg overflow-y-auto">
              <div className="flex justify-between items-center mb-6">
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
                <button onClick={() => setMobileMenuOpen(false)} className="p-2">
                  <XMarkIcon className="w-6 h-6 text-gray-700 dark:text-white" />
                </button>
              </div>

              <Disclosure as="div" className="mb-4">
                <DisclosureButton className="w-full flex items-center justify-between rounded py-2 text-left font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-zinc-800 px-2">
                  Tops
                  <ChevronDownIcon className="w-5 h-5 text-gray-400" />
                </DisclosureButton>
                <DisclosurePanel className="pl-4">
                  {topsMenu.map((item) =>
                    isOnTopsPage ? (
                      <a
                        key={item.name}
                        href={item.href}
                        className="block py-2 text-sm text-gray-700 dark:text-gray-300 hover:underline"
                      >
                        {item.name}
                      </a>
                    ) : (
                      <Link
                        key={item.name}
                        href={item.href}
                        className="block py-2 text-sm text-gray-700 dark:text-gray-300 hover:underline"
                      >
                        {item.name}
                      </Link>
                    )
                  )}
                </DisclosurePanel>
              </Disclosure>

              <Link
                href="/profile"
                className="block py-2 px-2 text-[16px] rounded font-medium hover:bg-gray-100 dark:hover:bg-zinc-800"
              >
                Profile
              </Link>

              <div className="w-full flex justify-center items-center mb-8 absolute bottom-0 left-0">
                <ThemeToggleButton mobile />
              </div>
            </DialogPanel>
          </Transition.Child>
        </Dialog>
      </Transition>
    </header>
  )
}
