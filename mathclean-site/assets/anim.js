/* ===== Génère bulles/gouttes/étincelles dans une scène ===== */
function spawn(stage, type, n){
  const layer=stage.querySelector('.fx');
  if(!layer) return;
  for(let i=0;i<n;i++){
    const e=document.createElementNS('http://www.w3.org/2000/svg','circle');
    const x=10+Math.random()*80, r= type==='bubble'? 1.5+Math.random()*3.5 : 1+Math.random()*2.2;
    e.setAttribute('cx',x); e.setAttribute('cy', type==='droplet'?20:80);
    e.setAttribute('r',r);
    e.setAttribute('class', type==='bubble'?'a-bubble':type==='droplet'?'a-droplet':type==='steam'?'a-steam':'a-spark');
    e.setAttribute('fill', type==='spark'?'#e7cd86': 'none');
    if(type!=='spark'){e.setAttribute('stroke','#e7cd86');e.setAttribute('stroke-width','.6');e.setAttribute('stroke-opacity','.7')}
    const dur=(type==='spark'?1.2:3)+Math.random()*2.5;
    e.style.animationDuration=dur+'s';
    e.style.animationDelay=(Math.random()*dur)+'s';
    layer.appendChild(e);
  }
}

/* ===== Déclenche les scènes au scroll ===== */
const animIO=new IntersectionObserver(es=>es.forEach(e=>{
  if(e.isIntersecting){
    e.target.classList.add('play');
    const t=e.target.dataset.fx;
    if(t==='bubble') spawn(e.target,'bubble',16);
    if(t==='droplet') spawn(e.target,'droplet',14);
    if(t==='steam'){spawn(e.target,'steam',10);spawn(e.target,'bubble',8)}
    if(t==='spark') spawn(e.target,'spark',14);
    if(t==='mix'){spawn(e.target,'bubble',10);spawn(e.target,'spark',8)}
  }
}),{threshold:.35});
document.querySelectorAll('.anim-stage').forEach(s=>animIO.observe(s));
