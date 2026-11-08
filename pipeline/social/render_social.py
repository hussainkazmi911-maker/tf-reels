#!/usr/bin/env python3
"""Render Forge Fix of the Day social assets (carousel slides, story, highlight covers).
Usage (run from anywhere; needs /home/claude/forge with node_modules/@fontsource/inter and logo.png from pipeline/setup.sh):
  python3 render_social.py carousel  <data.json> <outdir>   -> slide_1.png ... (1080x1350)
  python3 render_social.py story     <data.json> <outdir>   -> story.png (1080x1920)
  python3 render_social.py covers    <covers.json> <outdir> -> highlight_NN_name.png (1080x1920)
data.json for carousel: {"day":4,"niche":"Real estate agents","keyword":"LEADS","slides":[{"k":"hook|cost|fix|list|flow|cta", ...}]}
"""
import json, sys, os, html
from playwright.sync_api import sync_playwright

WORK = '/home/claude/forge/social'          # html is written here so ../node_modules and ../logo.png resolve
CSS = """
@font-face{font-family:Inter;font-weight:400;src:url(../node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(../node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2)}
@font-face{font-family:Inter;font-weight:800;src:url(../node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}
:root{--lime:#c6ff35;--bg:#181818;--mut:#9aa39a}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#000;font-family:Inter,Arial,sans-serif;color:#f2f2f2}
.sl{position:relative;width:540px;overflow:hidden;background:radial-gradient(520px 420px at 50% 42%,#26300f 0%,#181818 66%);margin-bottom:10px}
.sl.car{height:675px}.sl.st{height:960px}.sl.cv{height:960px}
.top{position:absolute;left:30px;right:30px;top:26px;height:44px;display:flex;align-items:center;gap:12px}
.top img{width:40px;height:40px;border-radius:10px}
.top b{display:block;font-weight:800;font-size:15px;letter-spacing:1.8px}
.top span{display:block;font-weight:700;font-size:10px;letter-spacing:1.4px;color:var(--lime);margin-top:2px}
.top .pg{margin-left:auto;font-weight:700;font-size:13px;color:var(--mut);letter-spacing:1px}
.bd{position:absolute;left:40px;right:40px;top:96px;bottom:84px;display:flex;flex-direction:column;justify-content:center;gap:18px}
.chip{align-self:flex-start;padding:7px 14px;border:1.5px solid var(--lime);border-radius:20px;color:var(--lime);font-weight:800;font-size:12px;letter-spacing:1.6px}
h1{font-weight:800;font-size:40px;line-height:1.12;letter-spacing:-.5px}
h2{font-weight:800;font-size:30px;line-height:1.15;letter-spacing:-.3px}
.lime{color:var(--lime)}.mut{color:#8a938a}
.sub{font-weight:700;font-size:20px;line-height:1.3;color:#c9d1c9}
.row{display:flex;gap:14px;align-items:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:14px 16px}
.row i{flex:none;width:34px;height:34px;border-radius:50%;background:var(--lime);color:#14200a;font-style:normal;font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center}
.row p{font-weight:700;font-size:19px;line-height:1.25}
.flow{display:flex;align-items:center;gap:8px}
.flow div{flex:1;text-align:center;padding:16px 4px;border-radius:14px;border:1.5px solid rgba(198,255,53,.5);background:rgba(198,255,53,.08);font-weight:800;font-size:18px}
.flow div.last{background:var(--lime);color:#14200a;border-color:var(--lime)}
.flow em{font-style:normal;color:var(--lime);font-weight:800;font-size:20px}
.key{align-self:flex-start;background:var(--lime);color:#14200a;font-weight:800;font-size:52px;letter-spacing:3px;padding:8px 26px;border-radius:16px}
.share{border:1.5px dashed rgba(198,255,53,.6);border-radius:16px;padding:14px 16px;font-weight:700;font-size:17px;line-height:1.3;color:#e6ece6}
.foot{position:absolute;left:30px;right:30px;bottom:26px;height:30px;display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:12px;letter-spacing:1.4px;color:var(--mut)}
.dots{display:flex;gap:6px}.dots u{width:7px;height:7px;border-radius:50%;background:#3a3f3a;text-decoration:none;display:block}.dots u.on{background:var(--lime);width:20px;border-radius:5px}
.sw{color:var(--lime)}
/* story */
.st .bd{top:150px;bottom:150px;gap:22px}
.st h1{font-size:50px}.st .sub{font-size:23px}
.bigday{font-weight:800;font-size:15px;letter-spacing:2px;color:var(--lime)}
.arrow{font-size:40px;color:var(--lime);font-weight:800}
/* cover */
.cv{display:flex;align-items:center;justify-content:center}
.ring{width:340px;height:340px;border-radius:50%;border:3px solid var(--lime);display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 40%,rgba(198,255,53,.18),rgba(198,255,53,.02) 70%);box-shadow:0 0 70px rgba(198,255,53,.25)}
.ring svg{width:170px;height:170px;stroke:var(--lime);fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
"""

def e(s): return html.escape(s, quote=False)

def hl(text, hi):
    """wrap the part of text between [[ ]] in lime"""
    return e(text).replace('[[', '<span class="lime">').replace(']]', '</span>')

def car_slide(d, i, n, s):
    k = s['k']; day = d['day']; niche = d['niche']; kw = d['keyword']
    if k == 'hook':
        body = f'<div class="chip">DAY {day} · {e(niche.upper())}</div><h1>{hl(s["t"],1)}</h1><div class="sub mut">{hl(s.get("s",""),1)}</div>'
    elif k == 'cost':
        body = f'<h1>{hl(s["t"],1)}</h1><div class="sub mut">{hl(s.get("s",""),1)}</div>'
    elif k == 'fix':
        body = f'<div class="chip">THE FIX</div><h1 class="lime">{hl(s["t"],1)}</h1><div class="sub">{hl(s.get("s",""),1)}</div>'
    elif k == 'list':
        rows = ''.join(f'<div class="row"><i>{j+1}</i><p>{e(x)}</p></div>' for j, x in enumerate(s['items']))
        body = f'<h2>{hl(s["t"],1)}</h2>{rows}'
    elif k == 'flow':
        st = s['steps']
        parts = []
        for j, x in enumerate(st):
            parts.append(f'<div class="{"last" if j==len(st)-1 else ""}">{e(x)}</div>')
            if j < len(st)-1: parts.append('<em>→</em>')
        body = f'<h2>{hl(s["t"],1)}</h2><div class="flow">{"".join(parts)}</div><div class="sub mut">{hl(s.get("s",""),1)}</div>'
    else:  # cta
        body = f'<h1>{hl(s["t"],1)}</h1><div class="key">{e(kw)}</div><div class="sub">Comment it and we\'ll DM you the details.</div><div class="share">{e(s["share"])}</div>'
    dots = ''.join(f'<u class="{"on" if j==i else ""}"></u>' for j in range(n))
    sw = '<span class="sw">SWIPE →</span>' if i < n-1 else '<span class="sw">@thetotalforgeofficial</span>'
    return (f'<div class="sl car"><div class="top"><img src="../logo.png"><div><b>THE TOTAL FORGE</b><span>FORGE FIX OF THE DAY</span></div>'
            f'<div class="pg">{i+1}/{n}</div></div><div class="bd">{body}</div><div class="foot"><div class="dots">{dots}</div>{sw}</div></div>')

def story_slide(d):
    return (f'<div class="sl st"><div class="top" style="top:60px"><img src="../logo.png"><div><b>THE TOTAL FORGE</b><span>FORGE FIX OF THE DAY</span></div></div>'
            f'<div class="bd"><div class="bigday">NEW TODAY · DAY {d["day"]}</div><h1>{e(d["niche"])}: {hl(d["line"],1)}</h1>'
            f'<div class="sub">Watch the new reel on our profile.</div><div class="arrow">↑</div>'
            f'<div class="share">{e(d["owner"])}? Comment <span class="lime">{e(d["keyword"])}</span> on the reel.</div></div></div>')

ICONS = {
 'audit':'<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><path d="M8 11l2 2 4-4"/>',
 'local':'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
 'health':'<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>',
 'shops':'<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
 'property':'<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 'ops':'<circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="7"/>' + ''.join(f'<line x1="12" y1="2" x2="12" y2="5" transform="rotate({a} 12 12)"/>' for a in range(0,360,45)),
 'pros':'<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 'creators':'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l6 3-6 3z"/>',
}

def cover_slide(c):
    return f'<div class="sl cv"><div class="ring"><svg viewBox="0 0 24 24">{ICONS[c["icon"]]}</svg></div></div>'

def render(mode, data, outdir):
    os.makedirs(WORK, exist_ok=True); os.makedirs(outdir, exist_ok=True)
    if mode == 'carousel':
        n = len(data['slides']); items = [car_slide(data, i, n, s) for i, s in enumerate(data['slides'])]; names = [f'slide_{i+1}.png' for i in range(n)]
    elif mode == 'story':
        items = [story_slide(data)]; names = ['story.png']
    else:
        items = [cover_slide(c) for c in data['covers']]; names = [f'highlight_{i+1:02d}_{c["file"]}.png' for i, c in enumerate(data['covers'])]
    path = os.path.join(WORK, f'{mode}.html')
    open(path, 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>' + ''.join(items))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 560, 'height': 1000}, device_scale_factor=2)
        pg.goto('file://' + path); pg.wait_for_timeout(500)
        pg.evaluate('document.fonts.ready')
        for el, nm in zip(pg.query_selector_all('.sl'), names):
            el.screenshot(path=os.path.join(outdir, nm))
        b.close()
    print('wrote', len(names), 'files to', outdir)

if __name__ == '__main__':
    mode, datafile, outdir = sys.argv[1:4]
    render(mode, json.load(open(datafile)), outdir)
