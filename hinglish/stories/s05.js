/* s05: repeat orders (perfume) - "Aath sau rupay ka ad lagaya, aur customer ne sirf ek baar khareeda" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.dark, rows: [['[Rs. 800|Aath sau rupay]', 80, 'amber'], ['ka ad lagaya, aur', 58, 'white'], ['customer ne', 66, 'white'], ['sirf ek baar khareeda.', 54, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 90, from: 0, to: 800, t0: X.ts('Aath') + .05, t1: X.te('rupay'), sign: '-', pre: 'Rs. ', col: RED, w: 440, size: 66, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'ig', x: 110, y: 300, s: 1.6, at: X.ts('ad'), wig: 5 },
        { t: 'rect', x: 110, y: 400, w: 100, h: 44, rx: 22, fill: AMB, txt: 'AD', size: 26, at: X.ts('ad') + .1, sfx: null },
        { t: 'arrow', x1: 175, y1: 300, x2: 330, y2: 300, col: '#fff', at: X.ts('customer') },
        { t: 'person', x: 410, y: 560, s: 1.2, shirt: '#ff5fa2', at: X.ts('customer'), mood: 'neutral', moodAt: [[X.ts('khareeda'), 'smile']] },
        { t: 'ico', name: 'perfume', x: 540, y: 330, s: 1.5, at: X.ts('khareeda'), kind: 'drop', wig: 5 },
        { t: 'badge', x: 560, y: 235, r: 30, n: '1x', fill: RED, at: X.ts('baar'), sfx: 'buzz' },
        { t: 'stamp', x: 25, y: 470, text: 'SIRF EK BAAR', fg: '#fff', bg: RED, rot: -7, at: X.ts('baar') + .15, size: 34 }
      ], punch: [X.t0 + .1, X.ts('khareeda')] });
    } });

  // 1 perfume runs out in 30 days
  SP.push({ line: 1, bg: BG.purple, rows: [['Perfume tees din', 66, 'white'], ['mein khatam,', 70, 'lime'], ['aur aapko', 58, 'white'], ['pata hi nahi.', 74, 'red']],
    build(sc, X) {
      const t0 = X.ts('tees'), t1 = X.te('khatam');
      K.stage(sc, X, { items: [
        { t: 'fn', f: (g, sc2) => {
          const e = S(g, 'g'); const liq = S(e, 'rect', { x: -40, y: -44, width: 80, height: 104, rx: 16, fill: '#7fd6ff' });
          S(e, 'rect', { x: -44, y: -48, width: 88, height: 112, rx: 22, fill: 'none', stroke: INK, 'stroke-width': 6 });
          S(e, 'rect', { x: -15, y: -76, width: 30, height: 20, rx: 5, fill: INK, stroke: INK, 'stroke-width': 4 });
          const lab = T(e, 'EAU', 0, 18, 22, '#fff');
          sc2.u.push(t => { const p = P(t, X.t0 + .1, X.t0 + .45); e.style.opacity = p > 0 ? 1 : 0; const q = eIO(P(t, t0, t1)); const h = 104 * (1 - q * .92); liq.setAttribute('y', 60 - h); liq.setAttribute('height', h); tf(e, 170, 330, 0, 2.0 * Math.max(0, eBack(p))); lab.style.opacity = 1 - q; }); } },
        { t: 'counter', x: 440, y: 150, from: 1, to: 30, t0: X.ts('tees'), t1: X.te('khatam'), pre: 'DIN ', col: AMB, w: 290, size: 50, at: X.ts('Perfume') + .1 },
        { t: 'person', x: 480, y: 570, s: 1.2, shirt: '#7d5fff', at: X.ts('aapko'), mood: 'neutral', moodAt: [[X.ts('pata'), 'worry']] },
        { t: 'text', txt: '?', x: 400, y: 340, size: 90, col: '#fff', at: X.ts('pata'), wig: 6, sfx: 'buzz' },
        { t: 'text', txt: '?', x: 560, y: 330, size: 70, col: AMB, at: X.ts('hi'), wig: 7 }
      ], punch: [X.ts('khatam'), X.ts('nahi')] });
    } });

  // 2 bought again elsewhere
  SP.push({ line: 2, bg: BG.red, rows: [['Usne dobara', 66, 'white'], ['kisi aur se', 80, 'amber'], ['kharid liya.', 78, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'store', x: 160, y: 300, s: 1.7, at: X.ts('kisi'), opt: { name: 'DOOSRA' }, wig: 3 },
        { t: 'ico', name: 'perfume', x: 160, y: 300, s: .8, at: X.ts('kharid'), kind: 'fade', move: [X.ts('kharid'), X.te('liya') + .2, 490, 410], fadeOut: [X.te('liya') + .3, X.te('liya') + .5], sfx: 'whoosh' },
        { t: 'person', x: 490, y: 560, s: 1.2, shirt: '#ff5fa2', at: X.t0 + .1, flip: true, mood: 'neutral', moodAt: [[X.ts('kharid'), 'smile']] },
        { t: 'bills', x: 490, y: 360, to: [160, 300], n: 5, at: X.ts('kharid'), dur: .8, gap: .09, spread: 50, arc: 90, sfx: 'coin' },
        { t: 'stamp', x: 120, y: 50, text: 'DOOSRE KE PAAS', fg: '#fff', bg: INK, rot: -6, at: X.te('liya'), size: 42 }
      ], punch: [X.ts('kisi'), X.te('liya')] });
    } });

  // 3 new customer vs old customer cost
  SP.push({ line: 3, bg: BG.navy, note: 'EXAMPLE MATH · MISAAL HAI', rows: [['Naya customer', 56, 'white'], ['[Rs. 800|aath sau rupay] ka,', 52, 'red'], ['purane ko ek message,', 52, 'white'], ['lagbhag muft.', 78, 'lime']],
    build(sc, X) {
      K.bars(sc, X, { bw: 210, base: 470, maxH: 330, bars: [
        { label: 'NAYA (AD)', v: 800, h: 1, col: RED, at: X.ts('Naya') + .1, pre: 'Rs. ', suf: '', lsize: 24 },
        { label: 'PURANA (MESSAGE)', lsize: 20, v: 0, h: .1, col: LIME, at: X.ts('purane') + .1, fg: LIME, pre: '~Rs. ', suf: '' }],
        items: [{ t: 'text', txt: 'EK ORDER KI COST', x: 320, y: 60, size: 34, col: '#fff', at: X.t0 + .1, sfx: null }] });
    } });

  // 4 day 27 AI asks
  SP.push({ line: 4, bg: BG.mint, rows: [['Din satais par', 62, 'lime'], ['A I poochta hai:', 58, 'white'], ['perfume khatam hone', 52, 'white'], ['wala hai, repeat?', 52, 'white']],
    build(sc, X) {
      K.chat(sc, X, { left: 282, title: 'Aroma Corner', sub: 'Business account', avatar: '#7fd6ff', msgs: [
        { who: 'r', label: 'AUTO · A I', text: 'Perfume khatam hone wala hai. Repeat karein?', at: X.ts('poochta') },
        { who: 'r', text: 'Haan, repeat', at: X.ts('repeat'), bg: '#fff3b0', sfx: 'ding' }],
        items: [
          { t: 'rect', x: 125, y: 110, w: 170, h: 66, rx: 22, fill: LIME, txt: 'DIN 27', size: 34, at: X.ts('Din'), sfx: 'pop' },
          { t: 'bot', x: 125, y: 545, s: .85, mood: 'happy', at: X.ts('A'), act: [X.ts('poochta'), X.ts('repeat')] },
          { t: 'ico', name: 'perfume', x: 125, y: 245, s: .9, at: X.ts('perfume'), wig: 5 }] });
    } });

  // 5 one tap, ad cost 0
  SP.push({ line: 5, bg: BG.dark, rows: [['Ek tap,', 80, 'lime'], ['doosra order,', 66, 'white'], ['ad ka ek rupay', 58, 'white'], ['nahi laga.', 74, 'lime']],
    build(sc, X) {
      const tap = X.ts('tap') + .1;
      K.stage(sc, X, { items: [
        { t: 'rect', x: 320, y: 190, w: 400, h: 120, rx: 60, fill: LIME, txt: 'REPEAT ORDER', size: 40, at: X.t0 + .1, sfx: 'pop' },
        { t: 'ring', x: 320, y: 190, at: tap, r0: 40, r1: 230, w: 8, col: '#fff', dur: .6 },
        { t: 'spark', x: 320, y: 190, at: tap, n: 12, r: 150, sfx: 'success' },
        { t: 'ico', name: 'ok', x: 190, y: 365, s: 1.2, at: X.ts('doosra'), sfx: 'ding' },
        { t: 'ico', name: 'truck', x: 400, y: 355, s: 1.3, at: X.ts('order'), wig: 8, sfx: 'whoosh' },
        { t: 'counter', x: 320, y: 520, from: 800, to: 0, t0: X.ts('ek') + .1, t1: X.te('rupay'), pre: 'AD KHARCH Rs. ', col: LIME, w: 560, size: 40, at: X.ts('ad') }
      ], punch: [tap, X.ts('nahi')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Repeat orders', 64, 'white'], ['chahiye?', 70, 'white'], ['Comment', 60, 'white'], ['REPEAT.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'REPEAT', kwIndex: 4 }); } });

  window.SCENE_SPECS = SP;
})();
