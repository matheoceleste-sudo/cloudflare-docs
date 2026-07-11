/* ===== Header au scroll ===== */
const navEl=document.querySelector('header.nav');
addEventListener('scroll',()=>navEl.classList.toggle('scrolled',scrollY>40));

/* ===== Menu mobile ===== */
const burger=document.querySelector('.burger');
const menu=document.querySelector('nav.menu');
if(burger){
  burger.addEventListener('click',()=>{burger.classList.toggle('x');menu.classList.toggle('open')});
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{burger.classList.remove('x');menu.classList.remove('open')}));
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
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

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
