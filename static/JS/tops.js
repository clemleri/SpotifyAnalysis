document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('[data-section]');
  const sections = document.querySelectorAll('.section-content');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-section');

      // Masquer toutes les sections
      sections.forEach(section => {
        section.classList.add('hidden');
      });

      // Afficher la section cible
      document.querySelector(`#section-${target}`).classList.remove('hidden');

      // Gérer l'état actif du bouton
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  const SidebartoggleBtn = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');

  SidebartoggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
    document.body.classList.toggle('overflow-hidden');
  });

  overlay.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
  });
});
 
 const dropdownBtn = document.getElementById('dropdownButton');
  const dropdownMenu = document.getElementById('dropdownMenu');

  dropdownBtn.addEventListener('click', () => {
    dropdownMenu.classList.toggle('hidden');
  });

  window.addEventListener('click', (e) => {
    if (!dropdownBtn.contains(e.target) && !dropdownMenu.contains(e.target)) {
      dropdownMenu.classList.add('hidden');
    }
  });

  const elements = document.querySelectorAll('.scroll-animate');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('opacity-100', 'translate-y-0');
      }
    });
  }, { threshold: 0.1 });

  elements.forEach(el => observer.observe(el));

 