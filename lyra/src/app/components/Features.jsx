"use client"

import { motion } from "framer-motion";

const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.1, duration: 0.5 },
  }),
};

const features = [
  {
    title: "Advanced Insights",
    description: ["Discover your top artists,", "tracks, albums, all in one place."],
    icon: "/assets/stats-icon.png",
    glowColor: "#433780",
    layout: "default",
  },
  {
    title: "Friends & Sharing",
    description: ["Connect with friends and see", "how your music tastes stack up."],
    icon: "/assets/friends-icon.png",
    glowColor: "#297c7d",
    layout: "wide",
  },
  {
    title: "Music Chats",
    description: ["Talk about your favorite tracks,", "start groups, and share your vibe."],
    icon: "/assets/chat-music-icon.png",
    glowColor: "#2e6b45",
    layout: "wide",
  },
  {
    title: "Import Spotify History",
    description: ["Dive into your past", "listening data like never before."],
    icon: "/assets/data-import-icon.png",
    glowColor: "#a64a11",
    layout: "default",
  },
];

export default function Features() {
  return (
    <section className="max-w-6xl mx-auto my-24 px-4">
      <p className="text-center text-5xl font-medium mb-2">Redefining users experience</p>
      <p className="text-center text-xl font-medium dark:text-gray-300 text-gray-500 mb-20">
        Lyra makes your Spotify stats simple again
      </p>

      {/* Garde le grid ici */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {features.map((feature, index) => (
          <motion.div
            key={index}
            custom={index}
            variants={fadeInUp}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            className={`${
              feature.layout === "wide" ? "lg:col-span-2" : ""
            } dark:bg-[#141414] bg-white border dark:border-[#212121] border-[#b5b5b5] rounded-xl p-8 shadow-lg min-h-80 flex flex-col justify-between ${
              feature.layout === "wide" ? "items-center text-center" : ""
            } group relative overflow-hidden`}
          >
            {/* Glow background */}
            <div className="absolute inset-0 flex justify-center items-center z-0 opacity-100 lg:opacity-0 lg:group-hover:opacity-100 transition duration-500 ease-out">
              <div
                className={`w-[300px] h-[300px] rounded-full blur-[100px] lg:animate-pulse`}
                style={{
                  backgroundColor: feature.glowColor,
                  willChange: "transform",
                  transform: "translateZ(0)",
                }}
              />
            </div>

            {/* Icon */}
            <div className="flex-grow flex items-center justify-center w-full z-10 mb-4">
              <img src={feature.icon} alt={feature.title} className="h-48 opacity-70" />
            </div>

            {/* Texte */}
            <div className={`z-10 ${feature.layout === "default" ? "text-left" : "mt-4"}`}>
              <h3 className="text-xl font-semibold mb-1">{feature.title}</h3>
              <p className="dark:text-gray-400 text-gray-500 flex flex-col">
                {feature.description.map((line, i) => (
                  <span key={i}>{line}</span>
                ))}
              </p>
            </div>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
