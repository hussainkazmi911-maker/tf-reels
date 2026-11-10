css=open('../base.css').read()
extra='''<style>
:root{--ember:#0d9488}
.bizlogo{background:#0d9488}
.ev.new{background:#0d9488;box-shadow:0 8px 20px rgba(13,148,136,.35)}
.ev{opacity:0}
.lrow{display:flex;align-items:center;gap:12px;background:#fff;border-radius:18px;padding:12px 14px;margin-top:10px;box-shadow:0 2px 10px rgba(30,20,10,.08);border:2px solid transparent;opacity:0}
.lav{width:42px;height:42px;border-radius:50%;background:#ccfbf1;color:#0d9488;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none}
.lt{font-weight:800;font-size:16px}.ls{font-size:12px;color:#8a857b;font-weight:500;margin-top:2px}
.lchip{margin-left:auto;padding:6px 11px;border-radius:12px;font-size:11px;font-weight:800;letter-spacing:.5px;background:#ccfbf1;color:#0d9488;white-space:nowrap}
.istat{padding:14px 18px;margin-top:16px;font-weight:700;font-size:14px;opacity:0;display:flex;justify-content:space-between}
.istat span{color:#8a857b;font-weight:600}
#pgChat{background:#fff}
.chh{display:flex;gap:12px;align-items:center;padding-bottom:14px;border-bottom:1px solid #eee}
.rcm{max-width:84%;padding:12px 16px;border-radius:20px;font-weight:600;font-size:15px;line-height:1.35;margin-top:14px;opacity:0}
.rcm.cl{background:#eceae6;border-bottom-left-radius:6px}
.rcm.cr{background:#0d9488;color:#fff;margin-left:auto;border-bottom-right-radius:6px}
.rtag{font-size:11px;color:#8a857b;font-weight:600;text-align:right;margin-top:6px;opacity:0}
.lhd{display:flex;gap:14px;align-items:center;margin-top:8px;opacity:0}
.lav2{width:64px;height:64px;border-radius:50%;background:#ccfbf1;color:#0d9488;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}
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
.kcard.hero{background:#0d9488;border-color:#5eead4}.kcard.hero small{color:rgba(255,255,255,.8)}
#cap{top:872px}
#cap span{white-space:nowrap}
.lchip{color:#115e59}
#end .s{position:absolute;left:30px;right:30px;top:868px;text-align:center;font-weight:600;font-size:30px;color:rgba(255,255,255,.92);opacity:0}
#end .s em{font-style:normal;color:#c6ff35}
</style>'''
body='''<body><div id="root">
<div id="top"><img src="logo.png"><div class="nm">THE TOTAL FORGE</div><div class="tg">FORGING DIGITAL EXCELLENCE</div><div id="tableChip">DAY 11</div></div>
<div id="chaos"></div>
<div id="series"><img id="sLogo" src="logo.png"><div id="sT1"></div><div id="sT2"></div><div id="sT3">DAY 11 · CLINICS</div></div>
<div class="phone" id="phA"><div class="screen"><div class="isl"></div><div class="sb">9:41</div>
 <div class="pg" id="pgInbox"><div class="biz"><div class="bizlogo">N</div><div><div class="bn">Northside Physio</div><div class="bs">Online booking</div></div></div>
  <div class="h1" style="margin-top:24px;font-size:26px">Book your session</div><div class="sub" style="margin-bottom:6px">Pick your visit</div>
  <div class="lrow" id="lr0"><div class="lav">I</div><div><div class="lt">Initial visit</div><div class="ls">First assessment</div></div><div class="lchip" id="lc0">BOOK</div></div>
  <div class="lrow" id="lr1"><div class="lav">F</div><div><div class="lt">Follow-up</div><div class="ls">Returning patients</div></div><div class="lchip">OPEN</div></div>
  <div class="lrow" id="lr2"><div class="lav">R</div><div><div class="lt">Review visit</div><div class="ls">Progress check</div></div><div class="lchip">OPEN</div></div>
  <div class="card istat" id="inStat"><span>Reminders</span><b>By text</b></div></div>
 <div class="pg" id="pgChat"><div class="chh"><div class="lav">N</div><div><div class="lt">Northside</div><div class="ls">Online booking</div></div></div>
  <div class="lrow" id="cm1" style="margin-top:22px;padding:18px 16px"><div><div class="lt">Pick a time</div><div class="ls">Tomorrow · 9:00 AM</div></div><div class="lchip" id="ci1">Tap</div></div>
  <div class="lrow" id="cm2" style="padding:18px 16px"><div><div class="lt">Fill in your forms</div><div class="ls">Intake and history</div></div><div class="lchip" id="bk1">Tap</div></div>
  <div class="rtag" id="cmTag" style="text-align:center;margin-top:14px;font-size:13px">No clipboard. No paper.</div></div>
 <div class="pg" id="pgLead"><div class="h1">Patient record</div>
  <div class="lhd" id="lhd"><div class="lav2">S</div><div><div class="lt" style="font-size:20px">Sam R.</div><div class="lchip" style="margin:6px 0 0;display:inline-block">Initial visit</div></div></div>
  <div class="card lcard"><div class="lfr" id="lf0"><span>Intake form</span><b style="color:#136b3b">Done</b></div><div class="lfr" id="lf1"><span>Session notes</span><b style="color:#136b3b">Saved</b></div><div class="lfr" id="lf2"><span>Patient record</span><b style="color:#115e59">Ready</b></div><div class="lfr" id="lf3"><span>Reminder text</span><b style="color:#136b3b">Set</b></div></div>
  <div class="lsv" id="lsv">Reminder sent ✓</div></div>
 <div class="pg" id="pgView"><div class="h1" style="margin-top:6px">Today’s sessions</div><div class="sub" id="vsub" style="opacity:0">Northside · Therapist calendar</div>
  <div id="tl2"><div class="hr" style="top:0">9 AM</div><div class="hr" style="top:80px">11 AM</div><div class="hr" style="top:160px">1 PM</div><div class="hr" style="top:240px">3 PM</div>
   <div class="ev new" id="ev1" style="top:40px;height:0;padding:0 14px">Sam R. · Initial<small>9 AM · Confirmed</small></div>
   <div class="ev old" id="ev0" style="top:186px;height:66px">Jo T. · Review<small>1 PM · Booked</small></div></div>
  <div id="vnote"><b>Reminder sent</b>Sam R. gets a text before the visit</div></div>
</div></div>
<div class="panel" id="pipe"><div class="tag">OWNER VIEW</div>
 <div class="fh"><span>PATIENT BOARD</span><span class="live"><i id="liveDot"></i>LIVE</span></div>
 <div id="kb">
  <div class="kcol" style="left:0"></div><div class="kcol" style="left:173px"></div><div class="kcol" style="left:346px"></div>
  <div class="kh" style="left:0"><span>BOOKED</span><b id="kc0">2</b></div><div class="kh" style="left:173px"><span>REMINDED</span><b id="kc1">1</b></div><div class="kh" style="left:346px"><span>SEEN</span><b id="kc2">1</b></div>
  <div class="kcard" id="kp" style="left:0;top:134px"><b>Ana M.</b><small>Review · booked</small></div>
  <div class="kcard" id="km" style="left:173px;top:40px"><b>Tom B.</b><small>Visit · reminded</small></div>
  <div class="kcard" id="kl" style="left:346px;top:40px"><b>Lee P.</b><small>Follow-up · seen</small></div>
  <div class="kcard hero" id="kd"><b>Sam R.</b><small>Initial visit</small></div></div></div>
<div class="l8" id="l8a" style="top:650px"></div><div class="l8" id="l8b" style="top:715px"></div><div class="l8" id="l8c" style="top:780px"></div>
<div id="finger"></div><div id="rip"></div>
<div id="cap"></div><div id="prog"></div>
<div id="end"><img src="logo.png"><div class="h">Forms done.<br><em>Reminders sent.</em></div><div class="u">Comment “HEALTH”</div><div class="s">Know a clinic owner? <em>Send them this.</em></div><div class="n">THE TOTAL FORGE</div><div class="t">FORGING DIGITAL EXCELLENCE</div><div class="sv">thetotalforge.com</div></div>
</div>'''
cfg=open('cfg.json').read()
js=open('reel.js').read().replace('/*CFG*/{}',cfg)
open('reel_built.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+css+extra+'</head>'+body+'<script>'+js+'</script></body></html>')
print('ok')
