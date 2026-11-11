# usage: python3 render_k.py test | python3 render_k.py run 4 K
import json,sys,os
from playwright.sync_api import sync_playwright
R=json.load(open('reel.json')); T=sum(b['d'] for b in R['beats'])
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
    ts=[0.0,.4]; t=0
    for i,b in enumerate(R['beats']):
        if i>0: ts.append(t+.5)
        ts.append(t+b['d']-.25); t+=b['d']
    run([int(x*30) for x in ts],'test',1);print(len(ts),'test frames')
else:
    n=int(a[2]);k=int(a[3]);run(range(k,int(T*30)+1,n),'frames',1.5)
