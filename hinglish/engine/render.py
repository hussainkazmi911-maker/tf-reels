# usage: python3 render.py test | python3 render.py run N K   (K=0..N-1, run N workers in parallel)
import json, sys, os
from playwright.sync_api import sync_playwright
T = json.load(open('timing.json'))

def run(frames, outdir, scale):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 720, 'height': 1280}, device_scale_factor=scale)
        msgs = []
        pg.on('pageerror', lambda e: msgs.append('ERR ' + str(e)))
        pg.on('console', lambda m: msgs.append('LOG ' + m.text) if m.type == 'error' else None)
        pg.goto('file://' + os.getcwd() + '/engine.html')
        pg.evaluate("Promise.all([document.fonts.load('40px \"Archivo Black\"'),document.fonts.load('500 30px Inter'),document.fonts.load('700 30px Inter'),document.fonts.load('800 30px Inter'),document.fonts.load('40px NCE')]).then(()=>document.fonts.ready)")
        pg.evaluate('refit()')
        pg.wait_for_timeout(700)
        for f in frames:
            pg.evaluate(f"draw({f/30})")
            pg.screenshot(path=f"{outdir}/f_{f:05d}.png")
        if msgs: print(msgs[:6])
        b.close()

a = sys.argv
if a[1] == 'test':
    with sync_playwright() as p0:
        b0 = p0.chromium.launch()
        pg0 = b0.new_page(viewport={'width': 720, 'height': 1280})
        pg0.goto('file://' + os.getcwd() + '/engine.html'); pg0.wait_for_timeout(500)
        sc = pg0.evaluate("SCENES.map(s=>[s.t0,s.t1])")
        b0.close()
    ts = []
    for t0, t1 in sc:
        d = t1 - t0
        ts += [t0 + d * .3, t0 + d * .65, t1 - .08]
    run([int(x * 30) for x in ts], 'test', 1)
    print(len(ts), 'test frames', [round(x, 2) for x in ts])
elif a[1] == 'dense':   # 6 frames per scene incl. mid-transition frames -> dense/ (for motion review)
    with sync_playwright() as p0:
        b0 = p0.chromium.launch()
        pg0 = b0.new_page(viewport={'width': 720, 'height': 1280})
        pg0.goto('file://' + os.getcwd() + '/engine.html'); pg0.wait_for_timeout(500)
        sc = pg0.evaluate("SCENES.map(s=>[s.t0,s.t1])")
        b0.close()
    ts = []
    for i, (t0, t1) in enumerate(sc):
        d = t1 - t0
        ts += [t0 - .1 if i else t0 + .02, t0 + .06 if i else t0 + .3, t0 + .5, t0 + d * .45, t0 + d * .75, t1 - .3]
    run([int(x * 30) for x in ts], 'dense', 1)
    print(len(ts), 'dense frames')
else:
    n = int(a[2]); k = int(a[3]); tot = int(T['total'] * 30) + 1
    sc = float(a[4]) if len(a) > 4 else 1.5
    run(range(k, tot, n), 'frames_prev' if sc < 1.5 else 'frames', sc)
