css=open('../base.css').read()
extra='''<style>
:root{--ember:#0ea5e9}
.bizlogo{background:#0ea5e9}
.ev.new{background:#0ea5e9;box-shadow:0 8px 20px rgba(14,165,233,.35)}
.ev{opacity:0}
.lrow{display:flex;align-items:center;gap:12px;background:#fff;border-radius:18px;padding:12px 14px;margin-top:10px;box-shadow:0 2px 10px rgba(30,20,10,.08);border:2px solid transparent;opacity:0}
.lav{width:42px;height:42px;border-radius:50%;background:#e0f2fe;color:#0ea5e9;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none}
.lt{font-weight:800;font-size:16px}.ls{font-size:12px;color:#8a857b;font-weight:500;margin-top:2px}
.lchip{margin-left:auto;padding:6px 11px;border-radius:12px;font-size:11px;font-weight:800;letter-spacing:.5px;background:#e0f2fe;color:#0ea5e9;white-space:nowrap}
.istat{padding:14px 18px;margin-top:16px;font-weight:700;font-size:14px;opacity:0;display:flex;justify-content:space-between}
.istat span{color:#8a857b;font-weight:600}
#pgChat{background:#fff}
.chh{display:flex;gap:12px;align-items:center;padding-bottom:14px;border-bottom:1px solid #eee}
.rcm{max-width:84%;padding:12px 16px;border-radius:20px;font-weight:600;font-size:15px;line-height:1.35;margin-top:14px;opacity:0}
.rcm.cl{background:#eceae6;border-bottom-left-radius:6px}
.rcm.cr{background:#0ea5e9;color:#fff;margin-left:auto;border-bottom-right-radius:6px}
.rtag{font-size:11px;color:#8a857b;font-weight:600;text-align:right;margin-top:6px;opacity:0}
.lhd{display:flex;gap:14px;align-items:center;margin-top:8px;opacity:0}
.lav2{width:64px;height:64px;border-radius:50%;background:#e0f2fe;color:#0ea5e9;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}
.lcard{padding:6px 16px;margin-top:20px}
.lfr{display:flex;justify-content:space-between;padding:13px 0;border-bottom:1px solid #f0ece4;font-size:14px;opacity:0}
.lfr:last-child{border:none}.lfr span{color:#8a857b;font-weight:600}.lfr b{font-weight:800}
.lsv{display:inline-flex;margin-top:18px;padding:11px 18px;border-radius:24px;background:#e5f7ec;color:#136b3b;font-weight:800;font-size:14px;opacity:0}
#tl2{position:relative;height:300px;margin-top:14px}
#vnote{position:absolute;left:14px;right:14px;top:52px;padding:14px 16px;border-radius:20px;background:#111;color:#fff;font-size:13px;font-weight:600;opacity:0;z-index:6}
#vnote b{display:block;font-size:15px;font-weight:800;margin-bottom:2px;color:#c6ff35}
#pipe{width:560px;height:470px;margin-left:-280px;margin-top:-235px;border-radius:30px;background:#1b1b1b;border:1px solid #2c2c2c;box-shadow:0 30px 80px rgba(0,0,0,.5);padding:26px}
#kb{position:relative;height:330px;margin-top:20px}
.kcol{position:absolute;top:30px;width:161px;height:290px;border-radius:18px;background:rgba(255,255,255,.035)}
.kh{position:absolute;top:2px;width:161px;font-weight:800;font-size:13px;letter-spacing:2px;color:rgba(255,255,255,.55);display:flex;justify-content:space-between;padding:0 6px}
.kh b{color:#c6ff35;font-weight:800}
.kcard{position:absolute;width:161px;height:84px;border-radius:16px;background:#2a2a2a;padding:15px 14px;border:1.5px solid transparent;opacity:0;box-sizing:border-box}
.kcard b{display:block;font-weight:800;font-size:16px}
.kcard small{display:block;font-size:12px;color:rgba(255,255,255,.5);font-weight:500;margin-top:4px}
.kcard.hero{background:#0ea5e9;border-color:#7dd3fc}.kcard.hero small{color:rgba(255,255,255,.8)}
#cap{top:872px}
#cap span{white-space:nowrap}
.lchip{color:#0369a1}
#end .s{position:absolute;left:30px;right:30px;top:868px;text-align:center;font-weight:600;font-size:30px;color:rgba(255,255,255,.92);opacity:0}
#end .s em{font-style:normal;color:#c6ff35}
</style>'''
body='''<body><div id="root">
<div id="top"><img src="logo.png"><div class="nm">THE TOTAL FORGE</div><div class="tg">FORGING DIGITAL EXCELLENCE</div><div id="tableChip">DAY 05</div></div>
<div id="chaos"></div>
<div id="series"><img id="sLogo" src="logo.png"><div id="sT1"></div><div id="sT2"></div><div id="sT3">DAY 05 · GYMS &amp; FITNESS</div></div>
<div class="phone" id="phA"><div class="screen"><div class="isl"></div><div class="sb">9:41</div>
 <div class="pg" id="pgInbox"><div class="biz"><div class="bizlogo">I</div><div><div class="bn">Ironside Fitness</div><div class="bs">Member app</div></div></div>
  <div class="h1" style="margin-top:24px;font-size:26px">Today's classes</div><div class="sub" style="margin-bottom:6px">Tap a class to book</div>
  <div class="lrow" id="lr0"><div class="lav">H</div><div><div class="lt">HIIT Burn</div><div class="ls">6:30 PM · Coach Mia</div></div><div class="lchip" id="lc0">OPEN</div></div>
  <div class="lrow" id="lr1"><div class="lav">Y</div><div><div class="lt">Yoga Flow</div><div class="ls">7:30 PM · Coach Leo</div></div><div class="lchip">OPEN</div></div>
  <div class="lrow" id="lr2"><div class="lav">S</div><div><div class="lt">Spin</div><div class="ls">8:15 PM · Coach Ana</div></div><div class="lchip">OPEN</div></div>
  <div class="card istat" id="inStat"><span>This week</span><b>3 visits · 1 class booked</b></div></div>
 <div class="pg" id="pgChat"><div class="chh"><div class="lav">H</div><div><div class="lt">HIIT Burn</div><div class="ls">Today · 6:30 PM · Coach Mia</div></div></div>
  <div class="lrow" id="cm1" style="margin-top:22px;padding:18px 16px"><div><div class="lt">Check in</div><div class="ls">At the front door</div></div><div class="lchip" id="ci1">Tap</div></div>
  <div class="lrow" id="cm2" style="padding:18px 16px"><div><div class="lt">Book this class</div><div class="ls">HIIT Burn · 6:30 PM</div></div><div class="lchip" id="bk1">Tap</div></div>
  <div class="rtag" id="cmTag" style="text-align:center;margin-top:14px;font-size:13px">Two taps. Done.</div></div>
 <div class="pg" id="pgLead"><div class="h1">Member profile</div>
  <div class="lhd" id="lhd"><div class="lav2">S</div><div><div class="lt" style="font-size:20px">Sam R.</div><div class="lchip" style="margin:6px 0 0;display:inline-block">Unlimited plan</div></div></div>
  <div class="card lcard"><div class="lfr" id="lf0"><span>Last visit</span><b>14 days ago</b></div><div class="lfr" id="lf1"><span>Status</span><b style="color:#d97706">At risk</b></div><div class="lfr" id="lf2"><span>Auto message</span><b>“We miss you” sent</b></div><div class="lfr" id="lf3"><span>Offer</span><b style="color:#0369a1">Free class</b></div></div>
  <div class="lsv" id="lsv">Nudge sent automatically ✓</div></div>
 <div class="pg" id="pgView"><div class="h1" style="margin-top:6px">Welcome back, Sam</div><div class="sub" id="vsub" style="opacity:0">Checked in · 6:02 PM</div>
  <div id="tl2"><div class="hr" style="top:0">6:00</div><div class="hr" style="top:80px">7:00</div><div class="hr" style="top:160px">8:00</div><div class="hr" style="top:240px">9:00</div>
   <div class="ev new" id="ev1" style="top:40px;height:0;padding:0 14px">HIIT Burn · booked<small>6:30 PM · Coach Mia</small></div>
   <div class="ev old" id="ev0" style="top:186px;height:66px">Spin<small>8:15 PM · Coach Ana</small></div></div>
  <div id="vnote"><b>Payment received</b>Membership renewed automatically · receipt sent</div></div>
</div></div>
<div class="panel" id="pipe"><div class="tag">OWNER VIEW</div>
 <div class="fh"><span>MEMBER BOARD</span><span class="live"><i id="liveDot"></i>LIVE</span></div>
 <div id="kb">
  <div class="kcol" style="left:0"></div><div class="kcol" style="left:173px"></div><div class="kcol" style="left:346px"></div>
  <div class="kh" style="left:0"><span>AT RISK</span><b id="kc0">2</b></div><div class="kh" style="left:173px"><span>NUDGED</span><b id="kc1">1</b></div><div class="kh" style="left:346px"><span>BACK</span><b id="kc2">1</b></div>
  <div class="kcard" id="kp" style="left:0;top:134px"><b>Jo P.</b><small>Class pack · 9 days</small></div>
  <div class="kcard" id="km" style="left:173px;top:40px"><b>Ravi K.</b><small>Monthly · nudged</small></div>
  <div class="kcard" id="kl" style="left:346px;top:40px"><b>Mia T.</b><small>Unlimited · back</small></div>
  <div class="kcard hero" id="kd"><b>Sam R.</b><small>Unlimited · 14 days</small></div></div></div>
<div class="l8" id="l8a" style="top:650px"></div><div class="l8" id="l8b" style="top:715px"></div><div class="l8" id="l8c" style="top:780px"></div>
<div id="finger"></div><div id="rip"></div>
<div id="cap"></div><div id="prog"></div>
<div id="end"><img src="logo.png"><div class="h">Keep every<br><em>member.</em></div><div class="u">Comment “MEMBERS”</div><div class="s">Know a gym owner? <em>Send them this.</em></div><div class="n">THE TOTAL FORGE</div><div class="t">FORGING DIGITAL EXCELLENCE</div><div class="sv">thetotalforge.com</div></div>
</div>'''
cfg=open('cfg.json').read()
js=open('reel.js').read().replace('/*CFG*/{}',cfg)
open('reel_built.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+css+extra+'</head>'+body+'<script>'+js+'</script></body></html>')
print('ok')
