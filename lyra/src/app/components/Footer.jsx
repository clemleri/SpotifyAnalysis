export default function Footer() {
  return (
    <footer className="mt-32 overflow-x-clip md:overflow-visible">
      {/* Partie haute : Logo + CTA */}
      <div className="w-full h-full mb-48">
        <div className="relative w-20 h-20 mx-auto mb-16">
          {/* Glow */}
          <div className="absolute -inset-48 z-[-1] rounded-full blur-[180px] bg-primary dark:bg-white/60"></div>

          {/* Icône */}
          <div className="relative z-10 flex items-center justify-center w-full h-full rounded-[10px] dark:bg-zinc-900 bg-white shadow-lg border dark:border-zinc-800 border-gray-200">
            <img
              src="/assets/Lyre_black.png"
              width="50"
              height="50"
              alt="Lyra Logo (Light)"
              className="block dark:hidden opacity-80"
            />
            <img
              src="/assets/Lyre_white.png"
              width="50"
              height="50"
              alt="Lyra Logo (Dark)"
              className="hidden dark:block opacity-80"
            />
          </div>
        </div>

        <div className=" flex flex-col items-center text-center">
          <h2 className="z-10 text-3xl font-bold mb-2">Start exploring with Lyra</h2>
          <p className="z-10 flex flex-col dark:text-gray-300 text-gray-600 mb-6">
            <span>Explore a new dimension of music analytics</span>
            <span>with a tool that listens deeper than Spotify ever could.</span>
          </p>
          <a
            href="/login"
            className="z-10 bg-primary hover:bg-primary-dark dark:text-black text-white text-center px-6 py-3 text-lg font-medium rounded-xl w-40 hover:-translate-y-1 transition duration-300"
          >
            Get started
          </a>
        </div>
      </div>

      {/* Partie basse : copyright */}
      <div className="dark:bg-black bg-white dark:text-gray-500 text-sm text-center py-6 px-4">
        <p>
          This software and its content are proprietary and may not be reproduced,
          distributed, or modified without explicit authorization.
        </p>
        <p>Lyra is provided as a service with a free and premium offering.</p>
        <p className="mt-1">&copy; 2024–present Lyra Inc.</p>
      </div>
    </footer>
  );
}
