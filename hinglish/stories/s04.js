/* s04: abandoned carts (sneakers) - "Ek lakh rupay ke sneakers aapke cart mein chhode hue hain" */
(function () {
  const K = KIT, { BG } = K, { COL, S, tf, P, eOut, eBack, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.teal, rows: [['[Rs. 1,00,000|Ek lakh rupay]', 74, 'amber'], ['ke sneakers', 70, 'white'], ['aapke cart mein', 64, 'white'], ['chhode hue hain.', 66, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 90, from: 0, to: 100000, t0: X.ts('Ek') + .05, t1: X.te('rupay'), pre: 'Rs. ', col: AMB, w: 520, size: 66, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'cart', x: 320, y: 380, s: 2.5, at: X.t0 + .15, wig: 3 },
        { t: 'ico', name: 'sneaker', x: 290, y: 330, s: 1.0, at: X.ts('sneakers'), kind: 'drop', sfx: 'pop', r: -10 },
        { t: 'ico', name: 'sneaker', x: 360, y: 300, s: .9, at: X.ts('sneakers') + .18, kind: 'drop', sfx: 'pop', r: 12, opt: { col: '#33d6ff' } },
        { t: 'ico', name: 'ghost', x: 520, y: 220, s: 1.4, at: X.ts('chhode'), bob: 8 },
        { t: 'stamp', x: 150, y: 470, text: 'ABANDONED', fg: '#fff', bg: RED, rot: -7, at: X.ts('hain'), size: 38 }
      ], punch: [X.t0 + .15, X.ts('chhode')] });
    } });

  // 1 picks size, adds to cart, phone rings
  SP.push({ line: 1, bg: BG.sky, rows: [['Customer ne size chuna,', 54, 'white'], ['cart mein dala,', 66, 'lime'], ['phir call', 70, 'white'], ['aa gaya.', 84, 'red']],
    build(sc, X) {
      const rg = (at, n) => Array.from({ length: n }, (_, i) => ({ t: 'ring', x: 520, y: 220, at: at + i * .45, r0: 30, r1: 110, w: 6, col: RED, dur: .7 }));
      K.stage(sc, X, { floor: '#7dc9ef', floorY: 520, items: [
        { t: 'person', x: 120, y: 560, s: 1.15, shirt: '#ff7a3d', at: X.t0 + .1, mood: 'smile', moodAt: [[X.ts('call'), 'wow']] },
        { t: 'ico', name: 'sneaker', x: 250, y: 170, s: 1.1, at: X.t0 + .15, bob: 4 },
        { t: 'rect', x: 250, y: 250, w: 150, h: 48, rx: 24, fill: LIME, txt: 'SIZE 9', size: 26, at: X.ts('size'), sfx: 'tick' },
        { t: 'ico', name: 'cart', x: 380, y: 420, s: 1.7, at: X.ts('cart'), wig: 3 },
        { t: 'ico', name: 'sneaker', x: 250, y: 170, s: .8, at: X.ts('dala'), kind: 'fade', move: [X.ts('dala'), X.te('dala') + .35, 380, 400], sfx: 'whoosh', fadeOut: [X.te('dala') + .3, X.te('dala') + .5] },
        { t: 'ico', name: 'phone', x: 520, y: 220, s: 1.4, at: X.ts('call'), wig: 50, opt: { scr: '#17331f' } },
        ...rg(X.ts('call'), 4),
        { t: 'rect', x: 520, y: 220, w: 100, h: 44, rx: 12, fill: COL.wa, txt: 'CALL', size: 22, col: '#fff', at: X.ts('call') + .1, sfx: null, s: .8 }
      ], punch: [X.ts('cart'), X.ts('call')] });
    } });

  // 2 7 out of 10 abandon (Baymard)
  SP.push({ line: 2, bg: BG.navy, note: 'SOURCE: BAYMARD INSTITUTE · AVG ~70%', rows: [['Research ke mutabiq,', 52, 'white'], ['[7/10|dus mein se saat]', 84, 'red'], ['log cart', 60, 'white'], ['chhod dete hain.', 60, 'white']],
    build(sc, X) {
      const t7 = X.ts('saat'), tm = X.ts('dus');
      K.stage(sc, X, { items: [
        { t: 'fn', f: (g, sc2) => {
          for (let i = 0; i < 10; i++) {
            const col = i % 5, row = Math.floor(i / 5), x = 100 + col * 110, y = 210 + row * 175, e = S(g, 'g');
            const head = S(e, 'circle', { cx: 0, cy: -34, r: 22, fill: LIME, stroke: INK, 'stroke-width': 5 });
            const body = S(e, 'path', { d: 'M-30 40 q0 -62 30 -62 q30 0 30 62z', fill: LIME, stroke: INK, 'stroke-width': 5, 'stroke-linejoin': 'round' });
            const cartI = S(e, 'g', { transform: 'translate(0,48) scale(.5)' }); K.ICO.cart(cartI, {});
            const at = tm + i * .09, flip = t7 + .1 + i * .11;
            sc2.u.push(t => { const p = P(t, at, at + .25); e.style.opacity = p > 0 ? 1 : 0; const bad = i < 7 && t >= flip;
              const c = bad ? RED : LIME; head.setAttribute('fill', c); body.setAttribute('fill', c);
              const j = bad ? Math.sin(t * 22 + i) * 2 : 0; tf(e, x + j, y, 0, Math.max(0, eBack(p))); });
            X.sfx(at, 'tick', .5); if (i < 7) X.sfx(flip, 'buzz', .25);
          } } },
        { t: 'text', txt: '7 / 10', x: 320, y: 90, size: 64, col: RED, at: t7, sfx: 'stamp' }
      ], punch: [t7] });
    } });

  // 3 you forget, system does not
  SP.push({ line: 3, bg: BG.dark, rows: [['Aap bhool gaye.', 70, 'red'], ['Smart system', 66, 'white'], ['nahi bhoolta.', 74, 'lime']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'rect', x: 165, y: 300, w: 290, h: 470, rx: 30, fill: '#2a0d0a', stroke: RED, sw: 6, at: X.t0 + .05, sfx: null },
        { t: 'text', txt: 'AAP', x: 165, y: 110, size: 50, col: RED, at: X.t0 + .1, sfx: 'pop' },
        { t: 'person', x: 165, y: 470, s: 1.1, shirt: '#ff7a3d', at: X.t0 + .2, mood: 'sleep' },
        { t: 'text', txt: '?!', x: 235, y: 235, size: 64, col: RED, at: X.ts('bhool'), wig: 6, sfx: 'buzz' },
        { t: 'rect', x: 475, y: 300, w: 290, h: 470, rx: 30, fill: '#10260a', stroke: LIME, sw: 6, at: X.ts('Smart'), sfx: null },
        { t: 'text', txt: 'SYSTEM', x: 475, y: 110, size: 50, col: LIME, at: X.ts('Smart'), sfx: 'pop' },
        { t: 'bot', x: 475, y: 470, s: .95, mood: 'happy', at: X.ts('system'), act: [X.ts('nahi'), X.te('bhoolta') + .6] },
        { t: 'ico', name: 'bell', x: 475, y: 240, s: 1.2, at: X.ts('nahi'), wig: 14, sfx: 'ding' }
      ], punch: [X.ts('bhool'), X.ts('nahi')] });
    } });

  // 4 1 hour later WhatsApp
  SP.push({ line: 4, bg: BG.mint, rows: [['Ek ghante baad', 62, 'white'], ['WhatsApp:', 76, 'lime'], ['aapke sneakers', 62, 'white'], ['wait kar rahe hain.', 58, 'white']],
    build(sc, X) {
      K.chat(sc, X, { left: 282, title: 'Kicks Corner', sub: 'Business account', avatar: '#4db8ff', msgs: [
        { who: 'r', label: 'AUTO · A I', text: 'Aapke sneakers wait kar rahe hain! Size 9 stock mein hai.', at: X.ts('WhatsApp') },
        { who: 'r', text: 'Order complete karein', at: X.ts('wait'), bg: '#fff3b0', sfx: 'ding' }],
        items: [
          { t: 'ico', name: 'clock', x: 125, y: 150, s: 1.15, at: X.t0 + .1, wig: 4 },
          { t: 'rect', x: 125, y: 255, w: 160, h: 50, rx: 25, fill: LIME, txt: '1 GHANTA', size: 24, at: X.ts('ghante'), sfx: 'success' },
          { t: 'ico', name: 'sneaker', x: 125, y: 420, s: 1.0, at: X.ts('aapke'), bob: 4 }] });
    } });

  // 5 customer comes back, order done, money in
  SP.push({ line: 5, bg: BG.warm, rows: [['Customer wapas aaya,', 54, 'white'], ['order complete,', 64, 'lime'], ['paise aapke', 66, 'white'], ['account mein.', 72, 'white']],
    build(sc, X) {
      K.stage(sc, X, { floor: '#c9783f', floorY: 520, items: [
        { t: 'person', x: 90, y: 560, s: 1.15, shirt: '#7d5fff', at: X.t0 + .1, walk: [X.ts('wapas'), X.te('aaya') + .3, 190], mood: 'smile' },
        { t: 'ico', name: 'cart', x: 340, y: 250, s: 1.4, at: X.ts('order'), wig: 3 },
        { t: 'ico', name: 'ok', x: 340, y: 250, s: 1, at: X.te('complete') - .2, kind: 'pop', sfx: 'success', opt: {} },
        { t: 'stamp', x: 180, y: 60, text: 'ORDER DONE', fg: INK, bg: LIME, rot: -6, at: X.te('complete'), size: 50 },
        { t: 'ico', name: 'moneybag', x: 500, y: 400, s: 1.7, at: X.ts('paise'), wig: 5 },
        { t: 'bills', x: 280, y: 360, to: [500, 400], n: 6, at: X.ts('paise') + .1, dur: .8, gap: .09, spread: 50, arc: 100, sfx: 'coin' },
        { t: 'conf', x: 500, y: 380, at: X.ts('account'), n: 26, seed: 7 }
      ], punch: [X.te('complete'), X.ts('account')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Cart wapas', 64, 'white'], ['lana hai?', 70, 'white'], ['Comment', 60, 'white'], ['CART.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'CART' }); } });

  window.SCENE_SPECS = SP;
})();
