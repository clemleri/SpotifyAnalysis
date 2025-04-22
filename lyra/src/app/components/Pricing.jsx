export default function Pricing() {
  return (
    <section id="pricing" className="max-w-5xl mx-auto px-4 py-20">
      <h2 className="text-3xl font-bold text-center mb-4">Choose your plan</h2>
      <p className="text-center dark:text-gray-400 text-gray-500 mb-12">
        Lyra is free forever — or go premium for an ad-free experience.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
        {/* Free Plan */}
        <div className="dark:bg-[#141414] bg-white border border-[#212121] rounded-2xl p-8 shadow-md hover:shadow-black/10 transition">
          <h3 className="text-xl font-semibold mb-2">Free Plan</h3>
          <p className="dark:text-gray-400 text-gray-800 mb-6">
            Enjoy the essential features of Lyra with occasional audio ads.
          </p>

          <div className="text-4xl font-bold text-primary mb-1">0€</div>
          <p className="text-sm dark:text-gray-500 mb-6">Free forever</p>

          <ul className="text-sm dark:text-gray-300 text-gray-500 space-y-2 mb-6">
            <li>✔️ Stats & tops every month</li>
            <li>✔️ Recent listening history</li>
            <li>🚫 No customization</li>
            <li>🚫 Contains ads</li>
          </ul>

          <button className="w-full bg-zinc-800 text-white border border-zinc-700 py-2 rounded hover:bg-zinc-700 transition">
            Continue with Free
          </button>
        </div>

        {/* Premium Plan */}
        <div className="bg-gradient-to-b from-primary to-transparent border border-primary rounded-2xl p-8 shadow-lg hover:shadow-primary transition duration-300">
          <h3 className="text-xl font-semibold mb-2">Premium Plan</h3>
          <p className="dark:text-gray-400 text-gray-800 mb-6">
            Unlock the full Lyra experience with no ads and extra features.
          </p>

          <div className="text-4xl font-bold mb-1">5,99€</div>
          <p className="text-sm dark:text-gray-500 mb-6">per month</p>

          <ul className="text-sm dark:text-gray-300 space-y-2 mb-6">
            <li>✔️ All Free features</li>
            <li>✔️ No ads</li>
            <li>✔️ Custom vibes & themes</li>
            <li>✔️ Extended historical data</li>
            <li>✔️ Priority support</li>
          </ul>

          <button className="w-full bg-primary font-semibold text-white py-2 rounded hover:bg-primary-dark transition">
            Upgrade to Premium
          </button>
        </div>
      </div>
    </section>
  );
}
