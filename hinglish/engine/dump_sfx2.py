# usage (from work/IDv2): python3 ../../engine/dump_sfx2.py -> sfx.json, sfx.wav (soft UI SFX), music.wav (bed)
import json, os, subprocess
from playwright.sync_api import sync_playwright
T = json.load(open('timing.json'))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 720, 'height': 1280}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + os.getcwd() + '/engine.html'); pg.wait_for_timeout(600); s = pg.evaluate('getSfx()'); b.close()
if errs: print('ERR', errs[:3])
json.dump(s, open('sfx.json', 'w'))
tot = T['total'] + 1
subprocess.run(['python3', '../../engine/sfx2.py', 'sfx.json', 'sfx.wav', str(tot)], check=True)
subprocess.run(['python3', '../../engine/music2.py', 'music.wav', str(tot + .5)], check=True)
