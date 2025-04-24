'use client'
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronLeft, ChevronRight } from 'lucide-react'

export default function PodiumCarousel({ items, isArtist = false }) {
  const [index, setIndex] = useState(0)

  const handleNext = () => {
    setIndex((prev) => (prev + 1) % items.length)
  }

  const handlePrev = () => {
    setIndex((prev) => (prev - 1 + items.length) % items.length)
  }

  const medals = [
    { emoji: '🥇', pulseClass: 'animate-glow-gold' },
    { emoji: '🥈', pulseClass: 'animate-glow-silver' },
    { emoji: '🥉', pulseClass: 'animate-glow-bronze' }
  ]

  const item = items[index]
  const style = medals[index] || {}

  if (!items || !items.length || !items[index]) return null
  const imageUrl = isArtist
  ? item?.images?.[0]?.url
  : item?.album?.images?.[0]?.url;

  return (
    <div className="relative w-full flex flex-col items-center sm:hidden">
      <div className="relative w-36 h-36 mb-4">
        <div className={`absolute z-0 w-36 h-36 rounded-full blur-2xl opacity-50 ${style.pulseClass}`} />
        <span className="absolute -top-3 -left-3 text-xl z-[20]">{style.emoji}</span>
        <AnimatePresence mode="wait">
          <motion.img
            key={item.id}
            src={imageUrl || "/icon_browser.png"}

            alt={item?.name || "Unknown"}
            className={`w-36 h-36 object-cover ${isArtist ? 'rounded-full' : 'rounded-md'} shadow relative z-10`}
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -50 }}
            transition={{ duration: 0.3 }}
          />
        </AnimatePresence>
      </div>

      <p className="text-sm font-medium text-center w-40">{item.name}</p>
      {!isArtist && (
        <p className="text-xs text-gray-500 text-center w-40">
          {item.artists.map((a) => a.name).join(', ')}
        </p>
      )}

      <div className="flex gap-4 mt-4">
        <button onClick={handlePrev} className="text-zinc-500 hover:text-black dark:hover:text-white">
          <ChevronLeft size={24} />
        </button>
        <button onClick={handleNext} className="text-zinc-500 hover:text-black dark:hover:text-white">
          <ChevronRight size={24} />
        </button>
      </div>
    </div>
  )
}
