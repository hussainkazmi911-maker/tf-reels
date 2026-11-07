# usage (inside day work dir): python3 render.py test | python3 render.py run 4 K   (K=0..3, run 4 in parallel)
import json,sys,os
from playwright.sync_api import sync_playwright
cfg=json.load(open('cfg.json')); S=cfg['starts']; D=cfg['durs']
def run(frames,outdir,scale):
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':720,'height':1280},device_scale_factor=scale)
        msgs=[];pg.on('pageerror',lambda e:msgs.append('ERR '+str(e)))
        pg.goto('file://'+os.getcwd()+'/reel_built.html');pg.wait_for_timeout(600)
        for f in frames:
            pg.evaluate(f"draw({f/30})");pg.screenshot(path=f"{outdir}/f_{f:05d}.png")
        if msgs:print(msgs[:5])
        b.close()
a=sys.argv
if a[1]=='test':
    ts=[0.0,0.5,1.5]
    for i in range(1,len(S)):
        ts+= [S[i]+.5,S[i]+D[i]*.75]
    ts.append(cfg['total']-.6)
    run([int(x*30) for x in ts],'test',1)
    print(len(ts),'test frames')
else:
    n=int(a[2]);k=int(a[3]);tot=int(cfg['total']*30)+1
    run(range(k,tot,n),'frames',1.5)
