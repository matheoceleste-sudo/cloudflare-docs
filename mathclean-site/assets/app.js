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


/* ===== Barre d'action flottante : Appeler + Devis (toutes pages sauf réservation/merci) =====
   Le téléphone n'apparaissait qu'une seule fois, tout en bas de la page : sur mobile il fallait
   faire défiler dix-sept écrans avant de pouvoir appeler. Il est désormais toujours à portée.
   Les guides sont au même niveau que services/ et zones/ : sans le préfixe, le bouton pointait
   vers /guides/reservation.html, qui n'existe pas. */
(function(){
  var path=location.pathname;
  if(/reservation\.html$|merci\.html$/.test(path)) return;
  var pre=/\/(services|zones|guides)\//.test(path)?'../':'';

  var st=document.createElement('style');
  st.textContent=
  '.cta-dock{position:fixed;z-index:96;right:22px;bottom:22px;display:flex;gap:10px;align-items:center}'+
  '.cta-dock a{display:flex;align-items:center;gap:9px;padding:14px 22px;border-radius:99px;'+
  'text-decoration:none;font-weight:700;font-size:.95rem;letter-spacing:.2px;white-space:nowrap;'+
  'box-shadow:0 10px 32px rgba(0,0,0,.45);transition:transform .3s ease,box-shadow .3s ease}'+
  '.cta-dock a:hover{transform:translateY(-3px);box-shadow:0 16px 40px rgba(0,0,0,.55)}'+
  '.cta-dock svg{flex:0 0 18px}'+
  '.cta-dock .d-call{background:linear-gradient(135deg,#c9a24b,#9c7a2e);color:#151004;'+
  'box-shadow:0 10px 32px rgba(0,0,0,.45),0 0 0 1px rgba(231,205,134,.35)}'+
  '.cta-dock .d-quote{background:rgba(18,16,12,.92);color:#f6f3ec;border:1px solid rgba(231,205,134,.45);'+
  '-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}'+
  '@media (max-width:700px){'+
  '.cta-dock{left:12px;right:12px;bottom:12px;gap:9px}'+
  '.cta-dock a{flex:1 1 0;justify-content:center;padding:15px 10px;font-size:1rem}'+
  'body{padding-bottom:88px}'+
  '}';
  document.head.appendChild(st);

  var d=document.createElement('div');
  d.className='cta-dock';
  d.innerHTML=
   '<a class="d-call" href="tel:+33623075259" aria-label="Appeler MathClean au 06 23 07 52 59">'+
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'+
   '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.4-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'+
   '</svg><span>Appeler</span></a>'+
   '<a class="d-quote" href="'+pre+'reservation.html" aria-label="Demander un devis gratuit">'+
   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'+
   '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'+
   '</svg><span>Devis gratuit</span></a>';
  document.body.appendChild(d);

  /* Le bandeau cookies occupe le bas de l'écran au premier passage : on remonte la barre. */
  function place(){
    var bk=document.querySelector('.ck-banner.on');
    var h=bk?Math.round(bk.getBoundingClientRect().height):0;
    d.style.bottom = h ? (h+20)+'px' : '';
  }
  place();
  window.addEventListener('resize',place);
  if(window.MutationObserver){
    new MutationObserver(place).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['class']});
  }
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

/* ===== Fonds d'image différés (cartes prestations) =====
   Les visuels ne sont chargés qu'à l'approche du viewport : la page d'accueil
   ne demande plus 8 images avant même d'être affichée. */
(function(){
  var els = document.querySelectorAll('[data-bg]');
  if (!els.length) return;
  function load(el){
    if (el.dataset.bg){
      el.style.backgroundImage = "url('" + el.dataset.bg + "')";
      el.removeAttribute('data-bg');
    }
  }
  if (!('IntersectionObserver' in window)){
    Array.prototype.forEach.call(els, load);
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){ load(e.target); io.unobserve(e.target); }
    });
  }, { rootMargin: '400px 0px' });
  Array.prototype.forEach.call(els, function(el){ io.observe(el); });
})();

/* ===== Vidéos à la demande =====
   Aucune vidéo n'est téléchargée au chargement : la source n'est posée
   qu'au moment où la vidéo entre dans l'écran, puis la lecture démarre. */
(function(){
  var vids = document.querySelectorAll('video source[data-src]');
  if (!vids.length) return;
  function start(video){
    if (video.dataset.poster){ video.poster = video.dataset.poster; video.removeAttribute('data-poster'); }
    var src = video.querySelector('source[data-src]');
    if (src){
      src.src = src.dataset.src;
      src.removeAttribute('data-src');
      video.load();
    }
    var p = video.play();
    if (p && p.catch) p.catch(function(){});
  }
  var list = [];
  Array.prototype.forEach.call(vids, function(s){ list.push(s.parentNode); });
  if (!('IntersectionObserver' in window)){ list.forEach(start); return; }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){ start(e.target); io.unobserve(e.target); }
    });
  }, { rootMargin: '200px 0px' });
  list.forEach(function(v){ io.observe(v); });
})();
