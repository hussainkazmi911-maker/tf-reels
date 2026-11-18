/* s02v2: COD returns as a client case study - "Our client had 12k ke parcels return every month" */
(function () {
  const K = K2, { BG, ic, card, txt, hx, tag, num, line, pill, chip, rise, el, ring, LIME, INK, RED, AMB, CY, PINK, MUTE, GL, GB } = K2;
  const { P, eOut, eIO, lerp, clamp, H, S, rng } = SL;
  const SP = [];
  const shuffled = n => { const R = rng(11), a = Array.from({ length: n }, (_, i) => i); for (let i = n - 1; i > 0; i--) { const j = Math.floor(R() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

  // 0 HOOK: client brief + returned-parcel loss counter
  SP.push({ line: 0, bg: BG.red, build(sc, X) {
    tag(sc, X, { x: 40, y: 26, text: 'CLIENT BRIEF', at: X.t0 + .1, col: '#ff8a7a' });
    el(sc, `right:40px;top:35px;font-weight:700;font-size:14px;letter-spacing:1.6px;color:${MUTE}`, 'LAWN BRAND · EXAMPLE');
    const c = card(sc, { x: 40, y: 84, w: 560, h: 236, at: X.t0 + .2, glow: 'rgba(255,75,58,.12)', bd: 'rgba(255,75,58,.4)' });
    txt(sc, c, { x: 28, y: 28, html: 'RETURNED PARCELS / MONTH', size: 14, ls: 2.4, col: MUTE, fw: 800 });
    const a = X.ts('twelve') - .05, b = X.te('K') + .3;
    num(sc, X, { x: 64, y: 130, size: 90, col: RED, from: 0, to: 12000, t0: a, t1: b, pre: 'Rs ', sign: '-', at: X.t0 + .35, tick: true });
    txt(sc, c, { x: 28, y: 188, html: 'STUCK IN COURIER · NO CASH BACK', size: 14, ls: 2, col: MUTE, fw: 700 });
    for (let i = 0; i < 5; i++) {
      const x = 52 + i * 112, at = X.ts('parcels') + i * .09;
      const bx = el(sc, `left:${x}px;top:362px;width:96px;height:96px;border-radius:24px;border:1.5px solid ${GB};background:${GL};display:flex;align-items:center;justify-content:center;opacity:0`, ic('box', 46, AMB, 1.8)); rise(sc, bx, at, { dy: 14 }); X.sfx(at, 'tick', .6);
      const rt = el(sc, `left:${x + 22}px;top:474px;width:52px;height:52px;border-radius:50%;background:rgba(255,75,58,.16);display:flex;align-items:center;justify-content:center;opacity:0`, ic('ret', 28, RED, 2.2)); rise(sc, rt, X.ts('return') + i * .09, { dy: 8, s0: .6 }); X.sfx(X.ts('return') + i * .09, 'pop', .5);
    }
    chip(sc, X, { x: 150, y: 552, text: 'HERE’S WHAT WE DID  →', at: X.ts('dekho') - .05, size: 20 });
    X.sfx(a, 'swell', .8); X.punch(a);
  } });

  // 1 customer ghosts the call
  SP.push({ line: 1, bg: BG.red, build(sc, X) {
    const pc = card(sc, { x: 40, y: 30, w: 560, h: 92, at: X.t0 + .1 });
    const bx = H('div', 'ui', 'position:absolute;left:22px;top:22px;opacity:.95', ic('box', 46, AMB, 1.8)); pc.appendChild(bx);
    txt(sc, pc, { x: 92, y: 20, html: 'LAWN SUIT', size: 26, cls: 'h', css: hx(26, '#fff') }); txt(sc, pc, { x: 92, y: 54, html: 'Rs 3,200 · shipped COD', size: 17, col: MUTE, fw: 700 });
    const tk = H('div', 'ui', `position:absolute;right:24px;top:30px;padding:8px 16px;border-radius:20px;background:rgba(198,255,53,.16);color:${LIME};font-weight:800;font-size:14px;letter-spacing:1.4px`, 'GAYA ✓'); pc.appendChild(tk);
    const ph = el(sc, `left:190px;top:150px;width:260px;height:416px;border-radius:44px;border:2px solid rgba(255,255,255,.22);background:#14090a;opacity:0;overflow:hidden`); rise(sc, ph, X.ts('customer') - .1, { dy: 24 });
    const av = H('div', 'ui', `position:absolute;left:85px;top:70px;width:90px;height:90px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;${hx(40, '#fff')}`, 'C'); ph.appendChild(av);
    const nm = H('div', 'ui', 'position:absolute;left:0;top:176px;width:260px;text-align:center;font-weight:800;font-size:24px;color:#fff', 'Customer'); ph.appendChild(nm);
    const stt = H('div', 'ui', `position:absolute;left:0;top:212px;width:260px;text-align:center;font-weight:700;font-size:17px;letter-spacing:1px;color:${MUTE}`, 'Calling…'); ph.appendChild(stt);
    const dc = H('div', 'ui', `position:absolute;left:100px;top:320px;width:60px;height:60px;border-radius:50%;background:${RED};display:flex;align-items:center;justify-content:center;opacity:0`, ic('phone', 28, '#fff', 2.2)); ph.appendChild(dc);
    const t1 = X.ts('phone'), t2 = X.ts('nahi'), t3 = X.ts('ghosted');
    for (let i = 0; i < 4; i++) { ring(sc, 320, 150 + 70 + 45, t1 + i * .5, { col: RED, r: 6, dur: .9, w: 3 }); X.sfx(t1 + i * .5, 'tick', .5); }
    sc.u.push(t => { stt.textContent = t >= t2 ? 'Missed call' : (t >= t1 ? 'Calling…' : ''); stt.style.color = t >= t2 ? RED : MUTE; dc.style.opacity = t >= t2 ? 1 : 0; });
    const st = el(sc, `left:120px;top:300px;padding:6px 24px;border:5px solid ${RED};border-radius:16px;${hx(58, RED)};background:rgba(18,9,8,.82);opacity:0;white-space:nowrap`, 'GHOSTED');
    sc.u.push(t => { const p = P(t, t3 - .02, t3 + .22); st.style.opacity = p > 0 ? 1 : 0; st.style.transform = `rotate(-8deg) scale(${1.5 - .5 * eOut(p)})`; });
    X.sfx(t3, 'stamp', .9); X.punch(t3);
  } });

  // 2 the maths: 100 orders, 35 returned
  SP.push({ line: 2, bg: BG.dark, note: 'EXAMPLE MATH · MISAAL HAI', build(sc, X) {
    const order = shuffled(100), cell = 44, gx = 100, gy = 56;
    const dots = [];
    for (let i = 0; i < 100; i++) { const r = Math.floor(i / 10), c = i % 10; const d = el(sc, `left:${gx + c * cell}px;top:${gy + r * cell}px;width:30px;height:30px;border-radius:50%;background:rgba(198,255,53,.9);opacity:0`); dots.push(d); }
    const ta = X.ts('hundred') - .1, tb = X.ts('thirty-five');
    dots.forEach((d, i) => { const at = ta + (Math.floor(i / 10) + (i % 10)) * .028; const rank = order.indexOf(i), isRed = rank < 35; const rt = tb + rank * .012;
      sc.u.push(t => { const p = clamp((t - at) / .22); const q = clamp((t - rt) / .25); d.style.opacity = p > 0 ? 1 : 0; d.style.background = isRed && q > 0 ? RED : 'rgba(198,255,53,.9)'; d.style.transform = `scale(${(.4 + .6 * eOut(p)) * (1 + (isRed ? .3 * Math.sin(Math.PI * clamp(q)) : 0))})`; }); });
    tag(sc, X, { x: 40, y: 8, text: '100 ORDERS', at: ta, col: LIME });
    tag(sc, X, { x: 360, y: 8, text: '35 RETURNED', at: tb, col: RED });
    const calc = el(sc, `left:40px;top:520px;width:560px;height:62px;border-radius:31px;border:1.5px solid rgba(255,75,58,.55);background:rgba(255,75,58,.1);display:flex;align-items:center;justify-content:center;opacity:0;${hx(26, '#fff')}`, `35 × Rs 350 = <span style="color:${RED};margin-left:12px">Rs 12,250</span>`);
    rise(sc, calc, X.ts('three') - .05, { dy: 16 }); X.sfx(X.ts('three'), 'pop', .8); X.sfx(X.te('rupay') - .05, 'stamp', .6);
    X.sfx(ta, 'swell', .6); X.sfx(tb, 'swell', .5); X.punch(tb);
  } });

  // 3 the rule: WhatsApp confirmation
  SP.push({ line: 3, bg: BG.dark, build(sc, X) {
    K.chat(sc, X, { title: 'Zara Lawn House', initial: 'Z', msgs: [
      { who: 'r', y: 120, w: 410, label: 'AUTO · AI', text: 'Salam! Your order: Lawn suit, Rs 3,200. Confirm?', at: X.ts('WhatsApp'), sfx: 'pop' },
      { who: 'r', y: 262, w: 330, text: '1 = Haan &nbsp;|&nbsp; 2 = Nahi', bg: 'rgba(255,207,51,.14)', bd: 'rgba(255,207,51,.5)', at: X.ts('pe'), sfx: 'ding' },
      { who: 'l', y: 372, w: 130, text: '1', size: 28, at: X.ts('confirm'), tick: true, sfx: 'pop' }] });
    chip(sc, X, { x: 396, y: 478, text: 'CONFIRMED', at: X.ts('confirm') + .35, size: 20, sfx: 'success' });
    X.punch(X.ts('confirm'));
  } });

  // 4 yes -> ship it / no -> cash saved
  SP.push({ line: 4, bg: BG.dark, build(sc, X) {
    const mkCol = (x, col, rgb, label, icn, sub, at, t2) => {
      const c = card(sc, { x, y: 40, w: 275, h: 440, at: X.t0 + .1, bd: `rgba(${rgb},.5)`, glow: `rgba(${rgb},.10)` });
      txt(sc, c, { x: 28, y: 28, html: label, size: 50, cls: 'h', css: hx(50, col) });
      const o = H('div', 'ui', `position:absolute;left:28px;top:112px;width:72px;height:72px;border-radius:50%;background:rgba(${rgb},.15);display:flex;align-items:center;justify-content:center;opacity:0`, ic(icn, 38, col, 2.4)); c.appendChild(o); rise(sc, o, at, { s0: .6, dy: 4 }); X.sfx(at, 'pop', .8);
      txt(sc, c, { x: 28, y: 372, html: sub, size: 24, cls: 'h', css: hx(24, '#fff') });
      return c;
    };
    const yes = mkCol(34, LIME, '198,255,53', 'YES', 'check', 'SHIP IT', X.ts('yes'));
    const tr = H('div', 'ui', 'position:absolute;left:28px;top:236px;opacity:0', ic('truck', 90, LIME, 1.7)); yes.appendChild(tr);
    sc.u.push(t => { const p = eOut(P(t, X.ts('Ship') - .05, X.ts('Ship') + .6)); tr.style.opacity = p > 0 ? 1 : 0; tr.style.transform = `translateX(${(1 - p) * -90}px)`; });
    for (let i = 0; i < 3; i++) { const sp = H('div', 'ui', `position:absolute;left:${6}px;top:${268 + i * 20}px;width:${30 - i * 6}px;height:3px;border-radius:2px;background:${LIME};opacity:0`); yes.appendChild(sp); rise(sc, sp, X.ts('Ship') + .2 + i * .05, { dx: -10, dy: 0 }); }
    X.sfx(X.ts('Ship'), 'whoosh', .6);
    const no = mkCol(331, RED, '255,75,58', 'NO', 'cross', 'CASH SAVED', X.ts('no'));
    for (let i = 0; i < 3; i++) { const cn = H('div', 'ui', `position:absolute;left:${34 + i * 3}px;top:${300 - i * 26}px;opacity:0`, ic('coin', 62, AMB, 1.8)); no.appendChild(cn); rise(sc, cn, X.ts('Paisa') + i * .14, { dy: -26, s0: .7 }); X.sfx(X.ts('Paisa') + i * .14, 'tick', .8); }
    chip(sc, X, { x: 236, y: 508, text: 'SORTED', at: X.ts('Sorted'), size: 20, sfx: 'success' });
    X.punch(X.ts('yes')); X.punch(X.ts('no'));
  } });

  // 5 return rate falls (industry range)
  SP.push({ line: 5, bg: BG.navy, note: 'SOURCE: eGROW COD GUIDE 2026 · INDUSTRY RANGE', build(sc, X) {
    const c = card(sc, { x: 40, y: 40, w: 560, h: 500, at: X.t0 + .1 });
    txt(sc, c, { x: 28, y: 26, html: 'RETURN RATE', size: 15, ls: 2.4, col: MUTE, fw: 800 });
    const base = 440, maxH = 280;
    [['BEFORE', 35, RED, '255,75,58', X.ts('Guides') + .05, 110], ['AFTER', 18, LIME, '198,255,53', X.ts('almost'), 350]].forEach((b, i) => {
      const h = maxH * b[1] / 35;
      const bar = el(sc, `left:${b[5]}px;top:${base - h + 0}px;width:150px;height:${h}px;border-radius:18px 18px 6px 6px;background:rgba(${b[3]},.85);transform-origin:50% 100%;opacity:0`);
      sc.u.push(t => { const p = eOut(P(t, b[4], b[4] + .7)); bar.style.opacity = p > 0 ? 1 : 0; bar.style.transform = `scaleY(${p})`; });
      const lab = el(sc, `left:${b[5] - 10}px;top:${base + 14}px;width:170px;text-align:center;font-weight:800;font-size:18px;letter-spacing:2px;color:${MUTE}`, b[0]);
      const val = el(sc, `left:${b[5] - 10}px;top:${base - h - 62}px;width:170px;text-align:center;${hx(54, b[2])};opacity:0`, '');
      sc.u.push(t => { const p = eOut(P(t, b[4] + .1, b[4] + .9)); val.textContent = '~' + Math.round(b[1] * p) + '%'; val.style.opacity = p > 0 ? 1 : 0; });
      X.sfx(b[4], 'swell', .5); X.sfx(b[4] + .85, 'tick', .8);
    });
    const ar = el(sc, `left:268px;top:230px;opacity:0`, ic('up', 64, '#fff', 2.2).replace('<svg ', '<svg style="transform:rotate(90deg)" ')); rise(sc, ar, X.ts('half') - .1, { dx: -14, dy: 0 }); X.sfx(X.ts('half'), 'ding', .6);
    X.punch(X.ts('almost'));
  } });

  // 6 result: returns fall, cash stays
  SP.push({ line: 6, bg: BG.dark, build(sc, X) {
    const order = shuffled(35), gx = 88, gy = 50, cell = 64;
    for (let i = 0; i < 35; i++) { const r = Math.floor(i / 7), c = i % 7; const d = el(sc, `left:${gx + c * cell}px;top:${gy + r * 56}px;width:34px;height:34px;border-radius:50%;background:${RED};opacity:0`);
      const at = X.ts('Result') + (r + c) * .03, rank = order.indexOf(i), flips = rank < 17, ft = X.ts('kam') + .1 + rank * .03;
      sc.u.push(t => { const p = clamp((t - at) / .22), q = clamp((t - ft) / .3); d.style.opacity = p > 0 ? 1 : 0; d.style.background = flips && q > 0 ? LIME : RED; d.style.transform = `scale(${(.4 + .6 * eOut(p)) * (1 + (flips ? .25 * Math.sin(Math.PI * q) : 0))})`; }); }
    tag(sc, X, { x: 40, y: 6, text: '35 RETURNS', col: RED, at: X.ts('Result') });
    tag(sc, X, { x: 360, y: 6, text: 'ALMOST HALF GONE', col: LIME, at: X.ts('kam') + .2 });
    const cc = card(sc, { x: 40, y: 360, w: 560, h: 190, at: X.ts('cash') - .1, bd: 'rgba(198,255,53,.5)', glow: 'rgba(198,255,53,.14)' });
    const o = H('div', 'ui', `position:absolute;left:30px;top:56px;width:78px;height:78px;border-radius:50%;background:rgba(198,255,53,.14);display:flex;align-items:center;justify-content:center`, ic('coin', 44, LIME, 2)); cc.appendChild(o);
    txt(sc, cc, { x: 130, y: 52, html: 'CASH STAYS', size: 36, cls: 'h', css: hx(36, '#fff') }); txt(sc, cc, { x: 130, y: 100, html: 'IN THE BUSINESS', size: 36, cls: 'h', css: hx(36, LIME) });
    X.sfx(X.ts('cash'), 'pop', .8); X.sfx(X.ts('kam') + .5, 'success', .6); X.punch(X.ts('kam'));
  } });

  SP.push({ line: 7, bg: BG.dark, note: false, build(sc, X) { K.cta(sc, X, { word: 'CONFIRM', dm: 'Hi! Sending you the confirm bot details on DM.' }); } });
  window.SCENE_SPECS = SP;
})();
