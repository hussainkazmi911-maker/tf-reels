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
        pg.goto('file://' + os.getcwd() + '/reel.html')
        pg.evaluate('document.fonts.ready')
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
        pg0.goto('file://' + os.getcwd() + '/reel.html'); pg0.wait_for_timeout(500)
        sc = pg0.evaluate("SCENES.map(s=>[s.t0,s.t1])")
        b0.close()
    ts = []
    for t0, t1 in sc:
        d = t1 - t0
        ts += [t0 + d * .3, t0 + d * .65, t1 - .08]
    run([int(x * 30) for x in ts], 'test', 1)
    print(len(ts), 'test frames', [round(x, 2) for x in ts])
else:
    n = int(a[2]); k = int(a[3]); tot = int(T['total'] * 30) + 1
    run(range(k, tot, n), 'frames', 1.5)
