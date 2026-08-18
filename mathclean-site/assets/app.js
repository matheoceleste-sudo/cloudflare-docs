/* ===== Header au scroll ===== */
const navEl=document.querySelector('header.nav');
if(navEl) addEventListener('scroll',()=>navEl.classList.toggle('scrolled',scrollY>40));

/* ===== Menu mobile ===== */
const burger=document.querySelector('.burger');
const menu=document.querySelector('nav.menu');
if(burger){
  burger.addEventListener('click',()=>{burger.classList.toggle('x');menu.classList.toggle('open')});
  // Les vrais liens ferment le menu — sauf le bouton « Services » qui ne fait que dérouler le sous-menu
  menu.querySelectorAll('a:not(.sub-toggle)').forEach(a=>a.addEventListener('click',()=>{burger.classList.remove('x');menu.classList.remove('open')}));
}

/* ===== Carrousel hero (10 s) ===== */
const slides=document.querySelectorAll('.slide');
const dots=document.querySelectorAll('.slide-dots i');
if(slides.length){
  let i=0,timer;
  const go=n=>{
    slides[i].classList.remove('active');dots[i]&&dots[i].classList.remove('on');
    i=(n+slides.length)%slides.length;
    slides[i].classList.add('active');dots[i]&&dots[i].classList.add('on');
  };
  const start=()=>timer=setInterval(()=>go(i+1),10000);
  dots.forEach((d,n)=>d.addEventListener('click',()=>{clearInterval(timer);go(n);start()}));
  start();
}

/* ===== Reveal au scroll ===== */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.16});
document.querySelectorAll('.reveal, .reveal-l, .reveal-r').forEach(el=>io.observe(el));

/* ===== Halo sur les cartes ===== */
document.querySelectorAll('.card').forEach(c=>{
  c.addEventListener('mousemove',e=>{
    const r=c.getBoundingClientRect();
    c.style.setProperty('--mx',(e.clientX-r.left)+'px');
    c.style.setProperty('--my',(e.clientY-r.top)+'px');
  });
});

/* ===== FAQ accordéon ===== */
document.querySelectorAll('.q button').forEach(b=>{
  b.addEventListener('click',()=>{
    const q=b.parentElement;
    document.querySelectorAll('.q.open').forEach(o=>{if(o!==q)o.classList.remove('open')});
    q.classList.toggle('open');
  });
});

/* ===== Année footer ===== */
const y=document.getElementById('y');if(y)y.textContent=new Date().getFullYear();


/* ===== Page de remerciement après envoi (devis & réservation) ===== */
document.querySelectorAll('form[action*="formsubmit.co"]').forEach(f=>{
  let n=f.querySelector('input[name="_next"]');
  if(!n){n=document.createElement('input');n.type='hidden';n.name='_next';f.appendChild(n);}
  n.value=new URL('merci.html',location.href).href;
});


/* ===== Bulle flottante Réserver (toutes pages sauf réservation/merci) ===== */
(function(){
  var path=location.pathname;
  if(/reservation\.html$|merci\.html$/.test(path)) return;
  var pre=/\/(services|zones)\//.test(path)?'../':'';
  var b=document.createElement('a');
  b.href=pre+'reservation.html';
  b.className='resa-bubble';
  b.setAttribute('aria-label','Réserver une prestation');
  b.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg><span>Réserver</span>';
  document.body.appendChild(b);
})();


/* ===== Envoi AJAX + redirection garantie vers la page de remerciement ===== */
document.querySelectorAll('form[action*="formsubmit.co"]').forEach(f=>{
  f.addEventListener('submit',function(e){
    e.preventDefault();
    if(!f.reportValidity()) return;
    var btn=f.querySelector('[type="submit"]');
    if(btn){btn.disabled=true;btn.textContent='Envoi en cours…';}
    var merci=new URL('merci.html',location.href).href;
    var url=f.action.replace('formsubmit.co/','formsubmit.co/ajax/');
    fetch(url,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})
      .then(function(){location.href=merci;})
      .catch(function(){ f.submit(); });   /* repli : envoi classique (redirigé via _next) */
  });
});

/* ===== Menu déroulant Services (clic + fermeture au clic extérieur) ===== */
document.querySelectorAll('.sub-toggle').forEach(function(t){
  t.addEventListener('click',function(e){
    e.preventDefault();
    var wrap=t.closest('.has-sub');
    var wasOpen=wrap.classList.contains('open');
    document.querySelectorAll('.has-sub.open').forEach(function(w){w.classList.remove('open')});
    if(!wasOpen) wrap.classList.add('open');
  });
});
document.addEventListener('click',function(e){
  if(!e.target.closest('.has-sub')) document.querySelectorAll('.has-sub.open').forEach(function(w){w.classList.remove('open')});
});

/* ===== Prochaines disponibilités (dates dynamiques) ===== */
(function(){
  var rows=document.querySelectorAll('.hero-dispo .hd-day');
  if(!rows.length) return;
  var J=['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi'];
  var M=['jan.','fév.','mars','avr.','mai','juin','juil.','août','sep.','oct.','nov.','déc.'];
  rows.forEach(function(el){
    var off=+el.getAttribute('data-off')||1;
    var d=new Date(); d.setDate(d.getDate()+off);
    el.textContent=(off===1?'Demain':J[d.getDay()]+' '+d.getDate()+' '+M[d.getMonth()]);
  });
})();

/* ===== Avis Google =====
   ↓ Une fois votre fiche Google Business créée, collez son identifiant (Place ID)
   entre les guillemets ci-dessous. Le bouton ouvrira alors directement la fenêtre d'avis.
   Comment l'obtenir : https://developers.google.com/maps/documentation/places/web-service/place-id */
const GOOGLE_PLACE_ID = ""; // ex : "ChIJN1t_tDeuEmsRUsoyG83frY4"
(function(){
  const links=document.querySelectorAll('.js-google-review');
  if(!links.length)return;
  const url=GOOGLE_PLACE_ID
    ? "https://search.google.com/local/writereview?placeid="+GOOGLE_PLACE_ID
    : "https://www.google.com/maps/search/?api=1&query=MathClean+nettoyage+Paris";
  links.forEach(a=>{a.href=url;});
})();

/* ===== Consentement cookies (Google Analytics chargé seulement après accord) ===== */
(function(){
  var KEY='mcConsent';
  var val=null; try{ val=localStorage.getItem(KEY); }catch(e){}
  if(val==='yes'||val==='no') return;              /* choix déjà fait */
  var pre=/\/(services|zones)\//.test(location.pathname)?'../':'';
  var b=document.createElement('div');
  b.className='ck-banner';
  b.setAttribute('role','dialog');
  b.setAttribute('aria-label','Consentement aux cookies');
  b.innerHTML='<p><b>Nous utilisons des cookies de mesure d’audience</b> pour comprendre comment '+
    'notre site est consulté et l’améliorer. Aucun cookie n’est déposé sans votre accord. '+
    'En savoir plus dans notre <a href="'+pre+'politique-cookies.html">politique de cookies</a>.</p>'+
    '<div class="ck-btns"><button type="button" class="ck-ok">Accepter</button>'+
    '<button type="button" class="ck-no">Refuser</button></div>';
  document.body.appendChild(b);
  setTimeout(function(){ b.classList.add('on'); }, 700);
  function choose(v){
    try{ localStorage.setItem(KEY,v); }catch(e){}
    if(v==='yes' && typeof gtag==='function'){
      gtag('consent','update',{ad_storage:'granted',analytics_storage:'granted',
        ad_user_data:'granted',ad_personalization:'granted'});
    }
    b.classList.remove('on');
    setTimeout(function(){ b.remove(); }, 600);
  }
  b.querySelector('.ck-ok').addEventListener('click',function(){ choose('yes'); });
  b.querySelector('.ck-no').addEventListener('click',function(){ choose('no'); });
})();
