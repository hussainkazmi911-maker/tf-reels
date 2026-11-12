# Story / scenario / tips series (Reels 3-15, Sat 14 - Thu 26 Nov). Text only: voice scripts, captions, DM replies.
# Animation specs live in make_tips.py. Line 0 hook, 1 story, 2 mistake, 3 bridge, 4-6 tips, 7 result, 8 CTA (built from `thing` + keyword).
# usage: imported by make_tips.py

TIPS = []
def T(id, date, label, fmt, topic, kw, thing, L, hashtags, dm, note=''):
    L = list(L)
    assert len(L) == 8, (id, len(L))
    L.append(f"Want the {thing}? Comment {kw}, hum aapko DM kar denge.")
    assert len(L) == 9, (id, len(L))
    assert 'teen' in L[3].lower().split(), (id, L[3])
    chars = sum(len(x) for x in L) + 8
    assert chars <= 640, (id, chars)
    assert len(hashtags.split()) == 5, id
    TIPS.append(dict(id=id, date=date, label=label, fmt=fmt, topic=topic, kw=kw, thing=thing, lines=L,
                     hashtags=hashtags, dm=dm, note=note, chars=chars))

T('r03', '2026-11-14', 'Sat 14 Nov', 'Where to find', '3 places to find US clients', 'SITES', 'list',
  ["US client chahiye? Pehle yeh teen jagah dekho.",
   "Ek freelancer sirf ek website par proposals bhejta raha. Mahina nikal gaya, kaam nahi mila.",
   "Ek hi jagah par sab daav lagana, yahi sabse badi galti hai.",
   "Toh yeh teen jagah try karo.",
   "One. Upwork. Fresh jobs par jaldi proposal bhejo.",
   "Two. LinkedIn. Founders ko seedha ek chhota message karo.",
   "Three. Contra. Portfolio banao, aur wahan commission nahi lagta.",
   "Result? Ek hafte mein teen raaste, aur clients ke saamne aap."],
  '#freelancing #usclients #upwork #freelancepakistan #thetotalforge',
  "US clients dhoondne ki list:\n1. Upwork: fresh jobs par jaldi proposal bhejo. Client ki payment verified ho, yeh check karo.\n2. LinkedIn: founders aur managers ko ek chhota, specific message karo.\n3. Contra: portfolio banao. Contra ke mutabiq wahan commission nahi lagta.\n\nPehle hafte mein teeno par ek ek kaam karo: ek proposal, paanch messages, ek portfolio.\nRules aur fees badalte rehte hain, platform par ek baar check kar lein.",
  'Contra: no commission (its own pricing page). Upwork: fresh jobs advice.')

T('r04', '2026-11-15', 'Sun 15 Nov', 'Story and tips', 'A proposal that gets replies', 'PROPOSAL', 'template',
  ["Chalis proposals bheje, reply zero. Galti kahan thi?",
   "Ek freelancer ne sabko wahi copy paste proposal bheja. Pehli line thi, hello sir, I am an expert.",
   "Client ne do second mein dekha, aur band kar diya.",
   "Toh yeh teen cheezein badlo.",
   "One. Pehli line client ki problem par likho, apne baare mein nahi.",
   "Two. Ek relevant project ka proof do, bas do line mein.",
   "Three. End mein ek sawaal poochho, taaki reply banta ho.",
   "Result? Proposal copy nahi lagta, aur reply aane lagte hain."],
  '#freelancingtips #upworktips #proposalwriting #freelancer #thetotalforge',
  "Proposal template:\n1. Pehli line: client ki problem, unhi ke lafzon mein. [client ki problem]\n2. Do line: ek relevant project aur uska result. [project, result]\n3. Aakhri line: ek sawaal. Jaise: Kya main ek chhota plan bhej doon?\n\nHar proposal ko job ke hisaab se badlo. Copy paste nahi.")

T('r05', '2026-11-16', 'Mon 16 Nov', 'How to', 'Getting paid from US clients in Pakistan', 'PAYMENT', 'guide',
  ["Client ne payment bhej di. Aap tak kaise aayegi?",
   "Ek freelancer ne kaam pura kiya, par payment ka rasta pehle se nahi dekha.",
   "Aakhri din pata chala, ki options hi limited hain.",
   "Toh yeh teen cheezein pehle dekho.",
   "One. Payoneer account banao. Yeh aapko US bank details deta hai.",
   "Two. Local bank mein payout aam taur par ek se teen working days leta hai.",
   "Three. Wise Pakistan mein abhi open nahi hai, toh uspar plan mat banao.",
   "Result? Kaam ke baad payment ka tension nahi, aur plan pehle se ready."],
  '#freelancerpakistan #payoneer #getpaid #remotework #thetotalforge',
  "US clients se payment lene ka checklist:\n1. Payoneer account banao. Isse aapko US bank details milte hain.\n2. Local bank mein payout aam taur par 1 se 3 working days leta hai.\n3. Wise abhi Pakistan ke residents ke liye open nahi hai, isliye uspar plan mat banao.\n4. Kaam shuru karne se pehle client se poochho: payment kis tarah karenge?\n\nFees aur rules badalte rehte hain. Payoneer ki official site par current charges check kar lein.",
  'Checked 12 Nov: Payoneer to local bank 1-3 working days; Wise not open to Pakistan residents. Caption says rules change.')

T('r06', '2026-11-17', 'Tue 17 Nov', 'Tips', 'Pricing without underpricing', 'PRICE', 'checklist',
  ["Sasta kaam karke koi aage nahi badha.",
   "Ek freelancer ne sabse kam rate rakha. Client bahut aaye, par mahine ke end mein haath khaali.",
   "Kam rate ka matlab zyada kaam hota hai, zyada paisa nahi.",
   "Toh yeh teen cheezein badlo.",
   "One. Ghante ke bajaye project ka price batao.",
   "Two. Teen packages rakho, basic, standard aur premium.",
   "Three. Price batane se pehle client ka budget poochho.",
   "Result? Client choose karta hai, aur aap bargain nahi karte."],
  '#freelancepricing #freelancingtips #freelancelife #pricingstrategy #thetotalforge',
  "Pricing checklist:\n1. Ghante ke bajaye project ka price batao.\n2. Teen packages: Basic, Standard, Premium. Har ek mein kya milega, likho.\n3. Price se pehle poochho: aapka budget kitna hai aur deadline kya hai?\n4. Beech wale package ko recommended rakho.")

T('r07', '2026-11-18', 'Wed 18 Nov', 'Story and tips', 'Replying to clients fast', 'REPLY', 'script',
  ["Client ne kaha kal tak bata do. Aapne parson bataya.",
   "Ek freelancer ne client ka message dekha, par raat ko reply kiya. Tab tak client doosre freelancer se baat kar raha tha.",
   "Kaam accha tha, par jawab jaldi nahi tha.",
   "Toh yeh teen cheezein yaad rakho.",
   "One. Mil gaya, kal tak bhejta hoon. Bas itna reply jaldi bhejo.",
   "Two. Apne kaam ke fixed ghante batao, taaki time zone ka masla na rahe.",
   "Three. Har baat likhit mein confirm karo, deadline bhi.",
   "Result? Client ko bharosa hota hai, aur kaam dobara milta hai."],
  '#clientcommunication #freelancingtips #freelancer #remotework #thetotalforge',
  "Reply script:\n1. Pehla reply (kuch ghante ke andar): Message mil gaya. Main aaj [time] tak details bhejta hoon.\n2. Apne ghante likho: Main Mon se Fri, [time] se [time] tak online hota hoon.\n3. Call ya chat ke baad: Jo humne baat ki: [1], [2], [3]. Deadline [date]. Theek hai?")

T('r08', '2026-11-19', 'Thu 19 Nov', 'Tips', 'A LinkedIn profile US clients open', 'LINKEDIN', 'checklist',
  ["Aapki LinkedIn profile client ko kya batati hai?",
   "Ek client ne profile kholi. Headline thi, hardworking professional. Usne ek second mein band kar di.",
   "Kyunki usse pata nahi chala, aap kya karte ho.",
   "Toh yeh teen cheezein theek karo.",
   "One. Headline mein likho, aap kya karte ho aur kiske liye.",
   "Two. Featured section mein apne teen best projects lagao.",
   "Three. Roz paanch sahi logon ko connect karo, chhote note ke saath.",
   "Result? Profile aapka kaam batati hai, aur client message karta hai."],
  '#linkedintips #linkedinprofile #freelancer #usclients #thetotalforge',
  "LinkedIn checklist:\n1. Headline: [kya karte ho] for [kiske liye]. Jaise: Shopify developer for skincare brands.\n2. Featured: apne 3 best projects.\n3. Roz 5 sahi log connect karo, note ke saath: Hi [naam], aapki [cheez] pasand aayi. Main [kaam] karta hoon, shayad kaam aaye.\n4. About ki pehli line client ki problem par likho.")

T('r09', '2026-11-20', 'Fri 20 Nov', 'Tips', 'Portfolio: 3 projects beat 20', 'PORTFOLIO', 'template',
  ["Bees projects ka portfolio, aur ek bhi client nahi.",
   "Ek freelancer ne har chhota bada kaam portfolio mein daal diya. Client scroll karta raha, aur kuch samajh nahi aaya.",
   "Zyada projects ka matlab, saaf message nahi.",
   "Toh yeh teen cheezein karo.",
   "One. Sirf apne teen best projects rakho.",
   "Two. Har project mein likho, problem kya thi aur aapne kya kiya.",
   "Three. Ek link rakho, aur mobile par kholkar check karo.",
   "Result? Client ko ek minute mein samajh aata hai, aap kya kar sakte ho."],
  '#portfolio #freelancerportfolio #freelancingtips #webdeveloper #thetotalforge',
  "Portfolio template (har project ke liye):\n1. Project ka naam aur client ka type.\n2. Problem: kya masla tha?\n3. Kya kiya: 2 line.\n4. Result: jo number ya feedback sach mein mila.\n5. Ek link ya screenshot.\n\nSirf 3 best projects rakho, aur link mobile par kholkar check karo.")

T('r10', '2026-11-21', 'Sat 21 Nov', 'Story and tips', 'A cold email to a US business', 'EMAIL', 'template',
  ["Chaar line ki email, aur US client ka reply. Kaise?",
   "Ek freelancer ne dus businesses ko lambi email bheji, apne baare mein. Reply ek bhi nahi aaya.",
   "Kisi ke paas aapki poori kahani padhne ka time nahi hota.",
   "Toh yeh teen line likho.",
   "One. Pehli line mein unki website ki ek specific cheez batao.",
   "Two. Doosri line mein ek problem aur uska chhota hal batao.",
   "Three. Aakhri line mein ek sawaal, kya main chhota plan bhej doon?",
   "Result? Email chhoti hai, aur jawab dena aasaan."],
  '#coldemail #coldoutreach #freelancingtips #usclients #thetotalforge',
  "Cold email template (4 line):\nSubject: Quick idea for [business name]\n1. Maine aapki website par [specific cheez] dekhi.\n2. [Problem] ho sakti hai, aur uska ek chhota hal hai: [hal].\n3. Maine [relevant kaam] kiya hai: [link].\n4. Kya main ek chhota plan bhej doon?\n\nEk email, ek hi ask. Aur wahi likho jo sach ho.")

T('r11', '2026-11-22', 'Sun 22 Nov', 'Where to find', 'Upwork Connects: do not waste them', 'UPWORK', 'checklist',
  ["Upwork par har proposal ka paisa lagta hai.",
   "Ek freelancer ne bina dekhe pachaas jobs par apply kiya. Connects khatam, aur kaam ek bhi nahi.",
   "Har Connect ki price pandrah cents hai, toh andaze se apply mat karo.",
   "Toh yeh teen cheezein check karo.",
   "One. Job fresh ho, taaki aap pehle proposals mein rahein.",
   "Two. Client ki payment verified ho, aur hiring history dekho.",
   "Three. Job post poori padho, aur usi ke hisaab se likho.",
   "Result? Kam Connects lagte hain, aur replies ke chance badhte hain."],
  '#upwork #upworkfreelancer #freelancingtips #freelancepakistan #thetotalforge',
  "Upwork par apply karne se pehle check karo:\n1. Job fresh hai (kuch ghante purani).\n2. Client ki payment verified hai.\n3. Client ki hiring history aur reviews dekho.\n4. Job post poori padho, aur proposal ki pehli line usi par likho.\n\nUpwork ke mutabiq ek Connect 15 cents ka hota hai, aur fees badalti rehti hain. Upwork ka current fee page dekh lein.",
  'Checked 12 Nov: Connects $0.15 each. Caption says rules change.')

T('r12', '2026-11-23', 'Mon 23 Nov', 'Story and tips', 'Scope creep', 'SCOPE', 'checklist',
  ["Bas ek chhota sa change. Aur phir chhe baar.",
   "Ek freelancer ne logo banaya. Client ne chhe baar change mangwaya, aur paisa wahi raha.",
   "Scope likhit mein nahi tha, toh kaam khatam hi nahi hua.",
   "Toh yeh teen cheezein pehle likho.",
   "One. Kaam mein kya kya milega, yeh likhit mein batao.",
   "Two. Revisions ki limit rakho, jaise do rounds.",
   "Three. Shuru karne se pehle aadha advance lo.",
   "Result? Kaam khatam hota hai, aur payment bhi."],
  '#scopecreep #freelancingtips #clientwork #freelancelife #thetotalforge',
  "Scope checklist:\n1. Kya kya milega: deliverables ki list.\n2. Kya nahi milega: extra cheezein.\n3. Revisions: 2 rounds. Uske baad extra charge.\n4. Deadline, aur client se kya chahiye (content, access).\n5. Shuru karne se pehle 50% advance.\n\nYeh sab ek message ya contract mein likhit mein bhejo.")

T('r13', '2026-11-24', 'Tue 24 Nov', 'Tips', 'Client red flags', 'FLAGS', 'checklist',
  ["Client mein yeh red flags dikhein, toh ruk jao.",
   "Ek freelancer ne free test project kiya. Client ne kaam le liya, aur payment kabhi nahi bheji.",
   "Signs pehle hi dikh gaye the.",
   "Toh yeh teen flags yaad rakho.",
   "One. Free test project, ya pehle poora kaam dikhao.",
   "Two. Advance se inkaar, ya payment baad mein dene ki baat.",
   "Three. Budget saaf nahi, aur har cheez urgent.",
   "Result? Aap sahi client choose karte hain, aur time bachta hai."],
  '#redflags #clientmanagement #freelancingtips #freelancer #thetotalforge',
  "Client red flags:\n1. Free test project, ya pehle poora kaam dikhao.\n2. Advance se inkaar, ya payment baad mein dene ki baat.\n3. Budget saaf nahi, aur har cheez urgent.\n\nEk flag dikhe toh ruk kar sawaal poochho. Do dikhein toh dobara soch lo.")

T('r14', '2026-11-25', 'Wed 25 Nov', 'Tips', 'Pick a niche', 'FOCUS', 'guide',
  ["Main web developer hoon. Isse kaam nahi milta.",
   "Ek freelancer ne bola, main sab kuch karta hoon. Client ko samajh hi nahi aaya, usse kaunsa kaam dena hai.",
   "Sab kuch karne wale ko, koi khaas kaam nahi milta.",
   "Toh yeh teen steps lo.",
   "One. Ek tarah ka client chuno, jaise skincare brands.",
   "Two. Ek problem chuno, jaise slow Shopify store.",
   "Three. Us ek problem ka ek sample banao.",
   "Result? Aap expert dikhte ho, aur client seedha aapko chunta hai."],
  '#niche #freelanceniche #freelancingtips #personalbranding #thetotalforge',
  "Niche chunne ka guide:\n1. Ek tarah ka client: jaise skincare brands, dentists ya coaches.\n2. Ek problem: jaise slow website ya purani branding.\n3. Ek sample: us problem ka ek chhota kaam banao.\n4. Headline: [kaam] for [client type].\n\nShuru mein ek niche, 30 din ke liye. Phir dekho kaunsa reply aata hai.")

T('r15', '2026-11-26', 'Thu 26 Nov', 'Tips', 'A 30-minute daily routine', 'ROUTINE', 'planner',
  ["Roz tees minute. Freelancer ka simple routine.",
   "Ek freelancer ek din bahut kaam karta, aur phir hafte bhar kuch nahi.",
   "Kabhi kabhi ka josh, clients nahi laata.",
   "Toh roz yeh teen kaam karo.",
   "One. Paanch clients ko message ya proposal bhejo.",
   "Two. Apni profile ya portfolio mein ek chhota sudhaar karo.",
   "Three. Ek sheet mein likho, kisne reply kiya aur kisne nahi.",
   "Result? Ek mahine mein, aapke paas ek system hota hai."],
  '#freelanceroutine #dailyroutine #productivity #freelancer #thetotalforge',
  "Roz 30 minute ka planner:\n- 15 min: 5 messages ya proposals.\n- 10 min: profile ya portfolio mein ek chhota sudhaar.\n- 5 min: sheet mein likho, kisne reply kiya.\n\nHafte ke end mein dekho: kitne bheje, kitne reply, kya sikha. Agle hafte ek cheez badlo.")


def caption(x):
    L = x['lines']; thing = x['thing'].capitalize()
    tips = [L[i].split('. ', 1)[1] for i in (4, 5, 6)]
    cap = (f"{L[0]}\n\n{L[1]}\n\n{L[3].replace('Toh ', '').capitalize().rstrip('.')}:\n"
           f"1. {tips[0]}\n2. {tips[1]}\n3. {tips[2]}\n\n"
           f"{thing} chahiye? Comment \"{x['kw']}\" karein, hum aapko DM kar denge.\n\n")
    if x['id'] in ('r03', 'r05', 'r11'):
        cap += "Fees aur rules badalte rehte hain, platform par ek baar check kar lein.\n\n"
    cap += f"Example scenario: yeh ek misaal hai, real client nahi.\n\n{x['hashtags']}"
    return cap

def first_comment(x):
    return f"{x['thing'].capitalize()} chahiye? Comment \"{x['kw']}\" aur hum DM mein bhej denge."

def alt(x):
    return f"Animated Hinglish tips reel for freelancers: {x['lines'][0]} Three tips, shown on screen."

if __name__ == '__main__':
    for x in TIPS:
        print(x['id'], x['chars'], x['kw'])
