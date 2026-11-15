/* s02: COD returns (lawn suits) - "Barah hazaar rupay parcel ban kar wapas aa rahe hain" */
(function () {
  const K = KIT, { BG } = K, { COL, S, tf, lerp, eIO, eOut, eBack, P } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK: money -> parcel -> boomerang back
  SP.push({ line: 0, bg: BG.red, rows: [['[Rs. 12,000|Barah hazaar rupay]', 84, 'amber'], ['parcel ban kar', 64, 'white'], ['wapas aa rahe hain.', 60, 'red']],
    build(sc, X) {
      const a = X.ts('ban'), b = X.ts('wapas'), c = X.ts('rahe');
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 500, from: 0, to: 12000, t0: X.ts('Barah') + .05, t1: X.te('rupay'), sign: '-', col: RED, w: 520, size: 74, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'moneybag', x: 150, y: 250, s: 1.5, at: X.t0 + .1, fadeOut: [a, a + .2], wig: 6 },
        { t: 'bills', x: 150, y: 220, to: [320, 240], n: 5, at: X.ts('parcel') - .1, dur: .55, gap: .07, spread: 30, arc: 50, sfx: 'coin' },
        { t: 'fn', f: (g, sc2) => { const e = S(g, 'g'); K.ICO.parcel(e, {});
            sc2.u.push(t => { if (t < a) { e.style.opacity = 0; return; } e.style.opacity = 1; let x = 320, y = 250, s = 1.7, r = 0; s *= Math.max(0, eBack(P(t, a, a + .3)));
              const q = P(t, b, b + .45), q2 = P(t, b + .45, b + 1.05);
              if (q > 0 && q2 <= 0) { x = 320 + 250 * eOut(q); y = 250 - 80 * q; r = q * 50; s *= 1 - .3 * q; } else if (q2 > 0) { x = lerp(570, 320, eIO(q2)); y = lerp(170, 250, eIO(q2)); r = lerp(50, 360, eIO(q2)); s *= .7 + .3 * q2; }
              tf(e, x, y + Math.sin(t * 3) * 3, r, s); }); } },
        { t: 'spark', x: 320, y: 250, at: a, n: 12, r: 110, sfx: 'zap' },
        { t: 'stamp', x: 170, y: 350, text: 'RETURNED', fg: RED, bg: '#fff', rot: -9, at: b + 1.0, size: 56 }
      ], sfx: [[b, 'whoosh', .7]], punch: [X.t0 + .1, b + 1.0] });
    } });

  // 1 customer does not pick up
  SP.push({ line: 1, bg: BG.warm, rows: [['Lawn suit bheja,', 58, 'white'], ['customer ne', 62, 'white'], ['phone nahi', 84, 'red'], ['uthaya.', 84, 'red']],
    build(sc, X) {
      const rg = (at, n) => Array.from({ length: n }, (_, i) => ({ t: 'ring', x: 470, y: 250, at: at + i * .45, r0: 30, r1: 120, w: 6, col: RED, dur: .7 }));
      K.stage(sc, X, { floor: '#c9783f', floorY: 520, items: [
        { t: 'ico', name: 'suit', x: 170, y: 300, s: 1.9, at: X.t0 + .1, bob: 4 },
        { t: 'text', txt: 'Rs. 3,200', x: 170, y: 440, size: 34, col: INK, at: X.t0 + .3, sfx: null },
        { t: 'ico', name: 'phone', x: 470, y: 250, s: 1.5, at: X.ts('phone'), wig: 50, opt: { scr: '#17331f' } },
        ...rg(X.ts('phone'), 4),
        { t: 'rect', x: 470, y: 250, w: 100, h: 44, rx: 12, fill: COL.wa, txt: 'CALL', size: 22, col: '#fff', at: X.ts('phone') + .1, sfx: null, s: .8 },
        { t: 'person', x: 500, y: 560, s: 1.15, flip: true, mood: 'sleep', shirt: '#7d5fff', at: X.t0 + .3, moodAt: [[X.ts('phone'), 'neutral']], tilt: 0 },
        { t: 'bub', x: 300, y: 450, w: 260, text: 'Baad mein dekhta hun...', who: 'c', at: X.ts('nahi'), label: 'CUSTOMER', lc: '#7d5fff', sfx: 'pop' },
        { t: 'stamp', x: 100, y: 60, text: 'MISSED CALL', fg: '#fff', bg: RED, rot: -6, at: X.ts('uthaya') - .05, size: 48 }
      ], punch: [X.ts('phone'), X.ts('uthaya')] });
    } });

  // 2 the maths
  SP.push({ line: 2, bg: BG.cream, note: 'EXAMPLE MATH · MISAAL HAI', rows: [['Sau mein se', 56, 'white'], ['[35|paintees] wapas,', 78, 'red'], ['har parcel par', 56, 'white'], ['[Rs. 350|teen sau pachaas rupay.]', 60, 'amber']],
    build(sc, X) {
      K.receipt(sc, X, { title: 'EK MAHINE KA HISAAB', rows: [
        { l: 'Orders', r: '100', at: X.ts('Sau') + .05 }, { l: 'Wapas aaye', r: '35', at: X.ts('paintees') + .05, col: RED }, { l: 'Loss har parcel', r: 'Rs. 350', at: X.ts('teen') + .05 }],
        total: { l: 'TOTAL NUKSAAN', r: '-Rs. 12,250', at: X.te('rupay') - .1 } });
    } });

  // 3 the fix: WhatsApp confirmation
  SP.push({ line: 3, bg: BG.mint, rows: [['Fix:', 70, 'lime'], ['order aate hi', 60, 'white'], ['WhatsApp par', 66, 'white'], ['confirm karwao.', 70, 'lime']],
    build(sc, X) {
      K.chat(sc, X, { left: 262, title: 'Zara Lawn House', sub: 'Business account', avatar: '#ff5fa2', msgs: [
        { who: 'r', label: 'AUTO · A I', text: 'Salam! Aapka order: Lawn suit, Rs. 3,200. Confirm karein?', at: X.ts('WhatsApp'), lc: '#128c7e' },
        { who: 'r', text: '1 = Haan   |   2 = Nahi', at: X.ts('confirm'), bg: '#fff3b0', sfx: 'ding' }],
        items: [{ t: 'bot', x: 120, y: 560, s: .95, mood: 'open', at: X.t0 + .1, wave: X.ts('order'), act: [X.ts('order'), X.ts('confirm')] },
          { t: 'ico', name: 'suit', x: 120, y: 250, s: 1.2, at: X.t0 + .15, bob: 4 }, { t: 'ico', name: 'wa', x: 120, y: 130, s: 1.1, at: X.ts('WhatsApp'), wig: 6 }] });
    } });

  // 4 haan / nahi
  SP.push({ line: 4, bg: BG.dark, rows: [['Haan bola', 72, 'lime'], ['to parcel nikalta hai,', 46, 'white'], ['nahi bola', 72, 'red'], ['to paise bache.', 60, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'rect', x: 165, y: 300, w: 290, h: 470, rx: 30, fill: '#10260a', stroke: LIME, sw: 6, at: X.t0 + .05, sfx: null },
        { t: 'text', txt: 'HAAN', x: 165, y: 120, size: 56, col: LIME, at: X.ts('Haan'), sfx: 'pop' },
        { t: 'ico', name: 'thumbs', x: 165, y: 230, s: 1.4, at: X.ts('bola'), opt: { col: LIME } },
        { t: 'ico', name: 'truck', x: 165, y: 400, s: 1.35, at: X.ts('parcel'), wig: 8, sfx: 'whoosh' },
        { t: 'rect', x: 475, y: 300, w: 290, h: 470, rx: 30, fill: '#2a0d0a', stroke: RED, sw: 6, at: X.ts('nahi'), sfx: null },
        { t: 'text', txt: 'NAHI', x: 475, y: 120, size: 56, col: RED, at: X.ts('nahi'), sfx: 'pop' },
        { t: 'ico', name: 'moneybag', x: 475, y: 270, s: 1.5, at: X.ts('paise'), wig: 5 },
        { t: 'bills', x: 475, y: 250, to: [475, 250], n: 4, at: X.ts('paise'), dur: .9, gap: .12, spread: 150, arc: 120, sfx: 'coin' },
        { t: 'stamp', x: 345, y: 400, text: 'BACH GAYE', fg: INK, bg: LIME, rot: -8, at: X.ts('bache'), size: 40 }
      ], punch: [X.ts('Haan'), X.ts('nahi')] });
    } });

  // 5 return rate falls (industry range)
  SP.push({ line: 5, bg: BG.navy, note: 'SOURCE: eGROW COD GUIDE 2026 · INDUSTRY RANGE', rows: [['Guides ke mutabiq,', 52, 'white'], ['wapsi', 84, 'white'], ['aadhi reh sakti hai.', 60, 'lime']],
    build(sc, X) {
      K.bars(sc, X, { bw: 190, base: 470, maxH: 320, bars: [
        { label: 'PEHLE', v: 35, h: 1, col: RED, at: X.ts('Guides') + .1, suf: '%', pre: '~' },
        { label: 'BAAD MEIN', lsize: 22, v: 18, h: .52, col: LIME, at: X.ts('aadhi'), fg: LIME, suf: '%', pre: '~' }],
        items: [{ t: 'arrow', x1: 235, y1: 150, x2: 400, y2: 250, col: '#fff', at: X.ts('aadhi') - .1 }, { t: 'text', txt: 'WAPSI KA RATE', x: 320, y: 70, size: 34, col: '#fff', at: X.t0 + .1, sfx: null }] });
    } });

  // 6 share, 7 CTA
  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Confirm bot', 64, 'white'], ['chahiye?', 70, 'white'], ['Comment', 60, 'white'], ['CONFIRM.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'CONFIRM' }); } });

  window.SCENE_SPECS = SP;
})();
