#!/usr/bin/env python3
"""v2 human-sounding scripts for s02-s11.
Each reel: 8 lines (scene order is fixed by stories/sNN.js). Per line: (spoken text, audio tag or '', caption rows).
Rows: [text, size, color]  ([Display|spoken words] shows Display for those spoken words).
Writes episodes/sNN.json (lines + rows) and work/sNN/tts_prompt.txt (lines with ElevenLabs tags)."""
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
W, L, R, A, C = 'white', 'lime', 'red', 'amber', 'cyan'

def share(who):  # line 6
    return (f"{who} Yeh reel usko bhej do.", '[warmly]')

def cta(first, kw):  # line 7
    return (f"{first} Toh comment mein {kw} likh do, hum DM kar denge.", '')

S = {}

S['s02'] = [
 ("Barah hazaar rupay, yaar, har mahine parcel ban kar wapas aa rahe hain.", '[frustrated]',
  [['[Rs. 12,000|Barah hazaar rupay,]', 80, A], ['yaar, har mahine,', 50, W], ['parcel ban kar', 64, W], ['wapas aa rahe hain.', 58, R]]),
 ("Lawn suit bheja, customer ne phone hi nahi uthaya... ab kya karein?", '[sighs]',
  [['Lawn suit bheja,', 50, W], ['customer ne phone hi', 54, W], ['nahi uthaya...', 80, R], ['ab kya karein?', 60, A]]),
 ("Sau mein se paintees wapas, aur har parcel par, teen sau pachaas rupay, seedha nuksaan.", '[serious]',
  [['Sau mein se', 50, W], ['[35|paintees] wapas,', 70, R], ['aur har parcel par,', 46, W], ['[Rs. 350|teen sau pachaas rupay,]', 46, A], ['seedha nuksaan.', 46, R]]),
 ("Toh fix simple hai, order aate hi, customer ko WhatsApp par confirm karwa lo.", '[warmly]',
  [['Toh fix simple hai,', 50, L], ['order aate hi,', 60, W], ['customer ko WhatsApp par', 46, W], ['confirm karwa lo.', 66, L]]),
 ("Haan bola, toh parcel nikalta hai, nahi bola, toh paise bache, simple.", '[happy]',
  [['Haan bola,', 76, L], ['toh parcel nikalta hai,', 46, W], ['nahi bola,', 76, R], ['toh paise bache, simple.', 50, W]]),
 ("Guides ke mutabiq, wapsi lagbhag aadhi reh sakti hai.", '',
  [['Guides ke mutabiq,', 52, W], ['wapsi', 84, W], ['lagbhag aadhi reh sakti hai.', 48, L]]),
 ("Koi seller dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi seller dost hai?', 58, W], ['Yeh reel usko', 72, L], ['bhej do.', 90, W]]),
 ("Confirm bot chahiye? Toh comment mein CONFIRM likh do, hum DM kar denge.", '',
  [['Confirm bot chahiye?', 54, W], ['Toh comment mein', 54, W], ['CONFIRM', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s03'] = [
 ("Sath hazaar rupay, yaar, aapke Instagram DMs mein pade hain.", '[serious]',
  [['[Rs. 60,000|Sath hazaar rupay,]', 80, A], ['yaar, aapke Instagram', 52, W], ['DMs mein', 66, W], ['pade hain.', 84, R]]),
 ("Customer ne likha, jhumka ka price? Aur aapne agle din reply kiya... sach bolo.", '[curious]',
  [['Customer ne likha,', 46, W], ['jhumka ka price?', 58, L], ['Aur aapne agle din', 48, W], ['reply kiya...', 66, R], ['sach bolo.', 44, W]]),
 ("Tab tak woh kisi aur se order kar chuki thi. Aur aapki sale, gayi.", '[sighs]',
  [['Tab tak woh', 56, W], ['kisi aur se', 70, A], ['order kar chuki thi.', 54, W], ['Aur aapki sale, gayi.', 58, R]]),
 ("Roz paanch aise DMs, har order par chaar sau rupay ka munafa... matlab mahine ke sath hazaar.", '[serious]',
  [['Roz paanch aise DMs,', 48, W], ['har order par', 46, W], ['[Rs. 400|chaar sau rupay] ka munafa...', 44, A], ['matlab mahine ke', 46, W], ['[Rs. 60,000|sath hazaar.]', 64, R]]),
 ("Toh auto reply laga lo, price, catalogue, order link, teen second mein.", '[excited]',
  [['Toh auto reply laga lo,', 46, L], ['price, catalogue,', 60, W], ['order link,', 60, W], ['teen second mein.', 66, L]]),
 ("Aap araam se sote raho, aur DMs, sale banate rahein.", '[warmly]',
  [['Aap araam se', 54, W], ['sote raho,', 66, W], ['aur DMs sale', 76, L], ['banate rahein.', 64, W]]),
 ("Koi jewellery seller dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi jewellery seller', 52, W], ['dost hai?', 66, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("DMs se sale chahiye? Toh comment mein REPLY likh do, hum DM kar denge.", '',
  [['DMs se sale chahiye?', 52, W], ['Toh comment mein', 54, W], ['REPLY', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s04'] = [
 ("Ek lakh rupay ke sneakers, yaar, aapke cart mein chhode hue hain.", '[serious]',
  [['[Rs. 1,00,000|Ek lakh rupay]', 74, A], ['ke sneakers, yaar,', 60, W], ['aapke cart mein', 62, W], ['chhode hue hain.', 66, R]]),
 ("Customer ne size chuna, cart mein dala, aur tabhi... ek call aa gaya.", '[curious]',
  [['Customer ne size chuna,', 48, W], ['cart mein dala,', 62, L], ['aur tabhi... ek call', 54, W], ['aa gaya.', 84, R]]),
 ("Research ke mutabiq, dus mein se saat log, cart chhod ke chale jaate hain.", '[serious]',
  [['Research ke mutabiq,', 50, W], ['[7/10|dus mein se saat]', 80, R], ['log, cart chhod ke', 52, W], ['chale jaate hain.', 54, W]]),
 ("Aap bhool gaye, ho jata hai. Par smart system, kabhi nahi bhoolta.", '[sighs]',
  [['Aap bhool gaye,', 64, R], ['ho jata hai. Par', 46, W], ['smart system,', 62, W], ['kabhi nahi bhoolta.', 62, L]]),
 ("Bas ek ghante baad, WhatsApp par message jaata hai: aapke sneakers wait kar rahe hain.", '[warmly]',
  [['Bas ek ghante baad,', 54, W], ['WhatsApp par message', 54, L], ['jaata hai: aapke sneakers', 46, W], ['wait kar rahe hain.', 56, W]]),
 ("Customer wapas aaya, order complete kiya, aur paise seedha, aapke account mein.", '[happy]',
  [['Customer wapas aaya,', 52, W], ['order complete kiya,', 58, L], ['aur paise seedha,', 58, W], ['aapke account mein.', 60, W]]),
 ("Sneakers ya kuch bhi bechne wala dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Sneakers ya kuch bhi', 48, W], ['bechne wala dost hai?', 48, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Cart wapas lana hai? Toh comment mein CART likh do, hum DM kar denge.", '',
  [['Cart wapas lana hai?', 54, W], ['Toh comment mein', 54, W], ['CART', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s05'] = [
 ("Aath sau rupay ka ad lagaya, aur customer ne sirf ek baar khareeda, phir gayab.", '[serious]',
  [['[Rs. 800|Aath sau rupay]', 74, A], ['ka ad lagaya, aur', 52, W], ['customer ne sirf ek baar', 50, R], ['khareeda, phir gayab.', 54, R]]),
 ("Perfume tees din mein khatam ho jaata hai, aur aapko pata hi nahi chalta.", '[sighs]',
  [['Perfume tees din', 60, W], ['mein khatam ho jaata hai,', 48, L], ['aur aapko', 56, W], ['pata hi nahi chalta.', 60, R]]),
 ("Usne dobara, kisi aur se, kharid liya... aapse nahi.", '[serious]',
  [['Usne dobara,', 66, W], ['kisi aur se,', 78, A], ['kharid liya...', 70, R], ['aapse nahi.', 66, W]]),
 ("Dekho, naya customer aath sau rupay ka, aur purane ko bas ek message, lagbhag muft.", '[serious]',
  [['Dekho, naya customer', 52, W], ['[Rs. 800|aath sau rupay] ka,', 50, R], ['aur purane ko bas ek message,', 44, W], ['lagbhag muft.', 74, L]]),
 ("Phir din satais par, A I khud poochta hai, perfume khatam hone wala hai, repeat karein?", '[excited]',
  [['Phir din satais par,', 58, L], ['A I khud poochta hai,', 52, W], ['perfume khatam hone', 50, W], ['wala hai, repeat karein?', 50, W]]),
 ("Bas ek tap, doosra order, aur ad ka ek rupay bhi nahi laga.", '[happy]',
  [['Bas ek tap,', 74, L], ['doosra order,', 62, W], ['aur ad ka ek rupay', 52, W], ['bhi nahi laga.', 70, L]]),
 ("Perfume ya attar bechne wala dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Perfume ya attar', 52, W], ['bechne wala dost hai?', 48, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Repeat orders chahiye? Toh comment mein REPEAT likh do, hum DM kar denge.", '',
  [['Repeat orders chahiye?', 54, W], ['Toh comment mein', 54, W], ['REPEAT', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s06'] = [
 ("Do lakh rupay ke ads lagaye, aur ab chaar sau messages kaun sambhalega, yaar?", '[serious]',
  [['[Rs. 2,00,000|Do lakh rupay]', 66, A], ['ke ads lagaye,', 58, W], ['aur ab [400|chaar sau] messages', 44, W], ['kaun sambhalega, yaar?', 58, R]]),
 ("Do log, ek phone, aur ek ghante mein chaar sau messages... bhai, pagal ho jaoge.", '[sighs]',
  [['Do log, ek phone,', 58, W], ['aur ek ghante mein', 52, W], ['[400|chaar sau] messages...', 58, R], ['bhai, pagal ho jaoge.', 52, A]]),
 ("Jab tak aap pehle ko reply karoge, baaqi customers intezaar karke, band kar denge.", '[serious]',
  [['Jab tak aap pehle ko', 50, W], ['reply karoge,', 64, L], ['baaqi customers intezaar karke,', 44, W], ['band kar denge.', 66, R]]),
 ("Yaad rakhna, sale mein jawab ki raftaar hi paisa banati hai.", '[serious]',
  [['Yaad rakhna,', 54, W], ['sale mein jawab ki', 56, W], ['raftaar hi', 76, L], ['paisa banati hai.', 66, A]]),
 ("Yahan A I sabko ek saath jawab deta hai, price, stock, order link.", '[excited]',
  [['Yahan A I sabko ek saath', 48, L], ['jawab deta hai,', 58, W], ['price, stock,', 66, W], ['order link.', 72, L]]),
 ("Aapki team bas packing aur dispatch sambhale, baaki tension hum le lenge.", '[warmly]',
  [['Aapki team bas', 54, W], ['packing aur dispatch', 56, L], ['sambhale,', 68, W], ['baaki tension hum le lenge.', 44, W]]),
 ("Sale lagane wala koi seller dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Sale lagane wala', 52, W], ['koi seller dost hai?', 52, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Sale ke liye bot chahiye? Toh comment mein SALE likh do, hum DM kar denge.", '',
  [['Sale ke liye bot chahiye?', 50, W], ['Toh comment mein', 54, W], ['SALE', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s07'] = [
 ("Pachaas hazaar rupay ka marketing budget, aap humein dein, toh hum yeh chaar kaam karte hain.", '[serious]',
  [['[Rs. 50,000|Pachaas hazaar rupay]', 56, A], ['ka marketing budget,', 50, W], ['aap humein dein, toh hum', 46, W], ['yeh [4|chaar] kaam karte hain.', 54, L]]),
 ("Number ek, har hafte hook wali reels, jo dekhne ke liye nahi, bechne ke liye bani hon.", '[warmly]',
  [['Number ek,', 66, L], ['har hafte hook wali reels,', 44, W], ['jo dekhne ke liye nahi,', 48, W], ['bechne ke liye bani hon.', 48, L]]),
 ("Number do, ads, jahan har ek rupay ka hisaab ho.", '',
  [['Number do,', 66, A], ['ads, jahan har ek rupay', 50, W], ['ka hisaab ho.', 66, A]]),
 ("Number teen, WhatsApp aur DM automation, taaki koi lead miss na ho.", '',
  [['Number teen,', 66, C], ['WhatsApp aur DM', 60, W], ['automation, taaki koi', 52, W], ['lead miss na ho.', 60, C]]),
 ("Aur number chaar, har hafte report, kitna kharch hua, kitna kamaya.", '',
  [['Aur number chaar,', 60, L], ['har hafte report,', 56, W], ['kitna kharch hua,', 56, W], ['kitna kamaya.', 66, L]]),
 ("Toh aap bas apna maal sambhalo, aur marketing, hum sambhalte hain.", '[warmly]',
  [['Toh aap bas apna', 50, W], ['maal sambhalo,', 66, W], ['aur marketing,', 66, L], ['hum sambhalte hain.', 62, L]]),
 ("Koi brand chalane wala dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi brand chalane', 52, W], ['wala dost hai?', 62, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Brand humein dena hai? Toh comment mein BRAND likh do, hum DM kar denge.", '',
  [['Brand humein dena hai?', 52, W], ['Toh comment mein', 54, W], ['BRAND', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s08'] = [
 ("Tees hazaar ke ads mein, yaar, das hazaar rupay galat logon ko dikh rahe hain.", '[frustrated]',
  [['[Rs. 30,000|Tees hazaar]', 64, A], ['ke ads mein, yaar,', 52, W], ['[Rs. 10,000|das hazaar rupay]', 52, R], ['galat logon ko dikh rahe hain.', 42, W]]),
 ("Earbuds ka ad chala, aur dekhne wale woh the, jo shopping karte hi nahi.", '[sighs]',
  [['Earbuds ka ad chala,', 58, W], ['aur dekhne wale woh the,', 46, W], ['jo shopping', 66, R], ['karte hi nahi.', 66, R]]),
 ("Na koi test, na retargeting, bas boost dabaya, aur dua ki.", '[sarcastic]',
  [['Na koi test, na retargeting,', 44, W], ['bas boost dabaya,', 62, A], ['aur dua ki.', 80, W]]),
 ("Hum pehle teen ads test karte hain, aur jo jeete, usi par poora budget lagate hain.", '[excited]',
  [['Hum pehle [3|teen] ads', 54, W], ['test karte hain,', 54, W], ['aur jo jeete,', 66, L], ['usi par poora budget lagate hain.', 40, L]]),
 ("Phir unhe dobara dikhate hain, jinhon ne dekha, par khareeda nahi.", '[warmly]',
  [['Phir unhe dobara', 62, L], ['dikhate hain,', 66, W], ['jinhon ne dekha,', 56, W], ['par khareeda nahi.', 56, R]]),
 ("Aur har hafte report, kharch, sales, aur munafa.", '',
  [['Aur har hafte report:', 52, W], ['kharch, sales,', 66, L], ['aur munafa.', 80, A]]),
 ("Ads chalane wala koi dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Ads chalane wala', 52, W], ['koi dost hai?', 62, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Ads ka hisaab chahiye? Toh comment mein ADS likh do, hum DM kar denge.", '',
  [['Ads ka hisaab chahiye?', 52, W], ['Toh comment mein', 54, W], ['ADS', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s09'] = [
 ("Paanch hazaar rupay mein, das hazaar followers kharide, aur ek bhi order nahi aaya.", '[frustrated]',
  [['[Rs. 5,000|Paanch hazaar rupay]', 56, A], ['mein, [10,000|das hazaar] followers', 46, W], ['kharide, aur ek bhi', 54, W], ['order nahi aaya.', 66, R]]),
 ("Kyunki followers sirf ginti hain, aur customers hi kharidte hain.", '[serious]',
  [['Kyunki followers', 60, W], ['sirf ginti hain,', 66, R], ['aur customers hi', 56, W], ['kharidte hain.', 70, L]]),
 ("Aapki serum ki reels mein, product toh hai, par hook nahi.", '[curious]',
  [['Aapki serum ki reels', 52, W], ['mein, product toh hai,', 52, L], ['par hook nahi.', 80, R]]),
 ("Sach bolun toh, log pehle teen second mein hi, scroll kar jaate hain.", '[serious]',
  [['Sach bolun toh,', 50, W], ['log pehle [3|teen] second', 54, A], ['mein hi, scroll', 54, W], ['kar jaate hain.', 60, W]]),
 ("Isliye hum hook, script, shoot, aur edit, sab kuch karte hain.", '[warmly]',
  [['Isliye hum hook, script,', 50, W], ['shoot, aur edit,', 66, L], ['sab kuch karte hain.', 58, W]]),
 ("Aur comment se, DM aur order tak ka, poora rasta banate hain.", '[excited]',
  [['Aur comment se,', 58, W], ['DM aur order tak ka,', 58, L], ['poora rasta', 64, W], ['banate hain.', 64, W]]),
 ("Koi page chalane wala dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi page chalane', 52, W], ['wala dost hai?', 62, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Page ko sale machine banana hai? Toh comment mein GROW likh do, hum DM kar denge.", '',
  [['Page ko sale machine', 50, W], ['banana hai?', 62, W], ['Toh comment mein GROW', 48, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s10'] = [
 ("Aapke marketing ka har ek rupay, pehle tees din mein, hum kahan lagate hain?", '[curious]',
  [['Aapke marketing ka', 56, W], ['har ek rupay,', 80, A], ['pehle [30|tees] din mein,', 56, L], ['hum kahan lagate hain?', 52, W]]),
 ("Din ek, pehle poora audit, store, page, aur ads, sab dekhte hain.", '[warmly]',
  [['[Din 1:|Din ek,]', 66, L], ['pehle poora audit,', 56, W], ['store, page, aur ads,', 50, W], ['sab dekhte hain.', 60, L]]),
 ("Din teen, profile, catalogue, aur WhatsApp auto reply, sab theek karte hain.", '',
  [['[Din 3:|Din teen,]', 66, L], ['profile, catalogue,', 54, W], ['aur WhatsApp auto reply,', 50, W], ['sab theek karte hain.', 54, L]]),
 ("Din saat, pehli reels, aur ads, dono live ho jaate hain.", '',
  [['[Din 7:|Din saat,]', 66, L], ['pehli reels, aur ads,', 60, W], ['dono live', 72, W], ['ho jaate hain.', 72, L]]),
 ("Din chaudah, jo chala, usme budget badhate hain, aur jo nahi chala, usse band.", '',
  [['[Din 14:|Din chaudah,]', 62, L], ['jo chala, usme', 54, W], ['budget badhate hain,', 54, L], ['aur jo nahi chala, usse band.', 44, R]]),
 ("Aur din tees, report, orders, aur agle mahine ka plan, aapke saamne.", '[happy]',
  [['Aur [Din 30:|din tees,]', 60, L], ['report, orders,', 56, W], ['aur agle mahine ka plan,', 50, W], ['aapke saamne.', 60, L]]),
 ("Koi seller dost hai, jo marketing mein phansa hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi seller dost hai,', 52, W], ['jo marketing mein phansa hai?', 44, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Tees din ka plan chahiye? Toh comment mein PLAN likh do, hum DM kar denge.", '',
  [['Tees din ka plan chahiye?', 50, W], ['Toh comment mein', 54, W], ['PLAN', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

S['s11'] = [
 ("Bees hazaar rupay ke ads se, hazaar log aaye, par sirf do ne khareeda, yaar.", '[frustrated]',
  [['[Rs. 20,000|Bees hazaar rupay]', 60, A], ['ke ads se, [1,000|hazaar] log aaye,', 44, W], ['par sirf [2|do] ne', 58, R], ['khareeda, yaar.', 62, R]]),
 ("Kyunki page dheere khulta hai, aur order button dhoondna padta hai... kaun itna wait karega?", '[sighs]',
  [['Kyunki page dheere', 54, W], ['khulta hai,', 66, R], ['aur order button dhoondna', 42, W], ['padta hai...', 58, W], ['kaun itna wait karega?', 44, A]]),
 ("Aur customer bharosa dekhta hai, reviews, delivery ki details, aur WhatsApp par seedha baat.", '[serious]',
  [['Aur customer bharosa', 54, W], ['dekhta hai, reviews,', 52, L], ['delivery ki details,', 50, W], ['aur WhatsApp par seedha baat.', 44, L]]),
 ("Isliye hum store tez banate hain, aur order, sirf do tap mein.", '[excited]',
  [['Isliye hum store', 56, W], ['tez banate hain,', 62, L], ['aur order, sirf', 52, W], ['[2|do] tap mein.', 78, L]]),
 ("Reviews, return policy, aur WhatsApp button, sab kuch, pehli screen par.", '[warmly]',
  [['Reviews, return policy,', 50, W], ['aur WhatsApp button,', 52, W], ['sab kuch,', 56, W], ['pehli screen par.', 66, L]]),
 ("Wahi traffic, wahi kharch, par orders zyada ho sakte hain.", '[happy]',
  [['Wahi traffic,', 66, W], ['wahi kharch,', 66, W], ['par orders zyada', 58, L], ['ho sakte hain.', 58, L]]),
 ("Koi store chalane wala dost hai? Yeh reel usko bhej do.", '[warmly]',
  [['Koi store chalane', 52, W], ['wala dost hai?', 62, W], ['Yeh reel usko', 66, L], ['bhej do.', 84, W]]),
 ("Store tez karwana hai? Toh comment mein STORE likh do, hum DM kar denge.", '',
  [['Store tez karwana hai?', 52, W], ['Toh comment mein', 54, W], ['STORE', 96, L], ['likh do, hum DM kar denge.', 40, W]]),
]

N = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
def check(rid, lines):
    bad = 0
    for i, (text, tag, rows) in enumerate(lines):
        words = text.split()
        toks = []
        for r in rows:
            for m in re.finditer(r'\[([^\]|]+)\|([^\]]+)\]|\S+', r[0]):
                toks += m.group(2).split() if m.group(1) else [m.group(0)]
        if [N(w) for w in toks] != [N(w) for w in words]:
            bad += 1; print(rid, 'line', i, 'CAPTION MISMATCH\n  spoken:', [N(w) for w in words], '\n  rows  :', [N(w) for w in toks])
        if len(rows) > 5 or sum(r[1] for r in rows) > 290: print(rid, 'line', i, 'tall rows', len(rows), sum(r[1] for r in rows))
    return bad

if __name__ == '__main__':
    tot = 0
    for rid, lines in S.items():
        tot += check(rid, lines)
        ep = json.load(open(f'{H}/episodes/{rid}.json'))
        ep['lines'] = [l[0] for l in lines]
        ep['rows'] = {str(i): l[2] for i, l in enumerate(lines)}
        ep['v'] = 2
        words = sum(len(l[0].split()) for l in lines)
        if '--write' in sys.argv:
            json.dump(ep, open(f'{H}/episodes/{rid}.json', 'w'), ensure_ascii=False, indent=1)
            os.makedirs(f'{H}/work/{rid}', exist_ok=True)
            open(f'{H}/work/{rid}/tts_prompt.txt', 'w').write(' '.join((l[1] + ' ' + l[0]).strip() for l in lines))
        print(rid, 'words', words, 'chars', sum(len((l[1] + ' ' + l[0]).strip()) + 1 for l in lines))
    print('mismatches', tot)
