css=open('../base.css').read()
extra='''<style>
:root{--ember:#e11d48}
.bizlogo{background:#e11d48}
.ev.new{background:#e11d48;box-shadow:0 8px 20px rgba(225,29,72,.35)}
.ev{opacity:0}
.lrow{display:flex;align-items:center;gap:12px;background:#fff;border-radius:18px;padding:12px 14px;margin-top:10px;box-shadow:0 2px 10px rgba(30,20,10,.08);border:2px solid transparent;opacity:0}
.lav{width:42px;height:42px;border-radius:50%;background:#ffe4ea;color:#e11d48;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none}
.lt{font-weight:800;font-size:16px}.ls{font-size:12px;color:#8a857b;font-weight:500;margin-top:2px}
.lchip{margin-left:auto;padding:6px 11px;border-radius:12px;font-size:11px;font-weight:800;letter-spacing:.5px;background:#ffe4ea;color:#e11d48;white-space:nowrap}
.istat{padding:14px 18px;margin-top:16px;font-weight:700;font-size:14px;opacity:0;display:flex;justify-content:space-between}
.istat span{color:#8a857b;font-weight:600}
#pgChat{background:#fff}
.chh{display:flex;gap:12px;align-items:center;padding-bottom:14px;border-bottom:1px solid #eee}
.rcm{max-width:84%;padding:12px 16px;border-radius:20px;font-weight:600;font-size:15px;line-height:1.35;margin-top:14px;opacity:0}
.rcm.cl{background:#eceae6;border-bottom-left-radius:6px}
.rcm.cr{background:#e11d48;color:#fff;margin-left:auto;border-bottom-right-radius:6px}
.rtag{font-size:11px;color:#8a857b;font-weight:600;text-align:right;margin-top:6px;opacity:0}
.lhd{display:flex;gap:14px;align-items:center;margin-top:8px;opacity:0}
.lav2{width:64px;height:64px;border-radius:50%;background:#ffe4ea;color:#e11d48;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}
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
.kcard.hero{background:#e11d48;border-color:#fda4af}.kcard.hero small{color:rgba(255,255,255,.8)}
#cap{top:872px}
#cap span{white-space:nowrap}
.lchip{color:#be123c}
#end .s{position:absolute;left:30px;right:30px;top:868px;text-align:center;font-weight:600;font-size:30px;color:rgba(255,255,255,.92);opacity:0}
#end .s em{font-style:normal;color:#c6ff35}
</style>'''
body='''<body><div id="root">
<div id="top"><img src="logo.png"><div class="nm">THE TOTAL FORGE</div><div class="tg">FORGING DIGITAL EXCELLENCE</div><div id="tableChip">DAY 06</div></div>
<div id="chaos"></div>
<div id="series"><img id="sLogo" src="logo.png"><div id="sT1"></div><div id="sT2"></div><div id="sT3">DAY 06 · SALON &amp; BARBER</div></div>
<div class="phone" id="phA"><div class="screen"><div class="isl"></div><div class="sb">9:41</div>
 <div class="pg" id="pgInbox"><div class="biz"><div class="bizlogo">C</div><div><div class="bn">Cutline Studio</div><div class="bs">Online booking</div></div></div>
  <div class="h1" style="margin-top:24px;font-size:26px">Book your visit</div><div class="sub" style="margin-bottom:6px">Pick a stylist</div>
  <div class="lrow" id="lr0"><div class="lav">M</div><div><div class="lt">Mia · Cuts &amp; colour</div><div class="ls">Next free: Sat 2:00 PM</div></div><div class="lchip" id="lc0">OPEN</div></div>
  <div class="lrow" id="lr1"><div class="lav">L</div><div><div class="lt">Leo · Fades &amp; beards</div><div class="ls">Next free: Sat 3:30 PM</div></div><div class="lchip">OPEN</div></div>
  <div class="lrow" id="lr2"><div class="lav">A</div><div><div class="lt">Ana · Styling</div><div class="ls">Next free: Sun 11:00 AM</div></div><div class="lchip">OPEN</div></div>
  <div class="card istat" id="inStat"><span>Calendar</span><b>One live calendar</b></div></div>
 <div class="pg" id="pgChat"><div class="chh"><div class="lav">M</div><div><div class="lt">Cutline Studio</div><div class="ls">Sat 2:00 PM · Cut &amp; colour</div></div></div>
  <div class="lrow" id="cm1" style="margin-top:22px;padding:18px 16px"><div><div class="lt">Pick a stylist</div><div class="ls">Mia · Cuts &amp; colour</div></div><div class="lchip" id="ci1">Tap</div></div>
  <div class="lrow" id="cm2" style="padding:18px 16px"><div><div class="lt">Book Sat 2:00 PM</div><div class="ls">Held by a small deposit</div></div><div class="lchip" id="bk1">Tap</div></div>
  <div class="rtag" id="cmTag" style="text-align:center;margin-top:14px;font-size:13px">Two taps. Done.</div></div>
 <div class="pg" id="pgLead"><div class="h1">Booking</div>
  <div class="lhd" id="lhd"><div class="lav2">J</div><div><div class="lt" style="font-size:20px">Jess R.</div><div class="lchip" style="margin:6px 0 0;display:inline-block">Cut &amp; colour</div></div></div>
  <div class="card lcard"><div class="lfr" id="lf0"><span>Slot</span><b>Sat 2:00 PM · Mia</b></div><div class="lfr" id="lf1"><span>Deposit</span><b style="color:#136b3b">Paid ✓</b></div><div class="lfr" id="lf2"><span>Double booking</span><b>Blocked</b></div><div class="lfr" id="lf3"><span>Status</span><b style="color:#be123c">Confirmed</b></div></div>
  <div class="lsv" id="lsv">Slot locked automatically ✓</div></div>
 <div class="pg" id="pgView"><div class="h1" style="margin-top:6px">See you Sat, Jess</div><div class="sub" id="vsub" style="opacity:0">Reminder sent · Fri 6:00 PM</div>
  <div id="tl2"><div class="hr" style="top:0">1:00</div><div class="hr" style="top:80px">2:00</div><div class="hr" style="top:160px">3:00</div><div class="hr" style="top:240px">4:00</div>
   <div class="ev new" id="ev1" style="top:40px;height:0;padding:0 14px">Cut &amp; colour · confirmed<small>Sat 2:00 PM · Mia</small></div>
   <div class="ev old" id="ev0" style="top:186px;height:66px">Beard trim<small>Sat 4:00 PM · Leo</small></div></div>
  <div id="vnote"><b>Jess replied YES</b>Reminder confirmed · slot stays booked</div></div>
</div></div>
<div class="panel" id="pipe"><div class="tag">OWNER VIEW</div>
 <div class="fh"><span>BOOKING BOARD</span><span class="live"><i id="liveDot"></i>LIVE</span></div>
 <div id="kb">
  <div class="kcol" style="left:0"></div><div class="kcol" style="left:173px"></div><div class="kcol" style="left:346px"></div>
  <div class="kh" style="left:0"><span>REQUESTED</span><b id="kc0">2</b></div><div class="kh" style="left:173px"><span>CONFIRMED</span><b id="kc1">1</b></div><div class="kh" style="left:346px"><span>DONE</span><b id="kc2">1</b></div>
  <div class="kcard" id="kp" style="left:0;top:134px"><b>Kai L.</b><small>Fade · Sat 11 AM</small></div>
  <div class="kcard" id="km" style="left:173px;top:40px"><b>Ana S.</b><small>Colour · deposit paid</small></div>
  <div class="kcard" id="kl" style="left:346px;top:40px"><b>Tom B.</b><small>Haircut · done</small></div>
  <div class="kcard hero" id="kd"><b>Jess R.</b><small>Cut · Sat 2 PM</small></div></div></div>
<div class="l8" id="l8a" style="top:650px"></div><div class="l8" id="l8b" style="top:715px"></div><div class="l8" id="l8c" style="top:780px"></div>
<div id="finger"></div><div id="rip"></div>
<div id="cap"></div><div id="prog"></div>
<div id="end"><img src="logo.png"><div class="h">Fill every<br><em>chair.</em></div><div class="u">Comment “CHAIR”</div><div class="s">Know a salon owner? <em>Send them this.</em></div><div class="n">THE TOTAL FORGE</div><div class="t">FORGING DIGITAL EXCELLENCE</div><div class="sv">thetotalforge.com</div></div>
</div>'''
cfg=open('cfg.json').read()
js=open('reel.js').read().replace('/*CFG*/{}',cfg)
open('reel_built.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+css+extra+'</head>'+body+'<script>'+js+'</script></body></html>')
print('ok')
