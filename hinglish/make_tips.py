# Generates episodes/r03..r15.json (animation data for the story/tips series), posts.json and scripts.json.
# usage: python3 make_tips.py     (text lives in tips_content.py, helpers in dsl.py)
import json, os
from dsl import *
import tips_content as TC
H = os.path.dirname(os.path.abspath(__file__))
X = {x['id']: x for x in TC.TIPS}
EPS = {}

# emoji stickers per reel (hook, pain-bubble reaction, mess, three tips, result); must exist in engine/make_emoji_font.py EMOJI
EMO = {
    'r02': dict(hook='🥲', pain='😬', mess='💀', tips=['⏳', '🎯', '🌍'], res='🚀'),
    'r03': dict(hook='🔎', pain='😬', mess='💀', tips=['🧵', '🏢', '📋'], res='🎉'),
    'r04': dict(hook='😬', pain='😮‍💨', mess='🤦', tips=['🎯', '📎', '❓'], res='🎉'),
    'r05': dict(hook='💸', pain='😬', mess='🤦', tips=['🏦', '⏱️', '🚫'], res='💰'),
    'r06': dict(hook='🏷️', pain='🥲', mess='💀', tips=['📦', '🧾', '🤝'], res='💰'),
    'r07': dict(hook='⏰', pain='😬', mess='💀', tips=['⚡', '🕒', '✍️'], res='🤝'),
    'r08': dict(hook='👀', pain='😬', mess='🤦', tips=['📝', '⭐', '🤝'], res='🚀'),
    'r09': dict(hook='🤯', pain='😮‍💨', mess='😵', tips=['🏆', '🧩', '📱'], res='🎉'),
    'r10': dict(hook='📩', pain='😬', mess='💀', tips=['🔍', '💡', '❓'], res='🎉'),
    'r11': dict(hook='💼', pain='😬', mess='🤦', tips=['💰', '🧰', '🫡'], res='🚀'),
    'r12': dict(hook='😮‍💨', pain='😤', mess='💀', tips=['📝', '🔁', '💵'], res='🎉'),
    'r13': dict(hook='🚩', pain='😬', mess='🚫', tips=['🆓', '💸', '⏰'], res='✅'),
    'r14': dict(hook='🎯', pain='🥲', mess='🤦', tips=['👥', '🔧', '📌'], res='🏆'),
    'r15': dict(hook='⏱️', pain='😮‍💨', mess='💀', tips=['📨', '🛠️', '📊'], res='🥳'),
}
import sys as _s; _s.path.insert(0, os.path.join(H, 'engine'))
from make_emoji_font import chars as _EC
for _id, _e in EMO.items():
    for _v in ([_e['hook'], _e['pain'], _e['mess'], _e['res']] + _e['tips']):
        assert all(c in _EC() for c in _v), (_id, _v)

def ep(id, hook, pain, mess, builds, res, chip, chipAt, hub='TIP'):
    x = X[id]; L = x['lines']; p = pain
    for b in builds:
        for mm in b['demo'].get('msgs', []):
            assert len(mm['text']) <= 29, (id, mm['text'])
    ch = [c[0] for c in mess['chips']]
    assert len(ch[0]) <= 7 and len(ch[2]) <= 7 and len(ch[1]) <= 10, (id, ch)
    pn = dict(bubble=dict(label=p['bl'], text=p['bt'], at=p['bat']),
              rows=rr(L[1], p['cap']), reply=dict(label=p['rl'], text=p['rt'], at=p['rat']),
              stamp=dict(text=p['st'], at=p['sat'], size=min(70, int(520 / (0.74 * len(p['st']))))))
    pn['clock'] = dict(**{'from': p['cf'], 'to': p['ct']}) if p.get('cf') is not None else None
    E = dict(id=id, business=x['topic'], keyword=x['kw'], lines=L, bridge=bridge_for(L[3]), hub=hub,
             tag='EXAMPLE SCENARIO', tagged=[1, 2], emo=EMO.get(id, {}),
             hook=dict(rows=rr(L[0], hook)), pain=pn,
             mess=dict(chips=[dict(text=t, at=a) for t, a in mess['chips']], rows=rr(L[2], mess['big']), sub=mess['sub'],
                       subAt=mess['subAt'], minisAt=mess['minisAt'], subSize=mess.get('subSize', 58)),
             builds=builds,
             result=dict(rows=rr(L[7], [(0, 1, 'lime', 44, dict(ls=6))] + list(res)), chip='&#10003; ' + chip, chipAt=chipAt),
             cta=dict(thing=x['thing'], noun=x['thing'], keyword=x['kw']))
    for k, bd in enumerate(builds):   # list demos get a punchy caption (last words of the tip) to fill the lower half
        dm = bd['demo']
        if dm['type'] == 'list' and 'caption' not in dm:
            ws = L[4 + k].split(); n = CAPN.get((id, k)) or (3 if len(' '.join(ws[-3:])) <= 22 else 2)
            dm['caption'] = dict(top=880, rows=rr(L[4 + k], [(len(ws) - n, len(ws), 'ink', 64)]))
    EPS[id] = E

CAPN = {('r03', 0): 3, ('r03', 1): 3}
W, LI, RD = 'white', 'lime', 'red'

# ------------------------------------------------------------ r02 CLIENTS (problem)
ep('r02',
   [(0, 3, W, 56), (3, 4, LI, 110, dict(mt=6)), (4, 6, W, 66, dict(mt=8)), (6, 7, W, 66), (7, 9, RD, 78, dict(mt=18))],
   dict(bl='AGENCY', bt='Website ready ✓', bat=4, cf=11, ct=13, cap=[(14, 15, 'ink', 66), (15, 18, 'ink', 66)],
        rl='INBOX', rt='0 inquiries', rat=14, st='ZERO INQUIRY.', sat=17),
   dict(chips=[('Client', 0), ('dhoondta', 2), ('nahi,', 3)], big=[(6, 7, W, 120), (7, 9, W, 120)],
        sub='intezaar?<br>nahi, outreach.', subAt=8, minisAt=5),
   [build('WAITING', 2, lst('REASON 1', [R('Waiting', 'Profile up, hope on', 'OLD', 2, **RED), R('Outreach', 'Message them first', 'NEW', 6)])),
    build('SKILLS VS RESULT', 2, lst('REASON 2', [R('Skills', 'React, design, SEO', 'OLD', 2, **RED), R('Result', 'A problem solved', 'NEW', 4)])),
    build('ONE PLACE', 2, lst('REASON 3', [R('One platform', 'Only here you exist', 'OLD', 3, **RED), R('Many places', 'Seen where clients look', 'NEW', 7)]))],
   [(1, 3, W, 72, dict(mt=60)), (3, 5, W, 72, dict(mt=10)), (5, 7, LI, 80, dict(mt=10)), (7, 9, LI, 80, dict(mt=6))], 'BAAT SHURU', 5, hub='WAJAH')

# ------------------------------------------------------------ r03 HIDDEN places
ep('r03',
   [(0, 2, W, 56), (2, 3, LI, 130, dict(mt=6)), (3, 5, W, 66), (5, 8, W, 56, dict(mt=14)), (8, 10, RD, 56, dict(mt=20)), (10, 13, RD, 56)],
   dict(bl='AGENCY OWNER', bt='Proposal bheja ✓', bat=7, cf=7, ct=9, cap=[(13, 15, 'ink', 66)],
        rl='UPWORK', rt='Bahut proposals', rat=10, st='BHEED ZYADA.', sat=11),
   dict(chips=[('Jahan', 0), ('sab', 1), ('jaate', 2)], big=[(5, 6, W, 120), (6, 8, W, 120)],
        sub='sab wahi,<br>toh bheed wahi.', subAt=8, minisAt=3),
   [build('HACKER NEWS', 1, lst('MONTHLY THREAD', [R('Companies post', 'They seek freelancers', 'GIGS', 6), R('You reply or post', 'Seeking work, remote', 'YOU', 10)])),
    build('CLUTCH', 1, lst('CLUTCH', [R('Free profile', 'Create it once', 'FREE', 3), R('Buyers search', 'Agencies by service', 'FIND', 5)])),
    build('SORTLIST', 1, lst('SORTLIST', [R('Free listing', 'Agency profile banao', 'FREE', 3), R('Buyers search', 'Agency dhoondte hain', 'LEADS', 5)]))],
   [(1, 2, W, 100, dict(mt=60)), (2, 3, LI, 130, dict(mt=6)), (3, 5, W, 72, dict(mt=10)), (5, 6, LI, 110, dict(mt=10))], 'LESS CROWDED', 5)

# ------------------------------------------------------------ r04 PROPOSAL
ep('r04',
   [(0, 2, W, 56), (2, 3, W, 78), (3, 4, LI, 130, dict(mt=6)), (4, 5, W, 66), (5, 8, RD, 56, dict(mt=22))],
   dict(bl='PROPOSAL', bt='Hello sir, I am an expert', bat=12, cf=None, ct=None, cap=[(4, 7, 'ink', 66)],
        rl='INBOX', rt='0 replies', rat=15, st='COPY PASTE.', sat=17),
   dict(chips=[('Client', 0), ('copy', 2), ('paste', 3)], big=[(4, 6, W, 110), (6, 10, W, 100)],
        sub='cringe.<br>sab same.', subAt=10, minisAt=2),
   [build('FIRST LINE', 2, lst('PROPOSAL', [R('Site slow hai', 'About their problem', 'GOOD', 4), R('Hello sir', 'About yourself', 'SKIP', 8, **RED)])),
    build('PROOF', 5, lst('PROOF', [R('Similar project', 'One relevant example', 'ADD', 3), R('Two lines only', 'Short and clear', 'OK', 8)])),
    build('A QUESTION', 4, chat([('r', 'Kya main ek plan bhej doon?', 4), ('c', 'Haan, zaroor bhejiye', 9)], rr(X['r04']['lines'][6], [(3, 5, LI, 72)])))],
   [(1, 2, W, 90, dict(mt=60)), (2, 3, LI, 110, dict(strike='copy', mt=14)), (3, 5, W, 72, dict(mt=14)), (5, 7, W, 56, dict(mt=14)), (7, 11, LI, 56, dict(mt=10))], 'REPLIES', 7)

# ------------------------------------------------------------ r05 PAYMENT
ep('r05',
   [(0, 2, W, 56), (2, 3, LI, 130, dict(mt=6)), (3, 5, W, 78), (5, 7, RD, 56, dict(mt=22)), (7, 9, RD, 56), (9, 12, RD, 56)],
   dict(bl='CLIENT', bt='Payment sent ✓', bat=7, cf=None, ct=None, cap=[(10, 14, 'ink', 60)],
        rl='FREELANCER', rt='Paisa kahan hai?', rat=11, st='RASTA NAHI.', sat=13),
   dict(chips=[('Bina', 0), ('plan', 1), ('kaam', 3)], big=[(6, 7, W, 120), (7, 9, W, 120)],
        sub='bina plan,<br>bada risk.', subAt=8, minisAt=3),
   [build('PAYONEER', 1, lst('PAYONEER', [R('Account', 'Create it first', 'OPEN', 2), R('US bank details', 'Client pays here', 'READY', 6)])),
    build('LOCAL BANK', 1, lst('PAYOUT', [R('Payoneer', 'Payout sent', 'SENT', 4), R('Bank transfer', 'Takes 1 to 3 days', 'WAIT', 11, **AMB), R('Local bank', 'Money received', 'DONE', 12)])),
    build('WISE', 1, lst('WISE', [R('Wise', 'Not open in Pakistan', 'CLOSED', 5, **RED), R('Your plan', 'Use another option', 'SKIP', 10, **AMB)]))],
   [(1, 2, W, 100, dict(mt=60)), (2, 3, LI, 100, dict(strike='tension', mt=14)), (3, 4, W, 90, dict(mt=14)), (4, 7, W, 72, dict(mt=14)), (7, 9, LI, 72, dict(mt=10))], 'PLAN READY', 8)

# ------------------------------------------------------------ r06 PRICE
ep('r06',
   [(0, 1, LI, 130), (1, 3, W, 78, dict(mt=6)), (3, 5, W, 66, dict(mt=8)), (5, 8, RD, 56, dict(mt=22)), (8, 10, W, 56, dict(mt=6))],
   dict(bl='FREELANCER', bt='Rate: sabse kam', bat=3, cf=11, ct=14, cap=[(14, 16, 'ink', 70)],
        rl='CLIENTS', rt='Bahut clients ✓', rat=7, st='HAATH KHAALI.', sat=14),
   dict(chips=[('Sasta', 0), ('rate', 1), ('kaam', 4)], big=[(3, 5, W, 110), (5, 8, W, 90)],
        sub='seedha<br>nuksan.', subAt=8, minisAt=1),
   [build('PROJECT PRICE', 4, lst('QUOTE', [R('Per hour', 'Hours, hours, hours', 'OLD', 1, **RED), R('Per project', 'One clear price', 'NEW', 4)])),
    build('PACKAGES', 2, lst('PACKAGES', [R('Basic', 'Core work only', 'ENTRY', 4), R('Standard', 'Most clients pick', 'POPULAR', 5), R('Premium', 'Everything included', 'FULL', 7, **AMB)])),
    build('BUDGET', 7, chat([('r', 'Aapka budget kitna hai?', 7), ('c', 'Let me check, bata deta hoon', 8)], rr(X['r06']['lines'][6], [(5, 8, LI, 70)])))],
   [(1, 3, W, 64, dict(mt=60)), (3, 5, LI, 90, dict(mt=14)), (5, 7, W, 72, dict(mt=14)), (7, 8, LI, 110, dict(strike='bargain', mt=14)), (8, 10, W, 72, dict(mt=10))], 'YOU CHOOSE', 3)

# ------------------------------------------------------------ r07 REPLY
ep('r07',
   [(0, 2, W, 56), (2, 4, LI, 120, dict(mt=6)), (4, 6, W, 78), (6, 8, W, 56, dict(mt=16)), (8, 10, RD, 78, dict(mt=18))],
   dict(bl='CLIENT', bt='Kal tak bata do', bat=3, cf=8, ct=11, cap=[(15, 17, 'ink', 56), (17, 20, 'ink', 60)],
        rl='DOOSRA FREELANCER', rt='Project start ✓', rat=17, st='CLIENT GAYA.', sat=21),
   dict(chips=[('Kaam', 0), ('mast', 1), ('reply', 4)], big=[(4, 6, W, 120), (6, 7, W, 120)],
        sub='vibe<br>kharab.', subAt=7, minisAt=3),
   [build('QUICK REPLY', 1, chat([('c', 'Update kab milega?', 1), ('r', 'Mil gaya, kal tak bhejta hoon', 5), ('c', 'Thanks, theek hai ✓', 11)], rr(X['r07']['lines'][4], [(9, 12, LI, 66)]))),
    build('FIXED HOURS', 4, lst('YOUR HOURS', [R('Working hours', 'Mon to Fri', 'SET', 5), R('Time zone', 'Overlap hours shared', 'SHARED', 9)])),
    build('CONFIRM', 5, chat([('r', 'Baat hui: logo, 2 revisions', 3), ('r', 'Deadline: Friday ✓', 7), ('c', 'Confirmed ✓', 8)], rr(X['r07']['lines'][6], [(5, 7, LI, 72)])))],
   [(1, 3, W, 64, dict(mt=60)), (3, 4, LI, 110, dict(mt=14)), (4, 6, W, 72, dict(mt=14)), (6, 8, W, 72, dict(mt=10)), (8, 11, LI, 64, dict(mt=10))], 'REPEAT WORK', 8)

# ------------------------------------------------------------ r08 LINKEDIN
ep('r08',
   [(0, 2, W, 56), (2, 3, LI, 110, dict(mt=6)), (3, 4, W, 78), (4, 6, RD, 56, dict(mt=22)), (6, 9, RD, 56)],
   dict(bl='HEADLINE', bt='Hardworking professional', bat=5, cf=10, ct=12, cap=[(13, 16, 'ink', 66)],
        rl='CLIENT', rt='Tab closed', rat=13, st='PROFILE BAND.', sat=15),
   dict(chips=[('usse', 1), ('pata', 2), ('nahi', 4)], big=[(8, 10, W, 120), (10, 12, LI, 100)],
        sub='headline?<br>koi clue nahi.', subAt=11, minisAt=2),
   [build('HEADLINE', 1, lst('HEADLINE', [R('Hardworking pro', 'Says nothing', 'OLD', 1, **RED), R('Shopify developer', 'for skincare brands', 'NEW', 9)])),
    build('FEATURED', 1, lst('FEATURED', [R('Project one', 'Your best work', 'PIN', 5), R('Project two', 'Your best work', 'PIN', 6), R('Project three', 'Your best work', 'PIN', 7)])),
    build('CONNECT', 6, chat([('r', 'Hi Sam, aapka kaam acha laga', 6), ('r', 'Main speed fix karta hoon', 8), ('c', 'Sure, baat karte hain', 11)], rr(X['r08']['lines'][6], [(1, 3, LI, 66)])))],
   [(1, 2, W, 100, dict(mt=60)), (2, 4, LI, 72, dict(mt=10)), (4, 6, W, 72, dict(mt=10)), (6, 8, W, 64, dict(mt=10)), (8, 11, LI, 64, dict(mt=10))], 'NEW MESSAGES', 8)

# ------------------------------------------------------------ r09 PORTFOLIO
ep('r09',
   [(0, 1, LI, 130), (1, 3, W, 66, dict(mt=6)), (3, 4, W, 78), (4, 6, W, 56, dict(mt=16)), (6, 7, RD, 90, dict(mt=6)), (7, 11, RD, 46, dict(mt=18))],
   dict(bl='PORTFOLIO', bt='20 projects', bat=7, cf=12, ct=14, cap=[(17, 21, 'ink', 66)],
        rl='CLIENT', rt='Samajh nahi aaya', rat=16, st='CLIENT GAYA.', sat=19),
   dict(chips=[('Zyada', 0), ('projects', 1), ('matlab', 2)], big=[(4, 5, W, 120), (5, 6, RD, 120)],
        sub='kya dekhein?<br>pata nahi.', subAt=6, minisAt=1),
   [build('ONLY THREE', 3, lst('PORTFOLIO', [R('Project one', 'Your best', 'KEEP', 3), R('Project two', 'Your best', 'KEEP', 4), R('Project three', 'Your best', 'KEEP', 5)])),
    build('PROBLEM + FIX', 5, lst('EACH PROJECT', [R('Problem', 'What was wrong', 'WHY', 5), R('What you did', 'In two lines', 'HOW', 9)])),
    build('ONE LINK', 2, lst('YOUR LINK', [R('One link', 'All projects inside', 'LINK', 2), R('Mobile check', 'Opens fast, reads easy', 'TEST', 5, chip2='OK ✓', chip2At=9)]))],
   [(1, 3, W, 64, dict(mt=60)), (3, 5, LI, 100, dict(mt=10)), (5, 7, W, 64, dict(mt=10)), (7, 9, W, 64, dict(mt=6)), (9, 14, W, 46, dict(mt=20))], 'ONE MINUTE', 4)

# ------------------------------------------------------------ r10 EMAIL
ep('r10',
   [(0, 1, LI, 130), (1, 4, W, 66, dict(mt=6)), (4, 7, W, 56, dict(mt=8)), (7, 9, W, 56), (9, 11, RD, 78, dict(mt=18))],
   dict(bl='EMAIL', bt='Main ek expert hoon...', bat=6, cf=None, ct=None, cap=[(9, 12, 'ink', 60)],
        rl='INBOX', rt='0 replies', rat=12, st='REPLY ZERO.', sat=15),
   dict(chips=[('Kisi', 0), ('story', 6), ('time', 9)], big=[(7, 9, W, 110), (9, 11, W, 120)],
        sub='lambi email?<br>delete.', subAt=10, minisAt=5),
   [build('LINE 1', 1, chat([('r', 'Aapki site dekhi, nice design', 5), ('r', 'Checkout page slow lagta hai', 9)], rr(X['r10']['lines'][4], [(7, 10, LI, 60)]))),
    build('LINE 2', 1, chat([('r', 'Slow checkout = lost orders', 5), ('r', 'Ek chhota fix mere paas hai', 9)], rr(X['r10']['lines'][5], [(8, 10, LI, 66)]))),
    build('LINE 3', 1, chat([('r', 'Chhota plan bhej doon?', 5), ('c', 'Haan, bhej dijiye', 11)], rr(X['r10']['lines'][6], [(4, 6, LI, 72)])))],
   [(1, 2, W, 110, dict(mt=60)), (2, 4, LI, 90, dict(mt=10)), (4, 7, W, 64, dict(mt=10)), (7, 8, LI, 100, dict(mt=10))], 'EASY REPLY', 5)

# ------------------------------------------------------------ r11 QUIT (job to agency)
ep('r11',
   [(0, 2, W, 56), (2, 3, LI, 120, dict(mt=6)), (3, 5, W, 70), (5, 8, W, 56, dict(mt=18)), (8, 11, RD, 78)],
   dict(bl='EMPLOYEE', bt='Resign de diya ✓', bat=5, cf=10, ct=12, cap=[(13, 16, 'ink', 66)],
        rl='INCOME', rt='Zero', rat=14, st='NO PLAN.', sat=16),
   dict(chips=[('Pehle', 0), ('clients,', 1), ('phir', 2)], big=[(4, 6, W, 110), (6, 10, W, 90)],
        sub='pehle income,<br>phir resign.', subAt=9, minisAt=3),
   [build('FIRST CLIENT', 7, lst('WHILE EMPLOYED', [R('Day job', 'Keep your salary', 'KEEP', 1), R('First client', 'One small paid project', 'PAID', 6)])),
    build('SKILL + NICHE', 2, lst('YOUR OFFER', [R('Skill', 'Web, ads or design', 'PICK', 2), R('3 samples', 'Show before you sell', 'PROOF', 9)])),
    build('RESIGN LATER', 1, lst('CHECK FIRST', [R('Monthly costs', 'Write the number down', 'LIST', 5), R('Client income', 'Covers those costs', 'MATCH', 8)]))],
   [(1, 4, W, 64, dict(mt=60)), (4, 6, W, 64, dict(mt=10)), (6, 7, LI, 110, dict(mt=10)), (7, 10, LI, 66, dict(mt=6))], 'READY FIRST', 4)

# ------------------------------------------------------------ r12 SCOPE
ep('r12',
   [(0, 2, W, 56), (2, 3, LI, 110, dict(mt=6)), (3, 5, W, 78), (5, 8, RD, 66, dict(mt=22)), (8, 11, RD, 66)],
   dict(bl='CLIENT', bt='Ek chhota change aur?', bat=5, cf=None, ct=None, cap=[(7, 10, 'ink', 66)],
        rl='FREELANCER', rt='Theek hai... ✓', rat=9, st='PAISA WAHI.', sat=13),
   dict(chips=[('Scope', 0), ('likha', 1), ('nahi', 2)], big=[(5, 7, W, 120), (7, 10, W, 120)],
        sub='ek change,<br>phir ek aur.', subAt=9, minisAt=3),
   [build('WRITE SCOPE', 1, lst('SCOPE', [R('3 logo options', 'Included', 'IN', 3), R('Final files', 'Included', 'IN', 4), R('Extra work', 'Not included', 'OUT', 5, **RED)])),
    build('REVISIONS', 1, lst('REVISIONS', [R('Round 1', 'Included', 'FREE', 5), R('Round 2', 'Included', 'FREE', 6), R('Round 3', 'Extra charge', 'PAID', 7, **AMB)])),
    build('ADVANCE', 6, chat([('r', 'Shuru: 50% advance pehle', 5), ('c', 'Done, bhej diya ✓', 7)], rr(X['r12']['lines'][6], [(5, 7, LI, 72)])))],
   [(1, 3, W, 90, dict(mt=60)), (3, 4, LI, 100, dict(mt=10)), (4, 5, W, 90, dict(mt=10)), (5, 6, LI, 110, dict(mt=10))], 'DONE + PAID', 5)

# ------------------------------------------------------------ r13 FLAGS
ep('r13',
   [(0, 3, W, 56), (3, 5, LI, 110, dict(mt=6)), (5, 6, W, 78), (6, 10, RD, 56, dict(mt=22))],
   dict(bl='CLIENT', bt='Pehle ek free test karo', bat=3, cf=None, ct=None, cap=[(13, 15, 'ink', 60), (15, 17, 'ink', 60)],
        rl='FREELANCER', rt='Test bhej diya ✓', rat=7, st='PAYMENT NAHI.', sat=15),
   dict(chips=[('Signs', 0), ('pehle', 1), ('dikh', 3)], big=[(3, 5, W, 120), (5, 6, W, 120)],
        sub='ignore kiya,<br>nuksan hua.', subAt=8, minisAt=3),
   [build('FREE TEST', 1, lst('RED FLAG 1', [R('Free test project', 'Unpaid trial work', 'FLAG', 3, **RED), R('Show work first', 'Before any payment', 'FLAG', 7, **RED)])),
    build('NO ADVANCE', 1, lst('RED FLAG 2', [R('No advance', 'Refuses upfront pay', 'FLAG', 3, **RED), R('Pay later', 'After delivery only', 'FLAG', 6, **RED)])),
    build('UNCLEAR', 1, lst('RED FLAG 3', [R('Budget', 'Not clear', 'FLAG', 2, **RED), R('Everything', 'Marked urgent', 'FLAG', 7, **RED)]))],
   [(1, 3, W, 72, dict(mt=60)), (3, 4, LI, 110, dict(mt=10)), (4, 7, W, 56, dict(mt=10)), (7, 11, W, 46, dict(mt=18))], 'RIGHT CLIENT', 3)

# ------------------------------------------------------------ r14 FOCUS
ep('r14',
   [(0, 2, W, 56), (2, 3, LI, 110, dict(mt=6)), (3, 5, W, 78), (5, 8, RD, 56, dict(mt=22)), (8, 12, RD, 56)],
   dict(bl='AGENCY', bt='Hum sab kuch karte hain', bat=4, cf=None, ct=None, cap=[(11, 15, 'ink', 60)],
        rl='CLIENT', rt='Kya dena hai? Pata nahi', rat=15, st='KAAM NAHI.', sat=19),
   dict(chips=[('Jo', 0), ('sab', 1), ('kuch', 2)], big=[(7, 8, W, 120), (8, 10, W, 120)],
        sub='sab kuch,<br>par pehchaan nahi.', subAt=9, minisAt=4),
   [build('CLIENT TYPE', 4, lst('PICK ONE', [R('Everyone', 'Too broad', 'SKIP', 4, **RED), R('Skincare brands', 'One type of client', 'PICK', 7)])),
    build('ONE PROBLEM', 2, lst('PROBLEM', [R('Slow store', 'Shopify speed', 'FIX', 5), R('Only this one', 'Not everything', 'FOCUS', 7)])),
    build('SAMPLE', 6, lst('SAMPLE', [R('Before', 'Slow Shopify page', 'SLOW', 3, **RED), R('After', 'Your sample fix', 'FAST', 7)]))],
   [(1, 2, W, 72, dict(mt=60)), (2, 3, LI, 110, dict(mt=10)), (3, 5, W, 72, dict(mt=10)), (5, 7, W, 64, dict(mt=10)), (7, 9, LI, 64, dict(mt=8)), (9, 11, LI, 70, dict(mt=6))], 'CHOSEN', 9)

# ------------------------------------------------------------ r15 ROUTINE
ep('r15',
   [(0, 2, W, 78), (2, 3, LI, 130, dict(mt=6)), (3, 4, W, 78), (4, 6, RD, 56, dict(mt=22)), (6, 9, RD, 56)],
   dict(bl='DAY ONE', bt='Aaj bahut kaam kiya', bat=4, cf=11, ct=12, cap=[(13, 15, 'ink', 66)],
        rl='WEEK', rt='Koi activity nahi', rat=13, st='JOSH GAYA.', sat=14),
   dict(chips=[('Kabhi', 0), ('josh,', 3), ('clients', 4)], big=[(4, 6, W, 110), (6, 7, W, 120)],
        sub='josh aaya,<br>josh gaya.', subAt=6, minisAt=3),
   [build('OUTREACH', 1, lst('5 PER DAY', [R('Client 1', 'Message sent', 'SENT', 2), R('Client 2', 'Message sent', 'SENT', 4), R('Client 3', 'Proposal sent', 'SENT', 6)])),
    build('ONE FIX', 2, lst('10 MINUTES', [R('Profile', 'Update one line', 'EDIT', 2), R('Portfolio', 'Improve one project', 'EDIT', 4)])),
    build('TRACK', 2, lst('YOUR SHEET', [R('Client A', 'Replied', 'YES', 7), R('Client B', 'No reply yet', 'NO', 10, **RED)]))],
   [(1, 4, W, 64, dict(mt=60)), (4, 6, W, 72, dict(mt=10)), (6, 8, LI, 110, dict(mt=10)), (8, 10, W, 72, dict(mt=10))], 'A SYSTEM', 7)

# ------------------------------------------------------------ outputs
os.makedirs(f'{H}/episodes', exist_ok=True)
posts = []; scripts = []
for x in TC.TIPS:
    id = x['id']
    json.dump(EPS[id], open(f'{H}/episodes/{id}.json', 'w'), indent=1)
    posts.append(dict(id=id, date=x['date'], keyword=x['kw'], topic=x['topic'], caption=TC.caption(x),
                      firstComment=TC.first_comment(x), alt=TC.alt(x), dm=x['dm'], chars=x['chars']))
    scripts.append(dict(id=id, date=x['date'], topic=x['topic'], keyword=x['kw'], text='\n\n'.join(x['lines']), chars=x['chars']))
json.dump(posts, open(f'{H}/posts.json', 'w'), indent=1, ensure_ascii=False)
json.dump(scripts, open(f'{H}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print(len(EPS), 'episodes')
