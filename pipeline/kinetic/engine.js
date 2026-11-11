const R=/*REEL*/{};
const cl=x=>Math.max(0,Math.min(1,x));
const E={out:t=>1-Math.pow(1-t,3),io:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,lin:t=>t,back:t=>{const c1=1.7,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2)}};
const pr=(t,a,b,e=E.out)=>e(cl((t-a)/(b-a)));
const $=id=>document.getElementById(id);
const beats=R.beats,T=R.total;
let st=0;beats.forEach(b=>{b.t=st;st+=b.d});
const stage=$('stage');
function words(line){const out=[];const re=/\*([^*]+)\*([^\s*]*)|(\S+)/g;let m;while((m=re.exec(line))){if(m[1])out.push({w:m[1]+m[2],hl:1});else out.push({w:m[3],hl:0})}return out}
beats.forEach((b,i)=>{
  const sc=document.createElement('div');sc.className='sc th-'+b.bg;sc.id='sc'+i;
  let h='<div class="in">';
  if(b.kicker)h+=`<div class="kick" id="k${i}">${b.kicker}</div>`;
  h+=`<div class="hl-wrap" style="font-size:${b.fs||100}px">`;
  b.W=[];
  (b.lines||[]).forEach((ln,li)=>{h+='<div class="ln">';words(ln).forEach(o=>{const id=`w${i}_${b.W.length}`;b.W.push(id);h+=`<span class="w${o.hl?' hl':''}" id="${id}">${o.w}</span> `});h+='</div>'});
  h+='</div>';
  if(b.sub)h+=`<div class="subt" id="s${i}">${b.sub}</div>`;
  const v=b.visual;
  if(v){h+=`<div class="vis v-${v.type}" id="v${i}">`;
    if(v.type=='checklist')v.items.forEach((x,n)=>{h+=`<div class="ci" id="v${i}_${n}"><span class="bx"><i>✓</i></span><span class="tx">${x[0]}</span>${x[1]?`<span class="tg">${x[1]}</span>`:''}</div>`});
    if(v.type=='chat')v.msgs.forEach((x,n)=>{h+=`<div class="bub ${x.f}" id="v${i}_${n}">${x.t}${x.m?`<small>${x.m}</small>`:''}</div>`});
    if(v.type=='flow')v.nodes.forEach((x,n)=>{h+=`<div class="nd" id="v${i}_${n}">${x}</div>${n<v.nodes.length-1?`<div class="cn" id="v${i}_c${n}"></div>`:''}`});
    if(v.type=='versus'){h+=`<div class="col a"><div class="ct">${v.a[0]}</div>`;v.a.slice(1).forEach((x,n)=>{h+=`<div class="vr" id="v${i}_a${n}">${x}</div>`});h+=`</div><div class="col b"><div class="ct">${v.b[0]}</div>`;v.b.slice(1).forEach((x,n)=>{h+=`<div class="vr" id="v${i}_b${n}">${x}</div>`});h+='</div>'}
    if(v.type=='pills')v.items.forEach((x,n)=>{h+=`<div class="pl" id="v${i}_${n}">✓ ${x}</div>`});
    if(v.type=='tag')h+=`<div class="tagv" id="v${i}_0">${v.text}</div>`;
    h+='</div>'}
  h+='</div>';sc.innerHTML=h;stage.appendChild(sc)});
const rise=(id,t,t0,d=.4,dy=26)=>{const e=$(id);if(!e)return 0;const k=pr(t,t0,t0+d,E.out);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*dy}px)`;return k};
function draw(t){
  $('prog').style.width=(720*cl(t/T))+'px';
  let cur=0;beats.forEach((b,i)=>{if(t>=b.t)cur=i});
  {const FG={ink:'#fff',lime:'#0b0b0b',paper:'#111',blue:'#fff',red:'#fff'},PG={ink:'#c6ff35',lime:'#0b0b0b',paper:'#ff4d2e',blue:'#c6ff35',red:'#0b0b0b'};const th=beats[cur].bg;$('top').style.color=FG[th];$('prog').style.background=PG[th]}
  beats.forEach((b,i)=>{
    const sc=$('sc'+i);
    const trans=(i>0&&t>=b.t&&t<b.t+.32);
    const show=(i==cur)||(trans&&i==cur)||(i==cur-1&&cur>0&&t<beats[cur].t+.32);
    sc.style.display=(i==cur||(i==cur-1&&t<beats[cur].t+.32))?'block':'none';
    sc.style.zIndex=i;
    if(i==cur){const k=i==0?1:pr(t,b.t,b.t+.32,E.io);sc.style.clipPath=`inset(${(1-k)*100}% 0 0 0)`;}
    else sc.style.clipPath='none';
    if(sc.style.display=='none')return;
    const lt=Math.max(0,t-b.t);
    const inn=sc.querySelector('.in');inn.style.transform=`scale(${1+.025*cl(lt/b.d)})`;
    if(b.kicker)rise('k'+i,lt,i==0?-.5:0.05,.4,14);
    b.W.forEach((id,j)=>{const off=i==0?-.9:0;const k=pr(lt,.12+off+j*.11,.12+off+j*.11+.42,E.back);const e=$(id);e.style.opacity=cl(k*1.4);e.style.transform=`translateY(${(1-k)*46}px) scale(${.88+.12*k})`});
    const t0=.12+b.W.length*.11+.25;
    if(b.sub)rise('s'+i,lt,b.subAt!=null?b.subAt:t0,.5,18);
    const v=b.visual;if(v){const vs=v.at!=null?v.at:t0+.2,sp=v.step||.6;
      if(v.type=='checklist')v.items.forEach((x,n)=>{const a=vs+n*sp;rise(`v${i}_${n}`,lt,a,.4,20);const kk=pr(lt,a+.35,a+.6,E.back);const bx=$(`v${i}_${n}`).querySelector('.bx');bx.classList.toggle('on',kk>.2);bx.querySelector('i').style.transform=`scale(${kk})`});
      if(v.type=='chat')v.msgs.forEach((x,n)=>{rise(`v${i}_${n}`,lt,vs+n*sp,.35,18)});
      if(v.type=='flow')v.nodes.forEach((x,n)=>{rise(`v${i}_${n}`,lt,vs+n*sp,.4,22);if(n<v.nodes.length-1){const c=$(`v${i}_c${n}`);const k=pr(lt,vs+n*sp+.25,vs+n*sp+.55,E.out);c.style.transform=`scaleY(${k})`}});
      if(v.type=='versus'){v.a.slice(1).forEach((x,n)=>rise(`v${i}_a${n}`,lt,vs+n*sp,.4,16));v.b.slice(1).forEach((x,n)=>rise(`v${i}_b${n}`,lt,vs+(v.a.length-1)*sp+.3+n*sp,.4,16))}
      if(v.type=='pills')v.items.forEach((x,n)=>{const k=pr(lt,vs+n*sp,vs+n*sp+.45,E.back);const e=$(`v${i}_${n}`);e.style.opacity=cl(k*1.5);e.style.transform=`scale(${.8+.2*k})`});
      if(v.type=='tag')rise(`v${i}_0`,lt,vs,.4,10)}
  });
}
