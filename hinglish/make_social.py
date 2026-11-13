#!/usr/bin/env python3
"""Carousel (6 slides, 1080x1350) + story (1080x1920) for each freelancer-tips reel.
Copy comes straight from the reel script lines in tips_content.py (no new claims).
usage: python3 make_social.py r02 r03 r04     -> ../social/tips/<id>/slide_1..6.png + story.png
Needs /home/claude/forge (node_modules/@fontsource/inter, logo.png) like pipeline/social/render_social.py."""
import sys, os, re, json, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
spec = importlib.util.spec_from_file_location('rs', os.path.join(H, '..', 'pipeline', 'social', 'render_social.py'))
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
from tips_content import TIPS
from playwright.sync_api import sync_playwright

e, hl, CSS, WORK = rs.e, rs.hl, rs.CSS, rs.WORK
EXTRA = """
.top b{font-size:15px}
.st .bd{top:300px;bottom:300px}
.sub.lime{color:var(--lime)}
.tipn{font-weight:800;font-size:15px;letter-spacing:2px;color:var(--lime)}
.big{position:absolute;right:34px;bottom:70px;font-weight:800;font-size:260px;line-height:1;color:rgba(198,255,53,.07);letter-spacing:-8px}
.ex{align-self:flex-start;padding:6px 12px;border:1.5px dashed rgba(255,255,255,.35);border-radius:20px;color:#c9d1c9;font-weight:800;font-size:11px;letter-spacing:1.6px}
"""
# lime emphasis per hook (hook line is the reel's line 0, text unchanged)
EMPH = {'r02': 'client nahi.', 'r03': 'Yeh teen spots pe kam log jaate hain.', 'r04': 'reply zero.',
        'r05': 'kaise aayega, bhai?', 'r06': 'koi aage nahi gaya, bhai.'}
SUB = 'FREELANCER TIPS'

def emph(text, ph):
    return e(text).replace(e(ph), f'<span class="lime">{e(ph)}</span>') if ph and ph in text else e(text)

def strip_num(s):
    return re.sub(r'^(One|Two|Three)\.\s*', '', s)

def split_first(s):
    m = re.match(r'(.+?[.?!])\s+(.+)', s)
    return (m.group(1), m.group(2)) if m else (s, '')

def top(n_label):
    return (f'<div class="top"><img src="../logo.png"><div><b>THE TOTAL FORGE</b><span>{SUB}</span></div>'
            f'<div class="pg">{n_label}</div></div>')

def foot(i, n):
    dots = ''.join(f'<u class="{"on" if j == i else ""}"></u>' for j in range(n))
    sw = '<span class="sw">SWIPE →</span>' if i < n - 1 else '<span class="sw">@thetotalforgeofficial</span>'
    return f'<div class="foot"><div class="dots">{dots}</div>{sw}</div>'

def carousel(t):
    L, kw, tid = t['lines'], t['kw'], t['id']
    slides = []
    # 1 hook
    slides.append(f'<h1>{emph(L[0], EMPH.get(tid))}</h1><div class="sub mut">Teen cheezein, swipe karo.</div>')
    # 2 scene
    slides.append(f'<div class="ex">EXAMPLE SCENARIO</div><h2>{e(L[1])}</h2><div class="sub lime">{e(L[2])}</div>')
    # 3-5 tips
    for k in range(3):
        head, sub = split_first(strip_num(L[4 + k]))
        s = f'<div class="chip">TIP {k + 1} OF 3</div><h1>{e(head)}</h1>'
        if sub: s += f'<div class="sub">{e(sub)}</div>'
        slides.append(s)
    # 6 cta
    slides.append(f'<h2>{e(L[7])}</h2><div class="key">{e(kw)}</div>'
                  f'<div class="sub">Comment karo, hum aapko DM kar denge.</div>'
                  f'<div class="share">Kisi freelancer dost ko yeh bhejo, aur save kar lo.</div>')
    n = len(slides)
    out = []
    for i, body in enumerate(slides):
        big = f'<div class="big">{i - 1}</div>' if 2 <= i <= 4 else ''
        out.append(f'<div class="sl car">{big}{top(f"{i + 1}/{n}")}<div class="bd">{body}</div>{foot(i, n)}</div>')
    return out

def story(t):
    thing = t['thing'].capitalize()
    return (f'<div class="sl st"><div class="top" style="top:60px"><img src="../logo.png"><div><b>THE TOTAL FORGE</b><span>{SUB}</span></div></div>'
            f'<div class="bd"><div class="bigday">NAYA REEL · LIVE HAI</div><h1>{emph(t["lines"][0], EMPH.get(t["id"]))}</h1>'
            f'<div class="sub">Profile pe dekho.</div><div class="arrow">↑</div>'
            f'<div class="share">{e(thing)} chahiye? Reel pe <span class="lime">{e(t["kw"])}</span> comment karo.</div></div></div>')

def render(tid):
    t = next(x for x in TIPS if x['id'] == tid)
    out = os.path.join(H, '..', 'social', 'tips', tid); os.makedirs(out, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    items = carousel(t) + [story(t)]
    names = [f'slide_{i + 1}.png' for i in range(6)] + ['story.png']
    path = os.path.join(WORK, f'tips_{tid}.html')
    open(path, 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}</style><body>' + ''.join(items))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 560, 'height': 1000}, device_scale_factor=2)
        pg.goto('file://' + path); pg.wait_for_timeout(500); pg.evaluate('document.fonts.ready')
        for el, nm in zip(pg.query_selector_all('.sl'), names):
            el.screenshot(path=os.path.join(out, nm))
        b.close()
    print(tid, 'wrote', len(names), 'files to', os.path.normpath(out))

if __name__ == '__main__':
    for tid in sys.argv[1:]:
        render(tid)
