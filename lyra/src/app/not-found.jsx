export default function NotFound() {
    return (
      <main className="relative grid min-h-screen place-items-center bg-white dark:bg-[#0f0f0f] px-6 py-24 sm:py-32 lg:px-8 overflow-hidden">
        {/* Radial background glow */}
        <div
          className="absolute inset-0 z-0"
          style={{
            background: 'radial-gradient(circle at center, rgba(138, 92, 246, 0.3) 0%, transparent 70%)',
          }}
        />
  
        <div className="text-center z-10">
          <p className="text-base font-semibold text-primary">404</p>
          <h1 className="mt-4 text-5xl sm:text-7xl font-extrabold tracking-tight text-balance text-gray-900 dark:text-white">
            Page not found
          </h1>
          <p className="mt-6 text-lg sm:text-xl font-medium text-gray-500 dark:text-gray-400">
            Sorry, we couldn’t find the page you’re looking for.
          </p>
  
          <div className="mt-10 flex justify-center">
            <a
              href="/"
              className="bg-primary hover:bg-primary-dark text-white dark:text-black px-6 py-3 text-sm font-medium rounded-xl transition duration-300"
            >
              Go back home
            </a>
          </div>
        </div>
      </main>
    )
  }
  