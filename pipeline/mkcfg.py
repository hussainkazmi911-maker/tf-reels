# usage: python3 mkcfg.py [mins comma list]  (run inside the day work dir after tts.py)
import json,sys
lines=json.load(open('script.json')); durs=json.load(open('durs.json'))
mins=[float(x) for x in (sys.argv[1] if len(sys.argv)>1 else '3.6,3.9,3.3,2.9,3.7,3.5,2.7,3.5,2.9,0').split(',')]
gap=.3; lens=[]
for i,d in enumerate(durs):
    lens.append(round(d+1.0,3) if i==len(durs)-1 else round(max(d+gap,mins[i]),3))
starts=[0]
for l in lens[:-1]: starts.append(round(starts[-1]+l,3))
total=round(sum(lens),2)
json.dump({'starts':starts,'lens':lens,'durs':durs,'lines':lines,'total':total,'voff':0.1},open('cfg.json','w'))
print('total',total,'starts',starts)
if total>40.5: print('WARNING: over 40 s - shorten lines or lower mins')
