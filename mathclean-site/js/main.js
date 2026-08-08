// Menu mobile : ouverture / fermeture de la navigation
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var ouvert = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', ouvert ? 'true' : 'false');
    });
  }

  // Année courante dans le pied de page
  var annee = document.getElementById('annee');
  if (annee) {
    annee.textContent = new Date().getFullYear();
  }
});
