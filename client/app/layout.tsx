import type { Metadata } from 'next'
import { DM_Sans } from 'next/font/google'
import './globals.css'
import Navbar from '@/components/Universal/Navbar/Navbar'
import Footer from '@/components/Universal/Footer/Footer'

const inter = DM_Sans({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'URL Shortener',
  description: 'This is a URL Shortener Made with Flask, Postgres and Next.js',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} flex flex-col gap-10`}>
        <Navbar />
        {children}
        <Footer />
        </body>
    </html>
  )
}
