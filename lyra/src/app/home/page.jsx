// pages/homepage.jsx
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Testimonials from "../components/Testimonials";
import Pricing from "../components/Pricing";
import Footer from "../components/Footer";

export default function Homepage() {
  return (
    <main className="bg-white dark:bg-[#0f0f0f] text-black dark:text-white min-h-screen">
      <Navbar />
      <Hero />
      <Features />
      <Testimonials />
      <Pricing />
      <Footer />
    </main>
  );
}
