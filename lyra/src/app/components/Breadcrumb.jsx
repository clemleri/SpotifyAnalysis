'use client'
import Link from 'next/link'

export default function Breadcrumb({ items = [] }) {
  return (
    <nav className="flex" aria-label="Breadcrumb">
      <ol className="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">
        {items.map((item, index) => {
          const isLast = index === items.length - 1
          const showChevron = index > 0

          return (
            <li key={item.label} className="inline-flex items-center">
              {showChevron && (
                <svg
                  className="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 6 10"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="m1 9 4-4-4-4"
                  />
                </svg>
              )}

              {isLast ? (
                <span className="ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400">
                  {item.label}
                </span>
              ) : item.label === 'Home' ? (
                <Link
                  href={item.href}
                  className="inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-dark dark:text-white dark:hover:text-primary-light"
                >
                  {item.icon && <item.icon className="w-3 h-3 me-2.5" />}
                  {item.label}
                </Link>
              ) : (
                <a
                  href={item.href}
                  className="inline-flex items-center ml-2 text-sm font-medium text-gray-700 hover:text-primary-dark dark:text-white dark:hover:text-primary-light"
                >
                  {item.icon && <item.icon className="w-3 h-3 me-2.5" />}
                  {item.label}
                </a>
              )}
            </li>
          )
        })}
      </ol>
    </nav>
  )
}
