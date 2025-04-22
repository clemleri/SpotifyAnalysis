'use client'

// pages/homepage.jsx
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Testimonials from "../components/Testimonials";
import Pricing from "../components/Pricing";
import Footer from "../components/Footer";
import Sidebar from "../components/Sidebar";
import LayoutWithSidebar from "../components/LayoutWithSidebar";
import UserAvatar from "../components/UserAvatar";

const userData = {
  username: 'Driss Baritaud',
  language: 'French 🇫🇷',
  followers: 258,
  avatarUrl: 'https://i.pravatar.cc/150?img=32',
}


export default function Tops() {
  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <div className="mt-[-4rem] flex items-center justify-center min-h-screen px-4">
      <UserAvatar
        username={userData.username}
        language={userData.language}
        followers={userData.followers}
        avatarUrl={userData.avatarUrl}
        onLogout={() => alert('Déconnecté !')}
      />
      </div>
      
      <Footer extend={false} />
    </main>
  );
}
