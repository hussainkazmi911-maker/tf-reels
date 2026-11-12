# Shared helpers for building episode JSON (copied from make_episodes.py so importing does not run that generator).
import re
N = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
AMB = dict(bg='#ffd166', fg='#0b0d09'); RED = dict(bg='#ff4b3a', fg='#ffffff')

def rr(line, specs, base=600, k=0.78, lo=34):
    """specs: (a, b, color, maxsize[, opts]) -> row dict spanning spoken words [a,b); size auto-fit to ~600px width."""
    ws = line.split(); out = []
    for s in specs:
        a, b, color, mx = s[:4]; o = s[4] if len(s) > 4 else {}
        assert 0 <= a < b <= len(ws), (line, s)
        txt = ' '.join(ws[a:b]); size = max(lo, min(mx, int(base / (k * len(txt)))))
        d = {'r': [a, b], 'size': size, 'color': color}; d.update(o); out.append(d)
    return out

def R(title, sub, chip, at, **k):
    d = dict(title=title, sub=sub, chip=chip, at=at); d.update(k); return d
def lst(header, rws): return dict(type='list', header=header, rows=rws)
def chat(msgs, cap=None):
    d = dict(type='chat', msgs=[dict(who=w, text=t, at=a, y=300 + i * 125) for i, (w, t, a) in enumerate(msgs)])
    if cap: d['caption'] = dict(top=900, rows=cap)
    return d
def form(header, fields, btn, at, done, doneAt):
    return dict(type='form', header=header, fields=[dict(label=a, value=b, at=c) for a, b, c in fields],
                button=dict(text=btn, at=at, done=done + ' ✓', doneAt=doneAt))
def build(title, titleAt, demo):
    bg = {'chat': 'dark', 'board': 'cream', 'form': 'white', 'list': 'cream'}[demo['type']]
    return dict(title=title, titleAt=titleAt, bg=bg, demo=demo)
def bridge_for(line):
    """Auto bridge layout for lines of the form 'Toh [roz] yeh teen <noun> <verb...>.'"""
    ws = line.split(); k = [N(w) for w in ws].index('teen')
    assert k + 2 < len(ws), line
    small = [[i, ws[i].upper()] for i in range(k)]
    toks = []
    for i, t in small: toks.append([i, t])
    tail = [[i, ws[i].upper()] for i in range(k + 2, len(ws))]
    tsize = min(72, int(640 / (0.78 * len(' '.join(t for _, t in tail)))))
    return dict(items=[dict(top=235, size=56, toks=toks), dict(top=330, size=230, toks=[[k, '3']]),
                       dict(top=578, size=100, toks=[[k + 1, ws[k + 1].upper()]]),
                       dict(top=715, size=tsize, toks=tail)], dots=[k, k + 1, len(ws) - 1])
