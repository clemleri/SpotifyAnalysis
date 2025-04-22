const toggleBtn = document.getElementById('theme-toggle');
const mobileMenu = document.getElementById('mobile-menu');
const toggleBtnMenu = document.getElementById('mobile-menu-toggle');
const html = document.documentElement;
const burgerIcon = document.getElementById('burger-icon');
const closeIcon = document.getElementById('close-icon');
const SidebartoggleBtn = document.getElementById('menu-toggle');

toggleBtnMenu.addEventListener('click', () => {
  const isOpen = !mobileMenu.classList.contains('hidden');

  if (isOpen) {
    // Fermer le menu
    SidebartoggleBtn.classList.toggle("hidden")

    mobileMenu.classList.add('opacity-0', '-translate-y-4');
    mobileMenu.classList.remove('opacity-100', 'translate-y-0');
    setTimeout(() => {
      mobileMenu.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    }, 300);
    // Switch icons
    burgerIcon.classList.remove('opacity-0', 'scale-90');
    burgerIcon.classList.add('opacity-100', 'scale-100');
    closeIcon.classList.remove('opacity-100', 'scale-100');
    closeIcon.classList.add('opacity-0', 'scale-90');
  } else {
    // Ouvrir le menu
    mobileMenu.classList.remove('hidden');
    setTimeout(() => {
      mobileMenu.classList.remove('opacity-0', '-translate-y-4');
      mobileMenu.classList.add('opacity-100', 'translate-y-0');
    }, 10);
    document.body.classList.add('overflow-hidden');
    // Switch icons
    burgerIcon.classList.remove('opacity-100', 'scale-100');
    burgerIcon.classList.add('opacity-0', 'scale-90');
    closeIcon.classList.remove('opacity-0', 'scale-90');
    closeIcon.classList.add('opacity-100', 'scale-100');
    SidebartoggleBtn.classList.toggle("hidden")
  }
});

  // Init (au chargement de la page)
  if (localStorage.getItem('theme') === 'light') {
    html.classList.add('light');
    html.classList.remove('dark');
  } else {
    html.classList.add('dark');
    html.classList.remove('light');
  }

  toggleBtn.addEventListener('click', () => {
    if (html.classList.contains('dark')) {
      html.classList.remove('dark');
      html.classList.add('light');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      html.classList.remove('light');
      localStorage.setItem('theme', 'dark');
    }
  });

  document.getElementById('theme-toggle-mobile')?.addEventListener('click', () => {
    if (html.classList.contains('dark')) {
      html.classList.remove('dark');
      html.classList.add('light');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      html.classList.remove('light');
      localStorage.setItem('theme', 'dark');
    }
  });

