'use client'
import Link from 'next/link';
import { useState, useEffect } from 'react';

export default function Navbar() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    console.log('change theme')
    darkMode
      ? document.documentElement.classList.add('dark')
      : document.documentElement.classList.remove('dark');
  }, [darkMode]);

  return (
    <nav className="fixed top-0 w-full backdrop-blur border-b dark:border-zinc-700 border-gray-300 py-4 z-50">
      <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
        <Link href="/" className="text-xl font-semibold flex items-center gap-2">
          <img src="/assets/Lyre_black.png" className="block dark:hidden w-8" alt="Lyra" />
          <img src="/assets/Lyre_white.png" className="hidden dark:block w-8" alt="Lyra" />
          Lyra
        </Link>
        <div className="hidden md:flex items-center gap-4">
          <Link href="/tops" className="hover:text-primary transition">Tops</Link>
          <Link href="/profile" className="border border-primary text-primary px-4 py-2 rounded-xl hover:bg-primary hover:text-white transition">
            Profile
          </Link>
          <button onClick={() => setDarkMode(!darkMode)} className="p-2">
            <img src="/assets/day-and-night.png" className="w-6 opacity-80 dark:invert" />
          </button>
        </div>
      </div>
    </nav>
  );
}
