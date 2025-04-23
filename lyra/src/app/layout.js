import { Inter } from 'next/font/google'
import './globals.css'
import { ConnectionProvider } from './context/ConnectionContext'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Lyra',
  description: 'Your Spotify stats',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              try {
                const theme = localStorage.getItem('theme');
                if (theme === 'dark') {
                  document.documentElement.classList.add('dark');
                }
              } catch(e) {}
            `,
          }}
        />
        <link href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css" rel="stylesheet" />
        <script src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"></script>

      </head>
      <body className="bg-white dark:bg-background text-black dark:text-white">
          <ConnectionProvider>
            {children}
          </ConnectionProvider>
      </body>
    </html>
  )
}
