/* s09: fake followers vs hook reels (serum) - "Paanch hazaar rupay mein das hazaar followers kharide, ek bhi order nahi aaya" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.purple, rows: [['[Rs. 5,000|Paanch hazaar rupay]', 58, 'amber'], ['mein [10,000|das hazaar] followers', 50, 'white'], ['kharide, ek bhi', 58, 'white'], ['order nahi aaya.', 66, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 70, from: 0, to: 5000, t0: X.ts('Paanch') + .05, t1: X.te('rupay'), sign: '-', pre: 'Rs. ', col: RED, w: 440, size: 58, at: X.t0 + .1, tickSfx: true },
        { t: 'counter', x: 320, y: 215, from: 0, to: 10000, t0: X.ts('das'), t1: X.te('followers'), pre: '', post: ' FOLLOWERS', col: LIME, w: 520, size: 46, at: X.ts('das') - .1, tickSfx: true },
        ...[[90, 330], [210, 360], [330, 330], [450, 365], [560, 330]].map((p, i) => ({ t: 'ico', name: 'ghost', x: p[0], y: p[1], s: 1.0, at: X.ts('kharide') + i * .1, bob: 6, ph: i })),
        { t: 'counter', x: 320, y: 490, from: 0, to: 0, t0: X.ts('ek'), t1: X.te('ek'), pre: 'ORDERS: ', col: RED, w: 400, size: 52, at: X.ts('order') - .1, sfx: 'buzz' }
      ], punch: [X.t0 + .1, X.ts('das'), X.ts('order')], shake: [X.ts('order')] });
    } });

  // 1 followers are counted, customers buy
  SP.push({ line: 1, bg: BG.dark, rows: [['Kyunki followers', 62, 'white'], ['ginti hain,', 76, 'red'], ['customers', 66, 'white'], ['kharidte hain.', 70, 'lime']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'rect', x: 165, y: 300, w: 290, h: 470, rx: 30, fill: '#2a0d0a', stroke: RED, sw: 6, at: X.t0 + .05, sfx: null },
        { t: 'text', txt: 'FOLLOWERS', x: 165, y: 110, size: 34, col: RED, at: X.ts('followers'), sfx: 'pop' },
        { t: 'ico', name: 'ghost', x: 165, y: 260, s: 1.6, at: X.ts('ginti'), bob: 6 },
        { t: 'text', txt: 'SIRF GINTI', x: 165, y: 430, size: 40, col: '#fff', at: X.ts('ginti'), sfx: 'tick' },
        { t: 'rect', x: 475, y: 300, w: 290, h: 470, rx: 30, fill: '#10260a', stroke: LIME, sw: 6, at: X.ts('customers'), sfx: null },
        { t: 'text', txt: 'CUSTOMERS', x: 475, y: 110, size: 34, col: LIME, at: X.ts('customers'), sfx: 'pop' },
        { t: 'person', x: 475, y: 510, s: 1.0, shirt: '#7d5fff', at: X.ts('customers') + .1, mood: 'smile' },
        { t: 'bills', x: 475, y: 300, to: [475, 235], n: 5, at: X.ts('kharidte'), dur: .8, gap: .1, spread: 130, arc: 110, sfx: 'coin' },
        { t: 'ico', name: 'moneybag', x: 475, y: 215, s: 1.0, at: X.ts('kharidte'), wig: 5 }
      ], punch: [X.ts('ginti'), X.ts('kharidte')] });
    } });

  // 2 product in reel, no hook
  SP.push({ line: 2, bg: BG.pink, rows: [['Aapki serum ki reels', 52, 'white'], ['mein product hai,', 62, 'lime'], ['hook nahi.', 84, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'phone', x: 320, y: 310, s: 3.1, at: X.ts('reels'), opt: { scr: '#fff' }, wig: 4 },
        { t: 'ico', name: 'serum', x: 320, y: 320, s: 1.6, at: X.ts('serum') + .05, bob: 3 },
        { t: 'rect', x: 105, y: 190, w: 190, h: 54, rx: 27, fill: LIME, txt: 'PRODUCT', size: 26, at: X.ts('product'), sfx: 'success' },
        { t: 'ico', name: 'ok', x: 105, y: 255, s: .6, at: X.ts('product') + .1 },
        { t: 'rect', x: 535, y: 190, w: 170, h: 54, rx: 27, fill: RED, col: '#fff', txt: 'HOOK', size: 26, at: X.ts('hook'), sfx: 'buzz' },
        { t: 'badge', x: 535, y: 255, r: 24, n: 'X', fill: RED, at: X.ts('nahi'), sfx: 'buzz' }
      ], punch: [X.ts('product'), X.ts('nahi')] });
    } });

  // 3 first 3 seconds, they scroll
  SP.push({ line: 3, bg: BG.red, rows: [['Log pehle', 62, 'white'], ['[3|teen] second mein', 66, 'amber'], ['scroll kar jaate hain.', 52, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'phone', x: 190, y: 320, s: 2.8, at: X.t0 + .1, opt: { scr: '#fff' } },
        { t: 'fn', f: (g, sc2) => {
          const mk = col => { const e = S(g, 'g'); S(e, 'rect', { x: -75, y: -125, width: 150, height: 250, rx: 12, fill: col, stroke: INK, 'stroke-width': 4 }); S(e, 'circle', { cx: 0, cy: -20, r: 34, fill: '#fff', opacity: .7 }); return e; };
          const A1 = mk('#ffb3d1'), B1 = mk('#bfe9ff'), ts0 = X.ts('scroll');
          sc2.u.push(t => { const q = eIO(P(t, ts0, ts0 + .3)); A1.style.opacity = t < X.t0 + .2 ? 0 : 1 - q; tf(A1, 190, 320 - q * 90, 0, 1); B1.style.opacity = q; tf(B1, 190, 320 + (1 - q) * 90, 0, 1); }); } },
        { t: 'ico', name: 'clock', x: 480, y: 190, s: 1.5, at: X.ts('teen'), wig: 3 },
        { t: 'counter', x: 480, y: 340, from: 3, to: 0, t0: X.ts('teen') + .1, t1: X.te('second'), pre: '', post: ' SEC', col: AMB, w: 220, size: 40, at: X.ts('teen') + .15 },
        { t: 'ico', name: 'bolt', x: 480, y: 470, s: 1.2, at: X.ts('scroll'), wig: 12, sfx: 'zap', opt: { col: RED } },
        { t: 'text', txt: 'SCROLL!', x: 480, y: 560, size: 40, col: '#fff', at: X.ts('scroll'), sfx: 'buzz' }
      ], punch: [X.ts('teen'), X.ts('scroll')] });
    } });

  // 4 we do hook, script, shoot, edit
  SP.push({ line: 4, bg: BG.dark, rows: [['Hum hook, script,', 58, 'white'], ['shoot aur edit', 66, 'lime'], ['sab karte hain.', 70, 'white']],
    build(sc, X) {
      const N = (label, ico, x, y, at, col) => ({ t: 'node', label, ico, x, y, w: 260, h: 210, is: .9, at, col, lc: '#fff', size: 30 });
      K.stage(sc, X, { items: [
        N('HOOK', 'bolt', 175, 175, X.ts('hook') - .05, LIME), N('SCRIPT', 'doc', 465, 175, X.ts('script') - .05, '#33d6ff'),
        N('SHOOT', 'camera', 175, 410, X.ts('shoot') - .05, '#ffb020'), N('EDIT', 'play', 465, 410, X.ts('edit') - .05, '#ff7ad9'),
        { t: 'ico', name: 'ok', x: 320, y: 295, s: 1.2, at: X.ts('sab'), sfx: 'success' }
      ], punch: [X.ts('hook'), X.ts('script'), X.ts('shoot'), X.ts('edit')] });
    } });

  // 5 comment -> DM -> order path
  SP.push({ line: 5, bg: BG.navy, rows: [['Aur comment se', 58, 'white'], ['DM aur order tak', 60, 'lime'], ['ka rasta banate hain.', 48, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'node', label: 'COMMENT', ico: 'ig', x: 105, y: 300, w: 180, h: 190, is: .8, at: X.ts('comment'), col: '#d6249f', size: 22 },
        { t: 'arrow', x1: 205, y1: 300, x2: 255, y2: 300, col: '#fff', at: X.ts('DM') - .1, w: 7 },
        { t: 'node', label: 'DM', ico: 'wa', x: 320, y: 300, w: 180, h: 190, is: .8, at: X.ts('DM'), col: COL.wa, size: 26 },
        { t: 'arrow', x1: 420, y1: 300, x2: 470, y2: 300, col: '#fff', at: X.ts('order') - .1, w: 7 },
        { t: 'node', label: 'ORDER', ico: 'parcel', x: 535, y: 300, w: 180, h: 190, is: .8, at: X.ts('order'), col: LIME, size: 26 },
        { t: 'conf', x: 535, y: 300, at: X.ts('banate'), n: 22, seed: 9 }
      ], punch: [X.ts('comment'), X.ts('DM'), X.ts('order')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Page sale machine', 56, 'white'], ['banana hai?', 70, 'white'], ['Comment', 60, 'white'], ['GROW.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'GROW', kwIndex: 6 }); } });

  window.SCENE_SPECS = SP;
})();
