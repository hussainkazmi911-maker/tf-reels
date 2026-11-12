# LEGACY (business series, Reels 1-15 of the first plan). Do not run: it overwrites episodes/ posts.json scripts.json. Current series: make_tips.py + tips_content.py.
# Generates episodes/r02..r15.json (animation data), posts.json (captions/dates) and scripts.json (voice scripts).
# usage: python3 make_episodes.py
import json, re, os
H = os.path.dirname(os.path.abspath(__file__))
N = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
BRIDGE = "Isiliye hum apne clients ke liye teen cheezein banate hain."

def rows(line, spec):
    ws = line.split(); i = 0; out = []
    for it in spec:
        if isinstance(it, int): i += it; continue
        seg, size, color = it[0], it[1], it[2]; o = it[3] if len(it) > 3 else {}
        sw = seg.split()
        assert [N(x) for x in sw] == [N(x) for x in ws[i:i + len(sw)]], (seg, ws[i:i + len(sw)])
        d = {'r': [i, i + len(sw)], 'size': size, 'color': color}; d.update(o); out.append(d); i += len(sw)
    return out

AMB = dict(bg='#ffd166', fg='#0b0d09'); RED = dict(bg='#ff4b3a', fg='#ffffff')
def R(title, sub, chip, at, **k):
    d = dict(title=title, sub=sub, chip=chip, at=at); d.update(k); return d

def form(header, fields, btn, at, done, doneAt):
    return dict(type='form', header=header, fields=[dict(label=a, value=b, at=c) for a, b, c in fields],
                button=dict(text=btn, at=at, done=done + ' ✓', doneAt=doneAt))
def chat(msgs, cap=None):
    d = dict(type='chat', msgs=[dict(who=w, text=t, at=a, y=300 + i * 125) for i, (w, t, a) in enumerate(msgs)])
    if cap: d['caption'] = dict(top=900, rows=cap)
    return d
def board(cols, cards, appear, colAts):
    cs = [dict(name=n, bg=b, fg=f, at=a) for (n, b, f), a in zip(cols, colAts)]
    return dict(type='board', appear=appear, cols=cs, cards=cards)
def lst(header, rws): return dict(type='list', header=header, rows=rws)
COLS3 = lambda a, b, c: [(a, '#ffd166', '#0b0d09'), (b, '#c6ff35', '#0b0d09'), (c, '#0b0d09', '#c6ff35')]
def card(i, n, it, row, moves=None, col=None):
    d = dict(id=i, name=n, item=it, row=row)
    if col: d['col'] = col
    if moves: d['moves'] = [dict(at=a, to=t) for a, t in moves]
    return d
def build(title, titleAt, demo):
    bg = {'chat': 'dark', 'board': 'cream', 'form': 'white', 'list': 'cream'}[demo['type']]
    return dict(title=title, titleAt=titleAt, bg=bg, demo=demo)

EPS = []
def ep(id, date, biz, kw, noun, L, hook, pain, mess, builds, res, chip, chipAt, hashtags, comment_biz):
    L = list(L); L[3] = BRIDGE
    L[8] = f"Want this for your {noun}? Comment {kw}, hum aap ko details bhej denge."
    assert len(L) == 9
    for b in builds:
        for mm in b['demo'].get('msgs', []):
            assert len(re.sub(r'&#\d+;', 'x', mm['text'])) <= 31, (id, mm['text'])
    ch = [c[0] for c in mess['chips']]
    assert len(ch[0]) <= 7 and len(ch[2]) <= 7 and len(ch[1]) <= 10, (id, ch)
    p = pain
    E = dict(id=id, business=biz, keyword=kw, lines=L,
        hook=dict(rows=rows(L[0], hook)),
        pain=dict(bubble=dict(label=p['bl'], text=p['bt'], at=p['bat']), clock=dict(from_=p['cf'], to=p['ct']),
                  rows=rows(L[1], p['cap']), reply=dict(label=p['rl'], text=p['rt'], at=p['rat']),
                  stamp=dict(text=p['st'], at=p['sat'], size=min(p.get('ss', 70), int(520 / (0.74 * len(p['st'])))))),
        mess=dict(chips=[dict(text=t, at=a) for t, a in mess['chips']], rows=rows(L[2], mess['big']), sub=mess['sub'],
                  subAt=mess['subAt'], minisAt=mess['minisAt'], subSize=mess.get('subSize', 58)),
        builds=builds,
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6))] + list(res)), chip='&#10003; ' + chip, chipAt=chipAt),
        cta=dict(noun=noun, keyword=kw))
    E['pain']['clock']['from'] = E['pain']['clock'].pop('from_')
    chars = sum(len(x) for x in L) + 8
    assert chars <= 640, (id, chars)
    EPS.append(dict(E=E, date=date, hashtags=hashtags, comment_biz=comment_biz, chars=chars))

def hook4(a, b, c, d, bsz=130, mt=6):
    return [(a, 56, 'white'), (b, bsz, 'lime', dict(mt=mt)), (c, 78, 'white'), (d, 46, 'red', dict(mt=22))]

# ---------------------------------------------------------------- r02 Salons
L = ["Aapki chair khaali hai, aur customer ka message unread.",
     "Customer ne poocha, kal ka slot hai? You replied next morning. Tab tak, booking gayi.",
     "Bookings DMs, WhatsApp aur calls mein bikhri hain.", None,
     "One. An online booking calendar. Customer apna time khud chunta hai.",
     "Two. Reminder messages, taaki koi apna slot miss na kare.",
     "Three. A daily schedule, jahan har chair ka kaam dikhta hai.",
     "Result? Aap chair bharte hain, messages nahi.", None]
ep('r02', '2026-11-13', 'Salons', 'CHAIR', 'salon', L,
   [('Aapki chair', 56, 'white'), ('khaali', 150, 'lime', dict(mt=8)), ('hai,', 78, 'white'), ('aur customer ka', 46, 'red', dict(mt=22)), ('message unread.', 46, 'red')],
   dict(bl='CUSTOMER', bt='kal ka slot hai?', bat='kal', cf='You', ct='morning.', cap=[9, ('next morning.', 66, 'ink')],
        rl='DOOSRA SALON', rt='Booking confirmed &#10003;', rat='Tab', st='BOOKING GAYI.', sat='booking'),
   dict(chips=[('DMs', 'DMs,'), ('WhatsApp', 'WhatsApp'), ('Calls', 'calls')], big=[6, ('bikhri', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaun aa raha hai?<br>pata nahi.', subAt='hain.', minisAt='calls'),
   [build('BOOKING CALENDAR', 'booking', lst('TOMORROW', [
        R('Ayesha K.', 'Haircut', 'BOOKED', 'calendar.', tag='10:00'), R('Bilal A.', 'Beard trim', 'BOOKED', 'apna', tag='11:30'),
        R('Sara M.', 'Facial', 'BOOKED', 'khud', tag='13:00'), R('Free slot', 'Open for booking', 'OPEN', 'chunta', tag='15:00', **AMB)]))
    , build('REMINDERS', 'Reminder', chat([('r', 'Reminder: kal 10:00 baje &#10003;', 'messages,'), ('c', 'Confirmed, aa rahi hoon', 'koi'),
        ('r', 'Slot reserved &#10003;', 'miss')], rows(L[5], [7, ('miss na kare.', 70, 'lime')])))
    , build('DAILY SCHEDULE', 'daily', board([('CHAIR 1', '#ffd166', '#0b0d09'), ('CHAIR 2', '#c6ff35', '#0b0d09'), ('CHAIR 3', '#0b0d09', '#c6ff35')],
        [card('10:00', 'Ayesha', 'Haircut', 0), card('10:30', 'Bilal', 'Beard trim', 0, None, 1), card('11:00', 'Sara', 'Facial', 0, None, 2), card('11:30', 'Hamza', 'Colour', 1)], 'jahan', ['har', 'chair', 'kaam']))],
   [('Aap chair', 88, 'white', dict(mt=70)), ('bharte hain,', 78, 'lime', dict(mt=30)), ('messages nahi.', 64, 'white', dict(mt=30, strike='messages'))],
   'FULL SCHEDULE', 'bharte', '#salonowner #salonbusiness #beautysalon #bookingsystem #thetotalforge', 'Salon owner')

# ---------------------------------------------------------------- r03 Restaurants
L = ["Rush ke time phone uthane wala koi nahi, aur order gaya.",
     "Customer ne poocha, aaj table milegi? You replied after an hour. Tab tak, woh chala gaya.",
     "Orders phone, WhatsApp aur DMs mein bikhre hain.", None,
     "One. A digital menu. Customer scan karta hai aur seedha order karta hai.",
     "Two. A table booking form. Date, time aur guests, bas teen tap.",
     "Three. A kitchen screen, jahan har order live dikhta hai.",
     "Result? Rush mein bhi order sahi, aur customer khush.", None]
ep('r03', '2026-11-14', 'Restaurants', 'MENU', 'restaurant', L,
   [('Rush ke time', 56, 'white'), ('phone', 150, 'lime', dict(mt=8)), ('uthane wala', 78, 'white'), ('koi nahi,', 78, 'white'), ('aur order gaya.', 52, 'red', dict(mt=22))],
   dict(bl='CUSTOMER', bt='aaj table milegi?', bat='aaj', cf='You', ct='hour.', cap=[8, ('after an hour.', 66, 'ink')],
        rl='DOOSRA RESTAURANT', rt='Table booked &#10003;', rat='Tab', st='CUSTOMER GAYA.', sat='woh', ss=54),
   dict(chips=[('Phone', 'phone,'), ('WhatsApp', 'WhatsApp'), ('DMs', 'DMs')], big=[6, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaunsa order bana?<br>pata nahi.', subAt='hain.', minisAt='DMs'),
   [build('DIGITAL MENU', 'digital', lst('MENU', [
        R('Chicken Biryani', 'Rs. 450', 'ADD', 'menu', chip2='ADDED ✓', chip2At='seedha'), R('Karahi (half)', 'Rs. 900', 'ADD', 'Customer'),
        R('Garlic Naan', 'Rs. 80', 'ADD', 'scan', chip2='ADDED ✓', chip2At='order')]))
    , build('TABLE BOOKING', 'table', form('Table booking', [('DATE', 'Friday', 'Date,'), ('TIME', '8:00 PM', 'time'), ('GUESTS', '4 people', 'guests,')], 'BOOK TABLE', 'bas', 'BOOKED', 'tap.'))
    , build('KITCHEN SCREEN', 'kitchen', board(COLS3('NEW', 'COOKING', 'READY'),
        [card('#21', 'Table 4', '2 Biryani', 0, [('live', 1), ('dikhta', 2)]), card('#22', 'Delivery', '1 Karahi', 1, [('dikhta', 1)]), card('#23', 'Table 7', '3 Naan', 2)], 'har', ['kitchen', 'order', 'live']))],
   [('Rush mein bhi', 72, 'white', dict(mt=66)), ('order sahi,', 90, 'lime', dict(mt=24)), ('aur customer khush.', 58, 'white', dict(mt=28))],
   'ORDER READY', 'sahi,', '#restaurantowner #restaurantbusiness #foodbusiness #digitalmenu #thetotalforge', 'Restaurant owner')

# ---------------------------------------------------------------- r04 Retail
L = ["Shop mein suit bik gaya, website par abhi bhi available hai.",
     "Customer ne order kiya, stock nahi tha. You apologised two days later. Tab tak, review kharab.",
     "Stock shop, website aur diary mein alag alag hai.", None,
     "One. Shop aur website ka stock, ek hi jagah sync.",
     "Two. A low-stock alert, taaki item khatam hone se pehle pata chale.",
     "Three. A daily sales screen, jahan har cheez ka hisaab dikhta hai.",
     "Result? Jo shop mein hai, wahi website par hai.", None]
ep('r04', '2026-11-15', 'Retail shops', 'STOCK', 'shop', L,
   [('Shop mein suit', 56, 'white'), ('bik gaya,', 120, 'lime', dict(mt=6)), ('website par abhi bhi', 50, 'white', dict(mt=14)), ('available hai.', 58, 'red', dict(mt=16))],
   dict(bl='CUSTOMER', bt='Order kar diya!', bat='order', cf='You', ct='later.', cap=[9, ('two days later.', 66, 'ink')],
        rl='NEW REVIEW', rt='&#9733; Item nahi mila', rat='Tab', st='REVIEW KHARAB.', sat='review', ss=58),
   dict(chips=[('Shop', 'shop,'), ('Website', 'website'), ('Diary', 'diary')], big=[6, ('alag', 120, 'white'), ('alag hai.', 120, 'white')],
        sub='kitna bacha hai?<br>pata nahi.', subAt='hai.', minisAt='diary'),
   [build('STOCK SYNC', 'stock,', lst('STOCK', [
        R('Black suit (M)', 'Shop + website', '3 LEFT', 'Shop', chip2='2 LEFT', chip2At='jagah'), R('Lawn suit', 'Shop + website', '5 LEFT', 'website'),
        R('Watch strap', 'Shop + website', '8 LEFT', 'stock,')]))
    , build('LOW-STOCK ALERT', 'low-stock', chat([('r', '&#9888; Black suit (M): sirf 2 bache', 'alert,'), ('r', 'Reorder reminder bhej diya &#10003;', 'pehle')], rows(L[5], [10, ('pata chale.', 80, 'lime')])))
    , build('SALES SCREEN', 'daily', lst('SALES TODAY', [
        R('Suits', 'Sold today', '12', 'jahan'), R('Shoes', 'Sold today', '8', 'har'), R('Accessories', 'Sold today', '21', 'cheez')]))],
   [('Jo shop mein hai,', 64, 'white', dict(mt=66)), ('wahi website', 88, 'lime', dict(mt=24)), ('par hai.', 88, 'lime')],
   'STOCK MATCHED', 'wahi', '#retailbusiness #shopowner #inventorymanagement #smallbusinesspakistan #thetotalforge', 'Shop owner')

# ---------------------------------------------------------------- r05 Tutors
L = ["Fees ka hisaab chats mein hai, aur mahine ke end mein pata chalta hai.",
     "Parent ne poocha, fees jama hui? You checked after two days. Tab tak, student chala gaya.",
     "Fees, attendance aur marks alag alag jagah bikhre hain.", None,
     "One. A fee tracker. Har student ki fee, due date ke saath.",
     "Two. Automatic reminders, taaki koi parent bhoole nahi.",
     "Three. A parent portal, jahan attendance aur marks dikhte hain.",
     "Result? Parents ko jawab milta hai, aapko time.", None]
ep('r05', '2026-11-16', 'Tutors and academies', 'LEARN', 'academy', L,
   [('Fees ka hisaab', 56, 'white'), ('chats', 150, 'lime', dict(mt=6)), ('mein hai,', 78, 'white'), ('aur mahine ke end mein', 40, 'red', dict(mt=18)), ('pata chalta hai.', 52, 'red', dict(mt=6))],
   dict(bl='PARENT', bt='fees jama hui?', bat='fees', cf='You', ct='days.', cap=[8, ('after two days.', 66, 'ink')],
        rl='DOOSRI ACADEMY', rt='Admission open &#10003;', rat='Tab', st='STUDENT GAYA.', sat='student', ss=62),
   dict(chips=[('Fees', 'Fees,'), ('Attendance', 'attendance'), ('Marks', 'marks')], big=[7, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaun defaulter hai?<br>pata nahi.', subAt='hain.', minisAt='marks'),
   [build('FEE TRACKER', 'fee', lst('FEES', [
        R('Ayesha K.', 'Class 9', 'PAID', 'Har'), R('Bilal A.', 'Class 8', 'DUE', 'student', **AMB), R('Sara M.', 'Class 10', 'DUE', 'fee,', chip2='PAID ✓', chip2At='saath.', bg='#ffd166', fg='#0b0d09', bg2='#0b0d09', fg2='#c6ff35')]))
    , build('REMINDERS', 'Automatic', chat([('r', 'Reminder: fee kal due hai', 'reminders,'), ('c', 'Thanks, kal bhej dunga', 'koi'),
        ('r', 'Payment mil gayi &#10003;', 'bhoole')], rows(L[5], [6, ('bhoole nahi.', 80, 'lime')])))
    , build('PARENT PORTAL', 'parent', lst('AYESHA K.', [
        R('Attendance', 'This month', '92%', 'jahan'), R('Math test', 'Unit 3', '85/100', 'attendance'), R('Fees', 'November', 'PAID', 'marks')]))],
   [('Parents ko', 72, 'white', dict(mt=66)), ('jawab milta hai,', 80, 'lime', dict(mt=24)), ('aapko time.', 72, 'white', dict(mt=24))],
   'NO CHASING', 'aapko', '#academyowner #tutoring #educationbusiness #feemanagement #thetotalforge', 'Academy owner')

# ---------------------------------------------------------------- r06 Clinics
L = ["Aaj teen patients nahi aaye, aur slot khaali gaye.",
     "Patient ne appointment li, phir bhool gaya. You noticed that evening. Tab tak, slot khaali.",
     "Appointments calls, WhatsApp aur diary mein bikhri hain.", None,
     "One. An online appointment booking. Patient khud slot chunta hai.",
     "Two. SMS aur WhatsApp reminders, appointment se pehle.",
     "Three. A patient record, jahan har visit ka note dikhta hai.",
     "Result? Slots bharte hain, patients bhoolte nahi.", None]
ep('r06', '2026-11-17', 'Clinics and dentists', 'CLINIC', 'clinic', L,
   [('Aaj teen', 56, 'white'), ('patients', 110, 'lime', dict(mt=8)), ('nahi aaye,', 78, 'white'), ('aur slot', 52, 'red', dict(mt=22)), ('khaali gaye.', 52, 'red', dict(mt=4))],
   dict(bl='PATIENT', bt='kal 10 baje &#10003;', bat='appointment', cf='You', ct='evening.', cap=[9, ('that evening.', 66, 'ink')],
        rl='10:00 SLOT', rt='Koi nahi aaya', rat='Tab', st='SLOT KHAALI.', sat='slot'),
   dict(chips=[('Calls', 'calls,'), ('WhatsApp', 'WhatsApp'), ('Diary', 'diary')], big=[6, ('bikhri', 120, 'white'), ('hain.', 120, 'white')],
        sub='aaj kaun aa raha hai?<br>pata nahi.', subAt='hain.', minisAt='diary', subSize=52),
   [build('ONLINE BOOKING', 'online', lst('TODAY', [
        R('Ayesha K.', 'Check-up', 'BOOKED', 'online', tag='09:00'), R('Bilal A.', 'Follow-up', 'BOOKED', 'Patient', tag='09:30'), R('Sara M.', 'Check-up', 'BOOKED', 'slot', tag='10:00')]))
    , build('REMINDERS', 'SMS', chat([('r', 'Reminder: kal 9:00 baje', 'reminders,'), ('c', 'Confirmed, aa raha hoon', 'appointment'),
        ('r', 'See you tomorrow &#10003;', 'pehle')], rows(L[5], [5, ('appointment se pehle.', 60, 'lime')])))
    , build('PATIENT RECORD', 'patient', lst('AYESHA K.', [
        R('Visit: 12 Oct', 'Follow-up in 2 weeks', 'SAVED', 'jahan'), R('Visit: 28 Oct', 'Reminder set', 'SAVED', 'har'), R('Next: 15 Nov', 'Booked online', 'BOOKED', 'note')]))],
   [('Slots bharte hain,', 70, 'white', dict(mt=66)), ('patients', 96, 'lime', dict(mt=20)), ('bhoolte nahi.', 78, 'lime')],
   'SLOT FULL', 'Slots', '#clinicowner #healthcarebusiness #appointmentbooking #clinicmanagement #thetotalforge', 'Clinic owner')

# ---------------------------------------------------------------- r07 Real estate
L = ["Client ne enquiry ki, aur aapne kal reply kiya.",
     "Buyer ne poocha, flat available hai? You replied next day. Tab tak, deal kisi aur ke paas.",
     "Leads portals, WhatsApp aur calls mein bikhri hain.", None,
     "One. An enquiry form. Har lead apni details khud bhejta hai.",
     "Two. An instant reply, jismein listings aur viewing link hain.",
     "Three. A pipeline screen, jahan har lead ka stage dikhta hai.",
     "Result? Har lead ka jawab, aur har deal ka hisaab.", None]
ep('r07', '2026-11-18', 'Real estate agents', 'LEADS', 'agency', L,
   [('Client ne', 56, 'white'), ('enquiry', 120, 'lime', dict(mt=8)), ('ki,', 78, 'white'), ('aur aapne', 52, 'red', dict(mt=22)), ('kal reply kiya.', 52, 'red', dict(mt=4))],
   dict(bl='BUYER', bt='flat available hai?', bat='flat', cf='You', ct='day.', cap=[8, ('next day.', 66, 'ink')],
        rl='DOOSRA AGENT', rt='Viewing booked &#10003;', rat='Tab', st='DEAL GAYI.', sat='deal'),
   dict(chips=[('Portals', 'portals,'), ('WhatsApp', 'WhatsApp'), ('Calls', 'calls')], big=[6, ('bikhri', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaunsa lead hot hai?<br>pata nahi.', subAt='hain.', minisAt='calls', subSize=54),
   [build('ENQUIRY FORM', 'enquiry', form('New enquiry', [('NAME', 'Bilal A.', 'lead'), ('PHONE', '03XX XXXXXXX', 'apni'), ('LOOKING FOR', '2-bed flat', 'details')], 'SEND ENQUIRY', 'khud', 'SENT', 'hai.'))
    , build('INSTANT REPLY', 'instant', chat([('c', 'flat available hai?', 'An'), ('r', 'Ji! Listings + viewing link &#8599;', 'jismein'), ('c', 'Saturday ko dekh sakta hoon', 'viewing')], None))
    , build('LEAD PIPELINE', 'pipeline', board(COLS3('NEW', 'VIEWING', 'CLOSED'),
        [card('Bilal A.', '2-bed flat', 'DHA', 0, [('stage', 1), ('dikhta', 2)]), card('Sara M.', '3-bed house', 'Clifton', 1, [('dikhta', 1)]), card('Hamza R.', 'Plot', 'Bahria', 2)], 'har', ['jahan', 'lead', 'stage']))],
   [('Har lead', 88, 'white', dict(mt=70)), ('ka jawab,', 88, 'lime'), ('aur har deal ka hisaab.', 44, 'white', dict(mt=26))],
   'LEAD REPLIED', 'jawab,', '#realestateagent #propertybusiness #leadgeneration #realestatepakistan #thetotalforge', 'Real estate agent')

# ---------------------------------------------------------------- r08 Gyms
L = ["Member ki fee due hai, lekin kisi ko pata nahi.",
     "Member ne poocha, plan renew kaise karun? You replied after three days. Tab tak, membership gayi.",
     "Fees, attendance aur plans alag alag diary mein hain.", None,
     "One. A member signup, jismein fee due date set hoti hai.",
     "Two. Renewal reminders, taaki koi membership expire na ho.",
     "Three. A check-in log, jahan har member ki attendance dikhti hai.",
     "Result? Sab members ka hisaab, ek hi screen par.", None]
ep('r08', '2026-11-19', 'Gyms', 'MEMBERS', 'gym', L,
   [('Member ki', 56, 'white'), ('fee due', 130, 'lime', dict(mt=8)), ('hai,', 78, 'white'), ('lekin kisi ko', 52, 'red', dict(mt=22)), ('pata nahi.', 52, 'red', dict(mt=4))],
   dict(bl='MEMBER', bt='renew kaise karun?', bat='plan', cf='You', ct='days.', cap=[9, ('after three days.', 62, 'ink')],
        rl='DOOSRA GYM', rt='Membership joined &#10003;', rat='Tab', st='MEMBER GAYA.', sat='membership'),
   dict(chips=[('Fees', 'Fees,'), ('Attendance', 'attendance'), ('Plans', 'plans')], big=[4, ('alag alag', 110, 'white'), ('diary mein hain.', 66, 'white')],
        sub='kaun active hai?<br>pata nahi.', subAt='hain.', minisAt='plans'),
   [build('MEMBER SIGNUP', 'member', form('New member', [('NAME', 'Hamza R.', 'member'), ('PLAN', 'Monthly', 'fee'), ('DUE DATE', '1 Dec', 'date')], 'JOIN GYM', 'set', 'JOINED', 'hai.'))
    , build('REMINDERS', 'Renewal', chat([('r', 'Membership kal expire hogi &#9888;', 'reminders,'), ('c', 'Renew kar do', 'koi'), ('r', 'Renewed &#10003; See you at the gym', 'expire')], rows(L[5], [6, ('expire na ho.', 70, 'lime')])))
    , build('CHECK-IN LOG', 'check-in', lst('TODAY', [
        R('Hamza R.', 'Checked in 6:15 AM', 'IN', 'har'), R('Sara K.', 'Checked in 7:00 AM', 'IN', 'member'), R('Bilal A.', 'Fee due', 'DUE', 'attendance', **AMB)]))],
   [('Sab members ka', 68, 'white', dict(mt=66)), ('hisaab,', 110, 'lime'), ('ek hi screen par.', 70, 'white', dict(mt=20))],
   'ALL TRACKED', 'hisaab,', '#gymowner #fitnessbusiness #gymmanagement #membershipmanagement #thetotalforge', 'Gym owner')

# ---------------------------------------------------------------- r09 Auto repair
L = ["Gaadi ready hai? Yeh sawaal din mein chaar baar.",
     "Customer ne poocha, gaadi ready hai? You called back after lunch. Tab tak, kaam ruk gaya.",
     "Jobs diary, WhatsApp aur phone mein bikhri hain.", None,
     "One. A job card, jismein gaadi ka kaam likha hota hai.",
     "Two. Status updates, jo customer ko khud mil jaate hain.",
     "Three. A workshop board, jahan har bay ka kaam dikhta hai.",
     "Result? Kam calls, zyada gaadiyan.", None]
ep('r09', '2026-11-20', 'Auto repair shops', 'GARAGE', 'garage', L,
   [('Gaadi', 56, 'white'), ('ready hai?', 120, 'lime', dict(mt=8)), ('Yeh sawaal din mein', 52, 'white', dict(mt=12)), ('chaar baar.', 60, 'red', dict(mt=10))],
   dict(bl='CUSTOMER', bt='gaadi ready hai?', bat='gaadi', cf='You', ct='lunch.', cap=[9, ('after lunch.', 66, 'ink')],
        rl='MECHANIC', rt='Phone pe busy hoon&#8230;', rat='Tab', st='KAAM RUKA.', sat='kaam'),
   dict(chips=[('Diary', 'diary,'), ('WhatsApp', 'WhatsApp'), ('Phone', 'phone')], big=[6, ('bikhri', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaunsi gaadi ready?<br>pata nahi.', subAt='hain.', minisAt='phone'),
   [build('JOB CARD', 'job', form('New job card', [('CAR', 'Honda City', 'gaadi'), ('PROBLEM', 'Brake check', 'kaam'), ('OWNER', 'Bilal A.', 'likha')], 'OPEN JOB', 'hota', 'JOB OPENED', 'hai.'))
    , build('STATUS UPDATES', 'updates,', chat([('r', 'Gaadi service mein hai', 'updates,'), ('r', 'Update: kaam complete &#10003;', 'khud'), ('r', 'Gaadi ready, pickup kar lein', 'hain.')], rows(L[5], [6, ('khud mil jaate hain.', 56, 'lime')])))
    , build('WORKSHOP BOARD', 'workshop', board(COLS3('WAITING', 'IN BAY', 'READY'),
        [card('#41', 'Honda City', 'Brake check', 0, [('kaam', 1), ('dikhta', 2)]), card('#42', 'Alto', 'Oil change', 1, [('dikhta', 1)]), card('#43', 'Corolla', 'AC service', 2)], 'har', ['jahan', 'bay', 'kaam']))],
   [('Kam calls,', 110, 'white', dict(mt=70)), ('zyada gaadiyan.', 96, 'lime', dict(mt=20))],
   'JOB READY', 'zyada', '#autorepair #garageowner #workshopmanagement #carservice #thetotalforge', 'Garage owner')

# ---------------------------------------------------------------- r10 Online stores
L = ["Instagram par sab like karte hain, order koi nahi.",
     "Customer ne poocha, website ka link? You sent it next morning. Tab tak, woh bhool gaya.",
     "Products DMs, Instagram aur Drive mein bikhre hain.", None,
     "One. A product website, jahan har cheez ek jagah hoti hai.",
     "Two. A secure checkout, jahan payment seedha hoti hai.",
     "Three. An order tracking page, jahan customer khud status dekhta hai.",
     "Result? Likes se orders tak, ek hi raasta.", None]
ep('r10', '2026-11-21', 'Online stores', 'STORE', 'store', L,
   [('Instagram par', 56, 'white'), ('sab like', 130, 'lime', dict(mt=8)), ('karte hain,', 78, 'white'), ('order koi nahi.', 54, 'red', dict(mt=22))],
   dict(bl='CUSTOMER', bt='website ka link?', bat='website', cf='You', ct='morning.', cap=[9, ('next morning.', 66, 'ink')],
        rl='DOOSRA STORE', rt='Checkout done &#10003;', rat='Tab', st='ORDER GAYA.', sat='bhool'),
   dict(chips=[('DMs', 'DMs,'), ('Instagram', 'Instagram'), ('Drive', 'Drive')], big=[6, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kya available hai?<br>pata nahi.', subAt='hain.', minisAt='Drive'),
   [build('PRODUCT PAGE', 'product', lst('PRODUCTS', [
        R('Black kurta', 'Rs. 3,500', 'IN STOCK', 'website,'), R('Sneakers', 'Rs. 6,000', 'IN STOCK', 'har'), R('Lawn suit', 'Rs. 4,200', 'IN STOCK', 'ek')]))
    , build('SECURE CHECKOUT', 'secure', form('Checkout', [('NAME', 'Ayesha K.', 'secure'), ('ADDRESS', 'House 12, Block 5', 'jahan'), ('PAYMENT', 'Card or COD', 'payment')], 'PAY NOW', 'seedha', 'PAID', 'hai.'))
    , build('ORDER TRACKING', 'tracking', board(COLS3('PACKED', 'SHIPPED', 'DELIVERED'),
        [card('#301', 'Ayesha', 'Black kurta', 0, [('khud', 1), ('dekhta', 2)]), card('#302', 'Bilal', 'Sneakers', 1, [('status', 1)]), card('#303', 'Sara', 'Lawn suit', 2)], 'jahan', ['tracking', 'status', 'dekhta']))],
   [('Likes se orders tak,', 64, 'white', dict(mt=70)), ('ek hi raasta.', 96, 'lime', dict(mt=24))],
   'ORDER PLACED', 'ek', '#ecommerce #onlinestore #ecommercebusiness #onlineshoppingpakistan #thetotalforge', 'Store owner')

# ---------------------------------------------------------------- r11 Wholesalers
L = ["Udhaar ka hisaab diary mein hai, aur diary kho gayi.",
     "Retailer ne poocha, mera balance kitna hai? You found it after an hour. Tab tak, order gaya.",
     "Orders, payments aur prices diary aur WhatsApp mein bikhre hain.", None,
     "One. A price list page, jo retailer khud dekh sakta hai.",
     "Two. A bulk order form, jismein retailer quantity khud bharta hai.",
     "Three. A payments ledger, jahan har retailer ka hisaab dikhta hai.",
     "Result? Udhaar ka hisaab, ek click par.", None]
ep('r11', '2026-11-22', 'Wholesalers', 'WHOLESALE', 'business', L,
   [('Udhaar ka hisaab', 56, 'white'), ('diary', 150, 'lime', dict(mt=6)), ('mein hai,', 78, 'white'), ('aur diary kho gayi.', 50, 'red', dict(mt=22))],
   dict(bl='RETAILER', bt='mera balance kitna hai?', bat='mera', cf='You', ct='hour.', cap=[10, ('after an hour.', 66, 'ink')],
        rl='DOOSRA SUPPLIER', rt='Order confirmed &#10003;', rat='Tab', st='ORDER GAYA.', sat='order'),
   dict(chips=[('Orders', 'Orders'), ('Payments', 'payments'), ('Prices', 'prices')], big=[8, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kis ka kitna baaki?<br>pata nahi.', subAt='hain.', minisAt='diary', subSize=52),
   [build('PRICE LIST', 'price', lst('PRICE LIST', [
        R('Sugar 50kg', 'Rs. 8,500', 'ORDER', 'list'), R('Rice 25kg', 'Rs. 7,200', 'ORDER', 'retailer'), R('Cooking oil 5L', 'Rs. 2,400', 'ORDER', 'dekh')]))
    , build('BULK ORDER', 'bulk', form('Bulk order', [('RETAILER', 'Karim Traders', 'retailer'), ('ITEM', 'Sugar 50kg', 'quantity'), ('QUANTITY', '20 bags', 'khud')], 'SEND ORDER', 'bharta', 'ORDER SENT', 'hai.'))
    , build('PAYMENTS LEDGER', 'payments', lst('LEDGER', [
        R('Karim Traders', 'Rs. 45,000 pending', 'DUE', 'har', chip2='PAID ✓', chip2At='dikhta', bg='#ffd166', fg='#0b0d09', bg2='#0b0d09', fg2='#c6ff35'),
        R('Noor Store', 'Cleared', 'PAID', 'retailer'), R('Ali and Sons', 'Rs. 12,500 pending', 'DUE', 'hisaab', **AMB)]))],
   [('Udhaar ka', 72, 'white', dict(mt=70)), ('hisaab,', 110, 'lime'), ('ek click par.', 90, 'white', dict(mt=20))],
   'BALANCE CLEAR', 'ek', '#wholesalebusiness #distributor #businessledger #tradingbusiness #thetotalforge', 'Wholesaler')

# ---------------------------------------------------------------- r12 Builders
L = ["Site par kya hua, raat ko WhatsApp se pata chalta hai.",
     "Owner ne poocha, kaam kahan tak pahuncha? You replied that night. Tab tak, delay ho chuka tha.",
     "Updates, bills aur photos WhatsApp mein bikhre hain.", None,
     "One. A project tracker, jahan har stage ka status dikhta hai.",
     "Two. A site-update log, jahan photos aur notes daily jaate hain.",
     "Three. A material and payment record, jahan har kharcha dikhta hai.",
     "Result? Site par kaam, aur screen par hisaab.", None]
ep('r12', '2026-11-23', 'Builders and contractors', 'BUILD', 'projects', L,
   [('Site par kya hua,', 56, 'white'), ('raat ko', 130, 'lime', dict(mt=8)), ('WhatsApp se', 52, 'red', dict(mt=22)), ('pata chalta hai.', 52, 'red', dict(mt=4))],
   dict(bl='OWNER', bt='kaam kahan tak pahuncha?', bat='kaam', cf='You', ct='night.', cap=[9, ('that night.', 66, 'ink')],
        rl='SITE', rt='Material nahi aaya &#9888;', rat='Tab', st='DELAY HO GAYA.', sat='delay', ss=56),
   dict(chips=[('Updates', 'Updates,'), ('Bills', 'bills'), ('Photos', 'photos')], big=[6, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaam kitna hua?<br>pata nahi.', subAt='hain.', minisAt='photos'),
   [build('SITE TRACKER', 'project', lst('VILLA 12 (EXAMPLE)', [
        R('Foundation', 'Stage 1', 'DONE', 'har'), R('Structure', 'Stage 2', 'IN PROGRESS', 'stage', chip2='DONE ✓', chip2At='dikhta', bg='#ffd166', fg='#0b0d09', bg2='#c6ff35', fg2='#0b0d09'), R('Finishing', 'Stage 3', 'PENDING', 'status', **AMB)]))
    , build('SITE-UPDATE LOG', 'site-update', chat([('r', 'Day 14: slab complete &#10003;', 'photos'), ('r', 'Photos uploaded &#10003;', 'notes'), ('c', 'Great, payment bhej raha hoon', 'daily')], rows(L[5], [8, ('daily jaate hain.', 66, 'lime')])))
    , build('PAYMENT RECORD', 'payment', lst('THIS WEEK', [
        R('Cement', 'Delivered', 'PAID', 'material'), R('Steel', 'Ordered', 'DUE', 'payment', **AMB), R('Labour', 'Weekly', 'PAID', 'kharcha')]))],
   [('Site par kaam,', 80, 'white', dict(mt=70)), ('aur screen par', 72, 'lime', dict(mt=18)), ('hisaab.', 110, 'lime')],
   'ALL UPDATED', 'hisaab.', '#construction #contractor #constructionmanagement #builderslife #thetotalforge', 'Builder or contractor')

# ---------------------------------------------------------------- r13 Courier
L = ["Parcel kahan hai? Din mein bees baar yahi sawaal.",
     "Customer ne poocha, parcel kahan hai? You checked after lunch. Tab tak, woh complaint kar chuka tha.",
     "Riders, bookings aur updates, sab calls mein bikhre hain.", None,
     "One. A booking form, jismein pickup aur drop address hota hai.",
     "Two. Rider assignment, jahan har parcel ka rider set hota hai.",
     "Three. A tracking link, jo customer ko khud mil jaata hai.",
     "Result? Customer ko jawab, aapko sukoon.", None]
ep('r13', '2026-11-24', 'Courier and delivery', 'DISPATCH', 'business', L,
   [('Parcel', 56, 'white'), ('kahan hai?', 120, 'lime', dict(mt=8)), ('Din mein bees baar', 52, 'white', dict(mt=12)), ('yahi sawaal.', 60, 'red', dict(mt=10))],
   dict(bl='CUSTOMER', bt='parcel kahan hai?', bat='parcel', cf='You', ct='lunch.', cap=[8, ('after lunch.', 66, 'ink')],
        rl='NEW REVIEW', rt='&#9733; Parcel late aaya', rat='Tab', st='COMPLAINT AAYI.', sat='complaint', ss=54),
   dict(chips=[('Riders', 'Riders,'), ('Bookings', 'bookings'), ('Updates', 'updates,')], big=[7, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='parcel kahan hai?<br>pata nahi.', subAt='hain.', minisAt='calls'),
   [build('BOOKING FORM', 'booking', form('New booking', [('NAME', 'Ayesha K.', 'booking'), ('PICKUP', 'Gulshan, Karachi', 'pickup'), ('DROP', 'DHA, Karachi', 'drop')], 'BOOK PARCEL', 'hota', 'BOOKED', 'hai.'))
    , build('ASSIGN RIDERS', 'assignment,', lst("TODAY'S RIDERS", [
        R('Parcel #1042', 'Rider: Imran', 'ASSIGNED', 'Rider'), R('Parcel #1043', 'Rider: Kamran', 'ASSIGNED', 'parcel'), R('Parcel #1044', 'Rider: Sajid', 'ASSIGNED', 'set')]))
    , build('TRACKING LINK', 'tracking', chat([('r', 'Parcel dispatched &#10003;', 'link,'), ('r', 'Track: link.xyz/1042 &#8599;', 'customer'), ('r', 'Delivered &#10003;', 'jaata')], rows(L[6], [7, ('khud mil jaata hai.', 66, 'lime')])))],
   [('Customer ko', 72, 'white', dict(mt=70)), ('jawab,', 120, 'lime'), ('aapko sukoon.', 84, 'white', dict(mt=16))],
   'DELIVERED', 'aapko', '#courierservice #logistics #deliverybusiness #parceltracking #thetotalforge', 'Courier owner')

# ---------------------------------------------------------------- r14 Property managers
L = ["Rent kisne diya, kisne nahi? Kisi ko yaad nahi.",
     "Tenant ne poocha, geyser kab theek hoga? You replied after two weeks. Tab tak, tenant naraaz.",
     "Rent, requests aur repairs chats mein bikhre hain.", None,
     "One. A tenant request form, jismein problem aur photo hoti hai.",
     "Two. A rent due tracker, jahan har tenant ka status dikhta hai.",
     "Three. A maintenance board, jahan har repair ka task dikhta hai.",
     "Result? Har request ka jawab, har rent ka hisaab.", None]
ep('r14', '2026-11-25', 'Property managers', 'TENANT', 'rentals', L,
   [('Rent', 56, 'white'), ('kisne diya,', 110, 'lime', dict(mt=8)), ('kisne nahi?', 78, 'white'), ('Kisi ko yaad nahi.', 52, 'red', dict(mt=22))],
   dict(bl='TENANT', bt='geyser kab theek hoga?', bat='geyser', cf='You', ct='weeks.', cap=[9, ('after two weeks.', 62, 'ink')],
        rl='DOOSRA FLAT', rt='Lease signed &#10003;', rat='Tab', st='TENANT GAYA.', sat='tenant'),
   dict(chips=[('Rent', 'Rent,'), ('Requests', 'requests'), ('Repairs', 'repairs')], big=[6, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaunsa kaam baaki?<br>pata nahi.', subAt='hain.', minisAt='repairs'),
   [build('REQUEST FORM', 'request', form('Repair request', [('FLAT', 'B-12', 'tenant'), ('ISSUE', 'Geyser not heating', 'problem'), ('PHOTO', 'geyser.jpg', 'photo')], 'SEND REQUEST', 'hoti', 'SENT', 'hai.'))
    , build('RENT TRACKER', 'rent', lst('NOVEMBER', [
        R('Flat B-12', 'Ayesha K.', 'PAID', 'har'), R('Flat C-04', 'Bilal A.', 'DUE', 'tenant', chip2='PAID ✓', chip2At='dikhta', bg='#ffd166', fg='#0b0d09', bg2='#c6ff35', fg2='#0b0d09'), R('Flat A-07', 'Sara M.', 'OVERDUE', 'status', **RED)]))
    , build('REPAIR BOARD', 'maintenance', board(COLS3('NEW', 'FIXING', 'DONE'),
        [card('B-12', 'Geyser', 'Plumber', 0, [('task', 1), ('dikhta', 2)]), card('C-04', 'Light', 'Electrician', 1, [('dikhta', 1)]), card('A-07', 'AC', 'Vendor', 2)], 'har', ['jahan', 'repair', 'task']))],
   [('Har request', 80, 'white', dict(mt=70)), ('ka jawab,', 100, 'lime'), ('har rent ka hisaab.', 56, 'white', dict(mt=20))],
   'NOTHING MISSED', 'jawab,', '#propertymanagement #landlord #rentalproperty #tenantmanagement #thetotalforge', 'Landlord or property manager')

# ---------------------------------------------------------------- r15 Travel
L = ["Ek trip ka quote banane mein ghanta lag jaata hai.",
     "Customer ne poocha, Dubai ka package? You sent the quote next day. Tab tak, usne book kar liya.",
     "Quotes, payments aur plans, sab chats mein bikhre hain.", None,
     "One. An enquiry form, jismein trip ki details hoti hain.",
     "Two. A quote template, jo minutes mein ready hota hai.",
     "Three. A booking tracker, jahan har payment ka status dikhta hai.",
     "Result? Quote jaldi, booking confirm.", None]
ep('r15', '2026-11-26', 'Travel agents', 'TRIP', 'agency', L,
   [('Ek trip ka', 56, 'white'), ('quote', 150, 'lime', dict(mt=6)), ('banane mein', 78, 'white'), ('ghanta lag', 52, 'red', dict(mt=22)), ('jaata hai.', 52, 'red', dict(mt=4))],
   dict(bl='CUSTOMER', bt='Dubai ka package?', bat='Dubai', cf='You', ct='day.', cap=[10, ('next day.', 66, 'ink')],
        rl='DOOSRA AGENT', rt='Package booked &#10003;', rat='Tab', st='CLIENT GAYA.', sat='usne'),
   dict(chips=[('Quotes', 'Quotes,'), ('Payments', 'payments'), ('Plans', 'plans,')], big=[7, ('bikhre', 120, 'white'), ('hain.', 120, 'white')],
        sub='kaunsa trip confirm?<br>pata nahi.', subAt='hain.', minisAt='chats'),
   [build('ENQUIRY FORM', 'enquiry', form('Trip enquiry', [('NAME', 'Ayesha K.', 'enquiry'), ('DESTINATION', 'Dubai', 'trip'), ('DATES', '15 to 20 Dec', 'details')], 'REQUEST QUOTE', 'hoti', 'SENT', 'hain.'))
    , build('QUOTE TEMPLATE', 'quote', lst('QUOTE', [
        R('Flights', 'Return', 'ADDED', 'quote'), R('Hotel', '4 nights', 'ADDED', 'template,'), R('Airport transfer', 'Both ways', 'ADDED', 'minutes')]))
    , build('BOOKING TRACKER', 'booking', board(COLS3('ENQUIRY', 'QUOTED', 'BOOKED'),
        [card('Dubai', 'Ayesha K.', '15 to 20 Dec', 0, [('status', 1), ('dikhta', 2)]), card('Istanbul', 'Bilal A.', '3 Jan', 1, [('dikhta', 1)]), card('Skardu', 'Sara M.', 'June', 2)], 'har', ['jahan', 'payment', 'status']))],
   [('Quote', 110, 'white', dict(mt=70)), ('jaldi,', 110, 'lime'), ('booking confirm.', 76, 'white', dict(mt=18))],
   'BOOKED', 'booking', '#travelagency #travelagent #tourismbusiness #tripplanning #thetotalforge', 'Travel agent')

def aap(s):
    for a, b in (('You replied ', 'Aapne reply kiya '), ('You called back ', 'Aapne call back kiya '), ('You found it ', 'Aapne dhoondha '),
                 ('You checked ', 'Aapne check kiya '), ('You noticed ', 'Aapne notice kiya '), ('You sent the quote ', 'Aapne quote bheja '),
                 ('You apologised ', 'Aapne apologise kiya ')):
        if a in s: return s.replace(a, b, 1)
    return s.replace('You ', 'Aap ', 1)

# ------------------------------------------------------------ outputs
os.makedirs(f'{H}/episodes', exist_ok=True)
posts = []; scripts = []
for x in EPS:
    E = x['E']; id = E['id']
    json.dump(E, open(f'{H}/episodes/{id}.json', 'w'), indent=1)
    kw = E['keyword']; noun = E['cta']['noun']
    L = E['lines']
    caption = (f"{L[0]}\n\n{aap(L[1])}\n\nHum apne clients ke liye teen cheezein banate hain:\n"
               f"1. {L[4].split('. ', 1)[1]}\n2. {L[5].split('. ', 1)[1]}\n3. {L[6].split('. ', 1)[1]}\n\n"
               f"{x['comment_biz']} hain? Comment \"{kw}\" karein, hum aapko details bhej denge.\n\n"
               f"Example scenario: yeh ek misaal hai, real client nahi.\n\n{x['hashtags']}")
    posts.append(dict(id=id, date=x['date'], keyword=kw, business=E['business'], caption=caption,
                      firstComment=f"{x['comment_biz']}? Comment \"{kw}\" aur hum DM mein details bhej denge.",
                      alt=f"Animated Hinglish reel for {E['business'].lower()}: {L[0]} The Total Forge shows three things it builds.",
                      chars=x['chars']))
    scripts.append(dict(id=id, date=x['date'], business=E['business'], keyword=kw, text='\n\n'.join(L), chars=sum(len(l) for l in L) + 8))
json.dump(posts, open(f'{H}/posts.json', 'w'), indent=1)
json.dump(scripts, open(f'{H}/scripts.json', 'w'), indent=1)
print(len(EPS), 'episodes;', 'max chars', max(x['chars'] for x in EPS), 'total', sum(x['chars'] for x in EPS))
