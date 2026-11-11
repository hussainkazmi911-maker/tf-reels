# usage: python3 mkaudio_k.py [voice.wav]  -> mix.wav (music + sfx from reel.json beats; optional voice track mixed on top)
import json,sys,numpy as np,soundfile as sf
R=json.load(open('reel.json')); B=R['beats']; sr=24000
st=0
for b in B: b['t']=st; st+=b['d']
T=st; N=int((T+.3)*sr); t=np.arange(N)/sr
rng=np.random.default_rng(7); sfx=np.zeros(N)
def add(at,y,g=1):
    a=int(max(0,at)*sr)
    if a<N: sfx[a:a+len(y)]+=g*y[:max(0,N-a)]
def tick(at,f=1500,g=.06):
    u=np.arange(int(.1*sr))/sr; add(at,np.sin(2*np.pi*f*u)*np.exp(-u*50),g)
def whoosh(at,dur=.5,g=.06):
    L=int(dur*sr); u=np.arange(L)/L; y=np.convolve(rng.standard_normal(L),np.ones(160)/160,'same'); add(at,y*np.sin(np.pi*u)**2*9,g)
def sub(at,g=.3):
    u=np.arange(int(1.3*sr))/sr; add(at,np.sin(2*np.pi*(46+30*np.exp(-u*5))*u)*np.exp(-u*3.4),g)
def bell(at,f,g=.06):
    u=np.arange(int(1.3*sr))/sr; add(at,(np.sin(2*np.pi*f*u)+.35*np.sin(2*np.pi*2.01*f*u))*np.exp(-u*3.4),g)
sub(.05,.32)
for i,b in enumerate(B):
    whoosh(b['t']-.12 if i else 0,.45,.06)
    if i: sub(b['t'],.16)
    nw=len(b.get('lines',[]) and ' '.join(b['lines']).replace('*','').split())
    for j in range(nw): tick(b['t']+.12+j*.11+.05,1300+60*(j%5),.035)
    v=b.get('visual')
    if v:
        n=len(v.get('items',v.get('msgs',v.get('nodes',[]))))
        vs=(v['at'] if v.get('at') is not None else .12+nw*.11+.45); sp=v.get('step',.6)
        for k in range(n): tick(b['t']+vs+k*sp+.05,1700,.06); 
        if v['type']=='checklist':
            for k in range(n): bell(b['t']+vs+k*sp+.4,1175+80*k,.035)
bell(B[-1]['t']+.5,1046,.05); bell(B[-1]['t']+.62,1568,.04)
bpm=88; beat=60/bpm; bar=beat*4
chords=[[220,261.6,329.6],[174.6,220,261.6],[196,246.9,293.7],[164.8,196,246.9]]
mus=np.zeros(N); n=0
while n*bar<T+.3:
    ch=chords[n%4]; a=int(n*bar*sr); b=min(N,a+int((bar+1.2)*sr))
    if a>=N: break
    u=np.arange(b-a)/sr; env=np.minimum(1,u/.8)*np.exp(-np.maximum(0,u-bar)*3)
    for f in ch: mus[a:b]+=.05*(np.sin(2*np.pi*f*u)+.5*np.sin(2*np.pi*f*1.005*u))*env
    mus[a:b]+=.07*np.sin(2*np.pi*(ch[0]/2)*u)*env
    for k in range(8):
        s0=int(k*beat/2*sr)
        if a+s0>=N: break
        pu=np.arange(min(int(1.2*sr),N-a-s0))/sr; f=ch[[0,1,2,1,2,1,2,1][k]]*2
        mus[a+s0:a+s0+len(pu)]+=.05*(np.sin(2*np.pi*f*pu)+.3*np.sin(2*np.pi*2*f*pu))*np.exp(-pu*4.5)
    n+=1
mus*=np.clip(t/1.0,0,1)*np.clip((T+.15-t)/1.4,0,1); mus=mus/np.max(np.abs(mus))*.20
mix=mus+sfx
if len(sys.argv)>1:
    x,r=sf.read(sys.argv[1]); assert r==sr; vo=np.zeros(N); vo[:min(N,len(x))]=x[:N]; mix=mix*.5+vo/np.max(np.abs(vo))*.9
mix=np.clip(mix/np.max(np.abs(mix))*.97,-1,1); sf.write('mix.wav',mix,sr); print('audio ok',T)
