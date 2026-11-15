# usage: python3 build_story.py sNN   -> work/sNN with ep.js, estimated timing, symlinks (engine.html = story.html, lib.js, scenes.js)
import json, re, os, sys
ep_id = sys.argv[1]
H = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..')
EP = json.load(open(f'{H}/episodes/{ep_id}.json'))
wd = f'{H}/work/{ep_id}'
os.makedirs(wd, exist_ok=True)
links = {'engine.html': f'{H}/engine/story.html', 'lib.js': f'{H}/engine/story_lib.js', 'kit.js': f'{H}/stories/kit.js', 'scenes.js': f'{H}/stories/{ep_id}.js',
         'fonts': f'{H}/engine/fonts', 'logo.png': f'{H}/engine/logo.png', 'render.py': f'{H}/engine/render.py'}
for n, src in links.items():
    dst = f'{wd}/{n}'
    if os.path.lexists(dst): os.remove(dst)
    os.symlink(src, dst)
open(f'{wd}/ep.js', 'w').write('window.EP=' + json.dumps(EP) + ';')
if not os.path.exists(f'{wd}/timing.json') or '--est' in sys.argv:
    t = 0.2; lines = []
    for line in EP['lines']:
        ws = []; st = t
        for w in line.split():
            n = len(re.sub(r'[^A-Za-z]', '', w)); d = 0.12 + 0.05 * n
            ws.append({'w': w, 's': round(t, 3), 'e': round(t + d, 3)}); t += d
        lines.append({'start': round(st, 3), 'end': round(t, 3), 'words': ws}); t += 0.35
    T = {'total': round(t + 0.6, 3), 'lines': lines, 'estimated': True}
    json.dump(T, open(f'{wd}/timing.json', 'w'), indent=1)
    open(f'{wd}/timing.js', 'w').write('window.TIMING=' + json.dumps(T) + ';')
    print(ep_id, 'est total', T['total'])
