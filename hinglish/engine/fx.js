/* Motion-graphics layer for the reel engine. Pure function of time: FX.init(scenes,H) once, FX.frame(t,scenes,si) per draw.
   Adds: scene-wipe transitions, progress bar, camera push/punch/shake, drifting shapes + glow + moving grid, emoji stickers with
   pop bursts, spark bursts, confetti cannons, sunburst, marquee bands, hub ring, title marker, row slide/flash, typing dots,
   CTA cursor / hearts stream. Everything is optional per episode through EP.emo = {hook,pain,mess,tips:[3],res}. */
window.FX = (function () {
  const NS = 'http://www.w3.org/2000/svg';
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const prog = (t, a, b) => clamp((t - a) / (b - a));
  const eOut = x => 1 - Math.pow(1 - x, 3);
  const eIn = x => x * x * x;
  const eIO = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const eBack = x => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
  const mk = (tag, cls, css, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (css) e.style.cssText = css; if (html != null) e.innerHTML = html; return e; };
  const rng = seed => { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; };
  const COL = { lime: '#c6ff35', ink: '#0b0d09', red: '#ff4b3a', white: '#ffffff', amber: '#ffd166', cyan: '#00e5ff' };
  const BGS = ['dark', 'white', 'red', 'cream', 'limebg'];
  const bgOf = sc => BGS.find(c => sc.el.classList.contains(c)) || 'dark';
  const PAL = {
    dark:  { a: 'rgba(198,255,53,.5)',  b: 'rgba(255,255,255,.22)', blob: 'rgba(198,255,53,.14)' },
    white: { a: 'rgba(11,13,9,.15)',    b: '#c6ff35',               blob: 'rgba(198,255,53,.38)' },
    cream: { a: 'rgba(11,13,9,.14)',    b: '#c6ff35',               blob: 'rgba(198,255,53,.40)' },
    red:   { a: 'rgba(255,255,255,.34)', b: 'rgba(11,13,9,.26)',    blob: 'rgba(255,200,120,.24)' },
    limebg:{ a: 'rgba(11,13,9,.20)',    b: 'rgba(255,255,255,.55)', blob: 'rgba(255,255,255,.30)' }
  };
  let trEl, slats = [], pbFill, pbWrap, STATE = {};

  const CSS = `
@font-face{font-family:NCE;src:url(fonts/noto-color-emoji-sub.woff2)}
.fxl{position:absolute;left:0;top:0;width:720px;height:1280px;pointer-events:none;overflow:hidden}
.emo{font-family:NCE,"Noto Color Emoji",sans-serif;line-height:1}
.dark:before{background-position:var(--gx,0px) var(--gy,0px),var(--gx,0px) var(--gy,0px)}
.dark .w[data-glow="lime"]{text-shadow:0 0 28px rgba(198,255,53,.45)}
.dark .w[data-glow="red"]{text-shadow:0 0 22px rgba(255,75,58,.5)}
`;

  // ---------------------------------------------------------------- small builders
  function shape(k, s, c) {
    const css = `position:absolute;left:0;top:0;width:${s}px;height:${s}px;`;
    const bw = Math.max(3, s / 10);
    if (k === 'ring') return mk('div', '', css + `border:${bw}px solid ${c};border-radius:50%`);
    if (k === 'dot') return mk('div', '', css + `width:${s * .45}px;height:${s * .45}px;border-radius:50%;background:${c}`);
    if (k === 'sq') return mk('div', '', css + `border:${bw}px solid ${c};border-radius:${s * .18}px`);
    if (k === 'plus') return mk('div', '', css, `<svg width="${s}" height="${s}" viewBox="0 0 20 20"><rect x="8" y="1" width="4" height="18" rx="2" fill="${c}"/><rect x="1" y="8" width="18" height="4" rx="2" fill="${c}"/></svg>`);
    return mk('div', '', css, `<svg width="${s}" height="${s}" viewBox="0 0 20 20"><path d="M10 0C11 6 14 9 20 10C14 11 11 14 10 20C9 14 6 11 0 10C6 9 9 6 10 0Z" fill="${c}"/></svg>`);
  }

  function ambient(sc) {
    const bg = bgOf(sc), P = PAL[bg];
    const layer = mk('div', 'fxl'); sc.el.insertBefore(layer, sc.el.firstChild); sc.fxLayer = layer;
    const R = rng(sc.line * 977 + 13);
    const blob = mk('div', '', `position:absolute;left:0;top:0;width:780px;height:780px;border-radius:50%;background:radial-gradient(circle,${P.blob} 0%,rgba(0,0,0,0) 62%)`);
    layer.appendChild(blob);
    const sh = [];
    ['ring', 'plus', 'dot', 'sq', 'spark', 'ring', 'plus', 'dot', 'spark', 'sq', 'dot', 'spark'].forEach((k, i) => {
      const size = 18 + R() * 36, outline = k === 'ring' || k === 'sq', e = shape(k, size, (!outline && i % 3 === 0) ? P.b : P.a);
      layer.appendChild(e);
      sh.push({ e, k, x0: R() * 720, y0: R() * 1500, vy: 16 + R() * 30, amp: 12 + R() * 26, ph: R() * 6.28, rs: (R() - .5) * 70 });
    });
    sc.fxu.push(t => {
      blob.style.transform = `translate(${-30 + Math.sin(t * .42 + sc.line) * 210}px,${250 + Math.cos(t * .33 + sc.line * 2) * 260}px)`;
      sh.forEach(s => {
        const y = (((s.y0 - s.vy * t) % 1500) + 1500) % 1500 - 110, x = s.x0 + Math.sin(t * .7 + s.ph) * s.amp;
        const sp = s.k === 'spark' ? (.7 + .5 * Math.sin(t * 2.4 + s.ph)) : 1;
        s.e.style.transform = `translate(${x}px,${y}px) rotate(${s.rs * t}deg) scale(${sp})`;
      });
      if (bg === 'dark') { sc.el.style.setProperty('--gy', (t * 16 % 60) + 'px'); sc.el.style.setProperty('--gx', (t * 9 % 60) + 'px'); }
    });
  }

  // emoji sticker: white badge + hard shadow, pops with overshoot, pop-burst lines, idle bob
  function sticker(sc, o) {
    const S = o.s || 84, B = Math.round(S * 1.55), dark = bgOf(sc) === 'dark', ph = o.ph || 0;
    const w = mk('div', '', `position:absolute;left:${o.x - B / 2}px;top:${o.y - B / 2}px;width:${B}px;height:${B}px;opacity:0;z-index:20`);
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('width', B); svg.setAttribute('height', B); svg.style.cssText = 'position:absolute;left:0;top:0;overflow:visible';
    const lines = [];
    for (let i = 0; i < 8; i++) { const l = document.createElementNS(NS, 'line'); l.setAttribute('stroke', o.lc || (dark ? COL.lime : COL.ink)); l.setAttribute('stroke-width', 5); l.setAttribute('stroke-linecap', 'round'); svg.appendChild(l); lines.push(l); }
    const badge = mk('div', '', `position:absolute;left:${B * .08}px;top:${B * .08}px;width:${B * .84}px;height:${B * .84}px;border-radius:50%;background:#fff;border:5px solid ${COL.ink};box-shadow:0 7px 0 ${dark ? COL.lime : COL.ink}`);
    const em = mk('div', 'emo', `position:absolute;left:0;top:${B * .02}px;width:${B}px;height:${B}px;line-height:${B}px;text-align:center;font-size:${S}px`, o.e);
    w.appendChild(svg); w.appendChild(badge); w.appendChild(em); (o.parent || sc.el).appendChild(w);
    sc.fxu.push(t => {
      if (t < o.at) { w.style.opacity = 0; return; }
      const d = t - o.at, p = prog(t, o.at, o.at + .36), bp = prog(t, o.at, o.at + .5), eb = eBack(p);
      w.style.opacity = o.out != null ? 1 - prog(t, o.out, o.out + .2) : 1;
      w.style.transform = `translate(0,${Math.sin(d * 3.1 + ph) * 5}px) rotate(${(o.r || 0) + Math.sin(d * 2.3 + ph) * 6}deg) scale(${Math.max(0, eb)})`;
      lines.forEach((l, i) => {
        const a = i * Math.PI / 4 + .2, r1 = B * .56 + 30 * eOut(bp), len = 22 * Math.sin(Math.PI * Math.min(1, bp * 1.2)), r2 = r1 + len, c = B / 2;
        l.setAttribute('x1', c + Math.cos(a) * r1); l.setAttribute('y1', c + Math.sin(a) * r1); l.setAttribute('x2', c + Math.cos(a) * r2); l.setAttribute('y2', c + Math.sin(a) * r2);
        l.style.opacity = bp >= 1 ? 0 : 1;
      });
    });
  }

  function sparks(sc, o) {
    const n = o.n || 10, els = [], R = rng(Math.floor(o.x * 7 + o.y * 3 + o.at * 100));
    const cols = o.cols || [COL.lime];
    for (let i = 0; i < n; i++) {
      const s = 10 + R() * 14, e = shape(i % 2 ? 'spark' : 'dot', s * (i % 2 ? 1.2 : 1), cols[i % cols.length]);
      e.style.opacity = 0; e.style.zIndex = 15; sc.el.appendChild(e);
      els.push({ e, a: i / n * 6.283 + R() * .5, v: (o.r || 90) * (.6 + R() * .7), s });
    }
    sc.fxu.push(t => {
      const p = prog(t, o.at, o.at + .6);
      els.forEach(q => {
        if (t < o.at || p >= 1) { q.e.style.opacity = 0; return; }
        const r = q.v * eOut(p);
        q.e.style.opacity = 1 - p * p;
        q.e.style.transform = `translate(${o.x + Math.cos(q.a) * r - q.s / 2}px,${o.y + Math.sin(q.a) * r - q.s / 2}px) rotate(${p * 180}deg) scale(${1 - .5 * p})`;
      });
    });
  }

  function ring(sc, o) { // expanding outline pulse. o:{x,y,r0,r1,at,col,w,loop,dur}
    const e = mk('div', '', `position:absolute;left:0;top:0;border-radius:50%;opacity:0;z-index:12;border:${o.w || 6}px solid ${o.col || COL.lime}`);
    sc.el.appendChild(e);
    sc.fxu.push(t => {
      if (t < o.at) { e.style.opacity = 0; return; }
      const dur = o.dur || .6, d = o.loop ? ((t - o.at) % o.loop) : (t - o.at), p = prog(d, 0, dur);
      if (p >= 1) { e.style.opacity = 0; return; }
      const r = o.r0 + (o.r1 - o.r0) * eOut(p);
      e.style.opacity = .9 * (1 - p); e.style.width = e.style.height = (r * 2) + 'px';
      e.style.transform = `translate(${o.x - r}px,${o.y - r}px)`;
    });
  }

  function confetti(sc, o) { // cannon from (x,y). o:{x,y,at,n,ang:[a0,a1] degrees (0=right, -90=up),sp:[min,max],seed}
    const n = o.n || 30, R = rng(o.seed || 7), cols = [COL.lime, COL.white, COL.red, COL.amber, COL.cyan], ps = [];
    for (let i = 0; i < n; i++) {
      const w = 9 + R() * 6, h = 16 + R() * 10, e = mk('div', '', `position:absolute;left:0;top:0;width:${w}px;height:${h}px;border-radius:2px;background:${cols[Math.floor(R() * cols.length)]};opacity:0;z-index:30`);
      sc.el.appendChild(e);
      const a = (o.ang[0] + R() * (o.ang[1] - o.ang[0])) * Math.PI / 180, v = o.sp[0] + R() * (o.sp[1] - o.sp[0]);
      ps.push({ e, vx: Math.cos(a) * v, vy: Math.sin(a) * v, rs: (R() - .5) * 900, fl: 6 + R() * 8, ph: R() * 6.28, dl: R() * .12 });
    }
    sc.fxu.push(t => {
      ps.forEach(p => {
        const d = t - o.at - p.dl;
        if (d < 0 || d > 2.6) { p.e.style.opacity = 0; return; }
        const k = .8, f = (1 - Math.exp(-k * d)) / k, x = o.x + p.vx * f + Math.sin(d * 5 + p.ph) * 12, y = o.y + p.vy * f + .5 * 1150 * d * d;
        p.e.style.opacity = d > 2.1 ? (2.6 - d) / .5 : 1;
        p.e.style.transform = `translate(${x}px,${y}px) rotate(${p.rs * d}deg) scaleY(${Math.abs(Math.cos(d * p.fl + p.ph)) * .8 + .2})`;
      });
    });
  }

  function band(sc, o) { // scrolling marquee band. o:{top,rot,text,bg,fg,dir,at,h,size,speed}
    const h = o.h || 66, txt = (o.text + '  ★  ').repeat(10);
    const wrap = mk('div', '', `position:absolute;left:-60px;top:${o.top}px;width:840px;height:${h}px;overflow:hidden;background:${o.bg};border-radius:8px;z-index:6;opacity:0`);
    const inner = mk('div', 'h', `position:absolute;left:0;top:0;height:${h}px;line-height:${h}px;white-space:nowrap;font-size:${o.size || 40}px;color:${o.fg};letter-spacing:1px`, txt);
    wrap.appendChild(inner); sc.el.appendChild(wrap);
    sc.fxu.push(t => {
      const p = prog(t, o.at, o.at + .45), eb = eOut(p);
      wrap.style.opacity = t >= o.at ? 1 : 0;
      wrap.style.transform = `translateX(${(o.dir > 0 ? -1 : 1) * 900 * (1 - eb)}px) rotate(${o.rot}deg)`;
      const sh = (t * (o.speed || 150)) % 760; inner.style.transform = `translateX(${o.dir > 0 ? -sh : sh - 760}px)`;
    });
  }

  function rays(sc, o) { // rotating sunburst behind content
    const e = mk('div', '', `position:absolute;left:${o.x - 750}px;top:${o.y - 750}px;width:1500px;height:1500px;background:repeating-conic-gradient(${o.c1} 0deg ${o.w}deg,${o.c2} ${o.w}deg ${o.w * 2}deg);opacity:0`);
    sc.el.insertBefore(e, sc.el.children[1]);
    sc.fxu.push(t => { e.style.opacity = prog(t, sc.t0, sc.t0 + .6); e.style.transform = `rotate(${(t - sc.t0) * (o.sp || 7)}deg)`; });
  }

  // ---------------------------------------------------------------- per-role decorations
  function defaults(EP) { const e = EP.emo || {}; return { hook: e.hook || '👀', pain: e.pain || '😬', mess: e.mess || '💀', tips: e.tips || ['💡', '✅', '🚀'], res: e.res || '🎉' }; }

  function decoHook(sc, H, E) {
    sc.glitch = true;
    const r = H.EP.hook.rows, last = r[r.length - 1].r[0];
    sticker(sc, { e: E.hook, x: 360, y: 925, s: 124, r: -6, at: H.wt(0, Math.min(2, H.W[0].length - 1)) + .1 });
    sticker(sc, { e: '✨', x: 604, y: 214, s: 56, r: 12, at: H.wt(0, last) + .1, ph: 1.6 });
  }

  function decoPain(sc, H, E) {
    const p = H.EP.pain, ss = H.wt(1, p.stamp.at);
    sc.punches.push(ss); sc.shakes.push(ss);
    ring(sc, { x: 360, y: 520, r0: 120, r1: 420, at: ss, col: COL.red, w: 8, dur: .5 });
    const pl = p.pile;   // optional: {at:[word idx..], closeAt, hlAt, secAt, sec} -> pile of copies, first-line highlight, timer chip, "tab closed" vanish
    sc.lazy.push(() => {
      const b = sc.el.querySelector('.bub.cust'); if (!b) return;
      sticker(sc, { e: E.pain, x: b.offsetLeft + b.offsetWidth - 10, y: b.offsetTop + b.offsetHeight + 2, s: 46, r: 12, at: H.wt(1, p.bubble.at) + .55, out: pl ? H.wt(1, pl.closeAt) + .05 : undefined });
      if (!pl) return;
      const rots = [-2, 1.8, -1.4, 2.2, -1.8, 1.4], dxs = [26, -12, 34, 4, -18, 22], gap = Math.round(b.offsetHeight * .8);
      const clones0 = [];
      const clones = pl.at.map((w, k) => {
        const c = b.cloneNode(true); c.dataset.clone = 1;
        c.style.left = (b.offsetLeft + dxs[k % 6]) + 'px'; c.style.top = (b.offsetTop + gap * (k + 1)) + 'px'; c.style.zIndex = '';
        (clones0.length ? clones0[clones0.length - 1] : b).after(c); clones0.push(c); return c;
      });
      const cs = H.wt(1, pl.closeAt), hs = H.wt(1, pl.hlAt), ts = H.wt(1, pl.secAt);
      const chip = mk('div', 'h', 'position:absolute;left:60px;top:850px;opacity:0;background:#0b0d09;color:#c6ff35;border-radius:30px;padding:14px 28px;font-size:36px;display:flex;gap:14px;align-items:center;z-index:3',
        `<span class="emo" style="font-size:38px">${pl.emo || '⏱️'}</span><span>${pl.sec || '2 SEC'}</span>`);
      sc.el.appendChild(chip);
      sticker(sc, { e: '❌', x: 360, y: b.offsetTop + gap * 2, s: 92, r: -8, at: cs + .05, out: cs + 1.3 });
      sc.fxu.push(t => {
        clones.forEach((c, k) => {
          const s = H.wt(1, pl.at[k]), q = prog(t, s, s + .26), qo = prog(t, cs + (k + 1) * .05, cs + (k + 1) * .05 + .3);
          c.style.opacity = t >= s ? 1 - qo : 0;
          c.style.transform = `rotate(${rots[k % 6]}deg) scale(${(1.3 - .3 * eBack(q)) * (1 - .35 * eIn(qo))})`;
        });
        const qo = prog(t, cs, cs + .3);
        if (qo > 0) { b.style.opacity = 1 - qo; b.style.transform = `scale(${1 - .35 * eIn(qo)})`; }
        const hq = prog(t, hs, hs + .18) * (1 - prog(t, hs + .8, hs + 1.1));
        b.style.boxShadow = hq > 0 ? `0 0 0 ${3 * hq}px #0b0d09, 0 0 0 ${10 * hq}px #c6ff35` : '';
        chip.style.opacity = t >= ts ? 1 : 0; chip.style.transform = `scale(${1.3 - .3 * eBack(prog(t, ts, ts + .26))}) rotate(${-3 * (1 - prog(t, ts, ts + .3))}deg)`;
      });
    });
  }

  function decoMess(sc, H, E) {
    const m = H.EP.mess, c2 = m.chips[m.chips.length - 1].at;
    sticker(sc, { e: E.mess, x: 628, y: 172, s: 84, r: 8, at: H.wt(2, c2) + .15 });
    sc.punches.push(H.wt(2, m.subAt));
    sc.lazy.push(() => { const dots = [...sc.el.querySelectorAll('.mini i')]; sc.fxu.push(t => dots.forEach((d, i) => { d.style.transform = `scale(${1.15 + .45 * Math.sin(t * 6 + i * 1.3)})`; d.style.background = i % 2 ? '#ff4b3a' : '#ffb020'; })); });
  }

  function decoBridge(sc, H) {
    const B = H.EP.bridge, k = B.items[1].toks[0][0], tk = H.wt(3, k);
    rays(sc, { x: 360, y: 450, c1: 'rgba(11,13,9,.085)', c2: 'rgba(11,13,9,0)', w: 9, sp: 9 });
    ring(sc, { x: 360, y: 450, r0: 110, r1: 520, at: tk, col: COL.ink, w: 10, dur: .55 });
    ring(sc, { x: 360, y: 450, r0: 90, r1: 400, at: tk + .12, col: '#fff', w: 8, dur: .5 });
    sc.punches.push(tk); sc.shakes.push(tk);
    sticker(sc, { e: '⚡', x: 612, y: 330, s: 84, r: 12, at: tk + .08 });
    sticker(sc, { e: '👇', x: 124, y: 430, s: 64, r: -10, at: H.wt(3, k + 1) + .1, ph: 2 });
    band(sc, { top: 812, rot: -3, text: (H.EP.bands || [])[0] || 'SAVE THIS REEL', bg: COL.ink, fg: COL.lime, dir: 1, at: sc.t0 + .25 });
    band(sc, { top: 1016, rot: 3, text: (H.EP.bands || [])[1] || '3 TIPS ★ NO FLUFF', bg: '#fff', fg: COL.ink, dir: -1, at: sc.t0 + .35, h: 58, size: 34 });
  }

  function decoTip(sc, H, E, k) {
    const b = sc._b, line = sc.line, dark = bgOf(sc) === 'dark', ts = H.wt(line, b.titleAt);
    sc.punches.push(ts);
    const gh = mk('div', 'h', `position:absolute;left:0;top:520px;width:720px;text-align:center;font-size:600px;line-height:1;color:${dark ? 'rgba(198,255,53,.07)' : 'rgba(11,13,9,.045)'};opacity:0`, String(k + 1));
    sc.el.insertBefore(gh, sc.el.children[1]);
    sc.fxu.push(t => { const p = prog(t, sc.t0 + .1, sc.t0 + .6); gh.style.opacity = p; gh.style.transform = `translateY(${(1 - eOut(p)) * 80}px) rotate(${Math.sin(t * .8 + k) * 2.5}deg) scale(${.82 + .18 * eOut(p)})`; });
    sticker(sc, { e: E.tips[k] || E.tips[0], x: 620, y: 252, s: 58, r: 8, at: ts + .35, ph: k });
    sc.lazy.push(() => {
      const hub = sc.el.querySelector('.hub'), title = sc.el.querySelector('.title');
      // hub spin-in + progress ring
      const sv = document.createElementNS(NS, 'svg'); sv.setAttribute('width', 170); sv.setAttribute('height', 170);
      sv.style.cssText = 'position:absolute;left:14px;top:96px;overflow:visible';
      const C = 2 * Math.PI * 72, col = dark ? COL.lime : COL.ink;
      sv.innerHTML = `<circle cx="85" cy="85" r="72" fill="none" stroke="${col}" stroke-opacity=".16" stroke-width="7"/><circle class="pr" cx="85" cy="85" r="72" fill="none" stroke="${col}" stroke-width="7" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C}" transform="rotate(-90 85 85)"/>`;
      sc.el.appendChild(sv); const pr = sv.querySelector('.pr');
      sc.fxu.push(t => {
        const p = prog(t, sc.t0 + .05, sc.t0 + .5), eb = Math.max(0, eBack(p));
        hub.style.transform = `rotate(${-200 * (1 - eOut(p))}deg) scale(${eb})`;
        sv.style.transform = `scale(${eb})`;
        pr.setAttribute('stroke-dashoffset', C * (1 - prog(t, sc.t0 + .3, sc.t1 - .1)));
      });
      // title marker / underline
      if (title) {
        const L0 = title.offsetLeft - 10, W0 = title.offsetWidth + 20;
        const bar = mk('div', '', `position:absolute;left:${L0}px;top:${dark ? title.offsetTop + title.offsetHeight + 8 : title.offsetTop + 27}px;width:0;height:${dark ? 9 : 32}px;border-radius:${dark ? 5 : 7}px;background:${COL.lime}`);
        sc.el.insertBefore(bar, title);
        sc.fxu.push(t => { bar.style.width = (W0 * eOut(prog(t, ts + .06, ts + .5))) + 'px'; });
      }
      // list rows: slide, flash, bob, chip pop, flip sparks
      const rows = [...sc.el.querySelectorAll('.lrow')];
      if (rows.length && b.demo.type === 'list') {
        b.demo.rows.forEach((r, i) => {
          const el = rows[i]; if (!el) return;
          const s = H.wt(line, r.at), ch = el.querySelector('.ch'), c2 = r.chip2At != null ? H.wt(line, r.chip2At) : null;
          sparks(sc, { x: el.offsetLeft + el.offsetWidth - 60, y: el.offsetTop + 56, at: s + .22, n: 8, r: 80, cols: dark ? [COL.lime, COL.white] : [COL.ink, COL.lime] });
          if (c2 != null) sparks(sc, { x: el.offsetLeft + el.offsetWidth - 70, y: el.offsetTop + 56, at: c2, n: 10, r: 90, cols: dark ? [COL.lime, COL.white] : [COL.ink, COL.lime] });
          sc.fxu.push(t => {
            const p = prog(t, s, s + .4), dx = (i % 2 ? 1 : -1) * 130 * (1 - eBack(p)), bob = Math.sin((t - s) * 2.3 + i * 1.7) * 3 * prog(t, s + .4, s + .8);
            el.style.transform = `translate(${dx}px,${(1 - eOut(p)) * 18 + bob}px) rotate(${(i % 2 ? 1 : -1) * 2.5 * (1 - eOut(p))}deg)`;
            const f = prog(t, s + .08, s + .55), ringW = t >= s ? 16 * (1 - f) : 0;
            el.style.boxShadow = `0 10px 26px rgba(0,0,0,.16),0 0 0 ${ringW}px rgba(198,255,53,${.95 * (1 - f)})`;
            if (ch) { let sc2 = Math.max(0, eBack(prog(t, s + .14, s + .42))); if (c2 != null && t >= c2) sc2 = 1 + .35 * Math.sin(Math.PI * prog(t, c2, c2 + .3)); ch.style.transform = `scale(${sc2})`; }
          });
        });
      }
      // chat: typing dots before each bubble + slide-in
      if (b.demo.type === 'chat') {
        const bs = [...sc.el.querySelectorAll('.bub')];
        b.demo.msgs.forEach((m, i) => {
          const el = bs[i]; if (!el) return;
          const s = H.wt(line, m.at) - (m.pre || 0), cust = m.who === 'c';
          const ty = mk('div', 'bub ' + (cust ? 'cust d' : 'rep'), `top:${el.offsetTop}px;width:120px;height:72px;padding:0;opacity:0`, `<i style="position:absolute;left:30px;top:30px;width:12px;height:12px;border-radius:50%;background:${cust ? '#fff' : COL.ink}"></i><i style="position:absolute;left:54px;top:30px;width:12px;height:12px;border-radius:50%;background:${cust ? '#fff' : COL.ink}"></i><i style="position:absolute;left:78px;top:30px;width:12px;height:12px;border-radius:50%;background:${cust ? '#fff' : COL.ink}"></i>`);
          sc.el.appendChild(ty); const dots = ty.querySelectorAll('i');
          const show = s - .5 >= sc.t0 + .05;
          sc.fxu.push(t => {
            const on = show && t >= s - .5 && t < s;
            ty.style.opacity = on ? 1 : 0;
            if (on) { const pp = eBack(prog(t, s - .5, s - .36)); ty.style.transform = `scale(${Math.max(0, pp)})`; dots.forEach((d, j) => { d.style.transform = `translateY(${-8 * Math.max(0, Math.sin(t * 11 - j * 1.0))}px)`; }); }
            const p = prog(t, s, s + .3);
            el.style.transform = `translate(${(cust ? -46 : 46) * (1 - eOut(p))}px,0) scale(${1.1 - .1 * Math.max(0, eBack(p))})`;
          });
        });
      }
    });
  }

  function decoResult(sc, H, E) {
    const r = H.EP.result, cs = H.wt(7, r.chipAt);
    rays(sc, { x: 360, y: 560, c1: 'rgba(198,255,53,.10)', c2: 'rgba(198,255,53,0)', w: 7, sp: 8 });
    sc.punches.push(cs);
    confetti(sc, { x: 20, y: 1040, at: cs, n: 30, ang: [-80, -55], sp: [1250, 1750], seed: 11 });
    confetti(sc, { x: 700, y: 1040, at: cs, n: 30, ang: [-125, -100], sp: [1250, 1750], seed: 23 });
    confetti(sc, { x: 360, y: 1100, at: cs + .45, n: 24, ang: [-105, -75], sp: [1100, 1500], seed: 37 });
    sticker(sc, { e: E.res, x: 596, y: 150, s: 88, r: 10, at: H.wt(7, 0) + .15 });
    sc.lazy.push(() => {
      const chipSpan = sc.el.querySelector('.ctr:last-child span.h') || [...sc.el.querySelectorAll('span.h')].pop();
      if (!chipSpan) return;
      const par = chipSpan.parentElement, cx = par.offsetLeft + chipSpan.offsetLeft + chipSpan.offsetWidth / 2, cy = par.offsetTop + chipSpan.offsetTop + chipSpan.offsetHeight / 2;
      ring(sc, { x: cx, y: cy, r0: 60, r1: 190, at: cs + .3, col: COL.lime, w: 5, loop: 1.3, dur: .9 });
    });
  }

  function decoCta(sc, H) {
    const c = H.EP.cta, v2 = c.thing != null, A = v2 ? { comp: 3, kw: 4, post: 5 } : { comp: 5, kw: 6, post: 7 };
    // rising reactions stream
    const R = rng(4242), HE = ['❤️', '💬', '🔥', '😍', '❤️', '✨'], hs = [];
    for (let i = 0; i < 9; i++) {
      const s = 38 + R() * 30, e = mk('div', 'emo', `position:absolute;left:0;top:0;font-size:${s}px;opacity:0`, HE[i % HE.length]);
      sc.fxLayer.appendChild(e); hs.push({ e, x: 60 + R() * 600, v: 200 + R() * 120, per: 3.6 + R() * 1.4, off: R() * 4, amp: 18 + R() * 30, ph: R() * 6.28, s });
    }
    sc.fxu.push(t => {
      hs.forEach(h => {
        const d = t - sc.t0 - .3 - h.off; if (d < 0) { h.e.style.opacity = 0; return; }
        const q = (d % h.per) / h.per, y = 1330 - q * (h.v * h.per);
        h.e.style.opacity = Math.min(1, q * 6) * (1 - prog(q, .7, 1)) * .95;
        h.e.style.transform = `translate(${h.x + Math.sin(d * 2 + h.ph) * h.amp}px,${y}px) scale(${.7 + .5 * Math.min(1, q * 3)}) rotate(${Math.sin(d * 1.7 + h.ph) * 14}deg)`;
      });
    });
    ring(sc, { x: 360, y: 205, r0: 78, r1: 190, at: sc.t0 + .35, col: COL.lime, w: 5, loop: 1.4, dur: 1.0 });
    sc.lazy.push(() => {
      const comp = [...sc.el.children].find(e => e.querySelector && e.querySelector('.post')), post = comp && comp.querySelector('.post');
      if (!post) return;
      const px = comp.offsetLeft + post.offsetLeft + post.offsetWidth / 2, py = comp.offsetTop + post.offsetTop + post.offsetHeight / 2;
      const pt = H.wt(8, A.post) - .05, ks = H.wt(8, A.kw) - .05;
      sc.punches.push(pt);
      sparks(sc, { x: px, y: py, at: pt, n: 12, r: 120, cols: [COL.lime, COL.white] });
      ring(sc, { x: px, y: py, r0: 30, r1: 110, at: pt, col: COL.lime, w: 5, dur: .45 });
      ring(sc, { x: comp.offsetLeft + comp.offsetWidth / 2, y: comp.offsetTop + 50, r0: 300, r1: 340, at: ks, col: 'rgba(198,255,53,.5)', w: 4, dur: .5 });
      for (let i = 0; i < 5; i++) { const a = H.wt(8, A.post); hearts(sc, px, py, pt + i * .06, i); }
      // cursor
      const cur = mk('div', '', `position:absolute;left:0;top:0;width:54px;height:54px;opacity:0;z-index:25`, `<svg width="54" height="54" viewBox="0 0 24 24"><path d="M4 2l15 9-6.5 1.5L9 19z" fill="#fff" stroke="${COL.ink}" stroke-width="1.6" stroke-linejoin="round"/></svg>`);
      sc.el.appendChild(cur);
      sc.fxu.push(t => {
        const a0 = pt - .75, a1 = pt - .06;
        if (t < a0 || t > pt + .7) { cur.style.opacity = 0; return; }
        const p = eIO(prog(t, a0, a1)), x = 520 + (px - 14 - 520) * p, y = 900 + (py - 6 - 900) * p + Math.sin(p * Math.PI) * -60;
        const press = t >= pt && t < pt + .16 ? .78 : 1, fade = 1 - prog(t, pt + .35, pt + .7);
        cur.style.opacity = Math.min(1, prog(t, a0, a0 + .15)) * fade;
        cur.style.transform = `translate(${x}px,${y}px) scale(${press})`;
      });
    });
  }

  function hearts(sc, x, y, at, i) {
    const R = rng(i * 31 + 5), e = mk('div', 'emo', `position:absolute;left:0;top:0;font-size:${34 + R() * 16}px;opacity:0;z-index:28`, i % 2 ? '❤️' : '🔥');
    sc.el.appendChild(e); const vx = (R() * .9 - .15) * 240, vy = -(300 + R() * 260);
    sc.fxu.push(t => {
      const d = t - at; if (d < 0 || d > 1.1) { e.style.opacity = 0; return; }
      e.style.opacity = 1 - prog(d, .6, 1.1);
      e.style.transform = `translate(${x + vx * d - 20}px,${y + vy * d + 500 * d * d - 20}px) scale(${.6 + .6 * eOut(prog(d, 0, .25))}) rotate(${vx * d * .08}deg)`;
    });
  }

  // ---------------------------------------------------------------- overlays: transition + progress bar
  function buildOverlays(root, T) {
    trEl = mk('div', '', 'position:absolute;left:0;top:0;width:720px;height:1280px;z-index:40;overflow:hidden;pointer-events:none;display:none');
    for (let i = 0; i < 5; i++) { const s = mk('div', '', `position:absolute;left:-90px;top:${i * 256}px;width:900px;height:260px;transform:translateX(-900px) skewX(-8deg)`); trEl.appendChild(s); slats.push(s); }
    root.appendChild(trEl);
    pbWrap = mk('div', '', 'position:absolute;left:34px;top:16px;width:652px;height:6px;border-radius:3px;z-index:49;background:rgba(128,128,128,.28);overflow:hidden');
    pbFill = mk('div', '', 'height:6px;width:0;border-radius:3px;background:#fff'); pbWrap.appendChild(pbFill); root.appendChild(pbWrap);
    STATE.T = T;
  }

  function transition(t, scenes) {
    let k = -1;
    for (let j = 1; j < scenes.length; j++) { const tc = scenes[j].t0; if (t > tc - .26 && t < tc + .3) { k = j; break; } }
    if (k < 0) { trEl.style.display = 'none'; return; }
    const tc = scenes[k].t0, o = bgOf(scenes[k - 1]), light = o === 'white' || o === 'cream' || o === 'limebg';
    const cols = light ? [COL.ink, COL.lime, COL.ink, COL.lime, COL.ink] : [COL.lime, '#ffffff', COL.lime, '#ffffff', COL.lime];
    trEl.style.display = 'block';
    slats.forEach((s, i) => {
      const dir = i % 2 ? 1 : -1, a = prog(t, tc - .2 + i * .015, tc - .07 + i * .015), b = prog(t, tc + .02 + i * .015, tc + .15 + i * .015);
      const x = dir * 900 * (-(1 - eOut(a)) + eIn(b));
      s.style.background = cols[i]; s.style.transform = `translateX(${x}px) skewX(-8deg)`;
    });
  }

  // ---------------------------------------------------------------- public
  function init(scenes, H) {
    const root = document.getElementById('root'), st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    buildOverlays(root, H.T);
    const E = defaults(H.EP);
    scenes.forEach(sc => {
      sc.fxu = []; sc.punches = []; sc.shakes = []; sc.lazy = [];
      ambient(sc);
      const l = sc.line;
      if (l === 0) decoHook(sc, H, E); else if (l === 1) decoPain(sc, H, E); else if (l === 2) decoMess(sc, H, E);
      else if (l === 3) decoBridge(sc, H); else if (l >= 4 && l <= 6) decoTip(sc, H, E, l - 4);
      else if (l === 7) decoResult(sc, H, E); else if (l === 8) decoCta(sc, H);
    });
  }

  function frame(t, scenes, si) {
    const sc = scenes[si];
    if (!sc._fxi) { sc._fxi = true; sc.lazy.forEach(f => f()); }
    sc.fxu.forEach(f => f(t));
    // camera: slow push + settle-in + beat punches + impact shake
    const push = .04 * prog(t, sc.t0, sc.t1), settle = (sc.line === 0 ? .16 : .07) * (1 - eOut(prog(t, sc.t0, sc.t0 + (sc.line === 0 ? .5 : .32))));
    let pu = 0, sx = 0, sy = 0;
    sc.punches.forEach(p => { const d = t - p; if (d >= 0 && d < .3) pu = Math.max(pu, .05 * Math.pow(1 - d / .3, 2)); });
    sc.shakes.forEach(p => { const d = t - p; if (d >= 0 && d < .28) { const a = 8 * (1 - d / .28); sx += Math.sin(d * 90) * a; sy += Math.cos(d * 77) * a * .6; } });
    sc.el.style.transform = `translate(${sx}px,${sy}px) scale(${1 + push + settle + pu})`;
    // progress bar
    const bg = bgOf(sc); pbFill.style.width = (clamp(t / STATE.T.total) * 100) + '%';
    pbFill.style.background = bg === 'dark' ? COL.lime : (bg === 'red' ? '#fff' : COL.ink);
    pbWrap.style.background = bg === 'dark' || bg === 'red' ? 'rgba(255,255,255,.22)' : 'rgba(11,13,9,.16)';
    transition(t, scenes);
  }

  return { init, frame };
})();
