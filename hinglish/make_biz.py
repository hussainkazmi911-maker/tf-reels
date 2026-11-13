#!/usr/bin/env python3
"""Animation specs for the business reels (Reel 1 style) -> episodes/<id>.json.
Copy comes straight from business_content.BIZ (no new claims). Currently: b01 (MENU), b02 (BOOKING), b03 (CLINIC), b04 (LEADS).
usage: python3 make_biz.py b01     then: python3 engine/build_ep.py b01 ; bash engine/finish_ep.sh b01 <mp3> <slug>"""
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
from business_content import BIZ

N = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())

def rows(line, spec):
    """spec items: int (skip n words) or (segment, size, color[, opts]); segment must match the spoken words exactly."""
    ws = line.split(); i = 0; out = []
    for it in spec:
        if isinstance(it, int): i += it; continue
        seg, size, color = it[0], it[1], it[2]; o = it[3] if len(it) > 3 else {}
        sw = seg.split()
        assert [N(x) for x in sw] == [N(x) for x in ws[i:i + len(sw)]], (seg, ws[i:i + len(sw)])
        d = {'r': [i, i + len(sw)], 'size': size, 'color': color}; d.update(o); out.append(d); i += len(sw)
    return out

def R(title, sub, chip, at, **k):
    d = dict(title=title, sub=sub, chip=chip, at=at); d.update(k); return d
def chat(msgs, cap=None):
    d = dict(type='chat', msgs=[dict(who=w, text=t, at=a, y=y) for (w, t, a, y) in msgs])
    if cap: d['caption'] = cap
    return d
def board(cols, cards, appear, colAts):
    return dict(type='board', appear=appear, cols=[dict(name=n, bg=b, fg=f, at=a) for (n, b, f), a in zip(cols, colAts)], cards=cards)
def card(i, n, it, row, moves=None):
    d = dict(id=i, name=n, item=it, row=row)
    if moves: d['moves'] = [dict(at=a, to=t) for a, t in moves]
    return d
def lst(header, rws, caption=None):
    d = dict(type='list', header=header, rows=rws)
    if caption: d['caption'] = caption
    return d
COLS3 = lambda a, b, c: [(a, '#ffd166', '#0b0d09'), (b, '#c6ff35', '#0b0d09'), (c, '#0b0d09', '#c6ff35')]
BG = {'chat': 'dark', 'board': 'cream', 'form': 'white', 'list': 'cream'}
def build(title, titleAt, demo): return dict(title=title, titleAt=titleAt, bg=BG[demo['type']], demo=demo)

BRIDGE_DEFAULT = {'items': [
    {'top': 215, 'size': 40, 'toks': [[0, 'ISILIYE'], [1, 'HUM'], [2, 'APNE'], 'br', [3, 'CLIENTS'], [4, 'KE'], [5, 'LIYE']]},
    {'top': 330, 'size': 230, 'toks': [[6, '3']]},
    {'top': 578, 'size': 100, 'toks': [[7, 'CHEEZEIN']]},
    {'top': 715, 'size': 72, 'toks': [[8, 'BANATE'], [9, 'HAIN.']]}], 'dots': [6, 7, 9]}

SPECS = {}

def b01(L):
    return dict(
        bands=['FOOD BUSINESS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '✅', '🔔'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Order WhatsApp', 52, 'white'), ('pe aaya, par', 60, 'white', dict(mt=4)),
                                   ('kitchen', 112, 'lime', dict(mt=6)), ('ko pata hi', 76, 'white'),
                                   ('nahi chala.', 70, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='WHATSAPP ORDER', text='1 kg cake, kal 5 baje', at='WhatsApp'),
                  rows=rows(L[1], [9, ('Do miss ho gaye,', 56, 'ink')]),
                  reply=dict(label='CUSTOMER', text='Yeh kya bheja?', at='customer'),
                  stamp=dict(text='WRONG CAKE.', at='wrong', size=min(70, int(520 / (0.74 * len('WRONG CAKE.'))))),
                  pile=dict(at=[6, 7, 8], hlAt='Do', secAt='miss', closeAt='gaye,', sec='2 MISS', emo='🚫'),
                  clock=None),
        mess=dict(chips=[dict(text='Chats', at='Chats'), dict(text='Orders', at='orders'), dict(text='Scroll', at='dhoondna,')],
                  rows=rows(L[2], [4, ('lowkey', 56, 'white'), ('sabse bada', 100, 'white'), ('stress hai.', 100, 'white')]),
                  sub='order kahan hai?<br>pata nahi.', subAt='hai.', minisAt='dhoondna,', subSize=58, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('MENU PAGE', 'menu', lst('MENU', [
                R('Chocolate Cake', '1 kg · Rs. 2,800', 'ADD', 'page.', chip2='ADDED ✓', chip2At='chunta'),
                R('Cupcakes (6)', 'Red velvet · Rs. 1,500', 'ADD', 'Customer'),
                R('Brownie Box', '12 pcs · Rs. 1,800', 'ADD', 'item')],
                dict(top=880, rows=rows(L[4], [9, ('order seedha', 84, 'ink'), ('aata hai.', 84, 'ink')])))),
            build('CONFIRMATION', 'auto-confirmation,', chat([
                ('c', 'Chocolate cake, kal 5 baje', 'so', 320),
                ('r', 'Order #21 confirmed &#10003;', 'reply', 470),
                ('r', 'Kal 5 baje tak ready', 'seconds.', 620)],
                dict(top=860, rows=rows(L[5], [8, ('reply', 64, 'lime'), ('in seconds.', 96, 'lime')])))),
            build('KITCHEN SCREEN', 'kitchen', board(COLS3('NEW', 'COOKING', 'READY'), [
                card('#21', 'Ayesha', 'Choc cake 1kg', 0, [('cooking,', 1), ('ready.', 2)]),
                card('#22', 'Bilal', 'Cupcakes (6)', 1, [('ready.', 1)]),
                card('#23', 'Sara', 'Brownie box', 2),
                card('#24', 'Hamza', 'Choc cake 2kg', 3)], 'screen:', ['new,', 'cooking,', 'ready.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Orders chats', 72, 'white', dict(mt=40)),
                                     ('mein nahi khote,', 52, 'lime', dict(mt=22)), ('aur kitchen', 66, 'white', dict(mt=30)),
                                     ('sorted', 120, 'lime', dict(mt=6)), ('rehta hai.', 78, 'white', dict(mt=4))]),
                    chip='&#10003; KITCHEN SORTED', chipAt='hai.'),
        cta=dict(noun='kitchen', keyword='MENU', dm=True))

SPECS['b01'] = b01

def b02(L):
    return dict(
        bands=['SALON BUSINESS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('DMs mein', 52, 'white'), ('appointments,', 60, 'white', dict(mt=4)),
                                   ('aur do log ek hi', 56, 'white', dict(mt=4)), ('slot pe.', 112, 'lime', dict(mt=6)),
                                   ('Scene kya hai?', 66, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='INSTAGRAM DM', text='Kal 4 baje ka slot?', at='DMs'),
                  rows=rows(L[1], [7, ('Do clients', 70, 'ink'), ('ek hi time pe', 70, 'ink')]),
                  reply=dict(label='CLIENT', text='Mera slot tha!', at=17),
                  stamp=dict(text='DOUBLE BOOKED.', at=13, size=min(70, int(520 / (0.74 * len('DOUBLE BOOKED.'))))),
                  pile=dict(at=[8], hlAt=7, secAt=11, closeAt=19, sec='2 CLIENTS', emo='😵'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='DMs', at=0), dict(text='Calendar', at=1), dict(text='Clash', at=3)],
                  rows=rows(L[2], [4, ('bhai.', 50, 'white'), ('Double', 96, 'white'), ('booking', 96, 'white'),
                                   ('pakki hai.', 84, 'ink')]),
                  sub='kaun pehle aaya?<br>pata nahi.', subAt=8, subTop=990, minisAt=4, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('BOOKING PAGE', 'booking', lst('BOOK NOW', [
                R('Haircut', '45 min · Rs. 1,500', 'BOOK', 'page.', chip2='4 PM ✓', chip2At='chunta'),
                R('Facial', '60 min · Rs. 3,000', 'BOOK', 'Customer'),
                R('Hair Colour', '90 min · Rs. 5,500', 'BOOK', 'service')],
                dict(top=880, rows=rows(L[4], [7, ('time khud', 84, 'ink'), ('chunta hai.', 84, 'ink')])))),
            build('AUTO-REMINDER', 'auto-reminder,', chat([
                ('r', 'Kal 4 PM, Haircut. Yaad hai?', 'auto-reminder,', 320),
                ('c', 'Haan, aa rahi hoon!', 'nobody', 470),
                ('r', 'See you at 4 PM &#10003;', 'slot.', 620)],
                dict(top=860, rows=rows(L[5], [4, ('nobody forgets', 64, 'lime'), ('their slot.', 90, 'lime')])))),
            build('ONE CALENDAR', 'One', board(COLS3('BOOKED', 'CONFIRMED', 'DONE'), [
                card('4 PM', 'Ayesha', 'Haircut', 0, [('confirmed,', 1), ('done.', 2)]),
                card('5 PM', 'Sana', 'Facial', 1, [('done.', 1)]),
                card('6 PM', 'Hira', 'Colour', 2),
                card('7 PM', 'Maham', 'Manicure', 3)], 'har', ['booked,', 'confirmed,', 'done.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Double booking', 70, 'white', dict(mt=40)),
                                     ('khatam,', 104, 'lime', dict(mt=16)), ('aur calendar', 66, 'white', dict(mt=30)),
                                     ('saaf', 120, 'lime', dict(mt=6)), ('rehta hai.', 78, 'white', dict(mt=4))]),
                    chip='&#10003; NO CLASHES', chipAt='hai.'),
        cta=dict(noun='salon', keyword='BOOKING', dm=True))

SPECS['b02'] = b02

def b03(L):
    return dict(
        bands=['CLINIC OWNERS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Patient aaya,', 60, 'white'), ('par register mein', 52, 'white', dict(mt=4)),
                                   ('uska', 76, 'white', dict(mt=6)), ('appointment', 100, 'lime', dict(mt=4)),
                                   ('hi nahi tha.', 70, 'red', dict(mt=14))])),
        pain=dict(bubble=dict(label='PHONE CALL', text='Kal 11 baje ka slot?', at='calls'),
                  rows=rows(L[1], [15, ('ghanta bhar wait', 66, 'ink'), ('karta raha.', 66, 'ink')]),
                  reply=dict(label='PATIENT', text='Ek ghanta!', at=18),
                  stamp=dict(text='ONE HOUR WAIT.', at=15, size=min(70, int(520 / (0.74 * len('ONE HOUR WAIT.'))))),
                  pile=dict(at=[], hlAt=9, secAt=10, closeAt=12, sec='NO ENTRY', emo='🚫'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='Calls', at=0), dict(text='Register', at=2), dict(text='Chaos', at=6)],
                  rows=rows(L[2], [7, ('lowkey', 56, 'white'), ('risky', 120, 'white'), ('hai.', 120, 'ink')]),
                  sub='next patient kaun?<br>pata nahi.', subAt=9, subTop=990, minisAt=4, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('ONLINE BOOKING', 'online', lst('BOOK A VISIT', [
                R('General Checkup', 'Dr. Ahmed · 30 min', 'BOOK', 'page.', chip2='11 AM ✓', chip2At='khud'),
                R('Dental Cleaning', 'Dr. Sara · 45 min', 'BOOK', 'Patient'),
                R('Eye Test', 'Dr. Bilal · 20 min', 'BOOK', 'apna')],
                dict(top=880, rows=rows(L[4], [7, ('time khud', 84, 'ink'), ('book karta hai.', 72, 'ink')])))),
            build('AUTO-REMINDER', 'auto-reminder', chat([
                ('r', 'Reminder: kal 11 AM check-up', 'auto-reminder', 320),
                ('c', 'Ji, main aa raha hoon!', 'before', 470),
                ('r', 'See you at 11 AM &#10003;', 'appointment.', 620)],
                dict(top=860, rows=rows(L[5], [3, ('before every', 64, 'lime'), ('appointment.', 88, 'lime')])))),
            build('ONE SCREEN', 'One', board(COLS3('BOOKED', 'ARRIVED', 'DONE'), [
                card('11 AM', 'Ayesha', 'Check-up', 0, [('arrived,', 1), ('done.', 2)]),
                card('11:30', 'Bilal', 'Dental', 1, [('done.', 1)]),
                card('12 PM', 'Sara', 'Eye test', 2),
                card('12:30', 'Hamza', 'Follow-up', 3)], 'har', ['booked,', 'arrived,', 'done.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Register ki', 72, 'white', dict(mt=40)),
                                     ('tension', 104, 'lime', dict(mt=16)), ('khatam,', 84, 'white', dict(mt=16)),
                                     ('aur front desk', 66, 'white', dict(mt=30)), ('relaxed.', 110, 'lime', dict(mt=6))]),
                    chip='&#10003; NO WAITING', chipAt='relaxed.'),
        cta=dict(noun='clinic', keyword='CLINIC', dm=True))

SPECS['b03'] = b03


def b04(L):
    return dict(
        bands=['PROPERTY DEALERS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Lead ne raat ko', 56, 'white'), ('inquiry bheji,', 60, 'white', dict(mt=4)),
                                   ('aur aapne', 60, 'white', dict(mt=4)), ('agle din', 112, 'lime', dict(mt=6)),
                                   ('reply kiya.', 76, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='NEW INQUIRY', text='Flat abhi available?', at=7),
                  rows=rows(L[1], [14, ('dealer se baat', 66, 'ink'), ('kar chuka tha.', 66, 'ink')]),
                  reply=dict(label='BUYER', text='Too late!', at=17),
                  stamp=dict(text='LOST LEAD.', at=14, size=min(70, int(520 / (0.74 * len('LOST LEAD.'))))),
                  pile=dict(at=[], hlAt=9, secAt=11, closeAt=19, sec='DEAL GONE', emo='🚫'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='Leads', at=0), dict(text='Wait', at=1), dict(text='Gone', at=3)],
                  rows=rows(L[2], [4, ('bhai.', 50, 'white'), ('Speed', 104, 'white'), ('hi game', 96, 'white'),
                                   ('hai.', 84, 'ink')]),
                  sub='lead kahan gaya?<br>pata nahi.', subAt=8, subTop=990, minisAt=4, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('INQUIRY FORM', 'inquiry', lst('NEW LEADS', [
                R('Ahmed: 3-Bed Flat', 'DHA Phase 6', 'SAVE', 'form', chip2='SAVED ✓', chip2At='save'),
                R('Sana: 10 Marla', 'Bahria Town', 'SAVE', 'har'),
                R('Bilal: Shop Rent', 'Gulshan', 'SAVE', 'lead')],
                dict(top=880, rows=rows(L[4], [8, ('seedha save', 84, 'ink'), ('karta hai.', 84, 'ink')])))),
            build('INSTANT REPLY', 'instant', chat([
                ('c', 'Flat available hai?', 'reply,', 320),
                ('r', 'Ji! Details yeh rahi &#10003;', 'every', 470),
                ('r', 'Visit kal 4 PM? &#10003;', 'seconds.', 620)],
                dict(top=860, rows=rows(L[5], [7, ('hears back', 64, 'lime'), ('in seconds.', 96, 'lime')])))),
            build('ONE BOARD', 'One', board(COLS3('NEW', 'CONTACTED', 'CLOSED'), [
                card('#101', 'Ahmed', 'DHA Flat', 0, [('contacted,', 1), ('closed.', 2)]),
                card('#102', 'Sana', '10 Marla', 1, [('closed.', 1)]),
                card('#103', 'Bilal', 'Shop Rent', 2),
                card('#104', 'Hamza', 'Villa', 3)], 'har', ['new,', 'contacted,', 'closed.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Koi lead miss', 66, 'white', dict(mt=40)),
                                     ('nahi hota,', 104, 'lime', dict(mt=16)), ('aur follow-up', 66, 'white', dict(mt=30)),
                                     ('easy', 120, 'lime', dict(mt=6)), ('ho jata hai.', 78, 'white', dict(mt=4))]),
                    chip='&#10003; NO LEAD LOST', chipAt=11),
        cta=dict(noun='office', keyword='LEADS', dm=True))

SPECS['b04'] = b04


def b05(L):
    return dict(
        bands=['GYM OWNERS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Member ne fees', 56, 'white'), ('nahi di,', 64, 'white', dict(mt=4)),
                                   ('aur kisi ko', 60, 'white', dict(mt=4)), ('yaad bhi', 104, 'lime', dict(mt=6)),
                                   ('nahi tha.', 76, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='NOTEBOOK ENTRY', text='Ali: fees baaki hai', at=4),
                  rows=rows(L[1], [16, ('mahine ke end', 70, 'ink'), ('mein pata chala.', 60, 'ink')]),
                  reply=dict(label='OWNER', text='Pata hi nahi!', at=19),
                  stamp=dict(text='FEES MISSED.', at=13, size=min(70, int(520 / (0.74 * len('FEES MISSED.'))))),
                  pile=dict(at=[], hlAt=9, secAt=10, closeAt=21, sec='3 MEMBERS', emo='🚫'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='Notebook', at=0), dict(text='Yaad?', at=1), dict(text='Paisa', at=3)],
                  rows=rows(L[2], [4, ('bhai.', 50, 'white'), ('Paisa', 104, 'white'), ('chala', 96, 'white'),
                                   ('jata hai.', 84, 'ink')]),
                  sub='paisa kahan gaya?<br>pata nahi.', subAt=8, subTop=990, minisAt=4, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('MEMBER APP', 'member', lst('MEMBERS', [
                R('Ali · Monthly', 'Due 5 Dec', 'ACTIVE', 'app', chip2='PAID ✓', chip2At='date'),
                R('Sara · Quarterly', 'Due 12 Dec', 'ACTIVE', 'har'),
                R('Hamza · Yearly', 'Due 20 Dec', 'ACTIVE', 'plan')],
                dict(top=880, rows=rows(L[4], [8, ('plan aur due', 76, 'ink'), ('date dikhta hai.', 62, 'ink')])))),
            build('AUTO-REMINDER', 'auto-reminder,', chat([
                ('r', 'Reminder: fees kal due hai', 'auto-reminder,', 320),
                ('c', 'Ji, aaj de deta hoon!', 'yaad', 470),
                ('r', 'Thanks Ali &#10003; Fees received', 'jaye.', 620)],
                dict(top=860, rows=rows(L[5], [5, ('time pe yaad', 76, 'lime'), ('dila di jaye.', 80, 'lime')])))),
            build('ONE SCREEN', 'One', board(COLS3('ACTIVE', 'DUE', 'EXPIRED'), [
                card('#01', 'Ali', 'Monthly', 0, [('due,', 1), ('expired.', 2)]),
                card('#02', 'Sara', 'Quarterly', 1, [('expired.', 1)]),
                card('#03', 'Hamza', 'Yearly', 2),
                card('#04', 'Zoya', 'Monthly', 3)], 'har', ['active,', 'due,', 'expired.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Fees yaad', 84, 'white', dict(mt=40)),
                                     ('rehti hain,', 90, 'lime', dict(mt=16)), ('aur members', 66, 'white', dict(mt=30)),
                                     ('ka track', 110, 'lime', dict(mt=6)), ('rehta hai.', 78, 'white', dict(mt=4))]),
                    chip='&#10003; FEES TRACKED', chipAt=10),
        cta=dict(noun='gym', keyword='MEMBERS', dm=True))

SPECS['b05'] = b05


def b06(L):
    return dict(
        bands=['ACADEMY OWNERS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Fees ka hisaab', 56, 'white'), ('copy mein, aur', 60, 'white', dict(mt=4)),
                                   ('parents ko roz', 58, 'white', dict(mt=4)), ('yaad dilana.', 84, 'lime', dict(mt=6)),
                                   ('Thak gaye?', 80, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='PARENT', text='Fees kal bhej dunga', at=5),
                  rows=rows(L[1], [18, ('record sab', 80, 'ink'), ('ka alag.', 80, 'ink')]),
                  reply=dict(label='PARENT', text='Bhool gaya!', at=15),
                  stamp=dict(text='FEES LATE.', at=13, size=min(70, int(520 / (0.74 * len('FEES LATE.'))))),
                  pile=dict(at=[], hlAt=12, secAt=18, closeAt=21, sec='NO RECORD', emo='🚫'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='Chasing', at=0), dict(text='Kaam', at=3), dict(text='Stress', at=5)],
                  rows=rows(L[2], [('Chasing hi', 104, 'white'), ('poora kaam', 100, 'lime'), ('ban jata hai.', 72, 'ink')]),
                  sub='Padhai kab<br>karwaoge?', subAt=7, subTop=990, minisAt=3, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('ENROLMENT FORM', 'enrolment', lst('NEW STUDENTS', [
                R('Ayaan · Class 6', 'Parent: Mr. Raza', 'SAVE', 'form', chip2='SAVED ✓', chip2At='jagah.'),
                R('Hira · Class 8', 'Parent: Mrs. Khan', 'SAVE', 'Parent'),
                R('Zain · Class 5', 'Parent: Mr. Ali', 'SAVE', 'student')],
                dict(top=880, rows=rows(L[4], [8, ('details ek', 84, 'ink'), ('hi jagah.', 84, 'ink')])))),
            build('AUTO REMINDER', 'auto', chat([
                ('r', 'Reminder: Ayaan ki fees due', 'reminder,', 320),
                ('c', 'Ji, aaj bhej raha hoon!', 'gets', 470),
                ('r', 'Thanks! Fees received &#10003;', 'time.', 620)],
                dict(top=860, rows=rows(L[5], [8, ('gets a message', 66, 'lime'), ('on time.', 100, 'lime')])))),
            build('ONE SCREEN', 'One', board(COLS3('PAID', 'DUE', 'LATE'), [
                card('#01', 'Ayaan', 'Class 6', 0, [('due,', 1), ('late.', 2)]),
                card('#02', 'Hira', 'Class 8', 1, [('late.', 1)]),
                card('#03', 'Zain', 'Class 5', 2),
                card('#04', 'Maya', 'Class 7', 3)], 'har', ['paid,', 'due,', 'late.']))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Chasing', 90, 'white', dict(mt=40)),
                                     ('kam,', 110, 'lime', dict(mt=16)), ('aur record', 66, 'white', dict(mt=30)),
                                     ('hamesha', 96, 'lime', dict(mt=6)), ('ready.', 84, 'white', dict(mt=4))]),
                    chip='&#10003; RECORD READY', chipAt=6),
        cta=dict(noun='academy', keyword='ACADEMY', dm=True))

SPECS['b06'] = b06


def b07(L):
    return dict(
        bands=['SHOP OWNERS', 'WHAT WE BUILD ★ 3 THINGS'],
        emo=dict(hook='😵', pain='🤦', mess='💀', tips=['📋', '🔔', '✅'], res='🎉'),
        hook=dict(rows=rows(L[0], [('Shop mein cheez', 56, 'white'), ('bik gayi,', 66, 'white', dict(mt=4)),
                                   ('par online', 64, 'white', dict(mt=4)), ('abhi bhi', 104, 'lime', dict(mt=6)),
                                   ('available hai.', 70, 'red', dict(mt=18))])),
        pain=dict(bubble=dict(label='ONLINE ORDER', text='Blue jacket, size M', at=10),
                  rows=rows(L[1], [17, ('aur refund', 78, 'ink'), ('dena pada.', 78, 'ink')]),
                  reply=dict(label='CUSTOMER', text='Refund do!', at=18),
                  stamp=dict(text='SOLD TWICE.', at=15, size=min(70, int(520 / (0.74 * len('SOLD TWICE.'))))),
                  pile=dict(at=[], hlAt=11, secAt=13, closeAt=20, sec='SAME ITEM', emo='🚫'),
                  clock=None, top=670),
        mess=dict(chips=[dict(text='Shop', at=0), dict(text='Online', at=2), dict(text='Mismatch', at=3)],
                  rows=rows(L[2], [5, ('toh', 50, 'white'), ('scene', 110, 'white'), ('bigadna hi', 96, 'white'),
                                   ('hai.', 84, 'ink')]),
                  sub='kitna stock bacha?<br>pata nahi.', subAt=9, subTop=990, minisAt=5, subSize=54, top=600),
        bridge=BRIDGE_DEFAULT,
        builds=[
            build('STOCK SCREEN', 'stock', lst('STOCK', [
                R('Blue Jacket', 'Shop 3 · Online 2', 'SYNC', 'screen', chip2='SYNCED ✓', chip2At='saath'),
                R('White Sneakers', 'Shop 5 · Online 1', 'SYNC', 'shop'),
                R('Black Cap', 'Shop 2 · Online 4', 'SYNC', 'online')],
                dict(top=880, rows=rows(L[4], [9, ('stock saath', 84, 'ink'), ('dikhta hai.', 84, 'ink')])))),
            build('STOCK ALERT', 'low-stock', chat([
                ('r', 'Low stock: Jacket, 2 left', 'alert,', 320),
                ('c', 'Reorder kar do!', 'reorder', 470),
                ('r', 'Reorder placed &#10003;', 'out.', 620)],
                dict(top=860, rows=rows(L[5], [6, ('reorder before', 66, 'lime'), ('it runs out.', 84, 'lime')])))),
            build('SALES REPORT', 'daily', lst('TODAY\'S SALES', [
                R('Blue Jacket', '4 sold today', 'SOLD', 'sales'),
                R('White Sneakers', '2 sold today', 'SOLD', 'report,'),
                R('Black Cap', '6 sold today', 'SOLD', 'know', chip2='TOP ✓', chip2At='sold.')],
                dict(top=880, rows=rows(L[6], [7, ('know what', 84, 'ink'), ('sold.', 110, 'ink')]))))],
        result=dict(rows=rows(L[7], [('Result?', 44, 'lime', dict(ls=6)), ('Stock mismatch', 66, 'white', dict(mt=40)),
                                     ('khatam,', 110, 'lime', dict(mt=16)), ('aur refund ki', 66, 'white', dict(mt=30)),
                                     ('tension', 104, 'lime', dict(mt=6)), ('bhi.', 78, 'white', dict(mt=4))]),
                    chip='&#10003; STOCK SYNCED', chipAt=8),
        cta=dict(noun='shop', keyword='STOCK', dm=True))

SPECS['b07'] = b07

def make(bid):
    b = next(x for x in BIZ if x['id'] == bid)
    L = b['lines']
    E = dict(id=bid, business=b['who'], keyword=b['kw'], lines=L)
    E.update(SPECS[bid](L))
    return E

if __name__ == '__main__':
    for bid in sys.argv[1:]:
        E = make(bid)
        out = os.path.join(H, 'episodes', f'{bid}.json')
        json.dump(E, open(out, 'w'), indent=1, ensure_ascii=False)
        print('wrote', out)
