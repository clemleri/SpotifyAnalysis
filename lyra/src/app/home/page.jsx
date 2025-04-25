// pages/homepage.jsx
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Testimonials from "../components/Testimonials";
import Pricing from "../components/Pricing";
import Footer from "../components/Footer";
import FadeInWhenVisible from "../components/FadeInWhenVisible";
import BottomNav from "../components/BottomNav";

export default function Homepage() {
  return (
    <main className="text-black dark:text-white min-h-screen space-y-24">
      <Navbar />
      <BottomNav />

      <FadeInWhenVisible><Hero /></FadeInWhenVisible>

      <FadeInWhenVisible delay={0.2}><Features /></FadeInWhenVisible>

      <FadeInWhenVisible delay={0.4}><Testimonials /></FadeInWhenVisible>

      <FadeInWhenVisible delay={0.6}><Pricing /></FadeInWhenVisible>

      <Footer extend={true} />
    </main>
  );
}