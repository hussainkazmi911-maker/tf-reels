# usage (from work/sNN): python3 ../../engine/dump_sfx.py  -> sfx.json, sfx.wav
import json, os, subprocess
from playwright.sync_api import sync_playwright
T = json.load(open('timing.json'))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 720, 'height': 1280})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + os.getcwd() + '/engine.html'); pg.wait_for_timeout(600)
    s = pg.evaluate('getSfx()'); b.close()
if errs: print('ERR', errs[:3])
json.dump(s, open('sfx.json', 'w'))
subprocess.run(['python3', '../../engine/sfx.py', 'sfx.json', 'sfx.wav', str(T['total'] + 1)], check=True)
print('sfx events', len(s))
