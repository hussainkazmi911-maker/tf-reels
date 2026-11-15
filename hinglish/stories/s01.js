/* s01: "Raat 2 baje customer ne message kiya" - why a business needs AI automation (meme-explainer style, original characters). */
(function () {
  const { S, H, T, tf, P, eOut, eBack, eIn, eIO, eElastic, lerp, COL, Bot, Person, Shop, star, heart, check, cross, rng, svgRoot, clamp } = SL;
  const INK = COL.ink, LIME = COL.lime;

  // ---- shared bits ---------------------------------------------------------------------------
  function bub(sc, X, o) { // chat bubble that pops at time o.at. o:{x,y,w,text,label,who:'c'|'r',at,parent}
    const cust = o.who !== 'r';
    const e = H('div', 'bub', `left:${o.x}px;top:${o.y}px;width:${o.w}px;background:${cust ? '#fff' : '#dcf8c6'};opacity:0;transform-origin:${cust ? '0% 100%' : '100% 100%'}`,
      (o.label ? `<div style="font-size:13px;font-weight:800;letter-spacing:1px;color:${o.lc || '#128c7e'};margin-bottom:3px">${o.label}</div>` : '') + o.text);
    (o.parent || sc.picin).appendChild(e);
    sc.u.push(t => {
      const p = P(t, o.at, o.at + .3);
      e.style.opacity = p > 0 ? 1 : 0;
      e.style.transform = `scale(${Math.max(0, eBack(p))}) rotate(${(cust ? -1 : 1) * 3 * (1 - eOut(p))}deg)`;
    });
    return e;
  }
  function sparks(sc, g, o) { // radial sparks at (x,y) at time o.at
    const n = o.n || 10, R = rng(Math.floor(o.x * 3 + o.y + o.at * 50)), els = [];
    for (let i = 0; i < n; i++) els.push({ e: star(g, 0, 0, 8 + R() * 8, (o.cols || [LIME, '#fff'])[i % (o.cols || [1, 2]).length]), a: i / n * 6.283 + R() * .4, v: (o.r || 90) * (.6 + R() * .7) });
    sc.u.push(t => { const p = P(t, o.at, o.at + .6); els.forEach(q => { if (t < o.at || p >= 1) { q.e.style.opacity = 0; return; } const r = q.v * eOut(p); q.e.style.opacity = 1 - p * p; tf(q.e, o.x + Math.cos(q.a) * r, o.y + Math.sin(q.a) * r, p * 200, 1 - .5 * p); }); });
  }
  function ringPulse(sc, g, o) {
    const e = S(g, 'circle', { cx: o.x, cy: o.y, r: 10, fill: 'none', stroke: o.col || LIME, 'stroke-width': o.w || 6, opacity: 0 });
    sc.u.push(t => { const p = P(t, o.at, o.at + (o.dur || .5)); if (p <= 0 || p >= 1) { e.setAttribute('opacity', 0); return; } e.setAttribute('r', lerp(o.r0 || 20, o.r1 || 120, eOut(p))); e.setAttribute('opacity', .9 * (1 - p)); });
  }
  function confetti(sc, g, o) {
    const R = rng(o.seed || 3), cols = [LIME, '#fff', COL.red, COL.amber, COL.cyan], ps = [];
    for (let i = 0; i < (o.n || 26); i++) {
      const a = (o.a0 + R() * (o.a1 - o.a0)) * Math.PI / 180, v = o.v0 + R() * (o.v1 - o.v0);
      ps.push({ e: S(g, 'rect', { x: -5, y: -8, width: 10, height: 16, rx: 2, fill: cols[Math.floor(R() * cols.length)] }), vx: Math.cos(a) * v, vy: Math.sin(a) * v, rs: (R() - .5) * 900, dl: R() * .1 });
    }
    sc.u.push(t => ps.forEach(p => { const d = t - o.at - p.dl; if (d < 0 || d > 2.2) { p.e.style.opacity = 0; return; } const k = .9, f = (1 - Math.exp(-k * d)) / k; p.e.style.opacity = d > 1.8 ? (2.2 - d) / .4 : 1; tf(p.e, o.x + p.vx * f, o.y + p.vy * f + .5 * 900 * d * d, p.rs * d, 1, Math.abs(Math.cos(d * 9)) * .8 + .2); }));
  }
  function stamp(sc, X, o) { // HTML slam stamp
    const e = H('div', 'h', `position:absolute;left:${o.x}px;top:${o.y}px;opacity:0;font-size:${o.size || 60}px;color:${o.fg};border:7px solid ${o.fg};border-radius:16px;padding:6px 20px;background:${o.bg || 'transparent'};white-space:nowrap;transform-origin:50% 50%;z-index:30;${o.css || ''}`, o.text);
    sc.picin.appendChild(e);
    sc.u.push(t => { const p = P(t, o.at, o.at + .22); e.style.opacity = p > 0 ? 1 : 0; const s = 2.4 - 1.4 * eOut(p); e.style.transform = `rotate(${o.rot || -8}deg) scale(${Math.max(1, s)})`; });
    return e;
  }

  // ---- bedroom (scenes 0 and 6) ----------------------------------------------------------------
  function bedroom(sc, X, o) {
    const g = svgRoot(sc.picin, 640, 600), R = rng(7), stars = [];
    for (let i = 0; i < 18; i++) stars.push(star(g, 20 + R() * 600, 16 + R() * 250, 4 + R() * 5, '#fff6c9'));
    const moon = S(g, 'g'); S(moon, 'circle', { cx: 552, cy: 96, r: 80, fill: '#fff6c9', opacity: .1 }); S(moon, 'circle', { cx: 552, cy: 96, r: 46, fill: '#fff1b8' });
    S(moon, 'circle', { cx: 538, cy: 84, r: 9, fill: '#e8d98f' }); S(moon, 'circle', { cx: 568, cy: 112, r: 6, fill: '#e8d98f' });
    S(g, 'rect', { x: 0, y: 500, width: 640, height: 100, fill: '#0f1740' }); S(g, 'rect', { x: 0, y: 496, width: 640, height: 8, fill: '#000', opacity: .35 });
    // bed
    S(g, 'rect', { x: 20, y: 356, width: 28, height: 176, rx: 10, fill: '#2a1d5c', stroke: INK, 'stroke-width': 5 });
    S(g, 'rect', { x: 40, y: 468, width: 430, height: 62, rx: 12, fill: '#3b2a78', stroke: INK, 'stroke-width': 5 });
    S(g, 'rect', { x: 50, y: 426, width: 412, height: 50, rx: 16, fill: '#e9edff', stroke: INK, 'stroke-width': 5 });
    S(g, 'ellipse', { cx: 116, cy: 416, rx: 58, ry: 25, fill: '#fff', stroke: INK, 'stroke-width': 5 });
    const hd = S(g, 'g');
    S(hd, 'circle', { cx: 120, cy: 388, r: 35, fill: COL.skin, stroke: INK, 'stroke-width': 4 });
    S(hd, 'path', { d: 'M85 384 a35 35 0 0 1 70 0 q-35 -18 -70 0z', fill: '#2b1d14' });
    S(hd, 'path', { d: 'M106 392 q6 6 12 0 M128 392 q6 6 12 0', stroke: INK, 'stroke-width': 3.5, fill: 'none', 'stroke-linecap': 'round' });
    const mf = S(hd, 'path', { d: 'M114 406 h14', stroke: INK, 'stroke-width': 3.5, fill: 'none', 'stroke-linecap': 'round' });
    const ms = S(hd, 'path', { d: 'M110 403 q11 12 22 0', stroke: INK, 'stroke-width': 3.5, fill: 'none', 'stroke-linecap': 'round' });
    (o.smile ? mf : ms).style.display = 'none';
    const bl = S(g, 'g'); S(bl, 'path', { d: 'M156 410 q32 -24 72 -8 q62 22 124 -4 q58 -14 110 10 v62 h-306z', fill: '#3d5cff', stroke: INK, 'stroke-width': 5, 'stroke-linejoin': 'round' });
    S(bl, 'path', { d: 'M156 440 h306', stroke: LIME, 'stroke-width': 8 }); bl.style.transformOrigin = '300px 480px';
    // nightstand + phone
    S(g, 'rect', { x: 484, y: 446, width: 130, height: 124, rx: 10, fill: '#3b2a78', stroke: INK, 'stroke-width': 5 });
    S(g, 'rect', { x: 498, y: 482, width: 102, height: 26, rx: 6, fill: '#2a1d5c' }); S(g, 'rect', { x: 536, y: 492, width: 26, height: 6, rx: 3, fill: LIME });
    const ph = S(g, 'g'); S(ph, 'rect', { x: -32, y: -104, width: 64, height: 104, rx: 11, fill: '#161a29', stroke: '#6b7392', 'stroke-width': 3 });
    const scr = S(ph, 'rect', { x: -26, y: -96, width: 52, height: 86, rx: 6, fill: '#0b0d09' });
    const phg = S(g, 'circle', { cx: 548, cy: 398, r: 90, fill: COL.wa, opacity: 0 });
    const badge = S(g, 'g'); S(badge, 'circle', { cx: 0, cy: 0, r: 17, fill: COL.red, stroke: '#fff', 'stroke-width': 3 }); const bt = T(badge, '1', 0, 7, 20, '#fff');
    const clk = S(g, 'g'); S(clk, 'rect', { x: 60, y: 76, width: 200, height: 92, rx: 18, fill: INK, stroke: COL.red, 'stroke-width': 5 });
    const ct = T(clk, '2:00', 138, 142, 58, COL.red); const am = T(clk, 'AM', 232, 142, 22, COL.red);
    clk.style.transformOrigin = '160px 122px';
    const zz = [0, 1, 2].map(i => { const z = T(g, 'Z', 0, 0, 30 + i * 14, '#fff'); z.style.opacity = 0; return z; });
    const upd = (t, k) => {
      stars.forEach((s, i) => { s.style.opacity = .45 + .5 * Math.sin(t * 2 + i * 1.7); });
      bl.style.transform = `scaleY(${1 + .025 * Math.sin(t * 2.2)})`;
      hd.style.transform = `translateY(${.8 * Math.sin(t * 2.2)}px)`;
      moon.style.transform = `translateY(${Math.sin(t * .7) * 4}px)`;
      ct.textContent = (Math.floor(t * 1.8) % 2 || P(t, k.clockAt, k.clockAt + .3) < 1) ? '2:00' : '2:00';
      const cp = P(t, k.clockAt, k.clockAt + .4);
      clk.style.opacity = cp > 0 ? 1 : 0; clk.style.transform = `scale(${Math.max(0, eBack(cp))})`;
      const bz = k.buzzAt != null && t >= k.buzzAt ? Math.sin(t * 64) * 6 * (1 - P(t, k.buzzAt, k.buzzAt + 1.1)) : 0;
      tf(ph, 548, 446, -9 + bz);
      const on = k.glowAt != null && t >= k.glowAt;
      scr.setAttribute('fill', on ? '#1d4d36' : '#0b0d09');
      phg.setAttribute('opacity', on ? .13 + .07 * Math.sin(t * 7) : 0);
      const bp = k.badgeAt != null ? P(t, k.badgeAt, k.badgeAt + .25) : 0; tf(badge, 575, 338, 0, Math.max(0, eBack(bp)));
      if (k.badgeN) bt.textContent = String(k.badgeN(t));
      zz.forEach((z, i) => {
        const s0 = k.zAt + i * .28, d = t - s0, c = d >= 0 ? (d % 1.6) / 1.6 : 0;
        z.style.opacity = d < 0 ? 0 : Math.sin(Math.PI * clamp(c)) * .95;
        tf(z, 170 + i * 28 + c * 14, 350 - i * 18 - c * 70, -8 + i * 6, .8 + c * .5);
      });
    };
    return { g, upd };
  }

  // =========================================================================================================
  const SP = [];

  // ---- 0: HOOK - 2 AM, customer messages, owner asleep ------------------------------------------------
  SP.push({
    line: 0, bg: 'linear-gradient(180deg,#0d1536 0%,#1c2a63 70%,#243473 100%)',
    rows: [['Raat ke do baje', 70, 'white'], ['customer ne', 62, 'white'], ['WhatsApp kiya,', 80, 'lime'], ['aur aap so rahe the.', 54, 'red', { mt: 14 }]],
    build(sc, X) {
      const room = bedroom(sc, X, { smile: false });
      const k = { clockAt: X.wt(2), buzzAt: X.wt(4), glowAt: X.wt(4), badgeAt: X.wt(6), zAt: X.wt(10), badgeN: t => (t >= X.wt(9) ? 3 : t >= X.wt(7) ? 2 : 1) };
      bub(sc, X, { x: 300, y: 250, w: 250, text: 'Bhai, price kya hai?', label: 'WHATSAPP · CUSTOMER', at: X.wt(6) });
      bub(sc, X, { x: 330, y: 168, w: 250, text: 'Reply karo please', label: 'WHATSAPP · CUSTOMER', at: X.wt(7) + .12 });
      bub(sc, X, { x: 270, y: 90, w: 200, text: 'Hello???', label: 'WHATSAPP · CUSTOMER', at: X.wt(9) });
      sc.u.push(t => room.upd(t, k));
      X.sfx(X.wt(2), 'pop'); X.sfx(X.wt(4), 'buzz'); X.sfx(X.wt(6) + .02, 'ding'); X.sfx(X.wt(7) + .14, 'ding'); X.sfx(X.wt(9) + .02, 'ding');
      X.punch(X.wt(2)); X.punch(X.wt(6)); X.shake(X.wt(4));
    }
  });

  // ---- 1: morning, customer walks to the competitor ----------------------------------------------------
  SP.push({
    line: 1, bg: 'linear-gradient(180deg,#ffe3b8 0%,#ffb27a 75%,#ff9a62 100%)',
    rows: [['Subah tak woh', 64, 'white'], ['aapke competitor', 66, 'lime'], ['ke paas ja', 64, 'white'], ['chuka tha.', 88, 'red']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      const sun = S(g, 'g'); S(sun, 'circle', { cx: 0, cy: 0, r: 92, fill: '#fff7c8', opacity: .35 }); S(sun, 'circle', { cx: 0, cy: 0, r: 54, fill: '#fff3a0' });
      const cl = [0, 1, 2].map(i => S(g, 'g')); cl.forEach((c, i) => { S(c, 'ellipse', { cx: 0, cy: 0, rx: 60 - i * 10, ry: 20 - i * 3, fill: '#fff', opacity: .85 }); S(c, 'ellipse', { cx: 26, cy: -12, rx: 34 - i * 6, ry: 17, fill: '#fff', opacity: .85 }); });
      S(g, 'rect', { x: 0, y: 478, width: 640, height: 122, fill: '#4b4766' }); S(g, 'rect', { x: 0, y: 470, width: 640, height: 16, fill: '#d6cdbd' });
      const dash = [0, 1, 2, 3, 4, 5].map(i => S(g, 'rect', { x: 0, y: 548, width: 60, height: 9, rx: 4, fill: '#fff', opacity: .6 }));
      // left (your) shop: dim
      const A = Shop(g, { w: 216, h: 300, color: '#a9a4bd', awn: ['#8a859f', '#c6c2d6'], name: 'AAPKI DUKAAN', signBg: '#2a2838', signFg: '#8f8aa8', signSize: 21, winCol: '#7e7a96', doorCol: '#6b667f' }); tf(A.g, 14, 170);
      const tag = S(g, 'g'); S(tag, 'rect', { x: -48, y: 0, width: 96, height: 44, rx: 8, fill: COL.red, stroke: INK, 'stroke-width': 4 }); T(tag, 'REPLY', 0, 19, 15, '#fff'); T(tag, 'NAHI', 0, 37, 15, '#fff');
      // right (competitor): vivid
      const B = Shop(g, { w: 216, h: 320, color: '#fff', awn: [COL.red, '#fff'], name: 'COMPETITOR', signSize: 22, winCol: '#ffe9a6' }); tf(B.g, 410, 150);
      const bot = Bot(S(g, 'g'));
      const neon = H('div', 'h', 'position:absolute;left:424px;top:104px;width:190px;text-align:center;font-size:25px;color:#c6ff35;border:4px solid #c6ff35;border-radius:12px;padding:5px 0;background:#0b0d09;box-shadow:0 0 22px #c6ff35;opacity:0', 'OPEN 24/7'); sc.picin.appendChild(neon);
      const cust = Person(S(g, 'g'), { shirt: '#ff8a3d', phone: true });
      const chip = H('div', 'h', `position:absolute;left:0;top:0;background:${INK};color:${LIME};border-radius:14px;padding:5px 12px;font-size:16px;letter-spacing:1px;opacity:0`, 'CUSTOMER'); sc.picin.appendChild(chip);
      const coins = [0, 1, 2, 3].map(i => { const c = S(g, 'g'); S(c, 'circle', { r: 15, fill: '#ffcf33', stroke: INK, 'stroke-width': 4 }); T(c, 'Rs', 0, 6, 14, INK); return c; });
      const tWalk0 = X.wt(5), tWalk1 = X.wt(8) - .02, tIn = X.wt(8) + .1, doorX = 410 + B.doorX, x0 = 330, x1 = doorX - 10;
      const stampT = X.wt(9) - .02;
      stamp(sc, X, { x: 40, y: 210, text: '-1 SALE', fg: '#fff', bg: COL.red, rot: -9, at: stampT, size: 56, css: 'border-color:#0b0d09' });
      sc.u.push(t => {
        // sun rise
        const sp = eOut(P(t, X.t0 + .05, X.wt(3)));
        tf(sun, 330, lerp(680, 110, sp)); sun.style.opacity = 1;
        cl.forEach((c, i) => tf(c, ((t * (10 + i * 5) + i * 230) % 840) - 100, 70 + i * 52));
        dash.forEach((d, i) => tf(d, (((i * 120 - t * 120) % 720) + 720) % 720 - 60, 0));
        tf(tag, 14 + 216 * .66, 252 + 26 * Math.sin(t * 1.8) * 0 + 4, Math.sin(t * 2.6) * 6);
        tag.style.transformOrigin = '0px 0px';
        // competitor goes live
        const live = P(t, X.wt(4) - .1, X.wt(4) + .3);
        neon.style.opacity = live > 0 ? (.8 + .2 * Math.sin(t * 30) > .85 ? 1 : .9) * 1 : 0; neon.style.transform = `scale(${Math.max(0, eBack(live))})`;
        B.dg.setAttribute('opacity', t >= tIn ? .9 : .0);
        const bp = P(t, X.wt(4), X.wt(4) + .3);
        bot.pose({ x: 471, y: 412, s: .33 * Math.max(.001, eBack(bp)), mood: t > tIn ? 'happy' : 'open', blink: (Math.sin(t * 2.3) > .97 ? 1 : 0), ant: t, armL: 20, armR: -20 });
        // customer
        let cx = x0, walk = 0, flip = true, vis = 1, sc2 = 1;
        if (t >= tWalk0) { flip = false; const wp = P(t, tWalk0, tWalk1); cx = lerp(x0, x1, eIO(wp)); walk = wp < 1 ? (t - tWalk0) * 2.1 : 0; }
        else if (t >= X.wt(3)) flip = false;
        if (t >= tIn) { const ip = P(t, tIn, tIn + .3); vis = 1 - ip; sc2 = 1 - .45 * ip; cx = x1 + 18 * ip; }
        cust.pose({ x: cx, y: 486, s: .95 * sc2, flip, walk, mood: t < tWalk0 ? 'worry' : 'smile', phone: t < tWalk0, tilt: flip ? -4 * Math.sin(t * 3) : 0, bob: Math.sin(t * 2.4) * 1.2 });
        cust.g.style.opacity = vis;
        const cp = P(t, X.t0 + .25, X.t0 + .5); chip.style.opacity = cp * vis;
        chip.style.transform = `translate(${cx - 44}px,${486 - 262 * .95 - 4}px) scale(${.8 + .2 * eBack(cp)})`;
        // coins fly from your shop to competitor after stamp
        coins.forEach((c, i) => {
          const s0 = stampT + .05 + i * .12, p = P(t, s0, s0 + .8);
          c.style.opacity = p > 0 && p < 1 ? 1 : 0;
          tf(c, lerp(120, 520, eIO(p)), lerp(300, 280, p) - Math.sin(p * Math.PI) * 120, p * 360);
        });
      });
      sparks(sc, g, { x: doorX, y: 400, at: tIn, n: 12, r: 100 });
      X.sfx(X.wt(4) - .1, 'zap'); X.sfx(tIn, 'ding'); X.sfx(stampT, 'stamp'); X.sfx(stampT + .08, 'coin'); X.sfx(stampT + .24, 'coin');
      X.punch(stampT); X.shake(stampT);
    }
  });

  // ---- 2: the competitor has AI automation, never sleeps -----------------------------------------------
  SP.push({
    line: 2, bg: 'radial-gradient(circle at 50% 38%,#0f5252 0%,#062323 78%)',
    rows: [['Kyunki competitor', 48, 'white'], ['ke paas', 48, 'white'], ['AI automation', 80, 'lime'], ['hai, aur woh', 48, 'white'], ['kabhi sota nahi.', 62, 'red']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      const dial = S(g, 'g'); S(dial, 'circle', { cx: 320, cy: 270, r: 214, fill: 'none', stroke: LIME, 'stroke-width': 6, opacity: .35 });
      for (let i = 0; i < 24; i++) { const a = i / 24 * 6.283; S(dial, 'line', { x1: 320 + Math.cos(a) * 196, y1: 270 + Math.sin(a) * 196, x2: 320 + Math.cos(a) * (i % 6 ? 208 : 226), y2: 270 + Math.sin(a) * (i % 6 ? 208 : 226), stroke: LIME, 'stroke-width': i % 6 ? 3 : 6, opacity: .5 }); }
      const orbit = S(g, 'g'); const sun = S(orbit, 'g'), moon = S(orbit, 'g');
      S(sun, 'circle', { cx: 0, cy: -214, r: 22, fill: '#ffd24a', stroke: INK, 'stroke-width': 4 });
      S(moon, 'circle', { cx: 0, cy: 214, r: 22, fill: '#fff1b8', stroke: INK, 'stroke-width': 4 }); S(moon, 'circle', { cx: 9, cy: 207, r: 17, fill: '#0b3b3b' });
      // counter + bot
      const bot = Bot(S(g, 'g'));
      S(g, 'rect', { x: 110, y: 470, width: 420, height: 140, rx: 20, fill: INK, stroke: LIME, 'stroke-width': 6 });
      T(g, '24/7', 320, 556, 56, LIME);
      // gears
      const gear = (cx, cy, r, n) => { const e = S(g, 'g'); S(e, 'circle', { cx: 0, cy: 0, r: r, fill: LIME, stroke: INK, 'stroke-width': 5 }); for (let i = 0; i < n; i++) S(e, 'rect', { x: -r * .16, y: -r * 1.28, width: r * .32, height: r * .4, rx: 4, fill: LIME, stroke: INK, 'stroke-width': 4, transform: `rotate(${i * 360 / n})` }); S(e, 'circle', { cx: 0, cy: 0, r: r * .38, fill: '#062323', stroke: INK, 'stroke-width': 4 }); e.dataset.cx = cx; e.dataset.cy = cy; return e; };
      const g1 = gear(96, 150, 38, 8), g2 = gear(548, 118, 48, 10);
      // AI badge
      const aib = S(g, 'g'); S(aib, 'circle', { cx: 0, cy: 0, r: 46, fill: '#fff', stroke: INK, 'stroke-width': 5 }); T(aib, 'AI', 0, 14, 38, INK);
      // zzz crossed
      const zz = S(g, 'g'); const zt = T(zz, 'Zzz', 0, 0, 56, '#fff'); const zx = S(zz, 'path', { d: 'M-70 -44 L74 24 M74 -44 L-70 24', stroke: COL.red, 'stroke-width': 12, 'stroke-linecap': 'round', fill: 'none', 'stroke-dasharray': 190, 'stroke-dashoffset': 190 });
      const neon = H('div', 'h', 'position:absolute;left:190px;top:14px;width:260px;text-align:center;font-size:36px;color:#c6ff35;border:5px solid #c6ff35;border-radius:16px;padding:8px 0;background:#0b0d09;box-shadow:0 0 30px #c6ff35;opacity:0;transform-origin:50% 0%', 'OPEN 24/7'); sc.picin.appendChild(neon);
      const wake = X.wt(4), auto = X.wt(5), kab = X.wt(9), sota = X.wt(10), nahi = X.wt(11);
      sc.u.push(t => {
        const sp = (t - sc.t0) * 36 * (t > kab ? 2.4 : 1); orbit.style.transformOrigin = '320px 270px'; orbit.style.transform = `rotate(${sp}deg)`;
        const awake = t >= wake, wp = P(t, wake, wake + .35);
        bot.pose({ x: 320, y: 500, s: 1.3, mood: !awake ? 'off' : (t < wake + .45 ? 'wow' : (t > nahi ? 'happy' : 'open')), blink: awake && (Math.sin(t * 2.1) > .96 ? 1 : 0), ant: t, armL: awake ? 20 + 18 * Math.sin(t * 7) : 6, armR: awake ? -20 - 18 * Math.sin(t * 7 + 1.6) : -6, bob: awake ? Math.sin(t * 3) * 4 : Math.sin(t * 1.4) * 2, glow: awake ? .6 + .4 * Math.sin(t * 3) : 0 });
        const ab = P(t, wake + .05, wake + .4); tf(aib, 120, 330, -12, Math.max(0, eBack(ab)));
        const gp = P(t, auto, auto + .3); tf(g1, 96, 150, (t - auto) * 70, Math.max(0, eBack(gp))); tf(g2, 548, 118, -(t - auto) * 55, Math.max(0, eBack(gp)));
        const nk = P(t, kab, kab + .5); neon.style.opacity = nk > 0 ? (Math.sin(t * 28) > -.7 ? 1 : .55) : 0;
        neon.style.transform = `rotate(${Math.sin(t * 7) * 7 * (1 - eOut(nk))}deg) translateY(${(1 - eOut(nk)) * -90}px)`;
        const zp = P(t, sota, sota + .25); tf(zz, 500, 220 + Math.sin(t * 3) * 4, 8, Math.max(0, eBack(zp))); zz.style.opacity = zp > 0 ? 1 : 0;
        zx.setAttribute('stroke-dashoffset', 190 * (1 - eOut(P(t, nahi - .02, nahi + .3))));
      });
      sparks(sc, g, { x: 320, y: 300, at: wake, n: 14, r: 150 });
      ringPulse(sc, g, { x: 320, y: 320, at: wake, r0: 40, r1: 260, w: 8, dur: .6 });
      X.sfx(wake, 'zap'); X.sfx(wake + .1, 'pop'); X.sfx(auto, 'pop'); X.sfx(kab, 'neon'); X.sfx(nahi, 'stamp');
      X.punch(wake); X.punch(kab); X.shake(wake); X.shake(nahi);
    }
  });

  // ---- 3: message -> AI replies in 3 s, order taken, appointment booked ---------------------------------
  SP.push({
    line: 3, bg: '#f4eedc',
    rows: [['AI ne', 64, 'white'], ['teen second mein', 72, 'lime'], ['reply kiya, order liya,', 46, 'white'], ['aur appointment book kar di.', 44, 'white']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      // phone
      const ph = H('div', 'ui', 'left:22px;top:26px;width:300px;height:548px;border-radius:38px;background:#0b0d09;padding:10px;box-shadow:0 8px 0 rgba(0,0,0,.25)');
      const scrn = H('div', 'ui', 'position:absolute;left:10px;top:10px;width:280px;height:528px;border-radius:30px;background:#e5ddd5;overflow:hidden');
      scrn.appendChild(H('div', 'ui', 'left:0;top:0;width:280px;height:62px;background:#075e54;color:#fff;font-weight:800;font-size:19px;line-height:62px;padding-left:64px', 'Customer'));
      scrn.appendChild(H('div', 'ui', 'left:14px;top:12px;width:38px;height:38px;border-radius:50%;background:#ff8a3d'));
      ph.appendChild(scrn); sc.picin.appendChild(ph);
      const mini = (cust, text, at, y) => { const e = H('div', 'bub', `left:${cust ? 12 : 60}px;top:${y}px;width:${cust ? 196 : 206}px;background:${cust ? '#fff' : '#dcf8c6'};font-size:18px;opacity:0;transform-origin:${cust ? '0% 100%' : '100% 100%'}`, text); scrn.appendChild(e); sc.u.push(t => { const p = P(t, at, at + .28); e.style.opacity = p > 0 ? 1 : 0; e.style.transform = `scale(${Math.max(0, eBack(p))})`; }); };
      const tReply = X.wt(5), tOrder = X.wt(7), tAppt = X.wt(10);
      mini(true, 'Hi! Price kya hai? Kal 4 baje appointment mil sakta hai?', X.t0 + .2, 82);
      const dots = H('div', 'bub', 'left:60px;top:226px;width:78px;height:44px;background:#dcf8c6;opacity:0;padding:0', '<i style="position:absolute;left:18px;top:17px;width:10px;height:10px;border-radius:50%;background:#0b0d09"></i><i style="position:absolute;left:34px;top:17px;width:10px;height:10px;border-radius:50%;background:#0b0d09"></i><i style="position:absolute;left:50px;top:17px;width:10px;height:10px;border-radius:50%;background:#0b0d09"></i>'); scrn.appendChild(dots); const di = dots.querySelectorAll('i');
      mini(false, 'Price Rs. 2,500 hai. Kal 4 PM book kar dun?', tReply, 226);
      mini(true, 'Haan, confirm kar do', X.wt(6) + .35, 332);
      mini(false, 'Done! Order confirm, 4 PM booked.', tAppt + .2, 396);
      // timer ring
      const tm = S(g, 'g'); const C = 2 * Math.PI * 44;
      S(tm, 'circle', { cx: 0, cy: 0, r: 44, fill: '#fff', stroke: INK, 'stroke-width': 5 });
      S(tm, 'circle', { cx: 0, cy: 0, r: 44, fill: 'none', stroke: 'rgba(11,13,9,.15)', 'stroke-width': 9 });
      const arc = S(tm, 'circle', { cx: 0, cy: 0, r: 44, fill: 'none', stroke: '#ff4b3a', 'stroke-width': 9, 'stroke-linecap': 'round', 'stroke-dasharray': C, 'stroke-dashoffset': C, transform: 'rotate(-90)' });
      const tt = T(tm, '0:00', 0, 9, 25, INK); T(tm, 'REPLY TIME', 0, 74, 14, INK, 'middle', 'Inter');
      // cards
      const card = (y, title, sub, at, col) => {
        const e = H('div', 'ui', `left:346px;top:${y}px;width:276px;height:84px;border-radius:20px;background:${col};border:5px solid ${INK};box-shadow:0 7px 0 ${INK};opacity:0;transform-origin:0% 50%`, `<div class="h" style="position:absolute;left:76px;top:14px;font-size:18px;color:${INK};white-space:nowrap">${title}</div><div style="position:absolute;left:76px;top:44px;font-weight:700;font-size:15px;color:${INK};opacity:.7;white-space:nowrap">${sub}</div>`);
        const sv = svgRoot(e, 70, 76, 'left:0;top:0'); const c = S(sv, 'circle', { cx: 38, cy: 38, r: 22, fill: INK }); const ck = check(sv, 38, 40, 1.15, LIME, 6); ck.setAttribute('stroke-dasharray', 60); ck.setAttribute('stroke-dashoffset', 60);
        sc.picin.appendChild(e);
        sc.u.push(t => { const p = P(t, at, at + .36); e.style.opacity = p > 0 ? 1 : 0; e.style.transform = `translateX(${(1 - eOut(p)) * 120}px) scale(${.85 + .15 * Math.max(0, eBack(p))})`; ck.setAttribute('stroke-dashoffset', 60 * (1 - eOut(P(t, at + .2, at + .5)))); });
      };
      card(190, 'ORDER CONFIRMED', 'Cake x1 · Rs. 2,500', tOrder, LIME); card(284, 'BOOKED · 4 PM', 'Kal, Haircut', tAppt, '#ffd166');
      const bot = Bot(S(g, 'g'));
      sc.u.push(t => {
        const tp = P(t, X.wt(2), X.we(3) + .1), proc = t >= X.wt(0) && t < tReply + .4, done = t >= tOrder;
        tf(tm, 484, 100, 0, Math.max(0, eBack(P(t, X.wt(1), X.wt(1) + .3))));
        arc.setAttribute('stroke-dashoffset', C * (1 - eIO(tp))); tt.textContent = '0:0' + Math.min(3, Math.floor(eIO(tp) * 3.0 + .05));
        const dp = t >= tReply - .6 && t < tReply; dots.style.opacity = dp ? 1 : 0; di.forEach((d, i) => d.style.transform = `translateY(${-6 * Math.max(0, Math.sin(t * 11 - i))}px)`);
        bot.pose({ x: 486, y: 580, s: .72, mood: done ? 'happy' : (X.wt(1) <= t ? 'open' : 'wow'), blink: (Math.sin(t * 2.5) > .97 ? 1 : 0), ant: t, armL: proc ? 38 + 30 * Math.sin(t * 14) : 8, armR: proc ? -38 - 30 * Math.sin(t * 14 + 2) : -8, bob: Math.sin(t * 3) * 3, glow: proc ? .8 : 0 });
      });
      sparks(sc, g, { x: 484, y: 380, at: tOrder, n: 10, r: 80 }); sparks(sc, g, { x: 484, y: 380, at: tAppt, n: 10, r: 80, cols: ['#ffd166', INK] });
      X.sfx(X.t0 + .2, 'ding'); X.sfx(X.wt(2), 'tick'); X.sfx(X.wt(2) + .35, 'tick'); X.sfx(X.wt(3) + .1, 'tick'); X.sfx(tReply, 'ding'); X.sfx(tOrder, 'success'); X.sfx(tAppt, 'success');
      X.punch(tOrder); X.punch(tAppt);
    }
  });

  // ---- 4: team 8 hours vs AI 24 hours --------------------------------------------------------------------
  SP.push({
    line: 4, bg: '#f4f4ee',
    rows: [['Aapki team', 62, 'white'], ['aath ghante', 92, 'red'], ['kaam karti hai.', 54, 'white'], ['AI chaubees ghante.', 64, 'lime']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      const W = 560, X0 = 40;
      const row = (y, label, col, tx) => {
        T(g, label, X0, y, 30, INK, 'start');
        S(g, 'rect', { x: X0, y: y + 22, width: W, height: 84, rx: 42, fill: '#e1e1d6', stroke: INK, 'stroke-width': 5 });
        const f = S(g, 'rect', { x: X0 + 6, y: y + 28, width: 4, height: 72, rx: 36, fill: col });
        const n = T(g, tx, X0 + 30, y + 80, 40, INK, 'start');
        return { f, n };
      };
      const A = row(30, 'AAPKI TEAM', COL.red, '0h'); const B = row(250, 'AI AUTOMATION', LIME, '0h');
      // tick labels
      ['12 AM', '6 AM', '12 PM', '6 PM', '12 AM'].forEach((s, i) => T(g, s, X0 + W * i / 4, 410, 15, '#6b6b60', i === 0 ? 'start' : i === 4 ? 'end' : 'middle', 'Inter'));
      for (let i = 0; i <= 24; i++) S(g, 'line', { x1: X0 + W * i / 24, y1: 424, x2: X0 + W * i / 24, y2: i % 6 ? 436 : 446, stroke: '#6b6b60', 'stroke-width': i % 6 ? 2 : 4 });
      const sunE = S(g, 'g'); const sunD = S(sunE, 'circle', { r: 20, fill: '#ffd24a', stroke: INK, 'stroke-width': 4 });
      const x3 = H('div', 'h', `position:absolute;left:380px;top:462px;font-size:72px;color:${INK};background:${LIME};border:6px solid ${INK};border-radius:22px;padding:4px 22px;box-shadow:0 8px 0 ${INK};opacity:0;transform-origin:50% 50%`, '3X HOURS'); x3.style.fontSize = '46px'; x3.style.left = '170px'; x3.style.top = '500px'; sc.picin.appendChild(x3);
      const cpath = S(g, 'clipPath', { id: 'cl4' }); const cp = S(cpath, 'rect', { x: X0 + 6, y: 278, width: 10, height: 72, rx: 36 }); const sgo = S(g, 'g', { 'clip-path': 'url(#cl4)' }); const sg = S(sgo, 'g');
      for (let i = 0; i < 14; i++) S(sg, 'path', { d: `M${X0 + i * 44} 350 l30 -72 h18 l-30 72z`, fill: '#9bd11f' });
      const mb = Bot(S(g, 'g'));
      const sA0 = X.wt(2), sA1 = X.we(3) + .1, sB0 = X.wt(8), sB1 = X.we(9) + .15;
      sc.u.push(t => {
        const pa = eOut(P(t, sA0, sA1)), pb = eOut(P(t, sB0, sB1)), wa = 4 + (W - 12) * (8 / 24) * pa, wb = 4 + (W - 12) * pb;
        A.f.setAttribute('width', wa); B.f.setAttribute('width', wb); cp.setAttribute('width', wb);
        A.n.textContent = Math.round(8 * pa) + 'h'; B.n.textContent = Math.round(24 * pb) + 'h';
        sg.style.transform = `translateX(${(t * 40) % 44}px)`;
        const pAll = Math.max(pa * 8 / 24, pb); tf(sunE, X0 + W * (pb > 0 ? pb : pa * 8 / 24), 468); sunE.style.opacity = (pa > 0 || pb > 0) ? 1 : 0;
        const xp = P(t, X.we(9), X.we(9) + .3); x3.style.opacity = xp > 0 ? 1 : 0; x3.style.transform = `rotate(${-6 + Math.sin(t * 5) * 2}deg) scale(${Math.max(0, eBack(xp))})`;
        mb.pose({ x: 560, y: 218, s: .32, mood: pb > .98 ? 'happy' : 'open', ant: t, blink: Math.sin(t * 2.7) > .97 ? 1 : 0, armL: 10, armR: -10 });
      });
      confetti(sc, g, { x: 330, y: 500, at: X.we(9) + .1, n: 22, a0: -120, a1: -60, v0: 500, v1: 800, seed: 9 });
      X.sfx(sA0, 'tick'); X.sfx(sA0 + .22, 'tick'); X.sfx(sB0, 'zap'); X.sfx(X.we(9) + .08, 'success'); X.punch(sA0); X.punch(sB0); X.punch(X.we(9));
    }
  });

  // ---- 5: na chhutti, na late reply, na lead miss ---------------------------------------------------------
  SP.push({
    line: 5, bg: 'radial-gradient(circle at 50% 35%,#1c2a0b 0%,#0b0d09 78%)',
    rows: [['Na chhutti,', 84, 'white'], ['na late reply,', 84, 'white'], ['na koi lead miss.', 72, 'lime']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      const items = [['CHHUTTI', 'Koi off day nahi', X.wt(1) - .05, X.wt(1)], ['LATE REPLY', 'Jawab seconds mein', X.wt(3) - .05, X.wt(3)], ['LEAD MISS', 'Har message milta hai', X.wt(7) - .05, X.wt(7)]];
      const els = items.map((it, i) => {
        const y = 22 + i * 190, e = H('div', 'ui', `left:26px;top:${y}px;width:588px;height:164px;border-radius:28px;background:#162008;border:5px solid ${LIME};opacity:0;transform-origin:0% 50%;box-shadow:0 8px 0 rgba(198,255,53,.25)`,
          `<div class="h" style="position:absolute;left:190px;top:34px;font-size:46px;color:#fff">${it[0]}</div><div style="position:absolute;left:190px;top:98px;font-weight:700;font-size:23px;color:#9aa58a">${it[1]}</div>`);
        const sv = svgRoot(e, 170, 154, 'left:0;top:0'); const c = S(sv, 'circle', { cx: 92, cy: 77, r: 62, fill: LIME, stroke: INK, 'stroke-width': 5 }); const z = T(sv, '0', 92, 108, 96, INK);
        sc.picin.appendChild(e); return { e, z, it, c };
      });
      els.forEach((o, i) => {
        sc.u.push(t => {
          const p = P(t, o.it[2], o.it[2] + .34), zp = P(t, o.it[3], o.it[3] + .25);
          o.e.style.opacity = p > 0 ? 1 : 0; o.e.style.transform = `translateX(${(1 - eOut(p)) * -160}px) scale(${.9 + .1 * Math.max(0, eBack(p))})`;
          o.z.style.transformOrigin = '92px 78px'; o.z.style.transform = `scale(${t >= o.it[3] ? 1 + .5 * Math.sin(Math.PI * zp) : 1})`;
          o.z.textContent = '0';
        });
        sparks(sc, g, { x: 118, y: 100 + i * 190, at: o.it[3], n: 10, r: 80 });
        X.sfx(o.it[2], 'pop'); X.sfx(o.it[3], 'stamp'); X.punch(o.it[3]);
      });
    }
  });

  // ---- 6: same night, same customer -> now the sale is yours -----------------------------------------------
  SP.push({
    line: 6, bg: 'linear-gradient(180deg,#0d1536 0%,#1c2a63 70%,#243473 100%)',
    rows: [['Wahi customer,', 64, 'white'], ['wahi raat.', 84, 'white'], ['Bas ab sale', 88, 'lime'], ['aapki hoti hai.', 60, 'white']],
    build(sc, X) {
      const room = bedroom(sc, X, { smile: true });
      const g = svgRoot(sc.picin, 640, 600);
      const k = { clockAt: X.t0 + .15, buzzAt: X.wt(1), glowAt: X.wt(1), badgeAt: 9999, zAt: X.wt(3), badgeN: () => 1 };
      bub(sc, X, { x: 300, y: 104, w: 260, text: 'Order karna hai', label: 'WHATSAPP · CUSTOMER', at: X.wt(1) });
      bub(sc, X, { x: 318, y: 196, w: 290, text: 'Order confirm! Kal 4 PM.', label: 'AI REPLY · 3 SEC', at: X.wt(3) + .2, who: 'r', lc: '#128c7e' });
      const mb = Bot(S(g, 'g'));
      const st = stamp(sc, X, { x: 120, y: 280, text: 'SALE  Rs. 4,500', fg: INK, bg: LIME, rot: -7, at: X.wt(6) - .02, size: 40 });
      const hearts = [0, 1, 2].map(i => { const h = heart(g, 0, 0, 1.4, COL.red); h.style.opacity = 0; return h; });
      sc.u.push(t => {
        room.upd(t, k);
        mb.pose({ x: 556, y: 446, s: .3, mood: t > X.wt(6) ? 'happy' : 'open', ant: t, blink: Math.sin(t * 2.7) > .97 ? 1 : 0, armL: 30 + 20 * Math.sin(t * 12), armR: -30 - 20 * Math.sin(t * 12 + 1) });
        hearts.forEach((h, i) => { const d = t - (X.wt(7) + i * .3); if (d < 0) { h.style.opacity = 0; return; } const c = (d % 1.5) / 1.5; h.style.opacity = Math.sin(Math.PI * c); tf(h, 126 + i * 24, 330 - c * 90, 0, 1 + c * .5); });
      });
      confetti(sc, g, { x: 320, y: 330, at: X.wt(6), n: 34, a0: -140, a1: -40, v0: 600, v1: 1000, seed: 5 });
      sparks(sc, g, { x: 430, y: 340, at: X.wt(6), n: 14, r: 120, cols: [LIME, '#ffd24a'] });
      X.sfx(X.t0 + .15, 'pop'); X.sfx(X.wt(1), 'buzz'); X.sfx(X.wt(1) + .02, 'ding'); X.sfx(X.wt(3) + .2, 'ding'); X.sfx(X.wt(6) - .02, 'coin'); X.sfx(X.wt(6) + .1, 'success'); X.punch(X.wt(6)); X.shake(X.wt(6));
    }
  });

  // ---- 7: CTA -----------------------------------------------------------------------------------------------
  SP.push({
    line: 7, bg: 'radial-gradient(circle at 50% 38%,#24400b 0%,#0b0d09 76%)', note: false,
    rows: [['Apne business ke liye', 48, 'white'], ['AI automation chahiye?', 54, 'white'], ['Comment AUTOMATE,', 72, 'lime'], ['hum aapko DM kar denge.', 46, 'white']],
    build(sc, X) {
      const g = svgRoot(sc.picin, 640, 600);
      const kw = H('div', 'ui', `left:50px;top:70px;width:540px;height:112px;border-radius:28px;background:#fff;border:6px solid ${INK};box-shadow:0 10px 0 ${INK};padding:0 24px;opacity:0;transform-origin:50% 50%`,
        `<div style="position:absolute;left:24px;top:12px;font-weight:800;font-size:16px;letter-spacing:2px;color:#6b6b60">ADD A COMMENT</div><div class="h" id="kwt" style="position:absolute;left:24px;top:40px;font-size:52px;color:${INK}"></div>`);
      sc.picin.appendChild(kw); const kt = kw.querySelector('#kwt');
      const btn = H('div', 'h', `position:absolute;left:402px;top:230px;width:188px;height:70px;border-radius:35px;background:${LIME};color:${INK};font-size:30px;line-height:70px;text-align:center;opacity:0;box-shadow:0 7px 0 rgba(198,255,53,.3)`, 'POST'); sc.picin.appendChild(btn);
      const word = 'AUTOMATE', kws = X.wt(8), post = kws + .75;
      const bot = Bot(S(g, 'g'));
      const logo = H('div', 'ui', `left:40px;top:500px;display:flex;align-items:center;gap:14px;opacity:0`, `<img src="logo.png" style="width:56px;height:56px;border-radius:50%;border:4px solid ${LIME}"><div><div class="h" style="font-size:24px;color:#fff">THE TOTAL FORGE</div><div style="font-weight:800;font-size:17px;color:#c6ff35">thetotalforge.com</div></div>`); sc.picin.appendChild(logo);
      const cur = S(g, 'g', null, 'opacity:0'); S(cur, 'path', { d: 'M4 2l24 14-10 3-5 11z', fill: '#fff', stroke: INK, 'stroke-width': 3, 'stroke-linejoin': 'round', transform: 'scale(1.6)' });
      const hs = [0, 1, 2, 3, 4, 5].map(i => { const h = heart(g, 0, 0, 1.5, COL.red); h.style.opacity = 0; return h; }); const R = rng(8);
      const hx = hs.map(() => 40 + R() * 560);
      sc.u.push(t => {
        const kp = P(t, X.wt(7) - .05, X.wt(7) + .3); kw.style.opacity = kp > 0 ? 1 : 0; kw.style.transform = `scale(${Math.max(0, eBack(kp))}) rotate(${(1 - eOut(kp)) * -4}deg)`;
        const n = Math.max(0, Math.min(word.length, Math.floor((t - kws) / .075))); kt.textContent = (t >= kws ? word.slice(0, n) : '') + ((t >= X.wt(7) && t < post && Math.sin(t * 10) > 0) ? '|' : '');
        const bp = P(t, kws + .3, kws + .6); btn.style.opacity = bp > 0 ? 1 : 0; btn.style.transform = `scale(${Math.max(0, eBack(bp)) * (t >= post && t < post + .15 ? .88 : 1)})`;
        const a0 = post - .6, cp = eIO(P(t, a0, post - .03)); cur.style.opacity = t > a0 - .1 && t < post + .6 ? 1 : 0; tf(cur, lerp(560, 480, cp), lerp(420, 262, cp) - Math.sin(cp * Math.PI) * 40, 0, 1);
        const wv = t >= X.wt(9);
        bot.pose({ x: 470, y: 590, s: .86, mood: 'happy', ant: t, blink: 0, armL: 8, armR: wv ? -150 + 24 * Math.sin(t * 9) : -10, bob: Math.sin(t * 3) * 3 });
        const lp = P(t, X.wt(9), X.wt(9) + .35); logo.style.opacity = lp > 0 ? 1 : 0; logo.style.transform = `translateY(${(1 - eOut(lp)) * 40}px)`;
        hs.forEach((h, i) => { const d = t - (post + .05 + i * .18); if (d < 0) { h.style.opacity = 0; return; } const c = (d % 2) / 2; h.style.opacity = Math.sin(Math.PI * c); tf(h, hx[i], 560 - c * 420, Math.sin(d * 3 + i) * 12, 1 + c * .6); });
      });
      sparks(sc, g, { x: 496, y: 265, at: post, n: 14, r: 110, cols: [LIME, '#fff'] });
      confetti(sc, g, { x: 496, y: 265, at: post + .05, n: 28, a0: -150, a1: -30, v0: 500, v1: 900, seed: 12 });
      X.sfx(X.wt(7), 'pop'); for (let i = 0; i < 8; i++) X.sfx(kws + i * .075, 'type'); X.sfx(post, 'success'); X.punch(post); X.shake(post);
    }
  });

  window.SCENE_SPECS = SP;
})();
