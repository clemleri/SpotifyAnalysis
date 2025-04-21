document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('[data-section]');
  const sections = document.querySelectorAll('.section-content');
  const SidebartoggleBtn = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');
  

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-section');
      sidebar.classList.add('-translate-x-full');
      overlay.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
      SidebartoggleBtn.classList.toggle("hidden")
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

  SidebartoggleBtn.addEventListener('click', () => {
    SidebartoggleBtn.classList.toggle("hidden")
    sidebar.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
    document.body.classList.toggle('overflow-hidden');
  });

  overlay.addEventListener('click', () => {
    SidebartoggleBtn.classList.toggle("hidden")
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
  });

  // Init Glide sliders
  const glideTrack = new Glide('#glideTopTracks', {
    type: 'carousel',
    perView: 6,
    breakpoints: {
      1024: { perView: 4 },
      768: { perView: 3 },
      480: { perView: 2 },
    }
  });

  const glideArtist = new Glide('#glideTopArtists', {
    type: 'carousel',
    perView: 6,
    breakpoints: {
      1024: { perView: 4 },
      768: { perView: 3 },
      480: { perView: 2 },
    }
  });

  glideTrack.mount();
  glideArtist.mount();
  var allReadyMountTrack = false
  var allReadyMountArtist = false

  // Toggle tracks view
  const btnTracks = document.getElementById('view-toggle-tracks');
  const glideTracks = document.getElementById('glideTopTracks');
  const gridTracks = document.getElementById('gridTopTracks');
  const btnTracksScroll = document.getElementById('view-toggle-tracks-scroll');
  const btnTracksBox = document.getElementById('view-toggle-tracks-box');
  const btnArtistsScroll = document.getElementById('view-toggle-artists-scroll');
  const btnArtistsBox = document.getElementById('view-toggle-artists-box');

  btnTracks.addEventListener('click', () => {
    glideTracks.classList.toggle('hidden');
    gridTracks.classList.toggle('hidden');
    
    // Afficher ou masquer les bons boutons
    btnTracksScroll.classList.toggle('hidden');
    btnTracksBox.classList.toggle('hidden');
    
    if (!allReadyMountTrack){
      glideTrack.mount();
      allReadyMountTrack = true
    }
    
    glideTrack.go('=12');
  });

  // Toggle artists view
  const btnArtists = document.getElementById('view-toggle-artists');
  const glideArtists = document.getElementById('glideTopArtists');
  const gridArtists = document.getElementById('gridTopArtists');

  btnArtists.addEventListener('click', () => {
    glideArtists.classList.toggle('hidden');
    gridArtists.classList.toggle('hidden');

    // Afficher ou masquer les bons boutons
    btnArtistsScroll.classList.toggle('hidden');
    btnArtistsBox.classList.toggle('hidden');

    if (!allReadyMountArtist){
      glideArtist.mount();
      allReadyMountArtist = true
    }

    glideArtist.go('=10');
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

  const dropdownBtn = document.getElementById('dropdownButton');
  const dropdownMenu = document.getElementById('dropdownMenu');

  dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation(); // évite de fermer direct après ouverture
    dropdownMenu.classList.toggle('hidden');
  });

  // Ferme le menu si on clique ailleurs
  document.addEventListener('click', (e) => {
    if (!dropdownMenu.classList.contains('hidden')) {
      dropdownMenu.classList.add('hidden');
    }
  });

  // Empêche la fermeture quand on clique sur un lien dans le menu
  dropdownMenu.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  const dropdownBtnArtist = document.getElementById('dropdownButtonArtist');
  const dropdownMenuArtist = document.getElementById('dropdownMenuArtist');

  dropdownBtnArtist.addEventListener('click', (e) => {
    e.stopPropagation(); // évite de fermer direct après ouverture
    dropdownMenuArtist.classList.toggle('hidden');
  });

  // Ferme le menu si on clique ailleurs
  document.addEventListener('click', (e) => {
    if (!dropdownMenuArtist.classList.contains('hidden')) {
      dropdownMenuArtist.classList.add('hidden');
    }
  });

  // Empêche la fermeture quand on clique sur un lien dans le menu
  dropdownMenuArtist.addEventListener('click', (e) => {
    e.stopPropagation();
  });
});
 



 