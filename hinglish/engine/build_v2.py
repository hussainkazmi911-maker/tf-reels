# usage: python3 build_v2.py s07v2   -> work/s07v2 symlinks for the clean engine (story2.html + kit.js + kit2.js + stories/<id>.js); timing.json must already exist (align_ctc)
import json, os, sys
ep_id = sys.argv[1]; H = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..')
EP = json.load(open(f'{H}/episodes/{ep_id}.json')); wd = f'{H}/work/{ep_id}'; os.makedirs(wd, exist_ok=True)
links = {'engine.html': f'{H}/engine/story2.html', 'lib.js': f'{H}/engine/story_lib.js', 'kit.js': f'{H}/stories/kit.js', 'kit2.js': f'{H}/stories/kit2.js', 'scenes.js': f'{H}/stories/{ep_id}.js',
         'fonts': f'{H}/engine/fonts', 'logo.png': f'{H}/engine/logo.png', 'render.py': f'{H}/engine/render.py'}
for n, src in links.items():
    dst = f'{wd}/{n}'
    if os.path.lexists(dst): os.remove(dst)
    os.symlink(src, dst)
open(f'{wd}/ep.js', 'w').write('window.EP=' + json.dumps(EP) + ';')
print(ep_id, 'built', 'timing' if os.path.exists(f'{wd}/timing.js') else 'NO TIMING')
