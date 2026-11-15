#!/usr/bin/env python3
"""Carousel (6 slides, 1080x1350) + story (1080x1920) for the 10 e-store/marketing reels s02-s11.
Copy only restates the facts already in each reel / approved caption (no new claims).
usage: python3 make_social_estore.py s04 s03 ...   -> ../social/e-store/<id>/slide_1..6.png + story.png
Needs /home/claude/forge (node_modules/@fontsource/inter, logo.png) like pipeline/social/render_social.py."""
import sys, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rs', os.path.join(H, '..', 'pipeline', 'social', 'render_social.py'))
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
from playwright.sync_api import sync_playwright

e, hl, CSS, WORK = rs.e, rs.hl, rs.CSS, rs.WORK
EXTRA = """
.top b{font-size:15px}
.sub.lime{color:var(--lime)}
.big{position:absolute;right:34px;bottom:70px;font-weight:800;font-size:260px;line-height:1;color:rgba(198,255,53,.07);letter-spacing:-8px}
.ex{align-self:flex-start;padding:6px 12px;border:1.5px dashed rgba(255,255,255,.35);border-radius:20px;color:#c9d1c9;font-weight:800;font-size:11px;letter-spacing:1.6px}
.st .bd{top:150px;bottom:150px}
"""

# slide kinds: hook, ex, tip(c=chip), big, list(items), flow(steps), cta(share). [[x]] = lime emphasis.
D = {
's04': dict(label='E-COMMERCE · CARTS', kw='CART', slides=[
  dict(k='hook', t='[[Rs 1,00,000]] of sneakers are sitting in carts right now.', s='Swipe to win them back.'),
  dict(k='ex', t='A sneaker store: shoppers add pairs to the cart, then leave.', s='About 70% of online carts are abandoned (Baymard Institute).'),
  dict(k='big', t='Most of them didn\'t say no.', s='They got busy. They needed one small nudge.'),
  dict(k='flow', t='The fix', steps=['Cart left', 'WhatsApp reminder', 'Order'], s='Sent about 1 hour later.'),
  dict(k='big', t='Same ad spend.', s='No new traffic needed.'),
  dict(k='cta', t='Want this set up for your store?', share='Save this and send it to a seller who needs it.')]),
's03': dict(label='E-COMMERCE · INSTAGRAM DMs', kw='REPLY', slides=[
  dict(k='hook', t='Your Instagram DMs could be costing you [[Rs 60,000]] a month.', s='Swipe for the maths.'),
  dict(k='ex', t='A customer DMs "Jhumka ka price?" You reply the next day.', s='By then they\'ve ordered from someone else.'),
  dict(k='list', t='The maths', items=['5 missed DMs a day', 'Rs 400 profit per order', 'x 30 days = Rs 60,000']),
  dict(k='big', t='Auto-reply in 3 seconds.', s='Price, catalogue and order link, sent instantly.'),
  dict(k='big', t='Even while you sleep.', s='Your DMs keep making sales.'),
  dict(k='cta', t='Want DM auto-replies for your store?', share='Save this and send it to a seller who answers DMs late.')]),
's07': dict(label='MARKETING · WHAT WE DO', kw='BRAND', slides=[
  dict(k='hook', t='What does an agency really do with your [[Rs 50,000]] marketing budget?', s='4 jobs, no jargon.'),
  dict(k='list', t='The 4 jobs we take over', items=['Hook-first reels', 'Ads tracked per rupee', 'WhatsApp + DM automation', 'A weekly report']),
  dict(k='tip', c='JOB 1', t='Reels built around a strong first line.', s='So people stop scrolling.'),
  dict(k='tip', c='JOB 2', t='Ads tracked per rupee.', s='You see what is working.'),
  dict(k='tip', c='JOBS 3 + 4', t='No lead goes cold.', s='WhatsApp and DM automation, plus a weekly report in plain language.'),
  dict(k='cta', t='Want us to run your marketing?', share='Save this if you are comparing agencies.')]),
's02': dict(label='E-COMMERCE · COD RETURNS', kw='CONFIRM', slides=[
  dict(k='hook', t='[[35]] COD returns out of 100 orders = [[Rs 12,250]] gone.', s='Swipe for the maths.'),
  dict(k='ex', t='A lawn suit store ships 100 COD orders.', s='35 come back.'),
  dict(k='list', t='The maths', items=['100 COD orders', '35 returns', 'Rs 350 lost on each = Rs 12,250']),
  dict(k='big', t='Confirm on WhatsApp before you dispatch.', s='Ship only the confirmed orders.'),
  dict(k='big', t='COD guides report returns can drop by up to about half.', s=''),
  dict(k='cta', t='Want COD confirmation set up?', share='Save this and send it to a seller who ships COD.')]),
's08': dict(label='MARKETING · ADS', kw='ADS', slides=[
  dict(k='hook', t='[[Rs 10,000]] of a Rs 30,000 ad budget is reaching the wrong people.', s='3 simple fixes.'),
  dict(k='ex', t='An earbuds store spends Rs 30,000 on Meta ads.', s='A third reaches people who were never going to buy.'),
  dict(k='tip', c='FIX 1 OF 3', t='Test 3 ads at the same time.', s='Keep the winner.'),
  dict(k='tip', c='FIX 2 OF 3', t='Retarget people who already visited your store.', s=''),
  dict(k='tip', c='FIX 3 OF 3', t='Read a weekly report.', s='Not a monthly surprise.'),
  dict(k='cta', t='Want your ads checked?', share='Save this before your next ad budget.')]),
's05': dict(label='E-COMMERCE · REPEAT ORDERS', kw='REPEAT', slides=[
  dict(k='hook', t='A [[Rs 800]] ad gets one sale. A free WhatsApp reminder gets the next one.', s='Swipe.'),
  dict(k='ex', t='A perfume brand runs an ad. The customer buys once.', s='Then nothing.'),
  dict(k='tip', c='NEW VS REPEAT', t='New customer: a Rs 800 ad.', s='Repeat customer: a free message.'),
  dict(k='flow', t='The reminder', steps=['Order', 'Day 27', 'Reminder', 'Reorder'], s='Sent right when the bottle runs low.'),
  dict(k='big', t='Repeat orders are the cheapest sales you will ever make.', s=''),
  dict(k='cta', t='Want repeat-order reminders set up?', share='Save this and send it to a seller with loyal customers.')]),
's09': dict(label='MARKETING · REELS THAT SELL', kw='GROW', slides=[
  dict(k='hook', t='[[10,000]] bought followers. [[0]] orders.', s='Swipe for why.'),
  dict(k='ex', t='A skincare brand pays Rs 5,000 for 10,000 followers.', s='Not one order.'),
  dict(k='big', t='Followers don\'t buy.', s='People who stop, watch and message do.'),
  dict(k='flow', t='How a reel gets built', steps=['Hook', 'Script', 'Shoot', 'Edit'], s='In this order.'),
  dict(k='flow', t='Then the path', steps=['Comment', 'DM', 'Order'], s='Make it easy and views turn into sales.'),
  dict(k='cta', t='Want reels that sell?', share='Save this before you spend on followers.')]),
's06': dict(label='E-COMMERCE · SALE DAY', kw='SALE', slides=[
  dict(k='hook', t='[[Rs 2,00,000]] in ads. [[400]] messages in one hour.', s='Who replies to all of them?'),
  dict(k='ex', t='Sale day: the ads work and the inbox floods.', s='Your team can\'t keep up.'),
  dict(k='big', t='Buyers who wait too long go to another store.', s=''),
  dict(k='big', t='An AI auto-reply answers in seconds.', s=''),
  dict(k='flow', t='Your team\'s job', steps=['Message', 'AI reply', 'Order', 'Pack'], s='They only pack and dispatch.'),
  dict(k='cta', t='Want sale-day auto-replies?', share='Save this before your next sale.')]),
's10': dict(label='MARKETING · 30-DAY PLAN', kw='PLAN', slides=[
  dict(k='hook', t='Where every rupee of your marketing goes in the first [[30 days]].', s='Day by day.'),
  dict(k='tip', c='DAY 1', t='Full audit.', s='Store, page and ads.'),
  dict(k='tip', c='DAY 3', t='Fix the basics.', s='Profile, catalogue and WhatsApp auto-reply.'),
  dict(k='tip', c='DAY 7', t='Go live.', s='First reels and ads.'),
  dict(k='tip', c='DAY 14 AND DAY 30', t='Budget moves to what works.', s='Day 30: a report with orders and next month\'s plan.'),
  dict(k='cta', t='Want the 30-day plan?', share='Save this if you are choosing an agency.')]),
's11': dict(label='MARKETING · STORE CONVERSION', kw='STORE', slides=[
  dict(k='hook', t='[[Rs 20,000]] in ads. 1,000 visitors. Only [[2]] orders.', s='The problem is often the store, not the ad.'),
  dict(k='list', t='Why visitors leave', items=['The page loads slowly', 'The order button is hard to find', 'Nothing builds trust']),
  dict(k='tip', c='WHAT HELPS', t='Reviews, return policy and WhatsApp on the first screen.', s=''),
  dict(k='big', t='An order in just 2 taps.', s=''),
  dict(k='big', t='Same traffic. Same spend. More orders.', s=''),
  dict(k='cta', t='Want a faster store?', share='Save this and send it to a seller whose ads get clicks but no sales.')]),
}

def top(label, page=''):
    pg = f'<div class="pg">{page}</div>' if page else ''
    return (f'<div class="top"><img src="../logo.png"><div><b>THE TOTAL FORGE</b><span>{e(label)}</span></div>{pg}</div>')

def foot(i, n):
    dots = ''.join(f'<u class="{"on" if j == i else ""}"></u>' for j in range(n))
    sw = '<span class="sw">SWIPE →</span>' if i < n - 1 else '<span class="sw">@thetotalforgeofficial</span>'
    return f'<div class="foot"><div class="dots">{dots}</div>{sw}</div>'

def body(s, kw):
    k = s['k']; sub = lambda cls='': (f'<div class="sub {cls}">{hl(s["s"], 1)}</div>' if s.get('s') else '')
    if k == 'hook':
        return f'<h1>{hl(s["t"], 1)}</h1>{sub("mut")}'
    if k == 'ex':
        return f'<div class="ex">EXAMPLE SCENARIO</div><h2>{hl(s["t"], 1)}</h2>{sub("lime")}'
    if k == 'tip':
        return f'<div class="chip">{e(s["c"])}</div><h1>{hl(s["t"], 1)}</h1>{sub()}'
    if k == 'big':
        return f'<h1 class="lime">{hl(s["t"], 1)}</h1>{sub()}'
    if k == 'list':
        rows = ''.join(f'<div class="row"><i>{j + 1}</i><p>{e(x)}</p></div>' for j, x in enumerate(s['items']))
        return f'<h2>{hl(s["t"], 1)}</h2>{rows}'
    if k == 'flow':
        st = s['steps']; parts = []
        for j, x in enumerate(st):
            parts.append(f'<div class="{"last" if j == len(st) - 1 else ""}">{e(x)}</div>')
            if j < len(st) - 1: parts.append('<em>→</em>')
        return f'<h2>{hl(s["t"], 1)}</h2><div class="flow">{"".join(parts)}</div>{sub("mut")}'
    return (f'<h1>{hl(s["t"], 1)}</h1><div class="key">{e(kw)}</div>'
            f'<div class="sub">Comment it and we\'ll DM you the details.</div><div class="share">{e(s["share"])}</div>')

def carousel(d):
    n = len(d['slides']); out = []
    for i, s in enumerate(d['slides']):
        out.append(f'<div class="sl car">{top(d["label"], f"{i + 1}/{n}")}<div class="bd">{body(s, d["kw"])}</div>{foot(i, n)}</div>')
    return out

def story(d):
    hook = d['slides'][0]
    return (f'<div class="sl st">{top(d["label"]).replace("class=\"top\"", "class=\"top\" style=\"top:60px\"")}'
            f'<div class="bd"><div class="bigday">NEW REEL · JUST POSTED</div><h1>{hl(hook["t"], 1)}</h1>'
            f'<div class="sub">Watch it on our profile.</div><div class="arrow">↑</div>'
            f'<div class="share">Comment <span class="lime">{e(d["kw"])}</span> on the reel and we\'ll DM you the details.</div></div></div>')

def render(tid):
    d = D[tid]
    out = os.path.join(H, '..', 'social', 'e-store', tid); os.makedirs(out, exist_ok=True); os.makedirs(WORK, exist_ok=True)
    items = carousel(d) + [story(d)]
    names = [f'slide_{i + 1}.png' for i in range(len(d['slides']))] + ['story.png']
    path = os.path.join(WORK, f'estore_{tid}.html')
    open(path, 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}</style><body>' + ''.join(items))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 560, 'height': 1000}, device_scale_factor=2)
        pg.goto('file://' + path); pg.wait_for_timeout(500); pg.evaluate('document.fonts.ready')
        for el, nm in zip(pg.query_selector_all('.sl'), names):
            el.screenshot(path=os.path.join(out, nm))
        b.close()
    print(tid, 'wrote', len(names), 'files to', os.path.normpath(out))

if __name__ == '__main__':
    for tid in (sys.argv[1:] or list(D)):
        render(tid)
