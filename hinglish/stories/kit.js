/* kit.js - reusable scene kit for the e-commerce story reels (original flat art, everything is a pure function of time).
   window.KIT = { ICO, stage, chat, receipt, donut, bars, cards, timeline, share, cta, bg, helpers }
   Scenes are plain specs: { line, bg, rows, note?, build(sc,X){ KIT.stage(sc,X,{items:[...]}) } } */
window.KIT = (function () {
  const SL = window.SL, { S, H, T, tf, P, eOut, eBack, eIn, eIO, lerp, COL, Bot, Person, star, heart, check, cross, rng, svgRoot, clamp } = SL;
  const INK = COL.ink, LIME = COL.lime, RED = COL.red, AMB = COL.amber;
  const BG = {
    night: 'linear-gradient(180deg,#0d1536 0%,#1c2a63 70%,#243473 100%)',
    dark: 'radial-gradient(circle at 50% 38%,#24400b 0%,#0b0d09 76%)',
    red: 'radial-gradient(circle at 50% 40%,#5a1212 0%,#1a0606 80%)',
    teal: 'radial-gradient(circle at 50% 38%,#0f5252 0%,#062323 78%)',
    purple: 'radial-gradient(circle at 50% 40%,#3d1f73 0%,#140a2e 82%)',
    cream: '#f4eedc', warm: 'linear-gradient(180deg,#ffe3b8 0%,#ffb27a 78%,#ff9a62 100%)',
    sky: 'linear-gradient(180deg,#cfeeff 0%,#8fd0f7 100%)', mint: 'linear-gradient(180deg,#e4ffd0 0%,#b9f08a 100%)',
    pink: 'linear-gradient(180deg,#ffe0ee 0%,#ffb3d1 100%)', white: '#f7f7f2', ink: '#0b0d09', navy: '#16214f'
  };
  const inr = n => { n = Math.round(n); let s = String(Math.abs(n)); if (s.length > 3) { const last = s.slice(-3); s = s.slice(0, -3).replace(/\B(?=(\d{2})+(?!\d))/g, ',') + ',' + last; } return (n < 0 ? '-' : '') + s; };
  const O = (g, tag, a, w) => S(g, tag, Object.assign({ stroke: INK, 'stroke-width': w || 5, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, a));
  const sfx = (X, t, k, v) => { if (k) X.sfx(t, k, v); };

  // ============================================================ ICONS (centered at 0,0, ~140 units wide)
  const ICO = {
    parcel(p, o = {}) { const g = S(p, 'g'), w = o.w || 112, h = o.h || 92;
      O(g, 'rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: 8, fill: o.col || '#d9a766' });
      O(g, 'rect', { x: -12, y: -h / 2, width: 24, height: h, fill: '#f0cf9a' }, 4);
      O(g, 'rect', { x: 20, y: h / 2 - 34, width: 34, height: 24, rx: 3, fill: '#fff' }, 3);
      S(g, 'path', { d: `M26 ${h / 2 - 25}h20M26 ${h / 2 - 18}h12`, stroke: INK, 'stroke-width': 2.5, 'stroke-linecap': 'round' }); return g; },
    suit(p, o = {}) { const g = S(p, 'g'), c = o.col || '#ff5fa2', c2 = o.col2 || '#ffd166';
      O(g, 'path', { d: 'M-34 -60 q-40 30 -22 112 l26 0 q-6 -62 22 -102z', fill: c2 }, 4);
      O(g, 'path', { d: 'M-28 -62 q28 14 56 0 l34 26 -16 22 -16 -10 6 84 h-72 l6 -84 -16 10 -16 -22z', fill: c });
      O(g, 'path', { d: 'M-14 -62 q14 22 28 0', fill: '#fff' }, 3);
      S(g, 'path', { d: 'M-33 52 h66', stroke: c2, 'stroke-width': 9 });
      [[-14, -10], [10, -2], [-6, 22], [16, 30], [-20, 38], [22, 6]].forEach(([x, y]) => S(g, 'circle', { cx: x, cy: y, r: 4, fill: '#fff', opacity: .85 })); return g; },
    sneaker(p, o = {}) { const g = S(p, 'g'), c = o.col || RED;
      O(g, 'path', { d: 'M-62 22 L-64 -26 Q-62 -40 -48 -40 L-34 -38 Q-26 -14 -4 -8 Q26 0 50 6 Q70 12 70 22 Z', fill: c });
      [[-34, -22], [-24, -14], [-12, -8]].forEach(([x, y]) => S(g, 'path', { d: `M${x} ${y} l14 -10`, stroke: '#fff', 'stroke-width': 5, 'stroke-linecap': 'round' }));
      S(g, 'path', { d: 'M-52 10 Q-10 -8 36 8', stroke: '#fff', 'stroke-width': 7, fill: 'none', 'stroke-linecap': 'round' });
      O(g, 'rect', { x: -70, y: 20, width: 142, height: 18, rx: 9, fill: '#fff' }); return g; },
    jhumka(p, o = {}) { const g = S(p, 'g'), c = o.col || '#ffcf33';
      [-36, 36].forEach(x => { const e = S(g, 'g', { transform: `translate(${x},4)` });
        O(e, 'circle', { cx: 0, cy: -52, r: 8, fill: 'none' }, 4);
        O(e, 'path', { d: 'M-30 -8 a30 30 0 0 1 60 0 z', fill: c });
        [[-22, 0], [-7, 6], [7, 6], [22, 0]].forEach(([bx, by]) => O(e, 'circle', { cx: bx, cy: by + 6, r: 7, fill: '#fff3c4' }, 3));
        S(e, 'path', { d: 'M-16 -24 a18 18 0 0 1 14 -10', stroke: '#fff', 'stroke-width': 4, fill: 'none', 'stroke-linecap': 'round', opacity: .85 }); }); return g; },
    perfume(p, o = {}) { const g = S(p, 'g'), c = o.col || '#7fd6ff';
      O(g, 'rect', { x: -15, y: -76, width: 30, height: 20, rx: 5, fill: INK }); O(g, 'rect', { x: -8, y: -58, width: 16, height: 12, fill: '#cfd3dd' }, 3);
      O(g, 'rect', { x: -44, y: -48, width: 88, height: 112, rx: 22, fill: c }); O(g, 'rect', { x: -30, y: -12, width: 60, height: 48, rx: 8, fill: '#fff' }, 3);
      T(g, o.label || 'EAU', 0, 22, 22, INK); S(g, 'path', { d: 'M-34 -34 q-5 30 0 58', stroke: '#fff', 'stroke-width': 6, fill: 'none', 'stroke-linecap': 'round', opacity: .75 }); return g; },
    earbuds(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -52, y: -8, width: 104, height: 66, rx: 30, fill: '#3b4254' }); S(g, 'path', { d: 'M-52 16 h104', stroke: INK, 'stroke-width': 4 });
      S(g, 'circle', { cx: 0, cy: 38, r: 5, fill: LIME, stroke: INK, 'stroke-width': 2 });
      [-1, 1].forEach(s => { O(g, 'rect', { x: s * 30 - 5, y: -26, width: 10, height: 34, rx: 5, fill: '#fff' }, 4); O(g, 'ellipse', { cx: s * 30, cy: -34, rx: 17, ry: 19, fill: '#fff' }); S(g, 'circle', { cx: s * 30, cy: -34, r: 6, fill: '#c9ced9' }); }); return g; },
    airfryer(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -58, y: -62, width: 116, height: 120, rx: 28, fill: '#2a2f3d' }); O(g, 'path', { d: 'M-58 -34 h116', stroke: INK, 'stroke-width': 4 });
      S(g, 'circle', { cx: 24, cy: -48, r: 9, fill: LIME, stroke: INK, 'stroke-width': 3 }); S(g, 'rect', { x: -40, y: -52, width: 34, height: 10, rx: 5, fill: '#5d6784' });
      O(g, 'rect', { x: -36, y: -16, width: 72, height: 46, rx: 12, fill: '#8fd3ff', opacity: .5 }, 4);
      O(g, 'rect', { x: -28, y: 36, width: 56, height: 14, rx: 7, fill: '#111' }, 3); return g; },
    serum(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -10, y: -82, width: 20, height: 34, rx: 10, fill: '#222' }); O(g, 'rect', { x: -18, y: -52, width: 36, height: 14, rx: 3, fill: '#e6c46a' }, 4);
      O(g, 'rect', { x: -36, y: -40, width: 72, height: 104, rx: 18, fill: o.col || '#ffd9a0' }); O(g, 'rect', { x: -26, y: -6, width: 52, height: 42, rx: 6, fill: '#fff' }, 3);
      T(g, 'SERUM', 0, 20, 12, INK); S(g, 'path', { d: 'M-27 -28 q-4 26 0 48', stroke: '#fff', 'stroke-width': 5, fill: 'none', 'stroke-linecap': 'round', opacity: .8 }); return g; },
    kidstee(p, o = {}) { const g = S(p, 'g');
      O(g, 'path', { d: 'M-26 -48 q26 14 52 0 l32 22 -16 22 -14 -10 4 64 h-58 l4 -64 -14 10 -16 -22z', fill: o.col || '#4db8ff' }); O(g, 'path', { d: 'M-14 -48 q14 18 28 0', fill: '#fff' }, 3);
      star(g, 0, 8, 16, '#ffd24a'); return g; },
    handbag(p, o = {}) { const g = S(p, 'g'), c = o.col || '#c0392b';
      S(g, 'path', { d: 'M-30 -26 q0 -52 30 -52 q30 0 30 52', stroke: INK, 'stroke-width': 8, fill: 'none', 'stroke-linecap': 'round' });
      O(g, 'path', { d: 'M-62 -26 h124 l14 82 q0 10 -10 10 h-132 q-10 0 -10 -10z', fill: c }); S(g, 'path', { d: 'M-62 -26 q62 38 124 0', stroke: INK, 'stroke-width': 5, fill: 'none' });
      O(g, 'rect', { x: -10, y: -6, width: 20, height: 20, rx: 5, fill: '#ffcf33' }, 4); return g; },
    cart(p, o = {}) { const g = S(p, 'g'), c = o.col || LIME;
      S(g, 'path', { d: 'M-76 -58 h22 l10 24', stroke: INK, 'stroke-width': 8, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
      O(g, 'path', { d: 'M-52 -34 h116 l-14 56 h-88 z', fill: c }); [-20, 6, 32].forEach(x => S(g, 'path', { d: `M${x} -30 v48`, stroke: INK, 'stroke-width': 3, opacity: .55 }));
      S(g, 'path', { d: 'M-42 30 h84', stroke: INK, 'stroke-width': 6, 'stroke-linecap': 'round' }); [-28, 34].forEach(x => O(g, 'circle', { cx: x, cy: 46, r: 10, fill: '#fff' }, 5)); return g; },
    phone(p, o = {}) { const g = S(p, 'g'), w = o.w || 76, h = o.h || 132;
      O(g, 'rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: 15, fill: '#161a29' }); const sc = S(g, 'rect', { x: -w / 2 + 6, y: -h / 2 + 10, width: w - 12, height: h - 20, rx: 8, fill: o.scr || '#0b0d09' }); g.scr = sc; return g; },
    store(p, o = {}) { const g = S(p, 'g'), c = o.col || '#fff';
      O(g, 'rect', { x: -62, y: -50, width: 124, height: 104, rx: 8, fill: c }); O(g, 'rect', { x: -52, y: -48, width: 104, height: 26, rx: 5, fill: INK }, 3); T(g, o.name || 'STORE', 0, -28, 15, LIME);
      for (let i = 0; i < 4; i++) O(g, 'path', { d: `M${-62 + i * 31} -18 h31 v18 a15.5 15.5 0 0 1 -31 0z`, fill: i % 2 ? '#fff' : RED }, 3);
      O(g, 'rect', { x: -48, y: 12, width: 40, height: 34, rx: 4, fill: '#bfe9ff' }, 3); O(g, 'rect', { x: 8, y: 8, width: 36, height: 46, rx: 4, fill: '#5b3a29' }, 3); return g; },
    plane(p, o = {}) { const g = S(p, 'g');
      O(g, 'path', { d: 'M-46 -4 L50 -34 L14 38 L2 8 Z', fill: '#fff' }); S(g, 'path', { d: 'M-46 -4 L2 8 L50 -34', stroke: INK, 'stroke-width': 4, fill: 'none', 'stroke-linejoin': 'round' }); S(g, 'path', { d: 'M2 8 L14 38', stroke: INK, 'stroke-width': 4 }); return g; },
    play(p, o = {}) { const g = S(p, 'g'); O(g, 'circle', { cx: 0, cy: 0, r: 46, fill: o.col || LIME }); O(g, 'path', { d: 'M-14 -22 L24 0 L-14 22z', fill: INK }, 4); return g; },
    chart(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -54, y: -48, width: 108, height: 96, rx: 12, fill: '#fff' }); [[-36, 8, 18], [-10, -12, 38], [16, -34, 60]].forEach(([x, y, h], i) => O(g, 'rect', { x, y: 38 - h, width: 20, height: h, rx: 3, fill: i === 2 ? LIME : '#9aa58a' }, 3));
      S(g, 'path', { d: 'M-40 -6 L-8 -22 L18 -38 L40 -52', stroke: RED, 'stroke-width': 0 }); return g; },
    doc(p, o = {}) { const g = S(p, 'g');
      O(g, 'path', { d: 'M-40 -54 h54 l26 26 v82 h-80z', fill: '#fff' }); O(g, 'path', { d: 'M14 -54 v26 h26', fill: '#e1e1d6' }, 4);
      [-12, 4, 20].forEach((y, i) => S(g, 'path', { d: `M-26 ${y} h${i === 2 ? 30 : 52}`, stroke: INK, 'stroke-width': 4, 'stroke-linecap': 'round', opacity: .6 })); check(g, 0, 36, 1, '#17a34a', 7); return g; },
    camera(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -54, y: -34, width: 108, height: 78, rx: 14, fill: '#2a2f3d' }); O(g, 'path', { d: 'M-20 -34 l8 -14 h24 l8 14', fill: '#2a2f3d' }, 5);
      O(g, 'circle', { cx: 0, cy: 6, r: 28, fill: '#8fd3ff' }); S(g, 'circle', { cx: 0, cy: 6, r: 14, fill: INK }); S(g, 'circle', { cx: 8, cy: -2, r: 5, fill: '#fff' }); S(g, 'circle', { cx: 40, cy: -20, r: 5, fill: RED }); return g; },
    clock(p, o = {}) { const g = S(p, 'g'); O(g, 'circle', { cx: 0, cy: 0, r: 50, fill: '#fff' }, 6);
      for (let i = 0; i < 12; i++) { const a = i / 12 * 6.283; S(g, 'line', { x1: Math.cos(a) * 40, y1: Math.sin(a) * 40, x2: Math.cos(a) * 46, y2: Math.sin(a) * 46, stroke: INK, 'stroke-width': 3 }); }
      g.hh = S(g, 'line', { x1: 0, y1: 0, x2: 0, y2: -26, stroke: INK, 'stroke-width': 5, 'stroke-linecap': 'round' }); g.mh = S(g, 'line', { x1: 0, y1: 0, x2: 0, y2: -38, stroke: RED, 'stroke-width': 4, 'stroke-linecap': 'round' }); return g; },
    ghost(p, o = {}) { const g = S(p, 'g'), c = o.col || '#8b93a8';
      S(g, 'path', { d: 'M-26 40 q0 -46 26 -46 q26 0 26 46z', fill: c, opacity: .9 }); S(g, 'circle', { cx: 0, cy: -26, r: 17, fill: c });
      S(g, 'path', { d: 'M-9 -31 l6 6 M-3 -31 l-6 6 M3 -31 l6 6 M9 -31 l-6 6', stroke: INK, 'stroke-width': 2.5, 'stroke-linecap': 'round' }); return g; },
    moneybag(p, o = {}) { const g = S(p, 'g');
      O(g, 'path', { d: 'M-44 14 q0 -48 44 -48 q44 0 44 48 q0 34 -44 34 q-44 0 -44 -34z', fill: AMB }); O(g, 'path', { d: 'M-16 -36 l-6 -18 h44 l-6 18z', fill: '#e69a10' }, 4); T(g, 'Rs', 0, 20, 34, INK); return g; },
    bill(p, o = {}) { const g = S(p, 'g'); O(g, 'rect', { x: -32, y: -18, width: 64, height: 36, rx: 6, fill: o.col || '#7be08a' }, 4); S(g, 'circle', { cx: 0, cy: 0, r: 11, fill: 'none', stroke: INK, 'stroke-width': 3, opacity: .7 }); T(g, 'Rs', 0, 5, 13, INK); return g; },
    coin(p, o = {}) { const g = S(p, 'g'); O(g, 'circle', { cx: 0, cy: 0, r: 22, fill: '#ffcf33' }, 4); T(g, 'Rs', 0, 7, 17, INK); return g; },
    bell(p, o = {}) { const g = S(p, 'g'); O(g, 'path', { d: 'M-30 24 q4 -10 4 -34 q0 -28 26 -28 q26 0 26 28 q0 24 4 34z', fill: '#ffcf33' }); O(g, 'circle', { cx: 0, cy: 32, r: 8, fill: '#ffcf33' }, 4); return g; },
    heartI(p, o = {}) { const g = S(p, 'g'); heart(g, 0, 0, 3, o.col || RED); return g; },
    bolt(p, o = {}) { const g = S(p, 'g'); O(g, 'path', { d: 'M8 -50 L-30 8 h24 l-8 44 L34 -10 H8z', fill: o.col || LIME }); return g; },
    truck(p, o = {}) { const g = S(p, 'g');
      O(g, 'rect', { x: -70, y: -40, width: 90, height: 66, rx: 8, fill: '#fff' }); O(g, 'path', { d: 'M20 -22 h30 l20 24 v24 h-50z', fill: o.col || '#ffcf33' });
      O(g, 'rect', { x: 28, y: -14, width: 22, height: 18, rx: 3, fill: '#bfe9ff' }, 3); [-44, 40].forEach(x => { O(g, 'circle', { cx: x, cy: 30, r: 13, fill: INK }, 4); S(g, 'circle', { cx: x, cy: 30, r: 5, fill: '#cfd3dd' }); });
      T(g, 'COURIER', -25, -2, 15, INK); return g; },
    wa(p, o = {}) { const g = S(p, 'g'); O(g, 'circle', { cx: 0, cy: 0, r: 34, fill: COL.wa }, 4); O(g, 'path', { d: 'M-18 24 l4 -12 q-8 -12 0 -24 q14 -16 30 -4 q12 12 2 26 q-12 12 -24 6z', fill: 'none', stroke: '#fff', 'stroke-width': 5 }, 0); return g; },
    ig(p, o = {}) { const g = S(p, 'g'); O(g, 'rect', { x: -34, y: -34, width: 68, height: 68, rx: 20, fill: '#d6249f' }, 4); O(g, 'circle', { cx: 0, cy: 0, r: 15, fill: 'none', stroke: '#fff', 'stroke-width': 5 }, 0); S(g, 'circle', { cx: 18, cy: -18, r: 4, fill: '#fff' }); return g; },
    ok(p, o = {}) { const g = S(p, 'g'); O(g, 'circle', { cx: 0, cy: 0, r: 46, fill: o.col || '#17a34a' }, 5); check(g, 0, 8, 1.5, '#fff', 9); return g; },
    thumbs(p, o = {}) { const g = S(p, 'g'); O(g, 'path', { d: 'M-34 -4 h20 l18 -40 q14 0 14 14 l-4 22 h30 q12 2 8 16 l-8 36 q-4 10 -14 10 h-64z', fill: o.col || LIME }); return g; }
  };

  // ============================================================ element animation helpers
  const money = (g, w) => ICO.bill(g, {});
  function A(sc, el, o) { // animate an SVG element: base pos x,y,s,r; appears at o.at
    const base = o.s == null ? 1 : o.s, rot = o.r || 0, k = o.kind || 'pop', d = o.dur || .34;
    sc.u.push(t => {
      const p = P(t, o.at, o.at + d);
      if (p <= 0 || (o.out != null && t > o.out)) { el.style.opacity = 0; return; }
      let x = o.x, y = o.y, s = base, r = rot;
      if (k === 'pop') s *= Math.max(0, eBack(p)); else if (k === 'drop') y -= (1 - eOut(p)) * 300; else if (k === 'L') x -= (1 - eOut(p)) * 480;
      else if (k === 'R') x += (1 - eOut(p)) * 480; else if (k === 'U') y += (1 - eOut(p)) * 320; else if (k === 'fade') s *= .8 + .2 * eOut(p);
      if (o.bob) y += Math.sin(t * 3 + (o.ph || 0)) * o.bob; if (o.wig) r += Math.sin(t * o.wig) * 4; if (o.spin) r += (t - o.at) * o.spin;
      if (o.fall) { const q = P(t, o.fall[0], o.fall[1]); y += eIn(q) * (o.fall[2] || 300); }
      if (o.move) { const q = eIO(P(t, o.move[0], o.move[1])); x = lerp(o.x, o.move[2], q); y = lerp(o.y, o.move[3], q); }
      el.style.opacity = (k === 'fade' ? eOut(p) : 1) * (o.fadeOut ? 1 - P(t, o.fadeOut[0], o.fadeOut[1]) : 1);
      tf(el, x, y, r, s * (o.flip ? -1 : 1), s);
    });
  }
  function HA(sc, el, o) { // animate an HTML element (absolute pos left/top given in css): translate + scale
    const k = o.kind || 'pop';
    sc.u.push(t => {
      const p = P(t, o.at, o.at + (o.dur || .32)); if (p <= 0 || (o.out != null && t > o.out)) { el.style.opacity = 0; return; }
      el.style.opacity = 1; let x = 0, y = 0, s = 1, r = 0;
      if (k === 'pop') { s = Math.max(0, eBack(p)); r = (o.rot || 0) * (1 - eOut(p)); } else if (k === 'L') x = -(1 - eOut(p)) * 420; else if (k === 'R') x = (1 - eOut(p)) * 420; else if (k === 'U') y = (1 - eOut(p)) * 300; else if (k === 'drop') y = -(1 - eOut(p)) * 300;
      el.style.transform = `translate(${x}px,${y}px) rotate(${r}deg) scale(${s})`;
    });
  }
  function sparks(sc, g, o) { const n = o.n || 10, R = rng(Math.floor(o.x * 3 + o.y + o.at * 50)), els = [], cols = o.cols || [LIME, '#fff'];
    for (let i = 0; i < n; i++) els.push({ e: star(g, 0, 0, 8 + R() * 8, cols[i % cols.length]), a: i / n * 6.283 + R() * .4, v: (o.r || 90) * (.6 + R() * .7) });
    sc.u.push(t => { const p = P(t, o.at, o.at + .6); els.forEach(q => { if (t < o.at || p >= 1) { q.e.style.opacity = 0; return; } const r = q.v * eOut(p); q.e.style.opacity = 1 - p * p; tf(q.e, o.x + Math.cos(q.a) * r, o.y + Math.sin(q.a) * r, p * 200, 1 - .5 * p); }); }); }
  function ringPulse(sc, g, o) { const e = S(g, 'circle', { cx: o.x, cy: o.y, r: 10, fill: 'none', stroke: o.col || LIME, 'stroke-width': o.w || 6, opacity: 0 });
    sc.u.push(t => { const p = P(t, o.at, o.at + (o.dur || .5)); if (p <= 0 || p >= 1) { e.setAttribute('opacity', 0); return; } e.setAttribute('r', lerp(o.r0 || 20, o.r1 || 120, eOut(p))); e.setAttribute('opacity', .9 * (1 - p)); }); }
  function confetti(sc, g, o) { const R = rng(o.seed || 3), cols = [LIME, '#fff', RED, AMB, COL.cyan], ps = [];
    for (let i = 0; i < (o.n || 26); i++) { const a = ((o.a0 == null ? -140 : o.a0) + R() * ((o.a1 == null ? -40 : o.a1) - (o.a0 == null ? -140 : o.a0))) * Math.PI / 180, v = (o.v0 || 500) + R() * ((o.v1 || 900) - (o.v0 || 500));
      ps.push({ e: S(g, 'rect', { x: -5, y: -8, width: 10, height: 16, rx: 2, fill: cols[Math.floor(R() * cols.length)] }), vx: Math.cos(a) * v, vy: Math.sin(a) * v, rs: (R() - .5) * 900, dl: R() * .1 }); }
    sc.u.push(t => ps.forEach(p => { const d = t - o.at - p.dl; if (d < 0 || d > 2.2) { p.e.style.opacity = 0; return; } const k = .9, f = (1 - Math.exp(-k * d)) / k; p.e.style.opacity = d > 1.8 ? (2.2 - d) / .4 : 1; tf(p.e, o.x + p.vx * f, o.y + p.vy * f + .5 * 900 * d * d, p.rs * d, 1, Math.abs(Math.cos(d * 9)) * .8 + .2); })); }
  function stamp(sc, o) { const e = H('div', 'h', `position:absolute;left:${o.x}px;top:${o.y}px;opacity:0;font-size:${o.size || 60}px;color:${o.fg};border:7px solid ${o.fg};border-radius:16px;padding:6px 20px;background:${o.bg || 'transparent'};white-space:nowrap;transform-origin:50% 50%;z-index:30;${o.css || ''}`, o.text);
    sc.picin.appendChild(e); sc.u.push(t => { const p = P(t, o.at, o.at + .22); e.style.opacity = p > 0 && !(o.out != null && t > o.out) ? 1 : 0; const s = 2.4 - 1.4 * eOut(p); e.style.transform = `rotate(${o.rot == null ? -8 : o.rot}deg) scale(${Math.max(1, s)})`; }); return e; }
  function bub(sc, o) { const cust = o.who !== 'r';
    const e = H('div', 'bub', `left:${o.x}px;top:${o.y}px;width:${o.w}px;background:${o.bg || (cust ? '#fff' : '#dcf8c6')};opacity:0;transform-origin:${cust ? '0% 100%' : '100% 100%'}`,
      (o.label ? `<div style="font-size:13px;font-weight:800;letter-spacing:1px;color:${o.lc || '#128c7e'};margin-bottom:3px">${o.label}</div>` : '') + o.text);
    (o.parent || sc.picin).appendChild(e);
    sc.u.push(t => { const p = P(t, o.at, o.at + .3); e.style.opacity = p > 0 && !(o.out != null && t > o.out) ? 1 : 0; e.style.transform = `scale(${Math.max(0, eBack(p))}) rotate(${(cust ? -1 : 1) * 3 * (1 - eOut(p))}deg)`; }); return e; }

  // ============================================================ stage: data-driven scene
  const ITEM = {
    ico(sc, X, g, it) { const e = S(g, 'g'); (ICO[it.name] || ICO.parcel)(e, it.opt || {}); A(sc, e, it); sfx(X, it.at, it.sfx == null ? 'pop' : it.sfx, it.v); if (it.punch) X.punch(it.at); return e; },
    person(sc, X, g, it) { const pp = Person(S(g, 'g'), { shirt: it.shirt, pants: it.pants, skin: it.skin, hair: it.hair, cap: it.cap, phone: it.phone }); const at = it.at != null ? it.at : X.t0;
      sc.u.push(t => { const p = P(t, at, at + .3); let x = it.x, walk = 0, flip = !!it.flip, mood = it.mood || 'neutral';
        if (it.walk) { const wp = P(t, it.walk[0], it.walk[1]); x = lerp(it.x, it.walk[2], eIO(wp)); walk = wp > 0 && wp < 1 ? (t - it.walk[0]) * 2.1 : 0; }
        if (it.moodAt) it.moodAt.forEach(([tt, m]) => { if (t >= tt) mood = m; });
        if (it.flipAt && t >= it.flipAt) flip = !flip;
        let op = p > 0 ? 1 : 0; if (it.out) op = 1 - P(t, it.out[0], it.out[1]);
        pp.g.style.opacity = op; pp.pose({ x, y: it.y, s: (it.s || 1) * Math.max(.01, eBack(p)), flip, walk, mood, phone: it.phone && !(it.phoneOff && t >= it.phoneOff), armF: it.armF, scr: it.scr, tilt: it.tilt != null ? it.tilt : Math.sin(t * 3) * 2, bob: Math.sin(t * 2.4) * 1.2 }); });
      return pp.g; },
    bot(sc, X, g, it) { const b = Bot(S(g, 'g')); const at = it.at != null ? it.at : X.t0;
      sc.u.push(t => { const p = P(t, at, at + .35); let mood = it.mood || 'open'; if (it.moodAt) it.moodAt.forEach(([tt, m]) => { if (t >= tt) mood = m; });
        const act = it.act ? t >= it.act[0] && t < it.act[1] : (it.busy ? true : false);
        b.g.style.opacity = p > 0 ? 1 : 0;
        b.pose({ x: it.x, y: it.y, s: (it.s || 1) * Math.max(.01, eBack(p)), flip: it.flip, mood, blink: Math.sin(t * 2.3 + (it.ph || 0)) > .97 ? 1 : 0, ant: t, armL: act ? 38 + 30 * Math.sin(t * 14) : (it.wave && t >= it.wave ? 20 : 8), armR: act ? -38 - 30 * Math.sin(t * 14 + 2) : (it.wave && t >= it.wave ? -150 + 24 * Math.sin(t * 9) : -8), bob: Math.sin(t * 3 + (it.ph || 0)) * 3, glow: act ? .8 : (it.glow || 0), chest: it.chest }); });
      sfx(X, at, it.sfx == null ? 'pop' : it.sfx); return b.g; },
    text(sc, X, g, it) { const e = S(g, 'g'); const tx = T(e, it.txt, 0, 0, it.size || 40, it.col || '#fff', it.anchor || 'middle', it.font); if (it.stroke) { tx.style.stroke = it.stroke; tx.style.strokeWidth = it.sw || 6; tx.style.paintOrder = 'stroke'; tx.style.strokeLinejoin = 'round'; }
      A(sc, e, it); sfx(X, it.at, it.sfx, it.v); return e; },
    rect(sc, X, g, it) { const e = S(g, 'g'); S(e, 'rect', { x: -it.w / 2, y: -it.h / 2, width: it.w, height: it.h, rx: it.rx == null ? 14 : it.rx, fill: it.fill || '#fff', stroke: it.stroke || 'none', 'stroke-width': it.sw || 5 });
      if (it.txt) { const tx = T(e, it.txt, 0, (it.size || 30) * .36, it.size || 30, it.col || INK, 'middle', it.font); if (it.sub) { tx.setAttribute('y', -(it.size || 30) * .1); const t2 = T(e, it.sub, 0, (it.size || 30) * .95, (it.size || 30) * .55, it.col2 || it.col || INK, 'middle', 'Inter'); t2.style.fontWeight = 800; } }
      A(sc, e, it); sfx(X, it.at, it.sfx, it.v); return e; },
    badge(sc, X, g, it) { const e = S(g, 'g'); S(e, 'circle', { cx: 0, cy: 0, r: it.r || 22, fill: it.fill || RED, stroke: '#fff', 'stroke-width': 4 }); const tx = T(e, '', 0, (it.r || 22) * .34, (it.r || 22) * 1.0, '#fff');
      sc.u.push(t => { tx.textContent = typeof it.n === 'function' ? it.n(t) : it.n; }); A(sc, e, it); sfx(X, it.at, it.sfx == null ? 'pop' : it.sfx); return e; },
    counter(sc, X, g, it) { const e = S(g, 'g'), w = it.w || 480, h = it.h || 112, col = it.col || RED, fin = (it.sign || '') + (it.pre == null ? 'Rs. ' : it.pre) + inr(it.to) + (it.post || '');
      S(e, 'rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: h / 2, fill: it.bg || INK, stroke: col, 'stroke-width': 7 });
      const size = Math.min(it.size || 66, (w - 50) / (fin.length * .66)); const tx = T(e, '', 0, size * .36, size, it.fg || col);
      sc.u.push(t => { const v = it.from + (it.to - it.from) * eOut(P(t, it.t0, it.t1)); tx.textContent = (it.sign || '') + (it.pre == null ? 'Rs. ' : it.pre) + inr(v) + (it.post || ''); });
      A(sc, e, Object.assign({ at: it.at != null ? it.at : it.t0 }, it)); sfx(X, it.at != null ? it.at : it.t0, 'pop'); if (it.tickSfx) for (let q = 0; q < 6; q++) X.sfx(it.t0 + q * (it.t1 - it.t0) / 6, 'tick'); return e; },
    bills(sc, X, g, it) { const R = rng(it.seed || 5), n = it.n || 6;
      for (let i = 0; i < n; i++) { const e = S(g, 'g'); ICO.bill(e, {}); const dl = i * (it.gap || .12), a = it.at + dl, x1 = it.to ? it.to[0] : it.x, y1 = it.to ? it.to[1] : it.y, sx = it.x + (R() - .5) * (it.spread || 40), ex = x1 + (R() - .5) * (it.spread || 40), ey = y1;
        sc.u.push(t => { const p = P(t, a, a + (it.dur || .9)); if (p <= 0 || p >= 1) { e.style.opacity = 0; return; } e.style.opacity = Math.min(1, p * 6) * (1 - P(p, .8, 1)); const q = eIO(p); tf(e, lerp(sx, ex, q), lerp(it.y, ey, q) - Math.sin(p * Math.PI) * (it.arc == null ? 70 : it.arc), (R() - .5) * 0 + q * (it.spin || 120) * (i % 2 ? 1 : -1), .9 + .2 * Math.sin(p * 3)); });
        sfx(X, a, it.sfx, .6); } },
    spark(sc, X, g, it) { sparks(sc, g, it); sfx(X, it.at, it.sfx); },
    ring(sc, X, g, it) { ringPulse(sc, g, it); },
    conf(sc, X, g, it) { confetti(sc, g, it); },
    stamp(sc, X, g, it) { stamp(sc, it); sfx(X, it.at, it.sfx == null ? 'stamp' : it.sfx); X.punch(it.at); if (it.shake !== false) X.shake(it.at); },
    bub(sc, X, g, it) { bub(sc, it); sfx(X, it.at, it.sfx == null ? 'ding' : it.sfx); },
    line(sc, X, g, it) { const e = S(g, 'line', { x1: it.x1, y1: it.y1, x2: it.x2, y2: it.y2, stroke: it.col || INK, 'stroke-width': it.w || 6, 'stroke-linecap': 'round', 'stroke-dasharray': it.dash || '' }); const L = Math.hypot(it.x2 - it.x1, it.y2 - it.y1);
      if (!it.dash) { e.setAttribute('stroke-dasharray', L); sc.u.push(t => e.setAttribute('stroke-dashoffset', L * (1 - eOut(P(t, it.at, it.at + (it.dur || .4)))))); } else sc.u.push(t => { e.style.opacity = t >= it.at ? 1 : 0; }); },
    arrow(sc, X, g, it) { const e = S(g, 'g'); const L = Math.hypot(it.x2 - it.x1, it.y2 - it.y1), a = Math.atan2(it.y2 - it.y1, it.x2 - it.x1) * 180 / Math.PI;
      S(e, 'line', { x1: 0, y1: 0, x2: L - 12, y2: 0, stroke: it.col || '#fff', 'stroke-width': it.w || 8, 'stroke-linecap': 'round' }); S(e, 'path', { d: `M${L - 22} -16 L${L} 0 L${L - 22} 16z`, fill: it.col || '#fff' });
      sc.u.push(t => { const p = eOut(P(t, it.at, it.at + .3)); e.style.opacity = p > 0 ? 1 : 0; tf(e, it.x1, it.y1, a, p, 1); }); sfx(X, it.at, it.sfx == null ? 'tick' : it.sfx); },
    node(sc, X, g, it) { const e = S(g, 'g'), w = it.w || 170, h = it.h || 150; S(e, 'rect', { x: -w / 2, y: -h / 2, width: w, height: h, rx: 24, fill: it.fill || '#162008', stroke: it.col || LIME, 'stroke-width': 6 });
      if (it.ico) { const ie = S(e, 'g', { transform: `translate(0,${-h * .1}) scale(${it.is || .8})` }); ICO[it.ico](ie, it.opt || {}); }
      const tx = T(e, it.label, 0, h / 2 - 16, it.size || 22, it.lc || '#fff'); A(sc, e, it); sfx(X, it.at, it.sfx == null ? 'pop' : it.sfx); return e; },
    grid(sc, X, g, it) { const e = S(g, 'g'); for (let i = 0; i <= 640; i += 40) { S(e, 'line', { x1: i, y1: 0, x2: i, y2: 600, stroke: it.col || 'rgba(0,0,0,.06)', 'stroke-width': 2 }); S(e, 'line', { x1: 0, y1: i, x2: 640, y2: i, stroke: it.col || 'rgba(0,0,0,.06)', 'stroke-width': 2 }); } },
    fn(sc, X, g, it) { it.f(g, sc, X); }
  };
  function stage(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600);
    if (o.floor) S(g, 'rect', { x: 0, y: o.floorY || 500, width: 640, height: 600 - (o.floorY || 500), fill: o.floor });
    if (o.floorLine) S(g, 'rect', { x: 0, y: (o.floorY || 500) - 6, width: 640, height: 10, fill: o.floorLine });
    (o.items || []).forEach(it => { if (!ITEM[it.t]) throw new Error('unknown item ' + it.t); ITEM[it.t](sc, X, g, it); });
    (o.sfx || []).forEach(([t, k, v]) => X.sfx(t, k, v)); (o.punch || []).forEach(t => X.punch(t)); (o.shake || []).forEach(t => X.shake(t));
    return g;
  }

  // ============================================================ chat phone
  function chat(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const W = o.w || 340, L = o.left == null ? (640 - W) / 2 : o.left, top = o.top == null ? 18 : o.top, Hh = o.h || 566;
    const th = o.theme === 'ig' ? { head: 'linear-gradient(90deg,#833ab4,#fd1d1d,#fcb045)', bg: '#fff', cust: '#efefef', me: '#a46bff', meTx: '#fff' } : { head: '#075e54', bg: '#e5ddd5', cust: '#fff', me: '#dcf8c6', meTx: INK };
    const ph = H('div', 'ui', `left:${L}px;top:${top}px;width:${W}px;height:${Hh}px;border-radius:40px;background:#0b0d09;padding:10px;box-shadow:0 8px 0 rgba(0,0,0,.25)`);
    const scr = H('div', 'ui', `position:absolute;left:10px;top:10px;width:${W - 20}px;height:${Hh - 20}px;border-radius:32px;background:${th.bg};overflow:hidden`);
    scr.appendChild(H('div', 'ui', `left:0;top:0;width:${W - 20}px;height:66px;background:${th.head};color:#fff;font-weight:800;font-size:20px;line-height:66px;padding-left:70px`, o.title || 'Customer'));
    scr.appendChild(H('div', 'ui', `left:16px;top:13px;width:40px;height:40px;border-radius:50%;background:${o.avatar || '#ff8a3d'};border:3px solid rgba(255,255,255,.6)`));
    if (o.sub) scr.appendChild(H('div', 'ui', 'left:70px;top:44px;font-size:12px;font-weight:700;color:rgba(255,255,255,.8);line-height:14px', o.sub));
    ph.appendChild(scr); sc.picin.appendChild(ph);
    let y = 82; const bw = W - 20 - 60, cpl = Math.floor((bw - 32) / 10.4);
    (o.msgs || []).forEach(m => { const cust = m.who !== 'r', lines = Math.max(1, Math.ceil(m.text.length / cpl)), hh = 28 + lines * 24 + (m.label ? 18 : 0), yy = m.y != null ? m.y : y; y = yy + hh + 14;
      const e = H('div', 'bub', `left:${cust ? 12 : 48}px;top:${yy}px;width:${bw}px;background:${m.bg || (cust ? th.cust : th.me)};color:${cust ? INK : th.meTx};font-size:19px;opacity:0;transform-origin:${cust ? '0% 100%' : '100% 100%'}`,
        (m.label ? `<div style="font-size:12px;font-weight:800;letter-spacing:1px;color:${m.lc || '#128c7e'};margin-bottom:3px">${m.label}</div>` : '') + m.text); scr.appendChild(e);
      sc.u.push(t => { const p = P(t, m.at, m.at + .28); e.style.opacity = p > 0 ? 1 : 0; e.style.transform = `scale(${Math.max(0, eBack(p))})`; }); sfx(X, m.at, m.sfx == null ? (cust ? 'ding' : 'pop') : m.sfx); if (m.punch) X.punch(m.at); });
    (o.dots || []).forEach(d => { const e = H('div', 'bub', `left:${d.who === 'c' ? 12 : 48}px;top:${d.y}px;width:78px;height:44px;background:${d.who === 'c' ? th.cust : th.me};opacity:0;padding:0`, [18, 34, 50].map(x => `<i style="position:absolute;left:${x}px;top:17px;width:10px;height:10px;border-radius:50%;background:${INK}"></i>`).join('')); scr.appendChild(e); const di = e.querySelectorAll('i');
      sc.u.push(t => { const on = t >= d.at && t < d.until; e.style.opacity = on ? 1 : 0; di.forEach((q, i) => q.style.transform = `translateY(${-6 * Math.max(0, Math.sin(t * 11 - i))}px)`); }); });
    (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it));
    return { g, scr, ph };
  }

  // ============================================================ receipt / calculator paper
  function receipt(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const pw = 470, px = 85, py = 24;
    const paper = H('div', 'ui', `left:${px}px;top:${py}px;width:${pw}px;height:${o.h || 540}px;background:#fffef6;border-radius:10px 10px 0 0;box-shadow:0 10px 0 rgba(0,0,0,.2);transform:rotate(${o.rot == null ? -1.5 : o.rot}deg);overflow:hidden;font-family:Inter,sans-serif`,
      `<div class="h" style="position:absolute;left:0;top:18px;width:100%;text-align:center;font-size:30px;color:${INK};letter-spacing:2px">${o.title || 'HISAAB'}</div><div style="position:absolute;left:26px;right:26px;top:66px;border-top:4px dashed #bdb8a4"></div>`);
    sc.picin.appendChild(paper);
    const zig = S(g, 'path', { d: `M${px + 4} ${py + (o.h || 540) - 2} ` + Array.from({ length: 24 }, (_, i) => `l9.6 14 l9.6 -14`).join(' '), fill: '#fffef6' }); zig.style.transform = `rotate(${o.rot == null ? -1.5 : o.rot}deg)`; zig.style.transformOrigin = '320px 300px';
    let y = 84; (o.rows || []).forEach(r => { const e = H('div', 'ui', `left:26px;right:26px;top:${y}px;height:44px;opacity:0;font-weight:800;font-size:${r.size || 27}px;color:${r.col || INK};display:flex;justify-content:space-between;align-items:center;white-space:nowrap`, `<span>${r.l}</span><span class="h" style="font-size:${(r.size || 27) + 2}px">${r.r}</span>`); paper.appendChild(e); y += r.gap || 58;
      sc.u.push(t => { const p = P(t, r.at, r.at + .25); e.style.opacity = p > 0 ? 1 : 0; e.style.transform = `translateX(${(1 - eOut(p)) * 40}px)`; }); sfx(X, r.at, r.sfx == null ? 'tick' : r.sfx); });
    if (o.total) { const T0 = o.total, e = H('div', 'ui', `left:18px;right:18px;top:${y + 8}px;height:98px;border-radius:16px;opacity:0;background:${T0.bg || RED};color:${T0.fg || '#fff'};display:flex;flex-direction:column;align-items:center;justify-content:center;transform-origin:50% 50%`, `<div style="font-weight:800;font-size:19px;letter-spacing:2px;opacity:.85">${T0.l}</div><div class="h" style="font-size:${T0.size || 52}px">${T0.r}</div>`); paper.appendChild(e);
      sc.u.push(t => { const p = P(t, T0.at, T0.at + .25); e.style.opacity = p > 0 ? 1 : 0; e.style.transform = `scale(${1 + (1 - eOut(p)) * .5})`; }); sfx(X, T0.at, T0.sfx || 'stamp'); X.punch(T0.at); X.shake(T0.at); }
    (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it));
    return g;
  }

  // ============================================================ donut
  function donut(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const cx = o.cx || 320, cy = o.cy || 270, r = o.r || 142, sw = o.sw || 62, C = 2 * Math.PI * r;
    S(g, 'circle', { cx, cy, r, fill: 'none', stroke: 'rgba(255,255,255,.12)', 'stroke-width': sw });
    let acc = 0; const segs = (o.segs || []).map(s => { const e = S(g, 'circle', { cx, cy, r, fill: 'none', stroke: s.col, 'stroke-width': sw, 'stroke-dasharray': `0 ${C}`, transform: `rotate(${-90 + acc * 3.6} ${cx} ${cy})` }); const o2 = { e, v: s.v, st: acc, at: s.at != null ? s.at : o.at }; acc += s.v; return o2; });
    const tx = T(g, '', cx, cy + (o.csize || 76) * .34, o.csize || 76, o.cfg || '#fff'); const sub = o.sub ? T(g, o.sub, cx, cy + (o.csize || 76) * .34 + 40, 20, o.sfg || '#c9d1b8', 'middle', 'Inter') : null; if (sub) sub.style.fontWeight = 800;
    sc.u.push(t => { segs.forEach(s => { const p = eOut(P(t, s.at, s.at + (o.dur || .9))); s.e.setAttribute('stroke-dasharray', `${C * s.v / 100 * p} ${C}`); }); const p0 = P(t, o.cat != null ? o.cat : segs[0].at, (o.cat != null ? o.cat : segs[0].at) + (o.dur || .9)); tx.textContent = (o.cprefix || '') + Math.round((o.cval == null ? segs[0].v : o.cval) * eOut(p0)) + (o.csuf == null ? '%' : o.csuf); });
    (o.legend || []).forEach((l, i) => { const e = S(g, 'g'); S(e, 'rect', { x: -20, y: -14, width: 28, height: 28, rx: 8, fill: l.col }); const t2 = T(e, l.txt, 22, 8, 22, l.fg || '#fff', 'start', 'Inter'); t2.style.fontWeight = 800; A(sc, e, { x: l.x || 60, y: l.y || (500 + i * 40), at: l.at, kind: 'L' }); });
    sc.u.push(t => { }); sfx(X, segs[0].at, 'zap', .6); (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it)); return g;
  }

  // ============================================================ bars (vertical)
  function bars(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const n = o.bars.length, bw = o.bw || 150, gap = (560 - n * bw) / (n + 1), base = o.base || 470, maxH = o.maxH || 340;
    S(g, 'line', { x1: 40, y1: base + 6, x2: 600, y2: base + 6, stroke: o.axis || '#fff', 'stroke-width': 6, 'stroke-linecap': 'round', opacity: .6 });
    o.bars.forEach((b, i) => { const x = 40 + gap + i * (bw + gap), r = S(g, 'rect', { x, y: base, width: bw, height: 0, rx: 14, fill: b.col, stroke: INK, 'stroke-width': 5 }); const val = T(g, '', x + bw / 2, base - 18, 44, b.fg || '#fff'); T(g, b.label, x + bw / 2, base + 46, b.lsize || 22, o.lfg || '#fff', 'middle', 'Inter').style.fontWeight = 800;
      sc.u.push(t => { const p = eOut(P(t, b.at, b.at + (o.dur || .8))), h = maxH * b.h * p; r.setAttribute('y', base - h); r.setAttribute('height', h); val.setAttribute('y', base - h - 16); val.textContent = p > 0 ? (b.pre || '') + Math.round(b.v * p) + (b.suf == null ? '%' : b.suf) : ''; }); sfx(X, b.at, 'zap', .5); });
    (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it)); return g;
  }

  // ============================================================ cards (numbered list)
  function cards(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const n = o.total || o.cards.length, ch = o.ch || Math.min(128, (560 - (n - 1) * 16) / n), y0 = o.y0 == null ? (600 - (n * ch + (n - 1) * 16)) / 2 : o.y0;
    o.cards.forEach((c, i) => { const y = y0 + i * (ch + 16); if (c.early || c.dim) { c.at = X.t0 - 1; c.sfx = false; c.punch = false; c.spark = false; }
      const e = H('div', 'ui', `left:24px;top:${y}px;width:592px;height:${ch}px;border-radius:26px;background:${c.bg || '#162008'};border:5px solid ${c.col || LIME};box-shadow:0 8px 0 rgba(0,0,0,.3);opacity:0;transform-origin:0% 50%`,
        `<div class="h" style="position:absolute;left:22px;top:${ch / 2 - 30}px;width:60px;height:60px;border-radius:50%;background:${c.col || LIME};color:${INK};font-size:34px;line-height:60px;text-align:center">${c.n != null ? c.n : i + 1}</div><div class="h" style="position:absolute;left:104px;top:${ch / 2 - (c.sub ? 34 : 16)}px;font-size:${c.size || 34}px;color:${c.fg || '#fff'};white-space:nowrap">${c.title}</div>${c.sub ? `<div style="position:absolute;left:104px;top:${ch / 2 + 6}px;font-weight:700;font-size:21px;color:${c.sfg || '#aeb89c'};white-space:nowrap">${c.sub}</div>` : ''}`);
      sc.picin.appendChild(e); HA(sc, e, { at: c.at, kind: 'L', dur: .36 }); if (c.dim) { sc.u.push(() => { e.style.opacity = .2; }); return; }
      if (c.ico) { const ie = S(g, 'g'); ICO[c.ico](ie, c.opt || {}); A(sc, ie, { x: 546, y: y + ch / 2, s: (c.is || .62), at: c.at + .1, kind: 'pop', wig: 3 }); }
      sfx(X, c.at, c.sfx == null ? 'pop' : c.sfx); if (c.punch !== false) X.punch(c.at); if (c.spark !== false) sparks(sc, g, { x: 52, y: y + ch / 2, at: c.at + .12, n: 8, r: 60 }); });
    (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it)); return g;
  }

  // ============================================================ timeline (vertical, active node pops)
  function timeline(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const n = o.nodes.length, y0 = 70, dy = (600 - 2 * y0) / (n - 1), lx = 110;
    S(g, 'line', { x1: lx, y1: y0, x2: lx, y2: y0 + dy * (n - 1), stroke: 'rgba(255,255,255,.18)', 'stroke-width': 10, 'stroke-linecap': 'round' });
    const fill = S(g, 'line', { x1: lx, y1: y0, x2: lx, y2: y0, stroke: LIME, 'stroke-width': 10, 'stroke-linecap': 'round' });
    sc.u.push(t => { const p = eOut(P(t, o.at, o.at + .5)); fill.setAttribute('y2', y0 + dy * (o.active * p)); });
    o.nodes.forEach((nd, i) => { const y = y0 + dy * i, lit = i <= o.active, cur = i === o.active, e = S(g, 'g');
      const c = S(e, 'circle', { cx: lx, cy: y, r: cur ? 30 : 24, fill: lit ? LIME : '#2a3320', stroke: INK, 'stroke-width': 5 }); T(e, String(nd.d), lx, y + 9, cur ? 28 : 22, lit ? INK : '#6b7560');
      const lab = H('div', 'ui', `left:170px;top:${y - 34}px;width:440px;opacity:${lit ? 1 : .45};white-space:nowrap`, `<div class="h" style="font-size:${cur ? 40 : 30}px;color:${cur ? LIME : '#fff'}">${nd.title}</div><div style="font-weight:700;font-size:21px;color:#aeb89c;margin-top:4px">${nd.sub || ''}</div>`); sc.picin.appendChild(lab);
      if (cur) { A(sc, e, { x: 0, y: 0, at: o.at, kind: 'pop' }); sc.u.push(t => { const p = P(t, o.at + .1, o.at + .45); lab.style.transform = `translateX(${(1 - eOut(p)) * 60}px) scale(${1 + .0 * p})`; lab.style.opacity = p > 0 ? 1 : 0; }); sparks(sc, g, { x: lx, y, at: o.at + .1, n: 10, r: 70 }); ringPulse(sc, g, { x: lx, y, at: o.at + .1, r0: 24, r1: 80, w: 6 }); sfx(X, o.at + .05, 'pop'); X.punch(o.at + .1); }
    });
    (o.items || []).forEach(it => ITEM[it.t](sc, X, g, it)); return g;
  }

  // ============================================================ share (send this reel to a seller)
  function share(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const at = X.wt(0), at2 = X.wt(4);
    const ph1 = S(g, 'g'); ICO.phone(ph1, { w: 150, h: 270 }); const pl = S(ph1, 'g'); ICO.play(pl, {}); pl.style.transform = 'scale(.8)'; T(ph1, 'REEL', 0, 98, 24, LIME);
    const st = S(g, 'g'); ICO.store(st, { name: o.name || 'SELLER' }); const trail = S(g, 'path', { d: 'M180 300 Q320 140 460 300', stroke: LIME, 'stroke-width': 6, fill: 'none', 'stroke-dasharray': '4 16', 'stroke-linecap': 'round', opacity: 0 });
    const plane = S(g, 'g'); ICO.plane(plane, {}); const hs = [0, 1, 2, 3, 4].map(i => { const h = heart(g, 0, 0, 1.6, RED); h.style.opacity = 0; return h; });
    const chip = H('div', 'h', `position:absolute;left:150px;top:30px;width:340px;text-align:center;background:${LIME};color:${INK};border-radius:18px;padding:12px 0;font-size:34px;opacity:0;box-shadow:0 7px 0 rgba(0,0,0,.35)`, 'SEND TO A SELLER'); sc.picin.appendChild(chip);
    const wow = H('div', 'h', `position:absolute;left:340px;top:370px;width:260px;text-align:center;color:#fff;font-size:26px;opacity:0`, 'Isko dekhna!'); sc.picin.appendChild(wow);
    sc.u.push(t => { A0(ph1, 150, 300, at, t); const flyT0 = X.wt(4), p = eIO(P(t, flyT0, flyT0 + .9)), q = P(t, flyT0, flyT0 + .9);
      A0(st, 490, 320, at + .1, t); plane.style.opacity = q > 0 && q < 1 ? 1 : 0; const bx = lerp(190, 450, p), by = lerp(300, 300, p) - Math.sin(p * Math.PI) * 160; tf(plane, bx, by, lerp(-30, 25, p) * 1, .9 + .1 * Math.sin(p * 3));
      trail.setAttribute('opacity', q > 0 ? .5 * (1 - P(q, .85, 1)) : 0);
      const cp = P(t, at, at + .3); chip.style.opacity = cp > 0 ? 1 : 0; chip.style.transform = `scale(${Math.max(0, eBack(cp))}) rotate(${-2 + Math.sin(t * 4)}deg)`;
      const wp = P(t, flyT0 + .9, flyT0 + 1.2); wow.style.opacity = wp > 0 ? 1 : 0; wow.style.transform = `scale(${Math.max(0, eBack(wp))})`;
      hs.forEach((h, i) => { const d = t - (flyT0 + .95 + i * .15); if (d < 0) { h.style.opacity = 0; return; } const c = (d % 1.6) / 1.6; h.style.opacity = Math.sin(Math.PI * c); tf(h, 470 + Math.sin(d * 3 + i) * 40, 250 - c * 120, 0, 1 + c * .6); }); });
    function A0(el, x, y, a, t) { const p = P(t, a, a + .35); el.style.opacity = p > 0 ? 1 : 0; tf(el, x, y, 0, Math.max(0, eBack(p))); }
    sparks(sc, g, { x: 460, y: 300, at: X.wt(4) + .9, n: 12, r: 100 }); X.sfx(at, 'pop'); X.sfx(X.wt(4), 'whoosh'); X.sfx(X.wt(4) + .9, 'success'); X.punch(X.wt(4) + .9);
    return g;
  }

  // ============================================================ CTA: comment keyword
  function cta(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600); const word = o.word, kwi = o.kwIndex, kws = X.wt(kwi);
    const kw = H('div', 'ui', `left:50px;top:70px;width:540px;height:112px;border-radius:28px;background:#fff;border:6px solid ${INK};box-shadow:0 10px 0 ${INK};padding:0 24px;opacity:0;transform-origin:50% 50%`,
      `<div style="position:absolute;left:24px;top:12px;font-weight:800;font-size:16px;letter-spacing:2px;color:#6b6b60">ADD A COMMENT</div><div class="h" id="kwt" style="position:absolute;left:24px;top:40px;font-size:52px;color:${INK}"></div>`);
    sc.picin.appendChild(kw); const kt = kw.querySelector('#kwt');
    const btn = H('div', 'h', `position:absolute;left:402px;top:230px;width:188px;height:70px;border-radius:35px;background:${LIME};color:${INK};font-size:30px;line-height:70px;text-align:center;opacity:0;box-shadow:0 7px 0 rgba(198,255,53,.3)`, 'POST'); sc.picin.appendChild(btn);
    const post = kws + .75, bot = Bot(S(g, 'g'));
    const logo = H('div', 'ui', `left:40px;top:500px;display:flex;align-items:center;gap:14px;opacity:0`, `<img src="logo.png" style="width:56px;height:56px;border-radius:50%;border:4px solid ${LIME}"><div><div class="h" style="font-size:24px;color:#fff">THE TOTAL FORGE</div><div style="font-weight:800;font-size:17px;color:#c6ff35">thetotalforge.com</div></div>`); sc.picin.appendChild(logo);
    const cur = S(g, 'g', null, 'opacity:0'); S(cur, 'path', { d: 'M4 2l24 14-10 3-5 11z', fill: '#fff', stroke: INK, 'stroke-width': 3, 'stroke-linejoin': 'round', transform: 'scale(1.6)' });
    const hs = [0, 1, 2, 3, 4, 5].map(i => { const h = heart(g, 0, 0, 1.5, RED); h.style.opacity = 0; return h; }), R = rng(8), hx = hs.map(() => 40 + R() * 560);
    sc.u.push(t => {
      const kp = P(t, X.t0 + .05, X.t0 + .4); kw.style.opacity = kp > 0 ? 1 : 0; kw.style.transform = `scale(${Math.max(0, eBack(kp))}) rotate(${(1 - eOut(kp)) * -4}deg)`;
      const n = Math.max(0, Math.min(word.length, Math.floor((t - kws) / .075))); kt.textContent = (t >= kws ? word.slice(0, n) : '') + ((t >= X.t0 && t < post && Math.sin(t * 10) > 0) ? '|' : '');
      const bp = P(t, kws + .3, kws + .6); btn.style.opacity = bp > 0 ? 1 : 0; btn.style.transform = `scale(${Math.max(0, eBack(bp)) * (t >= post && t < post + .15 ? .88 : 1)})`;
      const a0 = post - .6, cp = eIO(P(t, a0, post - .03)); cur.style.opacity = t > a0 - .1 && t < post + .6 ? 1 : 0; tf(cur, lerp(560, 480, cp), lerp(420, 262, cp) - Math.sin(cp * Math.PI) * 40, 0, 1);
      bot.pose({ x: 470, y: 590, s: .86, mood: 'happy', ant: t, blink: 0, armL: 8, armR: t >= post ? -150 + 24 * Math.sin(t * 9) : -10, bob: Math.sin(t * 3) * 3 });
      const lp = P(t, post, post + .35); logo.style.opacity = lp > 0 ? 1 : 0; logo.style.transform = `translateY(${(1 - eOut(lp)) * 40}px)`;
      hs.forEach((h, i) => { const d = t - (post + .05 + i * .18); if (d < 0) { h.style.opacity = 0; return; } const c = (d % 2) / 2; h.style.opacity = Math.sin(Math.PI * c); tf(h, hx[i], 560 - c * 420, Math.sin(d * 3 + i) * 12, 1 + c * .6); }); });
    sparks(sc, g, { x: 496, y: 265, at: post, n: 14, r: 110 }); confetti(sc, g, { x: 496, y: 265, at: post + .05, n: 28, a0: -150, a1: -30, v0: 500, v1: 900, seed: 12 });
    X.sfx(X.t0 + .1, 'pop'); for (let i = 0; i < word.length; i++) X.sfx(kws + i * .075, 'type'); X.sfx(post, 'success'); X.punch(post); X.shake(post);
    return g;
  }

  return { BG, ICO, ITEM, A, HA, stage, chat, receipt, donut, bars, cards, timeline, share, cta, sparks, ringPulse, confetti, stamp, bub, inr, O };
})();
