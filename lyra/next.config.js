/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        domains: ['i.pravatar.cc'],
        remotePatterns: [
          {
            protocol: 'https',
            hostname: 'i.scdn.co',
            pathname: '**',
          },
        ],
    },
    devIndicators: {
      port: 8080
    }
}

module.exports = nextConfig
