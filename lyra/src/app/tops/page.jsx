// pages/homepage.jsx
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Testimonials from "../components/Testimonials";
import Pricing from "../components/Pricing";
import Footer from "../components/Footer";
import Sidebar from "../components/Sidebar";
import LayoutWithSidebar from "../components/LayoutWithSidebar";

export default function Tops() {
  return (
    <main className="text-black dark:text-white min-h-screen">
      <Navbar />
      <LayoutWithSidebar></LayoutWithSidebar>

    </main>
  );
}
