export default function Hero() {
  return (
    <section className="text-center max-w-4xl mx-auto overflow-x-clip md:overflow-visible mt-[-4rem]">
      <div className="w-full h-screen flex flex-col justify-center items-center ">
        <h1 className="z-10 text-5xl font-extrabold mb-4 leading-tight">
          The Build Tool<br />
          For Your Playlist
        </h1>
        <p className="z-10 text-lg text-gray-500 dark:text-gray-300 mb-10">
          Lyra is your musical mirror,<br />
          revealing what Spotify doesn't.
        </p>

        <div className="flex justify-center gap-4 mb-10">
          <a
            href="/login"
            className="z-10 bg-primary hover:bg-primary-dark text-white dark:text-black px-6 py-3 text-lg font-medium rounded-xl hover:-translate-y-1 transition duration-300"
          >
            Get started
          </a>
          <a
            href="#pricing"
            className="z-10 border border-primary text-primary px-6 py-3 text-lg font-medium rounded-xl hover:bg-primary hover:text-white hover:-translate-y-1 transition duration-300"
          >
            See Pricing
          </a>
        </div>
      </div>

      {/* Logo avec glow */}
      <div className="relative w-28 h-28 mx-auto mb-80">
        <div className="absolute -inset-64 z-[-1] rounded-full blur-[180px] animate-pulse z-0 bg-primary dark:bg-white/60"></div>

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
