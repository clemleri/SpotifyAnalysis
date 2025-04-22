export default function Footer({ extend = true }) {
  return (
    <footer className="mt-32">
      {/* Partie top : uniquement si extend === true */}
      {extend && (
        <div className="w-full h-full mb-48">
          {/* Glow */}
          <div className="relative w-20 h-20 mx-auto mb-16">
            <div className="absolute -inset-48 z-[-1] rounded-full dark:bg-white/70 bg-primary blur-[180px]" />
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

          <div className="flex flex-col items-center">
            <h2 className="text-3xl font-bold text-center mb-2">Start exploring with Lyra</h2>
            <p className="flex flex-col items-center dark:text-gray-300 text-gray-600 mb-6">
              <span>Explore a new dimension of music analytics</span>
              <span>with a tool that listens deeper than Spotify ever could.</span>
            </p>
            <a
              href="/login"
              className="bg-primary w-[10rem] text-white dark:text-black text-center px-6 py-3 text-lg font-medium rounded-xl hover:bg-primary-dark hover:-translate-y-1 transition duration-300"
            >
              Get started
            </a>
          </div>
        </div>
      )}

      {/* Partie basse : copyright */}
      <div className=" dark:text-gray-300 text-black text-sm text-center py-6 px-4">
        <p>
          This software and its content are proprietary and may not be reproduced, distributed, or modified without
          explicit authorization.
        </p>
        <p>Lyra is provided as a service with a free and premium offering.</p>
        <p className="mt-1">Copyright © 2024-present Lyra Inc.</p>
      </div>
    </footer>
  );
}
