// TechDocs — Main JavaScript
document.addEventListener('DOMContentLoaded', () => {
  // Model filter functionality
  window.filterByModel = (model) => {
    const cards = document.querySelectorAll('.techdoc-card');
    cards.forEach(card => {
      const badges = card.querySelectorAll('.techdoc-badge');
      if (model === 'all') {
        card.style.display = '';
        return;
      }
      const matches = Array.from(badges).some(badge => badge.textContent.trim() === model);
      card.style.display = matches ? '' : 'none';
    });
  };

  // Smooth scroll for TOC links
  document.querySelectorAll('.techdoc-toc a').forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });
});
