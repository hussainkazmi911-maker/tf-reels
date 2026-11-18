/* kit2.js - "clean" scene kit for the client-case-study reels (glass cards, mono-line icons, calm motion).
   Everything is a pure function of time t. Canvas = 640x600 inside .picin.  window.K2 = { ... } */
window.K2 = (function () {
  const SL = window.SL, { H, S, P, eOut, eIO, eBack, lerp, COL, clamp, rng } = SL;
  const LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber, CY = COL.cyan, WA = COL.wa, PINK = '#ff7ad9';
  const MUTE = 'rgba(255,255,255,.56)', GL = 'rgba(255,255,255,.055)', GB = 'rgba(255,255,255,.14)';
  const BG = {
    dark: 'radial-gradient(circle at 50% 22%,#1b2a0d 0%,#0e120a 70%)',
    red: 'radial-gradient(circle at 50% 22%,#341411 0%,#120908 72%)',
    navy: 'radial-gradient(circle at 50% 22%,#17234f 0%,#0b1029 74%)',
    teal: 'radial-gradient(circle at 50% 22%,#0e3b3b 0%,#07191a 74%)',
    ink: '#0d110a'
  };
  const inr = n => { n = Math.round(n); let s = String(Math.abs(n)); if (s.length > 3) { const l = s.slice(-3); s = s.slice(0, -3).replace(/\B(?=(\d{2})+(?!\d))/g, ',') + ',' + l; } return (n < 0 ? '-' : '') + s; };
  const ICON = {
    play: '<path d="M8 5.5v13l11-6.5z" fill="currentColor"/>',
    reels: '<rect x="4" y="3" width="16" height="18" rx="4"/><path d="M10 9v6l5-3z" fill="currentColor"/>',
    chart: '<path d="M4 20V11M10 20V5M16 20v-6M22 20H2"/>',
    chat: '<path d="M4 5h16v11H10l-5 4v-4H4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    doc: '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h7"/>',
    check: '<path d="M5 12.5l4.2 4.2L19 7"/>',
    cross: '<path d="M6 6l12 12M18 6L6 18"/>',
    box: '<path d="M3 7.5L12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5l9 4.5 9-4.5M12 12v9"/>',
    ret: '<path d="M9 7L4 12l5 5"/><path d="M4 12h11a5 5 0 010 10"/>',
    phone: '<path d="M6.5 3h3l1.6 4.4-2 1.4a11 11 0 005.1 5.1l1.4-2L20 13.5v3A2.5 2.5 0 0117.5 19 14.5 14.5 0 013 4.5 2.5 2.5 0 015.5 2"/>',
    truck: '<path d="M2 6h12v10H2zM14 9h4.5l3.5 3.5V16h-8"/><circle cx="7" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    coin: '<circle cx="12" cy="12" r="9"/><path d="M8.5 8h6M8.5 11h6M9 8c4.5 0 4.5 5.5 0 5.5L15 17.5"/>',
    bolt: '<path d="M13 2L5 13.5h6L10 22l9-12h-6z"/>',
    up: '<path d="M5 15l7-7 7 7"/>',
    store: '<path d="M4 9l1.5-5h13L20 9M4 9h16v11H4zM4 9a3 3 0 006 0 3 3 0 006 0 3 3 0 004 0"/>',
    box2: '<rect x="4" y="4" width="16" height="16" rx="3"/>'
  };
  const ic = (n, s, c, sw) => `<svg viewBox="0 0 24 24" width="${s}" height="${s}" fill="none" stroke="${c}" stroke-width="${sw || 2}" stroke-linecap="round" stroke-linejoin="round" style="color:${c};display:block">${ICON[n]}</svg>`;
  const sfx = (X, t, k, v) => { if (k) X.sfx(t, k, v); };

  function el(sc, css, html, cls) { const e = H('div', cls || 'ui', css, html); sc.picin.appendChild(e); return e; }
  // calm entrance: fades + rises (+ optional sideways), no overshoot
  function rise(sc, e, at, o) {
    o = o || {}; const dy = o.dy == null ? 16 : o.dy, dx = o.dx || 0, dur = o.dur || .42, s0 = o.s0 == null ? .975 : o.s0, op = o.op == null ? 1 : o.op, out = o.out;
    sc.u.push(t => { const p = P(t, at, at + dur), q = eOut(p); let a = p > 0 ? Math.min(1, p * 3) * op : 0; if (out != null) a *= 1 - P(t, out, out + .25);
      e.style.opacity = a; e.style.transform = `translate(${(1 - q) * dx}px,${(1 - q) * dy}px) scale(${s0 + (1 - s0) * q})`; });
  }
  function card(sc, o) {
    const e = el(sc, `left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h}px;border-radius:${o.r == null ? 28 : o.r}px;background:${o.bg || GL};border:1.5px solid ${o.bd || GB};box-shadow:${o.glow ? `0 0 34px ${o.glow}` : 'none'};opacity:0;overflow:${o.clip ? 'hidden' : 'visible'}`);
    if (o.at != null) rise(sc, e, o.at, o); return e;
  }
  function txt(sc, p, o) { // text in a parent element
    const e = H('div', o.cls || 'ui', `position:absolute;left:${o.x}px;top:${o.y}px;${o.w ? `width:${o.w}px;` : ''}font-size:${o.size || 18}px;color:${o.col || '#fff'};font-weight:${o.fw || 700};letter-spacing:${o.ls || 0}px;line-height:${o.lh || 1.1};text-align:${o.align || 'left'};white-space:${o.nw === false ? 'normal' : 'nowrap'};${o.css || ''}`, o.html); p.appendChild(e); return e;
  }
  const hx = (size, col) => `font-family:'Archivo Black',Inter,sans-serif;font-size:${size}px;color:${col};letter-spacing:-.4px`;
  function tag(sc, X, o) { // small outlined pill: ● LABEL
    const e = el(sc, `left:${o.x}px;top:${o.y}px;height:34px;padding:0 14px;border-radius:17px;border:1.5px solid ${o.col || LIME};display:flex;align-items:center;gap:9px;opacity:0;font-weight:800;font-size:13px;letter-spacing:1.8px;color:${o.col || LIME};background:rgba(0,0,0,.2)`, `<span style="width:8px;height:8px;border-radius:50%;background:${o.col || LIME}"></span>${o.text}`);
    rise(sc, e, o.at, { dy: 8 }); return e;
  }
  function num(sc, X, o) { // big counting number
    const e = el(sc, `left:${o.x}px;top:${o.y}px;${o.w ? `width:${o.w}px;` : ''}text-align:${o.align || 'left'};${hx(o.size || 90, o.col || '#fff')};opacity:0;white-space:nowrap`);
    sc.u.push(t => { const p = P(t, o.t0, o.t1), v = o.from + (o.to - o.from) * eOut(p); e.textContent = (o.sign || '') + (o.pre == null ? '' : o.pre) + inr(v) + (o.post || ''); e.style.opacity = t >= (o.at == null ? o.t0 - .1 : o.at) ? 1 : 0; });
    if (o.tick) for (let i = 0; i < 7; i++) X.sfx(o.t0 + i * (o.t1 - o.t0) / 7, 'tick', .5);
    return e;
  }
  function line(sc, parent, o) { // drawn line (div) from (x,y) horizontal w or vertical h
    const e = H('div', 'ui', `position:absolute;left:${o.x}px;top:${o.y}px;${o.h ? `width:${o.th || 3}px;height:${o.h}px;transform-origin:50% 0` : `height:${o.th || 3}px;width:${o.w}px;transform-origin:0 50%`};background:${o.col || LIME};border-radius:3px;opacity:.9`); parent.appendChild(e);
    sc.u.push(t => { const p = eOut(P(t, o.at, o.at + (o.dur || .4))); e.style.opacity = p > 0 ? o.op || .9 : 0; e.style.transform = o.h ? `scaleY(${p})` : `scaleX(${p})`; }); return e;
  }
  function ring(sc, x, y, at, o) { o = o || {};
    const e = el(sc, `left:${x}px;top:${y}px;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;border:${o.w || 3}px solid ${o.col || LIME};opacity:0`);
    sc.u.push(t => { const p = P(t, at, at + (o.dur || .8)); e.style.opacity = p > 0 && p < 1 ? (1 - p) * .8 : 0; const s = 1 + p * (o.r || 7); e.style.transform = `scale(${s})`; }); return e;
  }
  function pill(sc, X, o) { // icon+label chip, can "light up" at o.lit
    const e = el(sc, `left:${o.x}px;top:${o.y}px;width:${o.w}px;height:${o.h || 74}px;border-radius:22px;border:1.5px solid ${GB};background:${GL};display:flex;align-items:center;gap:14px;padding:0 20px;opacity:0`,
      `<div class="ic" style="width:34px;height:34px;flex:none">${ic(o.ic, 34, MUTE, 1.9)}</div><div style="font-family:'Archivo Black';font-size:${o.size || 24}px;color:${MUTE};letter-spacing:-.2px;white-space:nowrap">${o.label}</div>`);
    const icn = e.querySelector('.ic'), lab = e.lastChild;
    rise(sc, e, o.at, { dy: 12 });
    sc.u.push(t => { const l = P(t, o.lit, o.lit + .3), q = eOut(l); if (o.lit == null) return;
      e.style.borderColor = l > 0 ? o.col || LIME : GB; e.style.background = l > 0 ? `rgba(${o.rgb || '198,255,53'},${.04 + .09 * q})` : GL; e.style.boxShadow = l > 0 ? `0 0 ${24 * q}px rgba(${o.rgb || '198,255,53'},${.22 * q})` : 'none';
      icn.innerHTML = ic(o.ic, 34, l > 0 ? o.col || LIME : MUTE, 1.9); lab.style.color = l > 0 ? '#fff' : MUTE; e.style.transform += ` scale(${1 + .03 * Math.sin(Math.PI * clamp(l))})`; });
    if (o.lit != null) sfx(X, o.lit, 'pop', .7); return e;
  }
  function chip(sc, X, o) { // solid lime/colored label pill
    const e = el(sc, `left:${o.x}px;top:${o.y}px;padding:10px 20px;border-radius:30px;background:${o.bg || LIME};color:${o.fg || INK};${hx(o.size || 22, o.fg || INK)};opacity:0;white-space:nowrap;box-shadow:0 8px 26px ${o.sh || 'rgba(198,255,53,.28)'}`, o.text); rise(sc, e, o.at, { dy: 10 }); sfx(X, o.at, o.sfx == null ? 'pop' : o.sfx); return e;
  }
  function stage(sc, X, f) { return f(sc, X); }

  // ---- CTA: type the keyword in a comment box, press POST, get a DM back
  function cta(sc, X, o) {
    const word = o.word; let kwi = null; for (let n = 0; ; n++) { try { kwi = X.W(word, n); } catch (e) { break; } } const kws = X.wt(kwi), post = kws + word.length * .075 + .55;
    const box = el(sc, `left:46px;top:70px;width:548px;height:126px;border-radius:30px;background:#fff;opacity:0;box-shadow:0 18px 50px rgba(0,0,0,.45)`,
      `<div style="position:absolute;left:26px;top:16px;font-weight:800;font-size:14px;letter-spacing:2.4px;color:#80806f">ADD A COMMENT</div><div id="kwt" style="position:absolute;left:26px;top:46px;${hx(56, INK)}"></div>`);
    const kt = box.querySelector('#kwt'); rise(sc, box, X.t0 + .1, { dy: 22 });
    const btn = el(sc, `left:392px;top:222px;width:200px;height:68px;border-radius:34px;background:${LIME};color:${INK};${hx(28, INK)};line-height:68px;text-align:center;opacity:0`, 'POST');
    sc.u.push(t => { const bp = P(t, kws + .2, kws + .55); btn.style.opacity = bp > 0 ? 1 : 0; btn.style.transform = `translateY(${(1 - eOut(bp)) * 14}px) scale(${t >= post && t < post + .18 ? .93 : 1})`;
      const n = clamp(Math.floor((t - kws) / .075), 0, word.length); kt.textContent = (t >= kws ? word.slice(0, n) : '') + ((t >= X.t0 && t < post && Math.sin(t * 9) > 0) ? '|' : ''); });
    ring(sc, 492, 256, post, { col: LIME, r: 6, dur: .7 });
    const dm = el(sc, `left:46px;top:330px;width:420px;border-radius:24px 24px 24px 6px;background:rgba(255,255,255,.08);border:1.5px solid ${GB};padding:18px 22px;opacity:0`,
      `<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px"><div style="width:38px;height:38px;border-radius:50%;background:${LIME};display:flex;align-items:center;justify-content:center">${ic('bolt', 22, INK, 2.2)}</div><div style="font-weight:800;font-size:17px;color:#fff;letter-spacing:.4px">The Total Forge</div><div style="margin-left:auto;font-size:13px;font-weight:700;color:${MUTE}">now</div></div><div style="font-size:21px;font-weight:600;line-height:1.3;color:#fff">${o.dm || 'Hi! Sending you the details on DM.'}</div>`);
    rise(sc, dm, post + .35, { dy: 26 });
    const lg = el(sc, `left:46px;top:500px;display:flex;align-items:center;gap:14px;opacity:0`, `<img src="logo.png" style="width:54px;height:54px;border-radius:50%;border:3px solid ${LIME}"><div><div style="${hx(24, '#fff')}">THE TOTAL FORGE</div><div style="font-weight:700;font-size:15px;letter-spacing:1px;color:${LIME}">thetotalforge.com</div></div>`);
    rise(sc, lg, post + .5, { dy: 14 });
    X.sfx(X.t0 + .1, 'pop'); for (let i = 0; i < word.length; i++) X.sfx(kws + i * .075, 'type'); X.sfx(post, 'success'); X.sfx(post + .35, 'ding', .8); X.punch(post);
  }

  // ---- WhatsApp-style chat card
  function chat(sc, X, o) {
    const c = card(sc, { x: 40, y: 40, w: 560, h: 520, at: X.t0 + .05, clip: true, bg: 'rgba(255,255,255,.045)' });
    txt(sc, c, { x: 26, y: 22, html: `<div style="display:flex;align-items:center;gap:12px"><div style="width:44px;height:44px;border-radius:50%;background:${o.av || PINK};display:flex;align-items:center;justify-content:center;${hx(20, INK)}">${o.initial || 'Z'}</div><div><div style="font-weight:800;font-size:20px;color:#fff">${o.title}</div><div style="font-weight:600;font-size:14px;color:${MUTE}">Business account</div></div></div>` });
    line(sc, c, { x: 0, y: 86, w: 560, th: 1.5, col: GB, at: X.t0 + .15, dur: .3 });
    o.msgs.forEach(m => {
      const right = m.who === 'r', w = m.w || 380;
      const b = H('div', 'ui', `position:absolute;${right ? `right:24px` : `left:24px`};top:${m.y}px;width:${w}px;padding:14px 18px;border-radius:${right ? '22px 22px 6px 22px' : '22px 22px 22px 6px'};background:${m.bg || (right ? 'rgba(37,211,102,.16)' : 'rgba(255,255,255,.1)')};border:1.5px solid ${m.bd || (right ? 'rgba(37,211,102,.55)' : GB)};font-size:${m.size || 21}px;font-weight:600;line-height:1.3;color:#fff;opacity:0`,
        (m.label ? `<div style="font-weight:800;font-size:12px;letter-spacing:1.6px;color:${m.lc || WA};margin-bottom:6px">${m.label}</div>` : '') + m.text + (m.tick ? `<span style="color:${CY};font-size:16px;margin-left:8px">✓✓</span>` : ''));
      c.appendChild(b); rise(sc, b, m.at, { dy: 14, dx: right ? 20 : -20 }); sfx(X, m.at, m.sfx || 'pop', .8);
    });
    return c;
  }

  return { BG, ICON, ic, inr, el, rise, card, txt, hx, tag, num, line, ring, pill, chip, cta, chat, LIME, INK, RED, AMB, CY, WA, PINK, MUTE, GL, GB, sfx };
})();
