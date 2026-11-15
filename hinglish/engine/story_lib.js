/* Story-reel library: easing, DOM/SVG helpers and original flat characters (Forge Bot, Person, Shop). Everything is a pure function of time. */
window.SL = (function () {
  const NSV = 'http://www.w3.org/2000/svg';
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const P = (t, a, b) => clamp((t - a) / (b - a));
  const eOut = x => 1 - Math.pow(1 - x, 3);
  const eIn = x => x * x * x;
  const eIO = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const eBack = x => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
  const eElastic = x => (x <= 0 ? 0 : x >= 1 ? 1 : Math.pow(2, -10 * x) * Math.sin((x * 10 - .75) * (2 * Math.PI) / 3) + 1);
  const lerp = (a, b, x) => a + (b - a) * x;
  const rng = seed => { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; };
  const COL = { lime: '#c6ff35', ink: '#0b0d09', red: '#ff4b3a', white: '#ffffff', amber: '#ffb020', cyan: '#33d6ff', wa: '#25d366', cream: '#f4eedc', navy: '#16214f', skin: '#f2c18d', skin2: '#c68b59' };

  const H = (tag, cls, css, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (css) e.style.cssText = css; if (html != null) e.innerHTML = html; return e; };
  const S = (parent, tag, attrs, css) => {
    const e = document.createElementNS(NSV, tag);
    if (attrs) for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (css) e.style.cssText = css;
    if (parent) parent.appendChild(e);
    return e;
  };
  const svgRoot = (parent, w, h, css) => S(parent, 'svg', { width: w, height: h, viewBox: `0 0 ${w} ${h}` }, 'position:absolute;left:0;top:0;overflow:visible;' + (css || ''));
  const tf = (el, x, y, r, sx, sy) => { el.style.transform = `translate(${x}px,${y}px) rotate(${r || 0}deg) scale(${sx == null ? 1 : sx},${sy == null ? (sx == null ? 1 : sx) : sy})`; };
  const T = (g, txt, x, y, size, fill, anchor, font) => { const e = S(g, 'text', { x, y, 'text-anchor': anchor || 'middle' }, `font-family:${font || "'Archivo Black',Inter,sans-serif"};font-size:${size}px;fill:${fill}`); e.textContent = txt; return e; };

  // ------------------------------------------------------------------ Forge Bot (original mascot). origin = feet centre.
  function Bot(parent, o) {
    o = o || {};
    const g = S(parent, 'g'); const L = o.lime || COL.lime, K = COL.ink;
    const legL = S(g, 'rect', { x: -26, y: -30, width: 17, height: 30, rx: 6, fill: K });
    const legR = S(g, 'rect', { x: 9, y: -30, width: 17, height: 30, rx: 6, fill: K });
    const body = S(g, 'g');
    S(body, 'rect', { x: -42, y: -114, width: 84, height: 88, rx: 26, fill: L, stroke: K, 'stroke-width': 6 });
    S(body, 'rect', { x: -26, y: -96, width: 52, height: 36, rx: 10, fill: K });
    const chest = T(body, 'AI', 0, -69, 22, L);
    // arms (pivot at shoulder)
    const mkArm = side => {
      const a = S(g, 'g'); const dx = side * 7;
      S(a, 'line', { x1: 0, y1: 0, x2: dx, y2: 50, stroke: K, 'stroke-width': 22, 'stroke-linecap': 'round' });
      S(a, 'line', { x1: 0, y1: 0, x2: dx, y2: 50, stroke: L, 'stroke-width': 11, 'stroke-linecap': 'round' });
      S(a, 'circle', { cx: dx, cy: 54, r: 11, fill: L, stroke: K, 'stroke-width': 5 });
      return a;
    };
    const armL = mkArm(-1), armR = mkArm(1);
    const head = S(g, 'g');
    const ant = S(head, 'g'); S(ant, 'line', { x1: 0, y1: -206, x2: 0, y2: -234, stroke: K, 'stroke-width': 6, 'stroke-linecap': 'round' });
    const ball = S(ant, 'circle', { cx: 0, cy: -242, r: 11, fill: L, stroke: K, 'stroke-width': 5 });
    S(head, 'rect', { x: -66, y: -178, width: 13, height: 36, rx: 6, fill: K });
    S(head, 'rect', { x: 53, y: -178, width: 13, height: 36, rx: 6, fill: K });
    S(head, 'rect', { x: -57, y: -208, width: 114, height: 96, rx: 32, fill: L, stroke: K, 'stroke-width': 6 });
    S(head, 'rect', { x: -45, y: -196, width: 90, height: 62, rx: 24, fill: K });
    const eyeO = S(head, 'g'), eyeH = S(head, 'g'), eyeW = S(head, 'g'), eyeX = S(head, 'g');
    const eL = S(eyeO, 'rect', { x: -31, y: -184, width: 21, height: 30, rx: 10, fill: L });
    const eR = S(eyeO, 'rect', { x: 10, y: -184, width: 21, height: 30, rx: 10, fill: L });
    S(eyeH, 'path', { d: 'M-33 -164 q12 -22 24 0 M9 -164 q12 -22 24 0', stroke: L, 'stroke-width': 8, fill: 'none', 'stroke-linecap': 'round' });
    S(eyeW, 'circle', { cx: -21, cy: -169, r: 14, fill: L }); S(eyeW, 'circle', { cx: 21, cy: -169, r: 14, fill: L });
    S(eyeW, 'circle', { cx: -21, cy: -169, r: 5, fill: K }); S(eyeW, 'circle', { cx: 21, cy: -169, r: 5, fill: K });
    S(eyeX, 'path', { d: 'M-32 -180 l22 22 M-10 -180 l-22 22 M10 -180 l22 22 M32 -180 l-22 22', stroke: L, 'stroke-width': 7, fill: 'none', 'stroke-linecap': 'round' });
    const mouth = S(head, 'path', { d: 'M-11 -145 q11 10 22 0', stroke: L, 'stroke-width': 5, fill: 'none', 'stroke-linecap': 'round' });
    const glow = S(g, 'circle', { cx: 0, cy: -150, r: 150, fill: L, opacity: 0 }); g.insertBefore(glow, g.firstChild);
    return {
      g,
      // o: x,y,s,rot,flip, mood(open|happy|wow|off), blink(0..1), armL/armR (deg, 0 = hanging), bob, ant(phase), glow(0..1), chest(text)
      pose(p) {
        const s = p.s == null ? 1 : p.s, bob = p.bob || 0, fl = p.flip ? -1 : 1;
        tf(g, p.x, p.y + bob, p.rot || 0, s * fl, s * (p.sq == null ? 1 : p.sq));
        tf(armL, -42, -96, p.armL == null ? 8 : p.armL); tf(armR, 42, -96, p.armR == null ? -8 : p.armR);
        const m = p.mood || 'open';
        eyeO.style.display = m === 'open' ? '' : 'none'; eyeH.style.display = m === 'happy' ? '' : 'none';
        eyeW.style.display = m === 'wow' ? '' : 'none'; eyeX.style.display = m === 'off' ? '' : 'none';
        const bl = 1 - clamp(p.blink || 0) * .92;
        [eL, eR].forEach(e => { e.style.transformOrigin = '0px -169px'; e.style.transform = `scaleY(${bl})`; });
        mouth.style.display = (m === 'off') ? 'none' : '';
        tf(ant, 0, 0, Math.sin((p.ant || 0) * 3) * 6); ant.style.transformOrigin = '0px -206px'; ball.setAttribute('r', 11 + 3 * Math.sin((p.ant || 0) * 7));
        glow.setAttribute('opacity', (p.glow || 0) * .35);
        if (p.chest != null) chest.textContent = p.chest;
        const w = p.walk || 0; tf(legL, 0, Math.max(0, Math.sin(w * 6.28)) * -6); tf(legR, 0, Math.max(0, -Math.sin(w * 6.28)) * -6);
      }
    };
  }

  // ------------------------------------------------------------------ Person (original). origin = feet centre, faces right.
  function Person(parent, o) {
    o = o || {}; const skin = o.skin || COL.skin, hair = o.hair || '#2b1d14', shirt = o.shirt || '#ff8a3d', pants = o.pants || '#2a3358';
    const g = S(parent, 'g');
    const mkLeg = () => { const l = S(g, 'g'); S(l, 'line', { x1: 0, y1: 0, x2: 0, y2: 66, stroke: pants, 'stroke-width': 17, 'stroke-linecap': 'round' }); S(l, 'ellipse', { cx: 5, cy: 68, rx: 14, ry: 7, fill: COL.ink }); return l; };
    const legB = mkLeg(), legF = mkLeg();
    const torso = S(g, 'g');
    S(torso, 'rect', { x: -25, y: -158, width: 50, height: 98, rx: 20, fill: shirt });
    const mkArm = back => { const a = S(g, 'g'); S(a, 'line', { x1: 0, y1: 0, x2: 0, y2: 58, stroke: shirt, 'stroke-width': 15, 'stroke-linecap': 'round' }); S(a, 'circle', { cx: 0, cy: 62, r: 9, fill: skin }); return a; };
    const armB = mkArm(true);
    const armF = mkArm(false);
    const phone = S(armF, 'g'); S(phone, 'rect', { x: -2, y: 46, width: 22, height: 38, rx: 5, fill: '#1c1f2b', stroke: '#6b7392', 'stroke-width': 2 });
    const scr = S(phone, 'rect', { x: 1, y: 50, width: 16, height: 30, rx: 3, fill: '#bfe9ff' });
    phone.style.display = o.phone ? '' : 'none';
    const head = S(g, 'g');
    S(head, 'circle', { cx: 0, cy: -190, r: 30, fill: skin });
    S(head, 'path', { d: 'M-31 -192 a31 31 0 0 1 62 0 q-30 -16 -62 0z', fill: hair });
    S(head, 'path', { d: o.cap ? 'M-34 -196 h68 v10 h-68z' : 'M0 0', fill: o.cap || 'none' });
    const eyes = S(head, 'g'); S(eyes, 'circle', { cx: 8, cy: -188, r: 3.6, fill: COL.ink }); S(eyes, 'circle', { cx: 21, cy: -188, r: 3.6, fill: COL.ink });
    const closed = S(head, 'path', { d: 'M3 -188 q5 5 10 0 M16 -188 q5 5 10 0', stroke: COL.ink, 'stroke-width': 3, fill: 'none', 'stroke-linecap': 'round' }); closed.style.display = 'none';
    const mouth = S(head, 'path', { d: 'M9 -176 q6 5 12 0', stroke: COL.ink, 'stroke-width': 3, fill: 'none', 'stroke-linecap': 'round' });
    const brow = S(head, 'path', { d: 'M3 -198 l10 3 M16 -195 l10 -3', stroke: COL.ink, 'stroke-width': 3, fill: 'none', 'stroke-linecap': 'round' }); brow.style.display = 'none';
    return {
      g,
      // p: x,y,s,flip, walk(phase 0..), mood(neutral|smile|worry|sleep|wow), armF/armB (deg), bob, tilt
      pose(p) {
        const s = p.s == null ? 1 : p.s, fl = p.flip ? -1 : 1, w = p.walk || 0, sw = Math.sin(w * 6.283);
        tf(g, p.x, p.y + (p.bob || 0) + Math.abs(sw) * (w ? -5 : 0) * s, p.rot || 0, s * fl, s);
        tf(legB, -6, -60, -sw * 30); tf(legF, 6, -60, sw * 30);
        tf(armB, 0, -146, p.armB != null ? p.armB : sw * 28); tf(armF, 0, -146, p.armF != null ? p.armF : -sw * 28);
        phone.style.display = (o.phone || p.phone) ? '' : 'none';
        scr.setAttribute('fill', p.scr || '#bfe9ff');
        head.style.transformOrigin = '0px -160px'; head.style.transform = `rotate(${p.tilt || 0}deg)`;
        const m = p.mood || 'neutral';
        eyes.style.display = m === 'sleep' ? 'none' : ''; closed.style.display = m === 'sleep' ? '' : 'none';
        brow.style.display = m === 'worry' ? '' : 'none';
        mouth.setAttribute('d', m === 'smile' ? 'M7 -177 q8 9 16 0' : m === 'worry' ? 'M9 -173 q6 -5 12 0' : m === 'wow' ? 'M12 -177 a4 5 0 1 0 .1 0z' : 'M9 -176 h12');
      }
    };
  }

  // ------------------------------------------------------------------ Shop facade. origin = top-left.
  function Shop(parent, o) {
    const w = o.w, h = o.h, g = S(parent, 'g'); const C = o.color, A = o.awn || [COL.red, '#fff'];
    S(g, 'rect', { x: 0, y: 0, width: w, height: h, rx: 14, fill: C, stroke: COL.ink, 'stroke-width': 6 });
    // sign
    const sign = S(g, 'g'); S(sign, 'rect', { x: 14, y: 14, width: w - 28, height: 52, rx: 10, fill: o.signBg || COL.ink });
    const st = T(sign, o.name, w / 2, 51, o.signSize || 24, o.signFg || COL.lime);
    // awning
    const n = 6, aw = (w - 12) / n;
    for (let i = 0; i < n; i++) S(g, 'path', { d: `M${6 + i * aw} 78 h${aw} v26 a${aw / 2} ${aw / 2} 0 0 1 -${aw} 0z`, fill: A[i % 2], stroke: COL.ink, 'stroke-width': 4 });
    // window + door
    const win = S(g, 'rect', { x: 18, y: 124, width: w * .4, height: h - 164, rx: 10, fill: o.winCol || '#bfe9ff', stroke: COL.ink, 'stroke-width': 5 });
    const door = S(g, 'g'); S(door, 'rect', { x: w * .56, y: 118, width: w * .34, height: h - 118 - 6, rx: 8, fill: o.doorCol || '#5b3a29', stroke: COL.ink, 'stroke-width': 5 });
    const dg = S(door, 'rect', { x: w * .56 + 6, y: 126, width: w * .34 - 12, height: h - 150, rx: 6, fill: '#ffe9a6', opacity: 0 });
    return { g, win, door, dg, sign, st, doorX: w * .73, doorY: h - 20 };
  }

  const star = (parent, cx, cy, r, fill) => S(parent, 'path', { d: `M${cx} ${cy - r} L${cx + r * .3} ${cy - r * .3} L${cx + r} ${cy} L${cx + r * .3} ${cy + r * .3} L${cx} ${cy + r} L${cx - r * .3} ${cy + r * .3} L${cx - r} ${cy} L${cx - r * .3} ${cy - r * .3}z`, fill });
  const heart = (parent, cx, cy, s, fill) => S(parent, 'path', { d: `M${cx} ${cy + 10 * s} C${cx - 18 * s} ${cy - 2 * s} ${cx - 12 * s} ${cy - 16 * s} ${cx} ${cy - 6 * s} C${cx + 12 * s} ${cy - 16 * s} ${cx + 18 * s} ${cy - 2 * s} ${cx} ${cy + 10 * s}z`, fill });
  const check = (parent, cx, cy, s, col, sw) => S(parent, 'path', { d: `M${cx - 10 * s} ${cy} l${7 * s} ${8 * s} l${14 * s} ${-17 * s}`, stroke: col, 'stroke-width': sw || 6, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
  const cross = (parent, cx, cy, s, col, sw) => S(parent, 'path', { d: `M${cx - 9 * s} ${cy - 9 * s} l${18 * s} ${18 * s} M${cx + 9 * s} ${cy - 9 * s} l${-18 * s} ${18 * s}`, stroke: col, 'stroke-width': sw || 6, fill: 'none', 'stroke-linecap': 'round' });

  return { NSV, clamp, P, eOut, eIn, eIO, eBack, eElastic, lerp, rng, H, S, svgRoot, tf, T, COL, Bot, Person, Shop, star, heart, check, cross };
})();
