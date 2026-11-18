#!/usr/bin/env python3
"""v2 reels: client-case-study scripts (third person, ~60/40 English/Hinglish, 50/50 hook). Writes episodes/<id>.json + work/<id>/tts_prompt.txt.
usage: python3 make_v2.py [--write]   (ids: s07v2, s02v2; base fields copied from the original s07 / s02 episodes)"""
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
W, L, R, A, C = 'white', 'lime', 'red', 'amber', 'cyan'
V = {}
# (spoken text, audio tag, caption rows).  Spoken text is exactly what the TTS reads (numbers as English words); [Display|spoken] shows digits on screen.
V['s07v2'] = ('s07', [
 ("Our client gave us fifty K ka marketing budget, aur exactly hum kya karte hain.", '[serious]',
  [['Our client gave us', 44, W], ['[50k|fifty K]', 92, A], ['ka marketing budget,', 44, W], ['aur exactly hum', 48, W], ['kya karte hain.', 56, L]]),
 ("One. Every week, hook-first reels. Views nahi, sales laane wali.", '[warmly]',
  [['One.', 70, L], ['Every week,', 56, W], ['hook-first reels.', 56, W], ['Views nahi,', 50, W], ['sales laane wali.', 56, L]]),
 ("Two. Ads jahan har rupay ka hisaab ho. Zero guessing.", '',
  [['Two.', 70, A], ['Ads jahan har rupay', 52, W], ['ka hisaab ho.', 56, A], ['Zero guessing.', 62, W]]),
 ("Three. WhatsApp aur DM automation, so no lead gets ghosted.", '',
  [['Three.', 66, C], ['WhatsApp aur DM', 54, W], ['automation,', 58, W], ['so no lead', 48, W], ['gets ghosted.', 54, C]]),
 ("Four. Weekly report. Kitna spend hua, kitna kamaya. Full transparency.", '',
  [['Four.', 70, L], ['Weekly report.', 60, W], ['Kitna spend hua,', 52, W], ['kitna kamaya.', 56, L], ['Full transparency.', 44, W]]),
 ("Client ne bas apna product sambhala. Marketing ka poora scene, hum ne sambhala.", '[warmly]',
  [['Client ne bas', 52, W], ['apna product', 56, W], ['sambhala.', 60, W], ['Marketing ka poora scene,', 44, W], ['hum ne sambhala.', 62, L]]),
 ("Result? Every rupay tracked, every lead answered.", '',
  [['Result?', 80, A], ['Every rupay tracked,', 52, W], ['every lead', 62, L], ['answered.', 70, L]]),
 ("Want this for your brand? Comment BRAND, hum DM kar denge.", '',
  [['Want this for', 50, W], ['your brand?', 56, W], ['Comment', 50, W], ['BRAND,', 88, L], ['hum DM kar denge.', 36, W]]),
])
V['s02v2'] = ('s02', [
 ("Our client had twelve K ke parcels return every month. Yeh dekho, hum ne kya kiya.", '[frustrated]',
  [['Our client had', 44, W], ['[12k|twelve K]', 92, A], ['ke parcels return', 50, W], ['every month.', 50, W], ['Yeh dekho, hum ne kya kiya.', 40, L]]),
 ("Lawn suit gaya, customer ne phone hi nahi uthaya. Straight up ghosted.", '[sighs]',
  [['Lawn suit gaya,', 48, W], ['customer ne phone', 50, W], ['hi nahi uthaya.', 56, R], ['Straight up', 50, W], ['ghosted.', 74, R]]),
 ("A hundred orders mein se thirty-five returns, and each one cost three fifty rupay.", '[serious]',
  [['[100|A hundred] orders', 56, W], ['mein se', 44, W], ['[35|thirty-five] returns,', 66, R], ['and each one cost', 44, W], ['[Rs. 350|three fifty] rupay.', 56, A]]),
 ("So we set one rule. Order aate hi, WhatsApp pe confirm.", '[warmly]',
  [['So we set', 46, W], ['one rule.', 66, L], ['Order aate hi,', 48, W], ['WhatsApp pe', 56, W], ['confirm.', 62, L]]),
 ("Customer said yes? Ship it. Said no? Paisa bacha. Sorted.", '[happy]',
  [['Customer said', 44, W], ['yes? Ship it.', 62, L], ['Said no?', 54, R], ['Paisa bacha.', 60, W], ['Sorted.', 58, L]]),
 ("Guides ke hisaab se, returns almost half ho sakte hain.", '',
  [['Guides ke hisaab se,', 50, W], ['returns', 80, W], ['almost half', 70, L], ['ho sakte hain.', 52, L]]),
 ("Result? Returns kam, aur cash business mein stay.", '[warmly]',
  [['Result?', 80, A], ['Returns kam,', 66, W], ['aur cash', 66, L], ['business mein stay.', 52, W]]),
 ("Want a confirm bot? Comment CONFIRM, hum DM kar denge.", '',
  [['Want a', 50, W], ['confirm bot?', 56, W], ['Comment', 48, W], ['CONFIRM,', 84, L], ['hum DM kar denge.', 36, W]]),
])
N = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
def check(rid, lines):
    bad = 0
    for i, (text, tag, rows) in enumerate(lines):
        words = text.split(); toks = []
        for r in rows:
            for m in re.finditer(r'\[([^\]|]+)\|([^\]]+)\]|\S+', r[0]):
                toks += m.group(2).split() if m.group(1) else [m.group(0)]
        if [N(w) for w in toks] != [N(w) for w in words]:
            bad += 1; print(rid, 'line', i, 'CAPTION MISMATCH\n  spoken:', [N(w) for w in words], '\n  rows  :', [N(w) for w in toks])
        if len(rows) > 5 or sum(r[1] for r in rows) > 300: print(rid, 'line', i, 'tall rows', len(rows), sum(r[1] for r in rows))
    return bad
if __name__ == '__main__':
    bad = 0
    for rid, (base, lines) in V.items():
        bad += check(rid, lines)
        ep = json.load(open(f'{H}/episodes/{base}.json'))
        ep['id'] = rid; ep['v'] = 3; ep['chip'] = 'CASE STUDY'
        ep['lines'] = [l[0] for l in lines]; ep['rows'] = {str(i): l[2] for i, l in enumerate(lines)}
        ep['note'] = 'EXAMPLE CLIENT SCENARIO · MISAAL HAI'
        prompt = ' '.join((l[1] + ' ' + l[0]).strip() for l in lines)
        print(rid, 'chars', len(prompt))
        if '--write' in sys.argv:
            json.dump(ep, open(f'{H}/episodes/{rid}.json', 'w'), ensure_ascii=False, indent=1)
            os.makedirs(f'{H}/work/{rid}', exist_ok=True)
            open(f'{H}/work/{rid}/tts_prompt.txt', 'w').write(prompt)
    print('mismatches', bad)
