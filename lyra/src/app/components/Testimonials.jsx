'use client';
import { motion } from 'framer-motion';

const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.05, duration: 0.4, ease: 'easeOut' },
  }),
};

const testimonials = [
  {
    name: "Ryan Carniato",
    username: "@RyanCarniato",
    img: "https://i.pravatar.cc/100?img=1",
    text: "Lyra lets me rediscover my listening habits. It’s simple, elegant, and exactly what I was missing from Spotify.",
  },
  {
    name: "Nikolaj",
    username: "@lopugit",
    img: "https://i.pravatar.cc/100?img=2",
    text: "Wow, wow, wow. Lyra is... Lyra is... just wow. 🤯🤤🙏",
  },
  {
    name: "David Cramer",
    username: "@zeeg",
    img: "https://i.pravatar.cc/100?img=3",
    text: "Lyra changed the way I look at my music. Now it’s like a time capsule I can open anytime.",
  },
  {
    name: "Anaïs G.",
    username: "@anais_music",
    img: "https://i.pravatar.cc/100?img=4",
    text: "The community features are 🔥 — sharing tracks and seeing what my friends love is so addictive.",
  },
  {
    name: "Tom Devs",
    username: "@tom_dev",
    img: "https://i.pravatar.cc/100?img=5",
    text: "I didn’t think I needed stats on my music. I was wrong. Lyra is a masterpiece.",
  },
  {
    name: "Sasha",
    username: "@sashaluvbeats",
    img: "https://i.pravatar.cc/100?img=6",
    text: "It’s like having my own private music analyst. Clean UI, cool features, 10/10.",
  },
  {
    name: "Yuna B.",
    username: "@yun4beats",
    img: "https://i.pravatar.cc/100?img=7",
    text: "Between playlists and friends, Lyra became my favorite app to reflect on what I listen to.",
  },
  {
    name: "Luca",
    username: "@lucalistens",
    img: "https://i.pravatar.cc/100?img=8",
    text: "One word: aesthetic. The vibes are unmatched. And the data? 🔥",
  },
  {
    name: "Amin A.",
    username: "@aminwave",
    img: "https://i.pravatar.cc/100?img=9",
    text: "I come back every week to check how my music taste evolves. Nothing else makes me do that.",
  },
];

export default function Testimonials() {
  return (
    <section className="max-w-6xl mx-auto px-4 py-20">
      <h2 className="text-5xl font-medium text-center mb-3">Loved by the community</h2>
      <p className="dark:text-gray-400 text-gray-500 text-center mb-10 text-lg">
        Don't take our word for it — listen to what the Lyra community has to say.
      </p>

      <div className="columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4">
        {testimonials.map((t, index) => (
          <motion.div
            key={index}
            className="break-inside-avoid dark:bg-[#141414] bg-white border dark:border-[#212121] border-[#b5b5b5] rounded-xl p-6 shadow-md"
            custom={index}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.2 }}
            variants={fadeInUp}
          >
            <div className="flex items-center gap-3 mb-4">
              <img
                src={t.img}
                alt={t.name}
                className="w-10 h-10 rounded-full object-cover"
              />
              <div>
                <div className="font-semibold leading-tight">{t.name}</div>
                <div className="text-sm text-gray-500">{t.username}</div>
              </div>
            </div>
            <p
              className={`dark:text-gray-300 text-gray-500 text-sm ${
                t.text.length > 150 ? 'text-[0.875rem]' : 'text-base'
              }`}
            >
              {t.text}
            </p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
