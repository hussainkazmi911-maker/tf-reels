const C=/*CFG*/{};
const S=C.starts,T=C.total;
const cl=x=>Math.max(0,Math.min(1,x));
const E={out:t=>1-Math.pow(1-t,3),io:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,lin:t=>t};
const pr=(t,a,b,e=E.out)=>e(cl((t-a)/(b-a)));
const $=id=>document.getElementById(id);
const lerp=(a,b,k)=>a+(b-a)*k;
const s=i=>S[i];
const WORDS=C.lines.map(l=>{let tot=l.length,c=0;return l.split(' ').map(x=>{const o={w:x,f:c/tot};c+=x.length+1;return o})});
const VS=S.map(x=>x+C.voff);
const wordTime=(li,wi)=>VS[li]+C.durs[li]*WORDS[li][wi].f;
function kf(arr,t){if(t<=arr[0][0])return arr[0].slice(1);for(let i=0;i<arr.length-1;i++){const a=arr[i],b=arr[i+1];if(t<=b[0]){const k=E.io(cl((t-a[0])/Math.max(1e-6,b[0]-a[0])));return [1,2,3,4].map(j=>lerp(a[j],b[j],k))}}return arr[arr.length-1].slice(1)}
function place(el,v){el.style.transform=`translate(${v[0]}px,${v[1]}px) scale(${v[2]})`;el.style.opacity=v[3]}
function pageOp(list,t){let o=0;for(const [a,b] of list){const f=.22;o=Math.max(o,cl((t-a)/f)*cl((b-t)/f))}return o}
const tapPos=id=>{const r=$(id).getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]};
const rise=(id,t,t0,d=.45,dy=14)=>{const k=pr(t,t0,t0+d,E.out);const e=$(id);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*dy}px)`;return k};
/* init */
$('sT1').textContent='Forge Fix';$('sT2').textContent='of the Day';
$('l8a').textContent='Fewer calls';$('l8b').textContent='Happier customers';$('l8c').textContent='Smoother days';
$('series').insertAdjacentHTML('beforeend','<div id="sLine"></div>');
const st='fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"';
const house=`<svg width="28" height="28" viewBox="0 0 24 24" ${st}><path d="M4 16v-4l2-5h12l2 5v4z"/><path d="M4 12h16"/><circle cx="8" cy="17" r="1.6"/><circle cx="16" cy="17" r="1.6"/></svg>`;
const moon=`<svg width="28" height="28" viewBox="0 0 24 24" ${st}><path d="M14.5 5.5a4 4 0 00-5 5L4 16l4 4 5.5-5.5a4 4 0 005-5l-3 3-2.5-.5-.5-2.5z"/></svg>`;
const xc=`<svg width="28" height="28" viewBox="0 0 24 24" ${st}><path d="M6 4l3 1 1 4-2 2a12 12 0 005 5l2-2 4 1 1 3c0 2-2 3-4 3C10 21 3 14 3 7c0-2 1-3 3-3z"/></svg>`;
const TOPS=[340,478,616];
const cards=[[house,'Sam R. · Brakes','Asking: is it ready?',true],[moon,'Dee K. · Detail','Voicemail left',false],[xc,'Next customer','Phone ringing again',false]];
$('chaos').innerHTML='<div id="wclock"></div><div class="kt" id="kA"></div><div class="kt" id="kB"></div>'
 +cards.map((c,i)=>`<div class="cc" id="k${i}" style="top:${TOPS[i]}px">${c[3]?`<div class="rg" id="rgk${i}"></div>`:''}<div class="ic">${c[0]}</div><div class="t1">${c[1]}</div><div class="t2" id="t2k${i}">${c[2]}</div><div class="st" id="stk${i}"></div></div>`).join('');
const AMB=['rgba(255,176,32,.15)','#ffb020'],RED=['rgba(255,122,122,.18)','#ff7a7a'];
const setChip=(id,txt,c)=>{const e=$(id);e.textContent=txt;e.style.background=c[0];e.style.color=c[1]};
const KA=[[-.8,s(1)-.2,'Garage owners:','#c6ff35',72],[wordTime(1,0)-.05,s(2)-.15,'Work stops.','#fff',70]];
const KB=[[-.8,wordTime(0,6)-.05,'Is my car ready?','#fff',64],[wordTime(0,6)-.05,s(1)-.2,'Fourth call.','#ffb020',66],[wordTime(1,6)-.05,s(2)-.15,'Afternoon gone.','#ff7a7a',64]];
function kin(id,list,t){const e=$(id);let a=null;for(const x of list)if(t>=x[0]&&t<x[1])a=x;
 if(!a){e.style.opacity=0;return}
 const k=pr(t,a[0],a[0]+.6,E.out);e.textContent=a[2];e.style.color=a[3];e.style.fontSize=a[4]+'px';
 e.style.opacity=k*(1-pr(t,a[1]-.25,a[1],E.lin));e.style.transform=`translateY(${(1-k)*34}px)`}
const phA=[[s(3),360,560,.84,0],[s(3)+.7,360,480,.88,1],[s(7),360,480,.88,1],[s(7)+.6,128,480,.58,1],[s(8),128,480,.58,1],[s(8)+.45,128,540,.55,0]];
const brd=[[s(7)+.35,900,480,.82,1],[s(7)+1.0,480,480,.82,1],[s(8),480,480,.82,1],[s(8)+.55,360,430,.85,1],[s(9)-.05,360,430,.85,1],[s(9)+.3,360,430,.85,0]];
const PG={pgInbox:[[s(3)+.3,s(4)+.35]],pgChat:[[s(4)+.1,s(5)+.35]],pgLead:[[s(5)+.1,s(6)+.35]],pgView:[[s(6)+.1,s(8)+.5]]};
const TAPS=[[s(4)-.05,'lr0']];
const kApp=[-.7,wordTime(0,6)-.1,wordTime(1,5)-.1];
const tClk=wordTime(1,0)-.05,tLate=wordTime(1,6),tLost=wordTime(1,9),tSign=wordTime(1,9);
const COLX=[0,173,346],ROWY=[40,134];
const tm1=wordTime(7,2)-.25,tm2=wordTime(7,5)-.1;
function draw(t){
 $('prog').style.width=(720*cl(t/T))+'px';
 let li=0;for(let i=0;i<S.length;i++)if(t>=S[i])li=i;
 const cap=$('cap');
 if(li<9&&t>=VS[li]-.05){const ws=WORDS[li];let cur=-1;for(let k=0;k<ws.length;k++)if(t>=VS[li]+C.durs[li]*ws[k].f)cur=k;
  cap.innerHTML='<div>'+ws.map((o,k)=>`<span class="${k<cur?'p':k==cur?'c':''}">${o.w}</span>`).join(' ')+'</div>';cap.style.display='flex'}
 else if(li<9)cap.innerHTML='';else cap.style.display='none';
 /* ===== problem ===== */
 const ch=$('chaos'),cO=1-pr(t,s(2)-.2,s(2)+.3,E.lin);ch.style.display=cO<=0?'none':'block';ch.style.opacity=cO;
 for(let i=0;i<3;i++){const c=$('k'+i),k=pr(t,kApp[i],kApp[i]+.55,E.out);
  c.style.opacity=k*(i==2&&t>=tSign?1:1);c.style.transform=`translateY(${(1-k)*24}px)`;const ic=c.querySelector('.ic');
  if(i==0){const lost=t>=tLost;setChip('stk0',lost?'MISSED':'CALLING',lost?RED:AMB);ic.style.background=lost?'rgba(255,122,122,.16)':'rgba(255,176,32,.2)';c.style.opacity=k*(lost?.7:1);
   const rg=$('rgk0'),q=((t*1.1)%1),on=t>=kApp[0]&&!lost;rg.style.opacity=on?(1-q)*.8:0;rg.style.transform=`scale(${1+q*.9})`}
  else if(i==1){const late=t>=tLate;setChip('stk1',late?'NO REPLY':'VOICEMAIL',late?RED:AMB);$('t2k1').textContent=late?'Still no call back':'Voicemail left';ic.style.background=late?'rgba(255,122,122,.16)':'rgba(255,176,32,.2)'}
  else{setChip('stk2','RINGING',RED);ic.style.background='rgba(255,122,122,.16)';c.style.borderColor='rgba(255,122,122,.5)'}}
 const wc=$('wclock');
 if(t<tClk){wc.textContent='MIDDAY   ·   PHONE RINGING';wc.style.color=t>=kApp[0]?'#ffb020':'#fff'}
 else{wc.textContent=t>=tSign?'CLOSING   ·   STILL RINGING':'AFTERNOON   ·   STILL RINGING';wc.style.color=t>=tSign?'#ff7a7a':'#ffb020'}
 kin('kA',KA,t);kin('kB',KB,t);
 /* ===== series ===== */
 const sO=pr(t,s(2)+.1,s(2)+.55,E.lin)*(1-pr(t,s(3)-.15,s(3)+.3,E.lin));
 const ser=$('series');ser.style.display=sO<=0?'none':'block';ser.style.opacity=sO;
 const lk=pr(t,s(2)+.2,s(2)+1.0,E.out);$('sLogo').style.transform=`scale(${.86+.14*lk})`;$('sLogo').style.opacity=lk;
 const k1=pr(t,s(2)+.5,s(2)+1.1,E.out),k2=pr(t,s(2)+.75,s(2)+1.35,E.out),kl=pr(t,s(2)+1.0,s(2)+1.7,E.io),k3=pr(t,s(2)+1.2,s(2)+1.8,E.out);
 $('sT1').style.opacity=k1;$('sT1').style.transform=`translateY(${(1-k1)*30}px)`;
 $('sT2').style.opacity=k2;$('sT2').style.transform=`translateY(${(1-k2)*30}px)`;
 $('sLine').style.width=(300*kl)+'px';$('sLine').style.opacity=kl;
 $('sT3').style.opacity=k3;$('sT3').style.transform=`translateX(-50%) translateY(${(1-k3)*20}px)`;
 $('tableChip').style.opacity=pr(t,s(2)+.6,s(2)+1.1,E.lin)*(1-pr(t,s(9),s(9)+.3,E.lin));
 /* ===== phone ===== */
 const pA=kf(phA,t);if(t<phA[0][0]||t>phA[phA.length-1][0])pA[3]=0;pA[1]+=Math.sin(t*1.6)*3;place($('phA'),pA);
 for(const id in PG)$(id).style.opacity=pageOp(PG[id],t);
 /* inbox */
 rise('lr1',t,s(3)+.6);rise('lr2',t,s(3)+.8);
 {const t0=wordTime(3,3),k=pr(t,t0,t0+.45,E.out);const e=$('lr0');e.style.opacity=k;e.style.transform=`scale(${.92+.08*k})`;e.style.borderColor='#1d4ed8'}
 rise('inStat',t,wordTime(3,6)+.25);
 /* chat */
 rise('cm1',t,wordTime(4,1));rise('cm2',t,wordTime(4,4));rise('cmTag',t,wordTime(4,7)+.3,.4,6);
 {const d1=t>=wordTime(4,3)+.05,d2=t>=wordTime(4,7)+.05;
  for(const [id,d,a,b] of [['ci1',d1,'Tap','Booked ✓'],['bk1',d2,'Tap','Saved ✓']]){const e=$(id);e.textContent=d?b:a;e.style.background=d?'#e5f7ec':'#dbeafe';e.style.color=d?'#136b3b':'#1e40af'}}
 /* lead profile */
 rise('lhd',t,s(5)+.3);
 rise('lf0',t,wordTime(5,1));rise('lf1',t,wordTime(5,3));rise('lf2',t,wordTime(5,5));rise('lf3',t,wordTime(5,8));rise('lsv',t,wordTime(5,10));
 /* viewing */
 rise('vsub',t,wordTime(6,0)+.1,.4,8);
 rise('ev0',t,s(6)+.5,.5,10);
 {const t0=wordTime(6,2),k=pr(t,t0,t0+.5,E.out);const e=$('ev1');e.style.opacity=k;e.style.height=(66*k)+'px'}
 {const t0=wordTime(6,5)+.05,k=pr(t,t0,t0+.45,E.out)*(1-pr(t,s(7)+.1,s(7)+.4,E.lin));const e=$('vnote');e.style.opacity=k;e.style.transform=`translateY(${(k-1)*30}px)`}
 /* pipeline board */
 const bd=kf(brd,t);if(t<brd[0][0]||t>brd[brd.length-1][0])bd[3]=0;place($('pipe'),bd);
 ['kd','kp','km','kl'].forEach((id,i)=>{const t0=s(7)+.95+i*.2,k=pr(t,t0,t0+.5,E.out);$(id).style.opacity=k});
 const m1=pr(t,tm1,tm1+.6,E.io),m2=pr(t,tm2,tm2+.6,E.io);
 const hx=lerp(lerp(COLX[0],COLX[1],m1),COLX[2],m2),hy=lerp(lerp(ROWY[0],ROWY[1],m1),ROWY[1],m2);
 const kd=$('kd');kd.style.left=hx+'px';kd.style.top=hy+'px';
 const pulse=Math.max(pr(t,wordTime(7,0),wordTime(7,0)+.3,E.out)*(1-pr(t,wordTime(7,0)+.5,wordTime(7,0)+1,E.lin)),m1>=1&&m2<=0?1:0,m2>=1?1:0);
 kd.style.boxShadow=`0 0 ${10+14*pulse}px rgba(29,78,216,${.25+.5*pulse})`;
 $('kc0').textContent=m1>.5?1:2;$('kc1').textContent=1+(m1>.5?1:0)-(m2>.5?1:0);$('kc2').textContent=1+(m2>.5?1:0);
 $('liveDot').style.opacity=.5+.5*Math.sin(t*3);
 /* result pills */
 const cw=[wordTime(8,0),wordTime(8,2),wordTime(8,4)];
 [['l8a',0],['l8b',1],['l8c',2]].forEach(([id,n])=>{const k=pr(t,cw[n]-.05,cw[n]+.5,E.out)*(1-pr(t,s(9)-.1,s(9)+.3,E.lin));const e=$(id);e.style.opacity=k;e.style.transform=`translateX(-50%) translateY(${(1-k)*18}px)`});
 /* end */
 const eo=pr(t,s(9)-.05,s(9)+.5,E.lin);$('end').style.opacity=eo;$('end').style.display=eo<=0?'none':'block';
 const el=pr(t,s(9)+.1,s(9)+.8,E.out),ei=$('end').querySelector('img');ei.style.transform=`scale(${.9+.1*el})`;ei.style.opacity=el;
 [['.h',.4],['.u',.85],['.s',wordTime(9,4)-s(9)-.1],['.n',1.3],['.t',1.45],['.sv',1.6]].forEach(([q,d])=>{const e=$('end').querySelector(q);const k=pr(t,s(9)+d,s(9)+d+.55,E.out);e.style.opacity=k;e.style.transform=(q=='.u'?'translateX(-50%) ':'')+`translateY(${(1-k)*22}px)`});
 /* finger */
 const fg=$('finger'),rp=$('rip');let fo=0,rpo=0,fx=0,fy=0,fsc=1,rps=0;
 for(const [t0,id] of TAPS){if(t>t0-.55&&t<t0+.55){const p=tapPos(id);const k=pr(t,t0-.55,t0,E.io);fx=p[0]+(1-k)*50;fy=p[1]+(1-k)*80;fo=cl((t-(t0-.55))/.25)*(1-pr(t,t0+.25,t0+.55,E.lin));fsc=(t>t0&&t<t0+.18)?.85:1;if(t>t0){const q=cl((t-t0)/.5);rpo=(1-q)*.8;rps=.6+q*1.6;rp.style.left=p[0]+'px';rp.style.top=p[1]+'px'}}}
 fg.style.opacity=fo*.9;fg.style.left=fx+'px';fg.style.top=fy+'px';fg.style.transform=`scale(${fsc})`;rp.style.opacity=rpo;rp.style.transform=`scale(${rps})`;
}
