# usage (in work dir): python3 build_k.py  -> reel_built.html (needs reel.json, engine.js, kinetic.css, logo.png)
import json
R=json.load(open('reel.json'))
R['total']=sum(b['d'] for b in R['beats'])
css=open('kinetic.css').read(); js=open('engine.js').read().replace('/*REEL*/{}',json.dumps(R,ensure_ascii=False))
body='<body><div id="root"><div id="stage"></div><div id="top"><img src="logo.png"><div class="nm">THE TOTAL FORGE</div><div class="hd">@thetotalforgeofficial</div></div><div id="prog"></div></div>'
open('reel_built.html','w').write('<!doctype html><html><head><meta charset="utf-8"><style>'+css+'</style></head>'+body+'<script>'+js+'</script></body></html>')
print('ok',R['total'])
