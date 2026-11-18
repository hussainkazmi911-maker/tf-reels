/* s07v2: brand takeover as a client case study - "Our client gave us 50k ka marketing budget, aur exactly hum kya karte hain" */
(function () {
  const K = K2, { BG, ic, card, txt, hx, tag, num, line, pill, chip, rise, el, ring, LIME, INK, RED, AMB, CY, PINK, MUTE, GL, GB } = K2;
  const { P, eOut, lerp, clamp, H, S, svgRoot } = SL;
  const SP = [];

  // 0 HOOK: client brief + budget counter, then the four jobs light up
  SP.push({ line: 0, bg: BG.dark, build(sc, X) {
    tag(sc, X, { x: 40, y: 26, text: 'CLIENT BRIEF', at: X.t0 + .1 });
    el(sc, `right:40px;top:35px;font-weight:700;font-size:14px;letter-spacing:1.6px;color:${MUTE}`, 'FASHION BRAND · EXAMPLE');
    const c = card(sc, { x: 40, y: 84, w: 560, h: 252, at: X.t0 + .2, glow: 'rgba(255,176,32,.10)' });
    txt(sc, c, { x: 28, y: 28, html: 'MONTHLY MARKETING BUDGET', size: 14, ls: 2.4, col: MUTE, fw: 800 });
    const a = X.ts('fifty') - .05, b = X.te('K') + .3;
    num(sc, X, { x: 64, y: 134, size: 92, col: AMB, from: 0, to: 50000, t0: a, t1: b, pre: 'Rs ', at: X.t0 + .35, tick: true });
    line(sc, sc.picin, { x: 68, y: 244, w: 504, th: 5, col: 'rgba(255,255,255,.12)', at: X.t0 + .35, dur: .3, op: 1 });
    line(sc, sc.picin, { x: 68, y: 244, w: 504, th: 5, col: AMB, at: a, dur: b - a, op: 1 });
    txt(sc, c, { x: 28, y: 204, html: 'PER MONTH · ALL CHANNELS', size: 14, ls: 2, col: MUTE, fw: 700 });
    line(sc, sc.picin, { x: 320, y: 338, h: 36, th: 3, col: LIME, at: X.ts('exactly') - .3, dur: .3 });
    const P4 = [['reels', 'REELS', LIME, '198,255,53', 'exactly', 40, 376], ['chart', 'ADS', AMB, '255,176,32', 'hum', 330, 376], ['chat', 'AUTOMATION', CY, '51,214,255', 'kya', 40, 462], ['doc', 'REPORT', PINK, '255,122,217', 'karte', 330, 462]];
    P4.forEach((p, i) => pill(sc, X, { x: p[5], y: p[6], w: 270, h: 74, ic: p[0], label: p[1], col: p[2], rgb: p[3], at: X.ts('exactly') - .3 + i * .05, lit: X.ts(p[4]), size: 22 }));
    X.sfx(a, 'swell', .8); X.punch(a);
  } });

  // 1-4 the four jobs
  const ROWS = [
    { n: 1, t: 'HOOK-FIRST REELS', s: 'Every week', ic: 'reels', col: LIME, rgb: '198,255,53' },
    { n: 2, t: 'ADS', s: 'Every rupay tracked', ic: 'chart', col: AMB, rgb: '255,176,32' },
    { n: 3, t: 'DM + WHATSAPP AUTOMATION', s: 'No lead ghosted', ic: 'chat', col: CY, rgb: '51,214,255', tsz: 22 },
    { n: 4, t: 'WEEKLY REPORT', s: 'Spend vs earned', ic: 'doc', col: PINK, rgb: '255,122,217' }];
  function micro(sc, X, k, mv, at) {
    if (k === 0) { // three reel thumbnails
      for (let j = 0; j < 3; j++) {
        const th = H('div', 'ui', `position:absolute;left:${6 + j * 60}px;top:16px;width:48px;height:80px;border-radius:13px;border:2px solid ${LIME};background:rgba(198,255,53,.08);display:flex;align-items:center;justify-content:center;opacity:0`, ic('play', 22, LIME, 2));
        mv.appendChild(th); rise(sc, th, at + .22 + j * .16, { dy: 14 }); X.sfx(at + .22 + j * .16, 'pop', .6);
        const bar = H('div', 'ui', `position:absolute;left:${6 + j * 60 + 6}px;top:${16 + 80 - 11}px;width:36px;height:3px;border-radius:2px;background:rgba(255,255,255,.18);opacity:0`); mv.appendChild(bar);
        const fill = H('div', 'ui', `width:0;height:3px;border-radius:2px;background:${LIME}`); bar.appendChild(fill);
        sc.u.push(t => { const p = P(t, at + .45 + j * .16, at + 1.5 + j * .16); bar.style.opacity = p > 0 ? 1 : 0; fill.style.width = (36 * eOut(p)) + 'px'; });
      }
    } else if (k === 1) { // bars growing + tracked tick
      const hs = [26, 46, 38, 70];
      hs.forEach((h, j) => { const b = H('div', 'ui', `position:absolute;left:${14 + j * 40}px;top:${100 - h}px;width:28px;height:${h}px;border-radius:7px 7px 3px 3px;background:${AMB};transform-origin:50% 100%;opacity:0`); mv.appendChild(b);
        sc.u.push(t => { const p = P(t, at + .22 + j * .13, at + .62 + j * .13); b.style.opacity = p > 0 ? .95 : 0; b.style.transform = `scaleY(${eOut(p)})`; }); X.sfx(at + .22 + j * .13, 'tick', .5); });
      const ck = H('div', 'ui', `position:absolute;left:172px;top:10px;width:30px;height:30px;border-radius:50%;background:${LIME};display:flex;align-items:center;justify-content:center;opacity:0`, ic('check', 18, INK, 3)); mv.appendChild(ck); rise(sc, ck, at + 1.0, { dy: 6, s0: .6 }); X.sfx(at + 1.0, 'ding', .5);
    } else if (k === 2) { // incoming + auto reply
      const b1 = H('div', 'ui', `position:absolute;left:0;top:12px;padding:8px 16px;border-radius:16px 16px 16px 4px;background:rgba(255,255,255,.12);font-size:17px;font-weight:700;color:#fff;opacity:0`, 'Price?'); mv.appendChild(b1); rise(sc, b1, at + .25, { dy: 10, dx: -14 }); X.sfx(at + .25, 'pop', .5);
      const b2 = H('div', 'ui', `position:absolute;left:46px;top:56px;padding:8px 16px;border-radius:16px 16px 4px 16px;background:rgba(37,211,102,.2);border:1.5px solid rgba(37,211,102,.6);font-size:17px;font-weight:700;color:#fff;opacity:0`, `Sent in 2s <span style="color:${CY};font-size:14px">✓✓</span>`); mv.appendChild(b2); rise(sc, b2, at + .75, { dy: 10, dx: 14 }); X.sfx(at + .75, 'ding', .5);
    } else { // line chart drawing
      const sv = svgRoot(mv, 200, 112), pts = [[8, 86], [46, 70], [84, 76], [122, 44], [160, 50], [192, 18]]; let L = 0; for (let i = 1; i < pts.length; i++) L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
      [30, 60, 90].forEach(y => S(sv, 'line', { x1: 0, y1: y, x2: 200, y2: y, stroke: 'rgba(255,255,255,.08)', 'stroke-width': 1.5 }));
      const pl = S(sv, 'path', { d: 'M' + pts.map(p => p.join(' ')).join(' L'), stroke: PINK, 'stroke-width': 5, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-dasharray': L, 'stroke-dashoffset': L });
      const dot = S(sv, 'circle', { cx: 192, cy: 18, r: 7, fill: PINK, opacity: 0 });
      sc.u.push(t => { const p = eOut(P(t, at + .25, at + 1.1)); pl.setAttribute('stroke-dashoffset', L * (1 - p)); dot.setAttribute('opacity', P(t, at + 1.0, at + 1.15)); });
      X.sfx(at + .25, 'swell', .4); X.sfx(at + 1.1, 'ding', .5);
    }
  }
  function stack(k) { return { line: k + 1, bg: BG.dark, build(sc, X) {
    const at = X.t0 + .12;
    ROWS.forEach((r, i) => {
      const y = 36 + i * 128, st = i < k ? 'done' : i === k ? 'act' : 'ghost';
      const e = el(sc, `left:40px;top:${y}px;width:560px;height:112px;border-radius:26px;border:1.5px solid ${st === 'act' ? r.col : st === 'done' ? `rgba(${r.rgb},.4)` : GB};background:${st === 'act' ? `rgba(${r.rgb},.085)` : GL};box-shadow:${st === 'act' ? `0 0 36px rgba(${r.rgb},.22)` : 'none'};opacity:0`,
        `<div style="position:absolute;left:22px;top:30px;width:52px;height:52px;border-radius:50%;background:${st === 'ghost' ? 'rgba(255,255,255,.1)' : r.col};color:${st === 'ghost' ? MUTE : INK};${hx(28, st === 'ghost' ? MUTE : INK)};text-align:center;line-height:52px">${r.n}</div>` +
        `<div style="position:absolute;left:94px;top:0;width:${st === 'act' ? 232 : 360}px;height:112px;display:flex;flex-direction:column;justify-content:center;gap:6px"><div style="${hx(r.tsz || 25, '#fff')};line-height:1.05;white-space:normal">${r.t}</div><div style="font-weight:700;font-size:16px;color:${MUTE};letter-spacing:.3px">${r.s}</div></div>`);
      if (st === 'done') { const c = H('div', 'ui', `position:absolute;right:26px;top:36px;width:40px;height:40px;border-radius:50%;background:rgba(${r.rgb},.16);display:flex;align-items:center;justify-content:center`, ic('check', 22, r.col, 2.6)); e.appendChild(c); }
      if (st === 'act') { const mv = H('div', 'ui', 'position:absolute;left:340px;top:0;width:210px;height:112px'); e.appendChild(mv); micro(sc, X, k, mv, at); rise(sc, e, at, { dx: 36, dy: 0, dur: .45 }); X.sfx(at, 'pop', .9); X.punch(at); ring(sc, 66, y + 56, at + .05, { col: r.col, r: 4, dur: .7 }); }
      else rise(sc, e, X.t0 - 1, { op: st === 'done' ? .9 : .28, dy: 0, dur: .01 });
    });
  } }; }
  [0, 1, 2, 3].forEach(k => SP.push(stack(k)));

  // 5 client handles product, we handle marketing
  SP.push({ line: 5, bg: BG.dark, build(sc, X) {
    const L = card(sc, { x: 34, y: 50, w: 275, h: 470, at: X.t0 + .08 });
    txt(sc, L, { x: 24, y: 24, html: 'CLIENT', size: 15, ls: 2.4, col: MUTE, fw: 800 });
    const Lw = H('div', 'ui', 'position:absolute;right:22px;top:16px;opacity:.9', ic('store', 30, MUTE, 1.8)); L.appendChild(Lw);
    [['Product', 'bas'], ['Stock', 'apna'], ['Packing', 'product']].forEach((r, i) => {
      const p = H('div', 'ui', `position:absolute;left:20px;top:${84 + i * 96}px;width:235px;height:74px;border-radius:20px;border:1.5px solid ${GB};background:rgba(255,255,255,.04);display:flex;align-items:center;gap:12px;padding:0 18px;opacity:0`, ic('check', 24, MUTE, 2.4) + `<div style="${hx(22, MUTE)}">${r[0]}</div>`);
      L.appendChild(p); rise(sc, p, X.ts(r[1]) - .05, { dy: 12 }); X.sfx(X.ts(r[1]), 'tick', .6);
    });
    const R = card(sc, { x: 331, y: 50, w: 275, h: 470, at: X.t0 + .08 });
    const rglow = H('div', 'ui', `position:absolute;left:0;top:0;width:275px;height:470px;border-radius:28px;border:1.5px solid ${LIME};box-shadow:0 0 38px rgba(198,255,53,.25);opacity:0`); R.appendChild(rglow);
    sc.u.push(t => { rglow.style.opacity = P(t, X.ts('hum') - .05, X.ts('hum') + .3); });
    txt(sc, R, { x: 24, y: 24, html: 'THE TOTAL FORGE', size: 15, ls: 2.4, col: LIME, fw: 800 });
    [['Reels', 'Marketing'], ['Ads', 'ka'], ['Automation', 'poora'], ['Reports', 'scene']].forEach((r, i) => {
      const p = H('div', 'ui', `position:absolute;left:20px;top:${70 + i * 76}px;width:235px;height:62px;border-radius:20px;border:1.5px solid rgba(198,255,53,.5);background:rgba(198,255,53,.08);display:flex;align-items:center;gap:12px;padding:0 18px;opacity:0`, ic('check', 24, LIME, 2.6) + `<div style="${hx(21, '#fff')}">${r[0]}</div>`);
      R.appendChild(p); rise(sc, p, X.ts(r[1]) - .05, { dy: 12 }); X.sfx(X.ts(r[1]), 'pop', .7);
    });
    chip(sc, X, { x: 366, y: 440, text: 'HANDLED', at: X.ts('sambhala', 1), size: 21 });
    X.punch(X.ts('hum'));
  } });

  // 6 result: every rupay tracked / every lead answered
  SP.push({ line: 6, bg: BG.dark, build(sc, X) {
    const mk = (y, icn, big, sub, col, rgb, at, rows) => {
      const c = card(sc, { x: 40, y, w: 560, h: 220, at: X.t0 + .1 + (y > 100 ? .12 : 0), glow: `rgba(${rgb},.08)` });
      const o = H('div', 'ui', `position:absolute;left:28px;top:30px;width:64px;height:64px;border-radius:50%;background:rgba(${rgb},.14);display:flex;align-items:center;justify-content:center`, ic(icn, 34, col, 2)); c.appendChild(o);
      txt(sc, c, { x: 28, y: 112, html: big, size: 30, col: '#fff', cls: 'h', css: `${hx(30, '#fff')}` });
      txt(sc, c, { x: 28, y: 152, html: sub, size: 22, col: col, fw: 800, ls: 1 });
      rows.forEach((w, i) => {
        const rowY = 36 + i * 54;
        const bar = H('div', 'ui', `position:absolute;left:290px;top:${rowY + 14}px;width:${w}px;height:10px;border-radius:5px;background:rgba(255,255,255,.16);opacity:0`); c.appendChild(bar);
        sc.u.push(t => { const p = eOut(P(t, at + i * .13, at + .4 + i * .13)); bar.style.opacity = p > 0 ? 1 : 0; bar.style.width = (w * p) + 'px'; });
        const ck = H('div', 'ui', `position:absolute;left:${290 + w + 14}px;top:${rowY + 3}px;width:32px;height:32px;border-radius:50%;background:${col};display:flex;align-items:center;justify-content:center;opacity:0`, ic('check', 18, INK, 3.2)); c.appendChild(ck); rise(sc, ck, at + .3 + i * .13, { dy: 4, s0: .5, dur: .3 }); X.sfx(at + .3 + i * .13, 'tick', .8);
      });
    };
    mk(56, 'coin', 'EVERY RUPAY', 'TRACKED', AMB, '255,176,32', X.ts('tracked'), [150, 190, 120]);
    mk(300, 'chat', 'EVERY LEAD', 'ANSWERED', CY, '51,214,255', X.ts('answered'), [170, 120, 190]);
    X.sfx(X.ts('answered') + .6, 'success', .7); X.punch(X.ts('tracked'));
  } });

  SP.push({ line: 7, bg: BG.dark, note: false, build(sc, X) { K.cta(sc, X, { word: 'BRAND', dm: 'Hi! Sending you the plan for your brand on DM.' }); } });
  window.SCENE_SPECS = SP;
})();
