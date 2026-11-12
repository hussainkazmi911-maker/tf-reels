# usage: python3 build_ep.py rNN   -> work/rNN with ep.js, estimated timing.js/json, symlinks
import json, re, os, sys
ep_id = sys.argv[1]
H = os.path.dirname(os.path.abspath(__file__)) + '/..'
EP = json.load(open(f'{H}/episodes/{ep_id}.json'))
wd = f'{H}/work/{ep_id}'
os.makedirs(wd, exist_ok=True)
for n in ('engine.html', 'fonts', 'logo.png', 'render.py'):
    dst = f'{wd}/{n}'
    if not os.path.lexists(dst):
        os.symlink(f'{os.path.abspath(H)}/engine/{n}', dst)
open(f'{wd}/ep.js', 'w').write('window.EP=' + json.dumps(EP) + ';')
# estimated timing (replaced by align_audio once the real voice exists)
t = 0.2; lines = []
for line in EP['lines']:
    ws = []; st = t
    for w in line.split():
        n = len(re.sub(r'[^A-Za-z]', '', w)); d = 0.12 + 0.05 * n
        ws.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)}); t += d
    lines.append({'start': round(st, 3), 'end': round(t, 3), 'words': ws}); t += 0.45
T = {'total': round(t + 0.6, 3), 'lines': lines, 'estimated': True}
json.dump(T, open(f'{wd}/timing.json', 'w'), indent=1)
open(f'{wd}/timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
print(ep_id, 'est total', T['total'])
