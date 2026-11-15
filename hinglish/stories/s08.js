/* s08: ads waste (earbuds) - "Tees hazaar ke ads mein das hazaar rupay galat logon ko dikh rahe hain" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK: donut, 1/3 of the money wasted
  SP.push({ line: 0, bg: BG.navy, chip: null, rows: [['[Rs. 30,000|Tees hazaar]', 66, 'amber'], ['ke ads mein', 56, 'white'], ['[Rs. 10,000|das hazaar rupay]', 56, 'red'], ['galat logon ko dikh rahe hain.', 46, 'white']],
    build(sc, X) {
      K.donut(sc, X, { cx: 320, cy: 320, r: 130, sw: 58, csize: 64, at: X.ts('Tees'), cat: X.ts('das'), cval: 33, csuf: '%', sub: 'WASTE', segs: [
        { v: 67, col: LIME, at: X.ts('ads') }, { v: 33, col: RED, at: X.ts('das') }],
        items: [
          { t: 'counter', x: 320, y: 55, from: 0, to: 30000, t0: X.ts('Tees') + .05, t1: X.te('hazaar'), pre: 'Rs. ', col: AMB, w: 400, h: 84, size: 48, at: X.t0 + .1, tickSfx: true },
          { t: 'ico', name: 'ghost', x: 540, y: 470, s: 1.1, at: X.ts('galat'), bob: 8 },
          { t: 'text', txt: '-Rs. 10,000', x: 320, y: 540, size: 44, col: RED, at: X.ts('rupay'), sfx: 'buzz' }] });
    } });

  // 1 earbuds ad shown to people who never shop
  SP.push({ line: 1, bg: BG.sky, rows: [['Earbuds ka ad,', 66, 'white'], ['aur dekhne wale woh,', 54, 'white'], ['jo shopping', 66, 'red'], ['karte hi nahi.', 66, 'red']],
    build(sc, X) {
      K.stage(sc, X, { floor: '#7dc9ef', floorY: 520, items: [
        { t: 'ico', name: 'ig', x: 100, y: 120, s: 1.1, at: X.t0 + .1, wig: 4 },
        { t: 'ico', name: 'earbuds', x: 140, y: 300, s: 1.7, at: X.ts('Earbuds'), wig: 3 },
        { t: 'rect', x: 140, y: 420, w: 110, h: 44, rx: 22, fill: AMB, txt: 'AD', size: 26, at: X.ts('ad'), sfx: null },
        { t: 'arrow', x1: 220, y1: 300, x2: 330, y2: 300, col: INK, at: X.ts('dekhne') },
        { t: 'person', x: 400, y: 570, s: 1.0, shirt: '#7d5fff', at: X.ts('dekhne'), mood: 'sleep' },
        { t: 'person', x: 500, y: 570, s: 1.0, shirt: '#ff7a3d', at: X.ts('dekhne') + .1, mood: 'neutral' },
        { t: 'person', x: 595, y: 570, s: 1.0, shirt: '#ff5fa2', at: X.ts('dekhne') + .2, mood: 'sleep' },
        ...[400, 500, 595].map((x, i) => ({ t: 'badge', x, y: 300, r: 24, n: 'X', fill: RED, at: X.ts('shopping') + i * .2, sfx: 'buzz' }))
      ], punch: [X.ts('Earbuds'), X.ts('shopping')] });
    } });

  // 2 no test, no retargeting, just boost and pray
  SP.push({ line: 2, bg: BG.red, rows: [['Na test, na retargeting,', 48, 'white'], ['bas boost dabaya', 66, 'amber'], ['aur dua ki.', 80, 'white']],
    build(sc, X) {
      const tap = X.ts('boost') + .15;
      K.stage(sc, X, { items: [
        { t: 'rect', x: 170, y: 100, w: 250, h: 52, rx: 26, fill: '#fff', col: RED, txt: 'NO TEST', size: 26, at: X.ts('test'), sfx: 'buzz' },
        { t: 'rect', x: 470, y: 100, w: 300, h: 52, rx: 26, fill: '#fff', col: RED, txt: 'NO RETARGET', size: 26, at: X.ts('retargeting'), sfx: 'buzz' },
        { t: 'rect', x: 320, y: 290, w: 380, h: 140, rx: 70, fill: LIME, txt: 'BOOST', size: 60, at: X.ts('bas'), sfx: 'pop' },
        { t: 'ring', x: 320, y: 290, at: tap, r0: 50, r1: 250, w: 8, col: '#fff', dur: .6 },
        { t: 'spark', x: 320, y: 290, at: tap, n: 12, r: 160, sfx: 'zap' },
        { t: 'text', txt: 'DUA...', x: 320, y: 500, size: 66, col: AMB, at: X.ts('dua'), wig: 4, bob: 5, sfx: 'tick' }
      ], punch: [tap, X.ts('dua')] });
    } });

  // 3 we test three ads, winner gets the budget
  SP.push({ line: 3, bg: BG.navy, rows: [['Hum [3|teen] ads', 66, 'white'], ['test karte hain,', 62, 'white'], ['jo jeete,', 70, 'lime'], ['usi par budget.', 62, 'lime']],
    build(sc, X) {
      K.bars(sc, X, { bw: 150, base: 450, maxH: 300, bars: [
        { label: 'AD 1', v: 3, h: .3, col: '#8b93a8', at: X.ts('teen') + .1, pre: '', suf: ' sales', lsize: 26 },
        { label: 'AD 2', v: 11, h: 1, col: LIME, at: X.ts('teen') + .4, fg: LIME, pre: '', suf: ' sales', lsize: 26 },
        { label: 'AD 3', v: 5, h: .45, col: '#8b93a8', at: X.ts('teen') + .7, pre: '', suf: ' sales', lsize: 26 }],
        items: [
          { t: 'stamp', x: 40, y: 20, text: 'WINNER', fg: INK, bg: LIME, rot: -6, at: X.ts('jeete'), size: 38 },
          { t: 'bills', x: 560, y: 520, to: [320, 170], n: 6, at: X.ts('budget'), dur: .9, gap: .1, spread: 40, arc: 40, sfx: 'coin' }] });
    } });

  // 4 retargeting: those who saw but did not buy
  SP.push({ line: 4, bg: BG.dark, rows: [['Phir unhe dobara', 62, 'lime'], ['dikhate hain,', 66, 'white'], ['jinhon ne dekha', 56, 'white'], ['par khareeda nahi.', 56, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'earbuds', x: 150, y: 250, s: 1.6, at: X.t0 + .1, bob: 3 },
        { t: 'person', x: 330, y: 540, s: 1.1, shirt: '#ff5fa2', at: X.ts('jinhon') - .1, mood: 'neutral', walk: [X.ts('khareeda'), X.te('nahi') + .4, 520] },
        { t: 'ico', name: 'cart', x: 150, y: 480, s: 1.2, at: X.ts('khareeda'), wig: 3 },
        { t: 'badge', x: 205, y: 440, r: 26, n: 'X', fill: RED, at: X.ts('nahi'), sfx: 'buzz' },
        { t: 'rect', x: 320, y: 100, w: 410, h: 64, rx: 32, fill: LIME, txt: 'DOBARA DIKHAO', size: 32, at: X.ts('dobara'), sfx: 'success' },
        { t: 'ring', x: 150, y: 250, at: X.ts('dobara'), r0: 40, r1: 140, w: 8, col: LIME, dur: .7 },
        { t: 'ico', name: 'bell', x: 480, y: 250, s: 1.0, at: X.ts('dikhate'), wig: 14, sfx: 'ding' }
      ], punch: [X.ts('dobara'), X.ts('nahi')] });
    } });

  // 5 weekly report
  SP.push({ line: 5, bg: BG.cream, note: 'EXAMPLE MATH · MISAAL HAI', rows: [['Har hafte report:', 56, 'white'], ['kharch, sales', 66, 'lime'], ['aur munafa.', 80, 'amber']],
    build(sc, X) {
      K.receipt(sc, X, { title: 'HAFTE KI REPORT', rows: [
        { l: 'Ad kharch', r: 'Rs. 30,000', at: X.ts('kharch') }, { l: 'Sales', r: 'Rs. 1,20,000', at: X.ts('sales'), col: '#17a34a' }],
        total: { l: 'SALES - AD KHARCH', r: '+Rs. 90,000', at: X.ts('munafa'), bg: '#17a34a' } });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Ads ka hisaab', 62, 'white'], ['chahiye?', 70, 'white'], ['Comment', 60, 'white'], ['ADS.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'ADS', kwIndex: 5 }); } });

  window.SCENE_SPECS = SP;
})();
