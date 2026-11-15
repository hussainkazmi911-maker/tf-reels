/* s10: 30-day plan (marketing) - "Aapke marketing ka har rupay, pehle tees din mein hum kahan lagate hain?" */
(function () {
  const K = KIT, { BG } = K, { COL, S, T, tf, P, eOut, eBack, eIO, lerp } = SL, LIME = COL.lime, INK = COL.ink, RED = COL.red, AMB = COL.amber;
  const SP = [];
  const NODES = [
    { d: 1, title: 'AUDIT', sub: 'Store, page, ads' }, { d: 3, title: 'FIX', sub: 'Profile, catalogue, auto reply' },
    { d: 7, title: 'LAUNCH', sub: 'Pehli reels + ads live' }, { d: 14, title: 'OPTIMISE', sub: 'Jo chala, usme budget' }, { d: 30, title: 'REPORT', sub: 'Orders + agle mahine ka plan' }];

  // 0 HOOK: every rupee across 30 days
  SP.push({ line: 0, bg: BG.dark, rows: [['Aapke marketing ka', 56, 'white'], ['har rupay,', 84, 'amber'], ['pehle [30|tees] din mein', 58, 'lime'], ['hum kahan lagate hain?', 52, 'white']],
    build(sc, X) {
      K.stage(sc, X, { items: [
        { t: 'ico', name: 'moneybag', x: 320, y: 95, s: 1.3, at: X.ts('rupay'), wig: 5 },
        { t: 'fn', f: (g, sc2) => {
          for (let i = 0; i < 30; i++) {
            const x = 75 + (i % 6) * 98, y = 215 + Math.floor(i / 6) * 75, e = S(g, 'g'), at = X.ts('tees') + i * .045;
            S(e, 'rect', { x: -40, y: -30, width: 80, height: 60, rx: 12, fill: i === 29 ? LIME : '#162008', stroke: LIME, 'stroke-width': 4 });
            T(e, String(i + 1), 0, 9, 26, i === 29 ? INK : '#fff');
            sc2.u.push(t => { const p = P(t, at, at + .2); e.style.opacity = p > 0 ? 1 : 0; tf(e, x, y, 0, Math.max(0, eBack(p))); });
            if (i % 3 === 0) X.sfx(at, 'tick', .5);
          } } },
        { t: 'bills', x: 320, y: 100, to: [320, 380], n: 6, at: X.ts('lagate'), dur: .9, gap: .1, spread: 220, arc: 30, sfx: 'coin' }
      ], punch: [X.ts('rupay'), X.ts('tees')] });
    } });

  const tl = (line, active, rows) => ({ line, bg: BG.dark, note: false, rows, build(sc, X) { K.timeline(sc, X, { nodes: NODES, active, at: X.t0 + .15 }); } });
  SP.push(tl(1, 0, [['[Din 1:|Din ek]', 66, 'lime'], ['store, page aur ads', 54, 'white'], ['ka poora audit.', 62, 'white']]));
  SP.push(tl(2, 1, [['[Din 3:|Din teen]', 66, 'lime'], ['profile, catalogue aur', 50, 'white'], ['WhatsApp auto reply', 54, 'white'], ['theek.', 76, 'lime']]));
  SP.push(tl(3, 2, [['[Din 7:|Din saat]', 66, 'lime'], ['pehli reels', 72, 'white'], ['aur ads live.', 72, 'white']]));
  SP.push(tl(4, 3, [['[Din 14:|Din chaudah]', 62, 'lime'], ['jo chala usme', 58, 'white'], ['budget badhate hain,', 54, 'lime'], ['jo nahi chala, band.', 54, 'red']]));
  SP.push(tl(5, 4, [['[Din 30:|Din tees]', 66, 'lime'], ['report, orders aur', 56, 'white'], ['agle mahine ka plan.', 52, 'white']]));

  SP.push({ line: 6, bg: BG.purple, note: false, rows: [['Yeh reel', 74, 'white'], ['kisi seller ko', 66, 'lime'], ['bhejein.', 90, 'white']], build(sc, X) { K.share(sc, X, {}); } });
  SP.push({ line: 7, bg: BG.dark, note: false, rows: [['Tees din ka plan', 56, 'white'], ['chahiye?', 70, 'white'], ['Comment', 60, 'white'], ['PLAN.', 96, 'lime']], build(sc, X) { K.cta(sc, X, { word: 'PLAN', kwIndex: 6 }); } });

  window.SCENE_SPECS = SP;
})();
