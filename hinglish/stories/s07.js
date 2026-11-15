/* s07: brand takeover (marketing) - "Pachaas hazaar rupay ka marketing budget dein, hum yeh chaar kaam karte hain" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber, CY = COL.cyan;
  const SP = [];
  const C = [
    { n: 1, title: 'HOOK REELS', sub: 'Har hafte, bechne ke liye', ico: 'camera', col: LIME },
    { n: 2, title: 'ADS', sub: 'Har rupay ka hisaab', ico: 'chart', col: AMB },
    { n: 3, title: 'AUTOMATION', sub: 'WhatsApp + DM, koi lead miss na ho', ico: 'wa', col: CY, size: 32 },
    { n: 4, title: 'WEEKLY REPORT', sub: 'Kitna kharch, kitna kamaya', ico: 'doc', col: '#ff7ad9', size: 32 }];
  const list = (k, at) => C.map((c, i) => i < k ? Object.assign({}, c, { early: true }) : i === k ? Object.assign({}, c, { at }) : Object.assign({}, c, { dim: true, sub: '' }));

  // 0 HOOK
  SP.push({ line: 0, bg: BG.dark, chip: null, rows: [['[Rs. 50,000|Pachaas hazaar rupay]', 58, 'amber'], ['ka marketing budget dein,', 50, 'white'], ['hum yeh', 66, 'white'], ['[4|chaar] kaam karte hain.', 66, 'lime']],
    build(sc, X) {
      const four = [['REELS', 175, 470], ['ADS', 465, 470], ['AUTO', 175, 555], ['REPORT', 465, 555]];
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 80, from: 0, to: 50000, t0: X.ts('Pachaas') + .05, t1: X.te('hazaar') + .35, pre: 'Rs. ', col: AMB, w: 520, size: 62, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'store', x: 150, y: 250, s: 1.5, at: X.ts('marketing'), wig: 3 },
        { t: 'arrow', x1: 235, y1: 250, x2: 380, y2: 250, col: '#fff', at: X.ts('hum') },
        { t: 'bot', x: 490, y: 330, s: .8, mood: 'happy', at: X.ts('hum'), act: [X.ts('karte'), X.te('hain')] },
        ...four.map((f, i) => ({ t: 'rect', x: f[1], y: f[2] - 40, w: 250, h: 60, rx: 18, fill: '#162008', stroke: LIME, sw: 5, col: '#fff', txt: f[0], size: 28, at: X.ts('chaar') + i * .18, sfx: 'pop' }))
      ], punch: [X.t0 + .1, X.ts('hum'), X.ts('chaar')] });
    } });

  const cs = (line, k, rows, noteTxt) => ({ line, bg: BG.dark, note: noteTxt || false, rows,
    build(sc, X) { K.cards(sc, X, { total: 4, ch: 118, cards: list(k, X.t0 + .15) }); } });
  SP.push(cs(1, 0, [['Ek:', 70, 'lime'], ['har hafte hook wali reels,', 46, 'white'], ['jo bechne ke liye', 56, 'white'], ['bani hon.', 66, 'lime']]));
  SP.push(cs(2, 1, [['Do:', 70, 'amber'], ['ads, jahan har rupay', 56, 'white'], ['ka hisaab ho.', 66, 'amber']]));
  SP.push(cs(3, 2, [['Teen:', 70, 'cyan'], ['WhatsApp aur DM', 60, 'white'], ['automation,', 62, 'white'], ['koi lead miss na ho.', 50, 'cyan']]));
  SP.push(cs(4, 3, [['Chaar:', 70, 'lime'], ['har hafte report,', 60, 'white'], ['kitna kharch hua,', 56, 'white'], ['kitna kamaya.', 66, 'lime']]));

  // 5 you handle stock, we handle marketing
  SP.push({ line: 5, bg: BG.dark, rows: [['Aap maal sambhalo,', 62, 'white'], ['marketing hum', 70, 'lime'], ['sambhalte hain.', 70, 'lime']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'rect', x: 165, y: 300, w: 290, h: 470, rx: 30, fill: '#2a1a0a', stroke: AMB, sw: 6, at: X.t0 + .05, sfx: null },
        { t: 'text', txt: 'AAP', x: 165, y: 110, size: 50, col: AMB, at: X.t0 + .1, sfx: 'pop' },
        { t: 'person', x: 165, y: 520, s: 1.1, shirt: '#ff7a3d', at: X.ts('maal') - .1, mood: 'smile' },
        { t: 'ico', name: 'parcel', x: 165, y: 195, s: 1.0, at: X.ts('sambhalo'), wig: 5 },
        { t: 'rect', x: 475, y: 300, w: 290, h: 470, rx: 30, fill: '#10260a', stroke: LIME, sw: 6, at: X.ts('marketing'), sfx: null },
        { t: 'text', txt: 'HUM', x: 475, y: 110, size: 50, col: LIME, at: X.ts('marketing'), sfx: 'pop' },
        { t: 'bot', x: 475, y: 525, s: .9, mood: 'happy', at: X.ts('hum'), act: [X.ts('sambhalte'), X.te('hain') + .6] },
        { t: 'ico', name: 'chart', x: 475, y: 195, s: .95, at: X.ts('sambhalte'), wig: 4 }
      ], punch: [X.ts('sambhalo'), X.ts('sambhalte')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Brand hume', 64, 'white'], ['dena hai?', 70, 'white'], ['Comment', 60, 'white'], ['BRAND.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'BRAND', kwIndex: 5 }); } });

  window.SCENE_SPECS = SP;
})();
