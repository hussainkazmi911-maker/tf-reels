/* s03: Instagram DMs (jhumka seller) - "Sath hazaar rupay aapke Instagram DMs mein pade hain" */
(function () {
  const K = KIT, { BG } = K, { COL } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];

  // 0 HOOK
  SP.push({ line: 0, bg: BG.purple, rows: [['[Rs. 60,000|Sath hazaar rupay]', 84, 'amber'], ['aapke Instagram', 58, 'white'], ['DMs mein', 66, 'white'], ['pade hain.', 84, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'counter', x: 320, y: 90, from: 0, to: 60000, t0: X.ts('Sath') + .05, t1: X.te('rupay'), pre: 'Rs. ', col: AMB, w: 500, size: 70, at: X.t0 + .1, tickSfx: true },
        { t: 'ico', name: 'ig', x: 190, y: 330, s: 2.3, at: X.ts('Instagram'), wig: 5 },
        { t: 'badge', x: 262, y: 262, r: 34, n: t => Math.min(99, Math.floor(Math.max(0, t - X.ts('DMs')) * 60)), at: X.ts('DMs'), sfx: 'ding' },
        { t: 'ico', name: 'moneybag', x: 470, y: 380, s: 1.7, at: X.ts('mein'), wig: 5 },
        { t: 'bills', x: 470, y: 340, to: [470, 330], n: 5, at: X.ts('pade'), dur: .8, gap: .09, spread: 120, arc: 120, sfx: 'coin' },
        { t: 'stamp', x: 190, y: 480, text: 'UNREAD', fg: '#fff', bg: RED, rot: -8, at: X.ts('hain'), size: 54 }
      ], punch: [X.t0 + .1, X.ts('hain')] });
    } });

  // 1 customer asks, you reply next day
  SP.push({ line: 1, bg: BG.pink, rows: [['Customer ne likha:', 52, 'white'], ['jhumka ka price?', 66, 'lime'], ['Aapne agle din', 56, 'white'], ['reply kiya.', 78, 'red']],
    build(sc, X) {
      K.chat(sc, X, { left: 280, theme: 'ig', title: 'sana.style', sub: 'Active now', avatar: '#ffcf33', msgs: [
        { who: 'c', text: 'Jhumka ka price?', at: X.ts('jhumka') },
        { who: 'r', label: 'AGLE DIN', lc: '#a46bff', text: 'Rs. 1,800 ji', at: X.ts('reply'), bg: '#a46bff', sfx: 'pop' }],
        items: [
          { t: 'ico', name: 'jhumka', x: 130, y: 160, s: 1.25, at: X.ts('jhumka') - .1, bob: 4 },
          { t: 'ico', name: 'clock', x: 130, y: 380, s: 1.2, at: X.ts('agle'), wig: 3 },
          { t: 'text', txt: '24 GHANTE', x: 130, y: 490, size: 26, col: RED, at: X.ts('din'), sfx: 'buzz' }] });
    } });

  // 2 lost sale
  SP.push({ line: 2, bg: BG.red, rows: [['Tab tak woh', 66, 'white'], ['kisi aur se', 78, 'amber'], ['order kar', 60, 'white'], ['chuki thi.', 78, 'red']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'person', x: 150, y: 560, s: 1.25, shirt: '#ff5fa2', phone: true, at: X.t0 + .1, mood: 'neutral', moodAt: [[X.ts('order'), 'smile']] },
        { t: 'ico', name: 'store', x: 500, y: 320, s: 1.7, at: X.ts('kisi'), opt: { name: 'DOOSRA' }, wig: 3 },
        { t: 'arrow', x1: 190, y1: 330, x2: 420, y2: 320, col: '#fff', at: X.ts('aur') },
        { t: 'rect', x: 290, y: 175, w: 300, h: 60, rx: 30, fill: COL.wa, txt: 'ORDER PLACED', size: 26, col: '#fff', at: X.ts('order'), sfx: 'ding' },
        { t: 'bills', x: 190, y: 330, to: [500, 320], n: 5, at: X.ts('kar'), dur: .8, gap: .08, spread: 40, arc: 90, sfx: 'coin' },
        { t: 'stamp', x: 150, y: 30, text: 'SALE GAYI', fg: '#fff', bg: INK, rot: -6, at: X.ts('thi'), size: 60 }
      ], punch: [X.ts('kisi'), X.ts('thi')] });
    } });

  // 3 the maths
  SP.push({ line: 3, bg: BG.cream, note: 'EXAMPLE MATH · MISAAL HAI', rows: [['Roz paanch aise DMs,', 52, 'white'], ['har order par', 52, 'white'], ['[Rs. 400|chaar sau rupay,]', 70, 'amber'], ['mahine ke [Rs. 60,000|sath hazaar.]', 56, 'red']],
    build(sc, X) {
      K.receipt(sc, X, { title: 'DMs KA HISAAB', rows: [
        { l: 'Miss DMs roz', r: '5', at: X.ts('paanch') }, { l: 'Munafa har order', r: 'Rs. 400', at: X.ts('chaar') }, { l: 'Mahine ke din', r: 'x 30', at: X.ts('mahine') }],
        total: { l: 'MAHINE KA NUKSAAN', r: '-Rs. 60,000', at: X.te('sath') } });
    } });

  // 4 the fix: auto reply
  SP.push({ line: 4, bg: BG.mint, rows: [['Auto reply laga lo:', 52, 'lime'], ['price, catalogue,', 60, 'white'], ['order link,', 60, 'white'], ['teen second mein.', 66, 'lime']],
    build(sc, X) {
      K.chat(sc, X, { left: 280, theme: 'ig', title: 'sana.style', sub: 'Auto reply ON', avatar: '#ffcf33', msgs: [
        { who: 'c', text: 'Jhumka ka price?', at: X.t0 + .15 },
        { who: 'r', label: 'AUTO · A I', lc: '#fff', text: 'Price: Rs. 1,800', at: X.ts('price'), bg: '#a46bff' },
        { who: 'r', text: 'Catalogue dekhein', at: X.ts('catalogue'), bg: '#a46bff' },
        { who: 'r', text: 'Order link: tap karein', at: X.ts('order'), bg: '#a46bff' }],
        items: [
          { t: 'bot', x: 120, y: 520, s: .95, mood: 'happy', at: X.t0 + .1, act: [X.ts('price'), X.ts('teen')] },
          { t: 'ico', name: 'clock', x: 120, y: 130, s: 1.1, at: X.ts('teen'), wig: 4 },
          { t: 'rect', x: 120, y: 240, w: 170, h: 54, rx: 27, fill: LIME, txt: '3 SECOND', size: 24, at: X.ts('second'), sfx: 'success' }] });
    } });

  // 5 you sleep, DMs make sales
  SP.push({ line: 5, bg: BG.night, rows: [['Aap sote raho,', 66, 'white'], ['DMs sale', 80, 'lime'], ['banate rahein.', 66, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'person', x: 140, y: 570, s: 1.25, shirt: '#7d5fff', mood: 'sleep', at: X.t0 + .1 },
        { t: 'text', txt: 'Zzz', x: 190, y: 330, size: 54, col: '#fff', at: X.ts('sote'), wig: 4, bob: 6 },
        { t: 'ico', name: 'phone', x: 440, y: 370, s: 2.0, at: X.ts('DMs'), opt: { scr: '#17331f' }, wig: 12 },
        { t: 'ico', name: 'bell', x: 530, y: 250, s: .9, at: X.ts('sale'), wig: 12, sfx: 'ding' },
        { t: 'counter', x: 440, y: 95, from: 0, to: 3, t0: X.ts('banate'), t1: X.te('rahein'), pre: '', post: ' ORDERS', sign: '+', col: LIME, w: 320, size: 42, at: X.ts('DMs') + .1, tickSfx: true },
        { t: 'rect', x: 440, y: 330, w: 112, h: 34, rx: 10, fill: LIME, txt: 'ORDER', size: 18, at: X.ts('banate'), sfx: 'ding' },
        { t: 'rect', x: 440, y: 378, w: 112, h: 34, rx: 10, fill: LIME, txt: 'ORDER', size: 18, at: X.ts('banate') + .5, sfx: 'ding' },
        { t: 'rect', x: 440, y: 426, w: 112, h: 34, rx: 10, fill: LIME, txt: 'ORDER', size: 18, at: X.ts('rahein'), sfx: 'ding' },
        { t: 'bills', x: 440, y: 330, to: [440, 190], n: 4, at: X.ts('banate'), dur: .8, gap: .12, spread: 90, arc: 60, sfx: 'coin' },
        { t: 'ico', name: 'coin', x: 540, y: 420, s: 1.1, at: X.ts('rahein'), wig: 6 }
      ], punch: [X.ts('DMs'), X.ts('banate')] });
    } });

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['DMs sale', 64, 'white'], ['banana hai?', 70, 'white'], ['Comment', 60, 'white'], ['REPLY.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'REPLY' }); } });

  window.SCENE_SPECS = SP;
})();
