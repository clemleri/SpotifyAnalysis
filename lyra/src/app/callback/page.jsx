"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function CallbackPage() {
  const router = useRouter();

  useEffect(() => {
    const handleCallback = async () => {
      const code = new URLSearchParams(window.location.search).get("code");

      if (!code) {
        console.error("Code manquant dans l'URL");
        return;
      }

      try {
        const response = await fetch(`http://localhost:8080/api/callback?code=${code}`);
        const data = await response.json();

        if (data.access_token) {
          localStorage.setItem("access_token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token); // 🔐
          router.push("/");
        } else {
          console.error("Erreur de callback :", data);
        }
      } catch (error) {
        console.error("Erreur lors de l'appel à l'API callback", error);
      }
    };

    handleCallback();
  }, [router]);

  const refreshAccessToken = async () => {
    const refreshToken = localStorage.getItem("refresh_token");
    if (!refreshToken) return;
  
    const res = await fetch("http://localhost:8080/api/refresh-token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ refresh_token: refreshToken })
    });
  
    const data = await res.json();
    if (data.access_token) {
      localStorage.setItem("access_token", data.access_token);
      return data.access_token;
    } else {
      console.error("Erreur lors du refresh", data);
    }
  };
  

  return <p>Connexion en cours...</p>;
}
