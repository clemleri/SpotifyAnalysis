'use client'
import { motion } from 'framer-motion'

export default function FlowIcons() {
  return (
    <>
      <motion.div
        className="absolute z-10 text-xl"
        initial={{ x: -500, y: 0 }}
        animate={{ x: [ -500, 0, 400, 500, 2000 ], y: [ 0, 20, 50, 0, 0 ] }}
        transition={{
          duration: 6,
          ease: "easeInOut",
          repeat: Infinity,
          repeatDelay: 1
        }}
      >
        🎵
      </motion.div>

      <motion.div
        className="absolute z-10 text-xl"
        initial={{ x: -500, y: 100 }}
        animate={{ x: [ -500, 0, 400, 500, 2000 ], y: [ 100, 120, 150, 250, 250 ] }}
        transition={{
          duration: 7,
          ease: "easeInOut",
          repeat: Infinity,
          repeatDelay: 2
        }}
      >
        👤
      </motion.div>

      <motion.div
        className="absolute z-10 text-xl"
        initial={{ x: -500, y: 300 }}
        animate={{ x: [ -500, 0, 400, 500, 2000 ], y: [ 300, 270, 260, 250, 250 ] }}
        transition={{
          duration: 8,
          ease: "easeInOut",
          repeat: Infinity,
          repeatDelay: 3
        }}
      >
        📂
      </motion.div>

      {/* Résultat final qui sort */}
      <motion.div
        className="absolute z-10 text-xl"
        initial={{ x: 500, y: 250 }}
        animate={{ x: [ 500, 1000, 1500, 2000 ] }}
        transition={{
          duration: 6,
          ease: "easeInOut",
          repeat: Infinity,
          repeatDelay: 1.5
        }}
      >
        📊
      </motion.div>
    </>
  )
}
