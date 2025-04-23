'use client'
import { motion } from 'framer-motion'
import { useEffect, useState } from 'react'

import Link from "next/link";

export default function Hero() {
  const [showSVG, setShowSVG] = useState(false)

  useEffect(() => {
    // Attendre que l'animation d'entrée soit finie
    const timeout = setTimeout(() => {
      setShowSVG(true)
    }, 1200) // durée de l’animation Hero (en ms)

    return () => clearTimeout(timeout)
  }, [])

  return (
    <section className="text-center max-w-4xl mx-auto overflow-x-clip md:overflow-visible mt-[-8rem]">
      <div className="w-full h-screen flex flex-col justify-center items-center ">
        <h1 className="z-10 text-5xl font-extrabold mb-4 leading-tight dark:text-white text-primary">
          The Build Tool<br />
          For Your Playlist
        </h1>
        <p className="z-10 text-lg text-gray-500 dark:text-gray-300 mb-10">
          Lyra is your musical mirror,<br />
          revealing what Spotify doesn't.
        </p>

        <div className="flex justify-center gap-4 mb-10">
          <Link
            href="/login"
            className="z-10 dark:bg-primary bg-background hover:bg-background-600 dark:hover:bg-primary-dark text-white dark:text-black px-6 py-3 text-lg font-medium rounded-xl hover:-translate-y-1 transition duration-300"
          >
            Get started
          </Link>
          <a
            href="#pricing"
            className="z-10 border dark:border-primary border-background dark:text-primary text-background px-6 py-3 text-lg font-medium rounded-xl dark:hover:border-primary-dark hover:border-background-600 dark:hover:text-primary-dark hover:text-background-600 hover:-translate-y-1 transition duration-300"
          >
            See Pricing
          </a>
        </div>
      </div>
      
      {showSVG && (
        <svg
          className="absolute left-0 top-[34.2rem] z-0 w-screen overflow-visible opacity-0 animate-fade-in delay-[1000ms] ..."
          width="100%"
          height="500"
          viewBox="-100 0 1700 500"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          {/* === Courbes SVG avec opacité 50% === */}
          <path id="curve1" d="M -100 0 C 500 0, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve2" d="M -100 80 C 500 80, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve3" d="M -100 160 C 500 160, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve4" d="M -100 250 C 500 250, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve5" d="M -100 340 C 500 340, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve6" d="M -100 420 C 500 420, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="curve7" d="M -100 500 C 500 500, 650 250, 750 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />
          <path id="exit" d="M 750 250 L 1600 250" stroke="black" strokeWidth="2" className="dark:stroke-white opacity-30" />

          {/* === Images animées === */}

          {/* 🎵 track_hero.png */}
          <g visibility="hidden">
            <set attributeName="visibility" to="visible" begin="0s" />
            <image
              href="/assets/track_hero.png"
              width="32"
              height="32"
              x="-16"
              y="-16"
              className='dark:invert'

            />
            <animateMotion dur="6s" repeatCount="indefinite" rotate="auto">
              <mpath href="#curve1" />
            </animateMotion>
          </g>

          {/* 👤 user_hero.png */}
          <g visibility="hidden">
          <set attributeName="visibility" to="visible" begin="1s" />
            <image
              href="/assets/user_hero.png"
              width="32"
              height="32"
              x="-16"
              y="-16"
              className='dark:invert'
            />
            <animateMotion dur="7s" begin="1s" repeatCount="indefinite" rotate="auto">
              <mpath href="#curve4" />
            </animateMotion>
          </g>

          {/* 📂 albums_hero.png */}
          <g visibility="hidden">
            <set attributeName="visibility" to="visible" begin="2s" />
            <image
              href="/assets/albums_hero.png"
              width="32"
              height="32"
              x="-16"
              y="-16"
              className='dark:invert'

            />
            <animateMotion dur="8s" begin="2s" repeatCount="indefinite" rotate="auto">
              <mpath href="#curve7" />
            </animateMotion>
          </g>

          {/* 📊 stat_hero.png */}
          <g visibility="hidden">
            <set attributeName="visibility" to="visible" begin="6s" />
            <image
              href="/assets/stat_hero.png"
              width="32"
              height="32"
              x="-16"
              y="-16"
              className='dark:invert'

            />
            <animateMotion dur="5s" begin="6s" repeatCount="indefinite" rotate="auto">
              <mpath href="#exit" />
            </animateMotion>
          </g>
        </svg>
      )}





      {/* Logo avec glow */}
      <div className="relative w-28 h-28 mx-auto mb-80">
        <div className="absolute -inset-64 z-[-1] rounded-full blur-[180px] animate-pulse bg-primary dark:bg-white/50" style={{willChange: 'transform',transform: 'translateZ(0)'}}></div>
    
        <div className="relative z-10 flex items-center justify-center w-full h-full rounded-[20px] dark:bg-zinc-900 bg-white shadow-lg border dark:border-zinc-800 border-gray-200">
          <img
            src="/assets/Lyre_black.png"
            width="70"
            height="70"
            alt="Lyra Logo (Light)"
            className="block dark:hidden opacity-80"
          />
          <img
            src="/assets/Lyre_white.png"
            width="70"
            height="70"
            alt="Lyra Logo (Dark)"
            className="hidden dark:block opacity-80"
          />
        </div>
        
      </div>
    </section>
  );
}
