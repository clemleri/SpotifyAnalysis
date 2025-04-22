"use client";
import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import LayoutWithSidebar from "../components/LayoutWithSidebar";
import SpotifyLoginButton from "../components/SpotifyLoginButton";
import StravaLoginButton from "../components/StravaLoginButton";

export default function Tops() {
  const [showSportStats, setShowSportStats] = useState(false);

  useEffect(() => {
    const checkHash = () => {
      const currentHash = window.location.hash;
      setShowSportStats(currentHash === "#sportStats");
    };

    checkHash();

    // écoute les changements d’ancre (hash)
    window.addEventListener("hashchange", checkHash);

    return () => {
      window.removeEventListener("hashchange", checkHash);
    };
  }, []);

  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <LayoutWithSidebar>
        {showSportStats && (
          <div className="w-full h-[100vh] mt-[-4rem] gap-6 flex-col md:flex-row flex justify-center items-center">
            <SpotifyLoginButton isConnected={false} />
            <StravaLoginButton isConnected={false} />
          </div>
        )}
      </LayoutWithSidebar>
    </main>
  );
}
