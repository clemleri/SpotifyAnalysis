// components/LayoutWithSidebar.jsx
import Sidebar from "./Sidebar";
import Footer from "./Footer";

export default function LayoutWithSidebar({ children }) {
  return (
    <div className="relative min-h-screen text-black dark:text-white">
      {/* Sidebar positionnée en absolute/fixed */}
      <Sidebar />

      {/* Contenu principal avec padding à gauche quand sidebar visible sur desktop */}
      <div className="sm:pl-64 transition-all duration-300">
        <div className="flex flex-col min-h-screen">
          <div className="flex-grow">{children}</div>
          <Footer extend={false} />
        </div>
      </div>
    </div>
  );
}
