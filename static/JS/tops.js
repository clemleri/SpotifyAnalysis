new Glide('#glideTopTracks', {
    type: 'carousel',
    perView: 6,
    gap: 12,
    breakpoints: {
      1024: { perView: 4 },
      768: { perView: 3 },
      480: { perView: 2 }
    }
  }).mount()

  new Glide('#glideTopArtists', {
    type: 'carousel',
    perView: 6,
    gap: 12,
    breakpoints: {
      1024: { perView: 4 },
      768: { perView: 3 },
      480: { perView: 2 }
    }
  }).mount()

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