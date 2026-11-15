/* s11: store conversion (marketing) - "Bees hazaar rupay ke ads se hazaar log aaye, sirf do ne khareeda" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.navy, rows: [['[Rs. 20,000|Bees hazaar rupay]', 60, 'amber'], ['ke ads se [1,000|hazaar] log aaye,', 46, 'white'], ['sirf [2|do] ne khareeda.', 62, 'red']],
    build(sc, X) {
      K.bars(sc, X, { bw: 190, base: 475, maxH: 310, bars: [
        { label: 'AAYE', v: 1000, h: 1, col: LIME, at: X.ts('hazaar', 1) - .1, pre: '', suf: '', lsize: 26 },
        { label: 'KHAREEDA', v: 2, h: .045, col: RED, at: X.ts('do'), fg: RED, pre: '', suf: '', lsize: 26 }],
        items: [
          { t: 'counter', x: 320, y: 58, from: 0, to: 20000, t0: X.ts('Bees') + .05, t1: X.te('rupay'), pre: 'Rs. ', col: AMB, w: 420, h: 84, size: 48, at: X.t0 + .1, tickSfx: true },
          { t: 'stamp', x: 330, y: 330, text: 'SIRF 2', fg: '#fff', bg: RED, rot: -7, at: X.te('khareeda'), size: 40 }] });
    } });

  // 1 slow page, hidden order button
  SP.push({ line: 1, bg: BG.warm, rows: [['Kyunki page', 66, 'white'], ['dheere khulta hai,', 62, 'red'], ['aur order button', 56, 'white'], ['dhoondna padta hai.', 52, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'phone', x: 190, y: 310, s: 2.8, at: X.t0 + .1, opt: { scr: '#fff' } },
        { t: 'fn', f: (g, sc2) => {
          const sp = S(g, 'path', { d: 'M0 -42 a42 42 0 1 1 -42 42', stroke: INK, 'stroke-width': 11, fill: 'none', 'stroke-linecap': 'round' }); const e = S(g, 'g'); e.appendChild(sp);
          const ts0 = X.ts('dheere'); sc2.u.push(t => { const p = P(t, X.t0 + .2, X.t0 + .5); e.style.opacity = p > 0 && t < X.ts('dhoondna') + .2 ? 1 : 0; tf(e, 190, 290, t * 280, 1); }); } },
        { t: 'text', txt: 'LOADING...', x: 190, y: 400, size: 28, col: INK, at: X.t0 + .3, sfx: null },
        { t: 'ico', name: 'clock', x: 480, y: 170, s: 1.5, at: X.ts('dheere'), wig: 4 },
        { t: 'rect', x: 480, y: 360, w: 200, h: 62, rx: 31, fill: '#d9d4c4', col: '#8b8774', txt: 'ORDER', size: 30, at: X.ts('button'), sfx: 'pop' },
        { t: 'text', txt: '?', x: 480, y: 480, size: 90, col: RED, at: X.ts('dhoondna'), wig: 6, sfx: 'buzz' }
      ], punch: [X.ts('dheere'), X.ts('dhoondna')] });
    } });

  // 2 what builds trust
  SP.push({ line: 2, bg: BG.dark, rows: [['Customer bharosa', 58, 'white'], ['dekhta hai:', 62, 'lime'], ['reviews, delivery details,', 44, 'white'], ['WhatsApp par baat.', 52, 'lime']],
    build(sc, X) {
      K.cards(sc, X, { cards: [
        { n: 1, title: 'REVIEWS', sub: 'Asli customers ki baat', ico: 'heartI', col: '#ff7ad9', at: X.ts('reviews') - .05 },
        { n: 2, title: 'DELIVERY DETAILS', sub: 'Kab aur kaise pahunchega', ico: 'truck', col: AMB, at: X.ts('delivery') - .05, size: 30 },
        { n: 3, title: 'WHATSAPP PAR BAAT', sub: 'Seedha seller se', ico: 'wa', col: LIME, at: X.ts('WhatsApp') - .05, size: 30 }] });
    } });

  // 3 faster store, two taps
  SP.push({ line: 3, bg: BG.mint, rows: [['Hum store', 66, 'white'], ['tez banate hain,', 66, 'lime'], ['aur order sirf', 56, 'white'], ['[2|do] tap mein.', 80, 'lime']],
    build(sc, X) {
      const t1 = X.ts('do') + .05, t2 = X.ts('tap') + .05;
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'phone', x: 180, y: 320, s: 2.7, at: X.t0 + .1, opt: { scr: '#fff' } },
        { t: 'ico', name: 'bolt', x: 480, y: 150, s: 2.0, at: X.ts('tez'), wig: 9, sfx: 'zap' },
        { t: 'rect', x: 180, y: 400, w: 150, h: 54, rx: 27, fill: LIME, txt: 'ORDER', size: 26, at: X.ts('order'), sfx: 'pop' },
        { t: 'ring', x: 180, y: 400, at: t1, r0: 20, r1: 90, w: 6, col: INK, dur: .5 },
        { t: 'ring', x: 180, y: 400, at: t2, r0: 20, r1: 90, w: 6, col: INK, dur: .5 },
        { t: 'rect', x: 480, y: 310, w: 160, h: 50, rx: 25, fill: INK, col: LIME, txt: 'TAP 1', size: 26, at: t1, sfx: 'tick' },
        { t: 'rect', x: 480, y: 380, w: 160, h: 50, rx: 25, fill: INK, col: LIME, txt: 'TAP 2', size: 26, at: t2, sfx: 'tick' },
        { t: 'ico', name: 'ok', x: 480, y: 480, s: 1.1, at: X.ts('mein'), sfx: 'success' }
      ], punch: [X.ts('tez'), t1, t2] });
    } });

  // 4 first screen: reviews, return policy, WhatsApp
  SP.push({ line: 4, bg: BG.sky, rows: [['Reviews, return policy', 52, 'white'], ['aur WhatsApp button,', 52, 'white'], ['pehli screen par.', 66, 'lime']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'phone', x: 320, y: 320, s: 3.2, at: X.t0 + .1, opt: { scr: '#fff' } },
        { t: 'rect', x: 320, y: 215, w: 190, h: 56, rx: 16, fill: '#ffd24a', txt: 'REVIEWS', size: 26, at: X.ts('Reviews'), sfx: 'pop' },
        { t: 'rect', x: 320, y: 305, w: 190, h: 56, rx: 16, fill: '#bfe9ff', txt: 'RETURN POLICY', size: 20, at: X.ts('return'), sfx: 'pop' },
        { t: 'rect', x: 320, y: 395, w: 190, h: 56, rx: 16, fill: COL.wa, col: '#fff', txt: 'WHATSAPP', size: 26, at: X.ts('WhatsApp'), sfx: 'pop' },
        { t: 'stamp', x: 60, y: 28, text: 'PEHLI SCREEN', fg: INK, bg: LIME, rot: -5, at: X.ts('pehli'), size: 36 }
      ], punch: [X.ts('Reviews'), X.ts('return'), X.ts('WhatsApp'), X.ts('pehli')] });
    } });

  // 5 same traffic, same spend, more orders
  SP.push({ line: 5, bg: BG.navy, rows: [['Wahi traffic,', 66, 'white'], ['wahi kharch,', 66, 'white'], ['par orders zyada', 58, 'lime'], ['ho sakte hain.', 58, 'lime']],
    build(sc, X) {
      K.bars(sc, X, { bw: 190, base: 470, maxH: 320, bars: [
        { label: 'ABHI', v: 2, h: .3, col: RED, at: X.ts('traffic') + .1, pre: '', suf: ' orders', lsize: 26 },
        { label: 'BAAD MEIN', v: 6, h: .9, col: LIME, at: X.ts('orders'), fg: LIME, pre: '~', suf: ' orders', lsize: 24 }],
        items: [
          { t: 'text', txt: '1,000 VISITORS · SAME SPEND', x: 320, y: 60, size: 26, col: '#fff', at: X.t0 + .1, sfx: null },
          { t: 'arrow', x1: 180, y1: 230, x2: 330, y2: 200, col: '#fff', at: X.ts('zyada') }] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Store tez', 64, 'white'], ['karwana hai?', 70, 'white'], ['Comment', 60, 'white'], ['STORE.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'STORE' }); } });

  window.SCENE_SPECS = SP;
})();
