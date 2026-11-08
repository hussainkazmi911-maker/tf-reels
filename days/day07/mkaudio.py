import json, numpy as np, soundfile as sf
cfg=json.load(open('cfg.json')); S=cfg['starts']; D=cfg['durs']; T=cfg['total']; V=cfg['voff']
sr=24000; N=int((T+0.3)*sr); t=np.arange(N)/sr
vo=np.zeros(N)
for i in range(len(S)):
    x,r=sf.read(f'vo_{i:02d}.wav'); assert r==sr
    a=int((S[i]+V)*sr); vo[a:a+len(x)]+=x[:max(0,N-a)]
vo=vo/np.max(np.abs(vo))*0.9
rng=np.random.default_rng(13)
def wt(li,wi):
    w=cfg['lines'][li].split(' ');cum=sum(len(x)+1 for x in w[:wi]);return S[li]+V+D[li]*cum/len(cfg['lines'][li])
sfx=np.zeros(N)
def add(at,y,g=1):
    a=int(at*sr)
    if a<N: sfx[a:a+len(y)]+=g*y[:max(0,N-a)]
def tick(at,f=1500,g=.10):
    u=np.arange(int(.12*sr))/sr; add(at,np.sin(2*np.pi*f*u)*np.exp(-u*45),g)
def soft_whoosh(at,dur=.7,g=.07):
    L=int(dur*sr); u=np.arange(L)/L
    y=np.convolve(rng.standard_normal(L),np.ones(160)/160,'same'); add(at,y*np.sin(np.pi*u)**2*9,g)
def sub(at,g=.30):
    u=np.arange(int(1.4*sr))/sr; add(at,np.sin(2*np.pi*(46+30*np.exp(-u*5))*u)*np.exp(-u*3.2),g)
def bell(at,f,g=.07):
    u=np.arange(int(1.4*sr))/sr; add(at,(np.sin(2*np.pi*f*u)+.35*np.sin(2*np.pi*2.01*f*u))*np.exp(-u*3.2),g)
def ring(at,g=.03):
    for k in (0,.42):
        L=int(.34*sr); u=np.arange(L)/sr
        env=np.sin(np.pi*u/.34)**2
        y=(np.sin(2*np.pi*880*u)+np.sin(2*np.pi*1108*u))*(0.6+0.4*np.sin(2*np.pi*22*u))*env
        add(at+k,y,g)
# problem: soft drone, notification ping on the enquiry, low ticks as it is lost
mDr=np.minimum(1,t/1.5)*np.clip((S[2]+.4-t)/.8,0,1)
drone=mDr*(0.035+0.05*np.clip(t/S[2],0,1))*np.sin(2*np.pi*(52+10*np.clip(t/S[2],0,1))*t)
bell(.12,1318,.05)                                           # soft cue
tick(wt(0,7),620,.07)                                        # nobody notices
for x in (wt(1,0)-.05,wt(1,4),wt(1,6)): tick(x,950,.05)
for x in (wt(1,4),wt(1,6)): tick(x+.04,420,.10)       # too late / lost / signed
soft_whoosh(S[2]-.25,.9,.06)
sub(S[2]+.35,.28)
for w in (S[3],S[4],S[5],S[6],S[7],S[9]): soft_whoosh(w-.15,.6,.05)
# music from the title
bpm=84; beat=60/bpm; bar=beat*4
chords=[[220,261.6,329.6],[174.6,220,261.6],[196,246.9,293.7],[164.8,196,246.9]]
mus=np.zeros(N); st=S[2]; n=0
while st+n*bar<T+.3:
    ch=chords[n%4]; a=int((st+n*bar)*sr); b=min(N,a+int((bar+1.2)*sr))
    if a>=N: break
    u=np.arange(b-a)/sr
    env=np.minimum(1,u/1.0)*np.exp(-np.maximum(0,u-bar)*3)
    for f in ch: mus[a:b]+=0.05*(np.sin(2*np.pi*f*u)+.5*np.sin(2*np.pi*f*1.005*u))*env
    mus[a:b]+=0.07*np.sin(2*np.pi*(ch[0]/2)*u)*env
    for k in range(8):
        s0=int(k*beat/2*sr)
        if a+s0>=N: break
        pu=np.arange(min(int(1.2*sr),N-a-s0))/sr
        f=ch[[0,1,2,1,2,1,2,1][k]]*2
        mus[a+s0:a+s0+len(pu)]+=0.05*(np.sin(2*np.pi*f*pu)+.3*np.sin(2*np.pi*2*f*pu))*np.exp(-pu*4.5)
    n+=1
mus*=np.clip((t-st+.1)/1.2,0,1)*np.clip((T+.15-t)/1.4,0,1)
mus=mus/np.max(np.abs(mus))*0.17
# app sfx
for x in (s0:=S[3]+.6,S[3]+.8): tick(x,1700,.04)             # older rows
tick(wt(3,3),1200,.07); bell(wt(3,3)+.05,1175,.05)           # new lead row
tick(S[3]+0.0+wt(3,6)-S[3]+.25,1500,.06); bell(wt(3,6)+.3,1175,.04)    # weekly stats
tick(S[4]-.05+.02,1500,.12)                                  # tap into class page
tick(wt(4,1),1100,.06)
tick(wt(4,3)+.05,1900,.10); bell(wt(4,3)+.1,1318,.06)        # checked in
tick(wt(4,5)+.05,1900,.10); bell(wt(4,5)+.1,1568,.07); bell(wt(4,5)+.22,2093,.05)   # booked
tick(wt(4,7),1250,.06)
for x in (wt(5,1),wt(5,3),wt(5,6),wt(5,8)): tick(x+.04,1600,.06)   # profile fields
bell(wt(5,10),988,.05); bell(wt(5,10)+.12,1318,.05)            # nudge sent
tick(wt(6,0)+.1,1300,.06); tick(wt(6,2)+.05,1100,.09)        # welcome back / class booked
bell(wt(6,3)+.05,1568,.07); bell(wt(6,3)+.2,2093,.04)        # payment received
for i in range(4): tick(S[7]+.95+i*.2,1400,.05)
tm1=wt(7,2)-.25; tm2=wt(7,6)-.25
soft_whoosh(tm1,.5,.05); soft_whoosh(tm2,.5,.05)             # booking moves
tick(tm1+.5,1250,.09); bell(tm1+.52,988,.04)
tick(tm2+.5,1250,.09); bell(tm2+.52,1318,.06); bell(tm2+.64,1760,.05)
for x in (wt(8,0),wt(8,2),wt(8,4)): tick(x,1250,.10)
bell(S[9]+.4,1046,.05); tick(wt(9,4),1250,.09)
mix=vo+mus+sfx+drone
mix=np.clip(mix/np.max(np.abs(mix))*0.97,-1,1)
sf.write('mix.wav',mix,sr);print('audio ok',T)
