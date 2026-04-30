// TechDocs Password Gate
// Provides client-side password protection for GitHub Pages deployments
// Note: This is not cryptographically secure - for sensitive content, use server-side auth

(function() {
  'use strict';

  // Check if already authenticated in this session
  if (sessionStorage.getItem(TECHDOCS_CONFIG.sessionKey) === 'true') {
    unlockSite();
    return;
  }

  // Initialize the password form
  const form = document.getElementById('techdocs-gate-form');
  const input = document.getElementById('techdocs-gate-input');
  const error = document.getElementById('techdocs-gate-error');
  const gate = document.getElementById('techdocs-gate');

  if (form && input) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const password = input.value;

      if (password === TECHDOCS_CONFIG.passwordHash) {
        sessionStorage.setItem(TECHDOCS_CONFIG.sessionKey, 'true');
        unlockSite();
      } else {
        error.style.display = 'block';
        input.style.borderColor = '#DC2626';
        input.value = '';
        input.focus();

        setTimeout(() => {
          error.style.display = 'none';
          input.style.borderColor = '';
        }, 3000);
      }
    });

    // Focus input on load
    setTimeout(() => input.focus(), 100);
  }

  function unlockSite() {
    const gateEl = document.getElementById('techdocs-gate');
    const mainContent = document.getElementById('mainContent');
    const mainFooter = document.getElementById('mainFooter');

    if (gateEl) {
      gateEl.style.transition = 'opacity 0.3s ease';
      gateEl.style.opacity = '0';
      setTimeout(() => {
        gateEl.style.display = 'none';
        if (mainContent) mainContent.style.display = '';
        if (mainFooter) mainFooter.style.display = '';
      }, 300);
    }
  }
})();
