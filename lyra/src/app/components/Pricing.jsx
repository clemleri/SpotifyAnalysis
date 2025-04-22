import { CheckIcon } from '@heroicons/react/20/solid';

const tiers = [
  {
    name: 'Free Plan',
    id: 'tier-free',
    href: '/login',
    priceMonthly: '0€',
    description: 'Enjoy essential features of Lyra with occasional audio ads.',
    features: [
      'Stats & tops every month',
      'Recent listening history',
      'No customization',
      'Contains ads',
    ],
    featured: false,
  },
  {
    name: 'Premium Plan',
    id: 'tier-premium',
    href: '/login',
    priceMonthly: '5,99€',
    description: 'Unlock the full Lyra experience with no ads and extra features.',
    features: [
      'All Free features',
      'No ads',
      'Custom vibes & themes',
      'Extended historical data',
      'Priority support',
    ],
    featured: true,
  },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

export default function Pricing() {
  return (
    <section id="pricing" className="relative isolate px-6 py-24 sm:py-32 lg:px-8 ">
      {/* Glow background */}
      <div
        aria-hidden="true"
        className="absolute inset-x-0 -top-3 -z-10 transform-gpu overflow-hidden px-36 blur-3xl"
      >
        <div
          style={{
            clipPath:
              'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)',
          }}
          className="mx-auto aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#8a5cf6] to-[#653acb] opacity-30"
        />
      </div>

      <div className="mx-auto max-w-4xl text-center">
        <h2 className="text-base font-semibold text-primary">Pricing</h2>
        <p className="mt-2 text-5xl font-medium tracking-tight text-gray-900 dark:text-white">
          Choose the right plan for you
        </p>
      </div>
      <p className="mx-auto mt-6 max-w-2xl text-center text-lg font-medium text-gray-600 dark:text-gray-400 ">
        Lyra is free forever — or go premium for an ad-free experience.
      </p>

      <div className="mx-auto mt-16 grid max-w-lg grid-cols-1 items-center gap-y-6 sm:mt-20 sm:gap-y-0 lg:max-w-4xl lg:grid-cols-2">
        {tiers.map((tier, tierIdx) => (
          <div
            key={tier.id}
            className={classNames(
              tier.featured ? 'relative dark:bg-primary-darkDeep bg-primary-lightDeep shadow-2xl text-white' : 'bg-white/60 dark:bg-[#141414]',
              tier.featured
                ? ''
                : tierIdx === 0
                ? 'rounded-t-3xl sm:rounded-b-none lg:rounded-tr-none lg:rounded-bl-3xl'
                : 'sm:rounded-t-none lg:rounded-tr-3xl lg:rounded-bl-none',
              'rounded-3xl p-8 ring-1 ring-gray-900/10 dark:ring-gray-700 sm:p-10',
            )}
          >
            <h3 id={tier.id} className={classNames(tier.featured ? 'text-primary' : 'text-primary', 'text-base font-semibold')}>
              {tier.name}
            </h3>
            <p className="mt-4 flex items-baseline gap-x-2">
              <span className={classNames('text-5xl font-semibold tracking-tight', tier.featured ? 'text-white' : 'text-gray-900 dark:text-white')}>
                {tier.priceMonthly}
              </span>
              <span className={classNames(tier.featured ? 'text-gray-400' : 'text-gray-500', 'text-base')}>/month</span>
            </p>
            <p className={classNames('mt-6 text-base', tier.featured ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400')}>
              {tier.description}
            </p>
            <ul role="list" className={classNames('mt-8 space-y-3 text-sm sm:mt-10', tier.featured ? 'text-gray-300' : 'text-gray-600 dark:text-gray-400')}>
              {tier.features.map((feature) => (
                <li key={feature} className="flex gap-x-3">
                  <CheckIcon
                    aria-hidden="true"
                    className={classNames('h-6 w-5 flex-none', tier.featured ? 'text-primary' : 'text-primary')}
                  />
                  {feature}
                </li>
              ))}
            </ul>
            <a
              href={tier.href}
              aria-describedby={tier.id}
              className={classNames(
                tier.featured
                  ? 'bg-primary text-white hover:bg-primary-dark focus-visible:outline-primary'
                  : 'text-primary ring-1 ring-primary ring-inset hover:bg-primary hover:text-white focus-visible:outline-primary',
                'mt-8 block rounded-md px-3.5 py-2.5 text-center text-sm font-semibold transition-colors duration-300 focus-visible:outline-2 focus-visible:outline-offset-2 sm:mt-10',
              )}
            >
              Get started today
            </a>
          </div>
        ))}
      </div>
    </section>
  );
}
