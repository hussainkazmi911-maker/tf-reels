# Estimated timings (used until real audio exists). usage: python3 mktiming_est.py
import json, re
S = json.load(open('script.json'))
t = 0.15
lines = []
for L in S['lines']:
    ws = []
    start = t
    for w in L['words']:
        n = len(re.sub(r'[^A-Za-z]', '', w))
        d = 0.12 + 0.05 * n
        ws.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)})
        t += d
    lines.append({'start': round(start, 3), 'end': round(t, 3), 'words': ws})
    t += 0.38
total = round(t + 0.6, 3)
T = {'total': total, 'lines': lines, 'estimated': True}
json.dump(T, open('timing.json', 'w'), indent=1)
open('timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
print('total', total, 'lines', len(lines))
