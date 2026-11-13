#!/usr/bin/env python3
"""Build the 'Reel Voice Scripts' page (two tabs: business reels, freelancer tips) from tips_content.py, business_content.py and posts.json.
usage: python3 make_scripts_page.py <out.html>"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
from tips_content import TIPS
from business_content import BIZ

posts = json.load(open(os.path.join(H, 'posts.json')))
P = {p['id']: p for p in (posts if isinstance(posts, list) else posts['posts'])}

tips = []
for t in TIPS:
    p = P[t['id']]
    tips.append(dict(id=t['id'], title='Reel ' + str(int(t['id'][1:])), meta=f"{t['label']} · 10:00 PKT · {t['topic']}", kw=t['kw'],
                     lines=t['lines'], caption=p['caption'], comment=p['firstComment'], dm=p['dm']))
biz = []
for i, b in enumerate(BIZ, 1):
    biz.append(dict(id=b['id'], title=f'Business reel {i}', meta=b['topic'], kw=b['kw'], lines=b['lines'],
                    caption=b['caption'], comment=b['comment'], dm=b['dm']))

data = ('var TIPS=' + json.dumps(tips, ensure_ascii=False) + ';\nvar BIZ=' + json.dumps(biz, ensure_ascii=False) +
        ';\nvar series="biz",D=BIZ;')
# keep the script block safe inside HTML
data = data.replace('</', '<\\/')
html = open(os.path.join(H, 'scripts_page.tpl.html')).read().replace('/*DATA*/', data)
open(sys.argv[1], 'w').write(html)
print('wrote', sys.argv[1], len(html), 'bytes;', len(tips), 'tips,', len(biz), 'business')
