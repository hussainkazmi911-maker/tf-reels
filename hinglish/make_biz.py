#!/usr/bin/env python3
"""Animation specs for the business reels (Reel 1 style) -> episodes/<id>.json.
Copy comes straight from business_content.BIZ (no new claims). Currently: b01 (MENU).
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
