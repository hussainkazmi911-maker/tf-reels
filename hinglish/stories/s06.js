/* s06: sale rush - "Do lakh rupay ke ads lagaye, ab chaar sau messages kaun sambhalega?" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.red, rows: [['[Rs. 2,00,000|Do lakh rupay]', 70, 'amber'], ['ke ads lagaye,', 64, 'white'], ['ab [400|chaar sau] messages', 52, 'white'], ['kaun sambhalega?', 66, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 80, from: 0, to: 200000, t0: X.ts('Do') + .05, t1: X.te('rupay'), pre: 'Rs. ', col: AMB, w: 540, size: 62, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'ig', x: 130, y: 300, s: 1.5, at: X.ts('ads'), wig: 5 },
        { t: 'ico', name: 'wa', x: 270, y: 330, s: 2.4, at: X.ts('chaar'), wig: 5 },
        { t: 'badge', x: 340, y: 262, r: 40, n: t => Math.min(400, Math.floor(400 * Math.max(0, Math.min(1, (t - X.ts('chaar')) / (X.te('messages') - X.ts('chaar')))))), at: X.ts('chaar'), sfx: 'ding' },
        { t: 'person', x: 500, y: 570, s: 1.25, shirt: '#7d5fff', at: X.ts('kaun') - .2, mood: 'worry' },
        { t: 'text', txt: '?', x: 450, y: 330, size: 100, col: '#fff', at: X.ts('kaun'), wig: 6, sfx: 'buzz' },
        { t: 'text', txt: '?', x: 560, y: 300, size: 80, col: AMB, at: X.ts('sambhalega'), wig: 7 }
      ], punch: [X.t0 + .1, X.ts('chaar'), X.ts('kaun')] });
    } });

  // 1 two people, one phone, 400 messages in an hour
  SP.push({ line: 1, bg: BG.warm, rows: [['Do log, ek phone,', 62, 'white'], ['aur ek ghante mein', 56, 'white'], ['[400|chaar sau] messages.', 76, 'red']],
    build(sc, X) {
      const pills = [['Price?', 90, 175], ['Stock hai?', 545, 215], ['COD hai?', 95, 250], ['Order?', 555, 330]];
      K.stage(sc, X, { floor: '#c9783f', floorY: 520, items: [
        { t: 'person', x: 120, y: 570, s: 1.15, shirt: '#ff7a3d', at: X.ts('Do') - .05, mood: 'worry' },
        { t: 'person', x: 215, y: 570, s: 1.15, shirt: '#7d5fff', at: X.ts('log'), flip: false, mood: 'worry' },
        { t: 'ico', name: 'phone', x: 420, y: 350, s: 1.9, at: X.ts('phone'), opt: { scr: '#17331f' }, wig: 16 },
        ...pills.map((p, i) => ({ t: 'rect', x: p[1], y: p[2], w: 132, h: 44, rx: 22, fill: '#fff', txt: p[0], size: 21, at: X.ts('ghante') + i * .25, sfx: 'ding' })),
        { t: 'ico', name: 'clock', x: 575, y: 110, s: .75, at: X.ts('ghante'), wig: 4 },
        { t: 'counter', x: 300, y: 80, from: 0, to: 400, t0: X.ts('chaar'), t1: X.te('messages'), pre: '', post: ' MESSAGES', col: RED, w: 360, size: 40, at: X.ts('chaar') - .1, tickSfx: true }
      ], punch: [X.ts('phone'), X.ts('chaar')] });
    } });

  // 2 others leave while you reply to the first
  SP.push({ line: 2, bg: BG.dark, rows: [['Jab tak pehle ko', 56, 'white'], ['reply karoge,', 66, 'lime'], ['baaqi customers', 62, 'white'], ['tab band kar denge.', 56, 'red']],
    build(sc, X) {
      const tL = X.ts('baaqi');
      K.stage(sc, X, { items: [
        { t: 'fn', f: (g, sc2) => {
          for (let i = 0; i < 6; i++) {
            const x = 70 + i * 100, y = 360, e = S(g, 'g');
            const head = S(e, 'circle', { cx: 0, cy: -40, r: 24, fill: i === 0 ? LIME : '#ffd9a0', stroke: INK, 'stroke-width': 5 });
            const body = S(e, 'path', { d: 'M-32 50 q0 -66 32 -66 q32 0 32 66z', fill: i === 0 ? LIME : '#ff7a3d', stroke: INK, 'stroke-width': 5, 'stroke-linejoin': 'round' });
            const at = X.t0 + .1 + i * .1, gone = tL + .2 + (i - 1) * .12;
            sc2.u.push(t => { const p = P(t, at, at + .25); let op = p > 0 ? 1 : 0, dy = 0, gray = false;
              if (i > 0 && t >= gone) { const q = P(t, gone, gone + .6); op = 1 - q; dy = -80 * eOut(q); gray = true; }
              e.style.opacity = op; if (gray) { head.setAttribute('fill', '#8b93a8'); body.setAttribute('fill', '#8b93a8'); } else if (i > 0) { head.setAttribute('fill', '#ffd9a0'); body.setAttribute('fill', '#ff7a3d'); }
              tf(e, x, y + dy, 0, Math.max(0, eBack(p))); });
            if (i > 0) X.sfx(gone, 'tick', .5);
          } } },
        { t: 'rect', x: 70, y: 200, w: 110, h: 44, rx: 22, fill: LIME, txt: 'REPLY', size: 24, at: X.ts('reply'), sfx: 'pop' },
        { t: 'text', txt: 'WAIT...', x: 400, y: 150, size: 44, col: AMB, at: X.ts('tak'), wig: 5, sfx: 'tick' },
        { t: 'stamp', x: 190, y: 470, text: 'BAND KAR DENGE', fg: '#fff', bg: RED, rot: -6, at: X.ts('band'), size: 38 }
      ], punch: [X.ts('baaqi'), X.ts('band')] });
    } });

  // 3 speed = sales
  SP.push({ line: 3, bg: BG.purple, rows: [['Sale mein', 66, 'white'], ['jawab ki raftaar', 66, 'lime'], ['paisa banati hai.', 66, 'amber']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'bolt', x: 170, y: 270, s: 2.3, at: X.ts('raftaar'), wig: 9, sfx: 'zap' },
        { t: 'ico', name: 'clock', x: 440, y: 230, s: 1.6, at: X.ts('jawab'), wig: 4 },
        { t: 'ico', name: 'moneybag', x: 440, y: 450, s: 1.5, at: X.ts('paisa'), wig: 5 },
        { t: 'bills', x: 440, y: 260, to: [440, 440], n: 6, at: X.ts('paisa'), dur: .8, gap: .09, spread: 80, arc: 40, sfx: 'coin' },
        { t: 'rect', x: 170, y: 460, w: 250, h: 62, rx: 31, fill: LIME, txt: 'SPEED = SALE', size: 30, at: X.ts('Sale'), sfx: 'pop' }
      ], punch: [X.ts('raftaar'), X.ts('paisa')] });
    } });

  // 4 AI answers all at once
  SP.push({ line: 4, bg: BG.mint, rows: [['A I sabko ek saath', 56, 'lime'], ['jawab deta hai:', 58, 'white'], ['price, stock,', 66, 'white'], ['order link.', 72, 'lime']],
    build(sc, X) {
      K.chat(sc, X, { left: 282, title: 'Sale Store', sub: 'Auto reply ON', avatar: '#ff5fa2', msgs: [
        { who: 'c', text: 'Price?', at: X.t0 + .12 }, { who: 'c', text: 'Stock hai?', at: X.t0 + .3 },
        { who: 'r', label: 'AUTO · A I', text: 'Price: Rs. 2,999', at: X.ts('price') },
        { who: 'r', text: 'Stock: available', at: X.ts('stock') },
        { who: 'r', text: 'Order link: tap karein', at: X.ts('order'), bg: '#fff3b0', sfx: 'ding' }],
        items: [
          { t: 'bot', x: 125, y: 545, s: .9, mood: 'happy', at: X.t0 + .1, act: [X.ts('sabko'), X.te('link')] },
          { t: 'ico', name: 'wa', x: 125, y: 180, s: 1.3, at: X.ts('sabko'), wig: 6 },
          { t: 'rect', x: 125, y: 300, w: 170, h: 54, rx: 27, fill: LIME, txt: 'EK SAATH', size: 24, at: X.ts('saath'), sfx: 'success' }] });
    } });

  // 5 team only packs and dispatches
  SP.push({ line: 5, bg: BG.warm, rows: [['Aapki team sirf', 58, 'white'], ['packing aur dispatch', 56, 'lime'], ['sambhale.', 80, 'white']],
    build(sc, X) {
      K.stage(sc, X, { floor: '#c9783f', floorY: 520, items: [
        { t: 'person', x: 100, y: 570, s: 1.15, shirt: '#ff7a3d', at: X.t0 + .1, mood: 'smile' },
        { t: 'person', x: 200, y: 570, s: 1.15, shirt: '#7d5fff', at: X.t0 + .2, mood: 'smile' },
        { t: 'ico', name: 'parcel', x: 300, y: 440, s: 1.0, at: X.ts('packing'), wig: 5 },
        { t: 'ico', name: 'parcel', x: 360, y: 400, s: .9, at: X.ts('packing') + .2, wig: 6, sfx: 'pop' },
        { t: 'ico', name: 'truck', x: 520, y: 420, s: 1.5, at: X.ts('dispatch'), wig: 6, sfx: 'whoosh' },
        { t: 'ico', name: 'parcel', x: 300, y: 440, s: .7, at: X.ts('dispatch') + .1, kind: 'fade', move: [X.ts('dispatch') + .15, X.ts('dispatch') + .75, 520, 400], fadeOut: [X.ts('dispatch') + .7, X.ts('dispatch') + .9], sfx: null },
        { t: 'stamp', x: 190, y: 70, text: 'SAB SMOOTH', fg: INK, bg: LIME, rot: -6, at: X.ts('sambhale'), size: 46 }
      ], punch: [X.ts('packing'), X.ts('dispatch')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Sale ke liye', 62, 'white'], ['bot chahiye?', 70, 'white'], ['Comment', 60, 'white'], ['SALE.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'SALE' }); } });

  window.SCENE_SPECS = SP;
})();
