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

T('r02', '2026-11-13', 'Fri 13 Nov', 'Problem', 'Why freelancers and agencies get no clients', 'CLIENTS', 'plan',
  ["Freelancer ho ya agency, skills hain par client nahi.",
   "Ek small agency ne website banayi, portfolio banaya, aur intezaar kiya. Mahine nikal gaye, inquiry ek bhi nahi.",
   "Client aapko dhoondta nahi, aapko client dhoondna padta hai.",
   "Toh yeh teen wajah hoti hain.",
   "One. Aap intezaar karte ho, aur outreach nahi karte.",
   "Two. Client skills nahi, result khareedta hai.",
   "Three. Aap sirf ek jagah par ho, baaki jagah invisible.",
   "Result? Teeno badlo, aur baat shuru hone lagti hai."],
  '#freelancer #smallagency #findclients #freelancingtips #thetotalforge',
  "Client dhoondne ka plan:\n1. Roz 5 logon ko pehle message karo. Intezaar nahi.\n2. Skill nahi, unka problem aur result likho: [problem] ko [result] mein badlo.\n3. Ek nahi, teen jagah par raho: LinkedIn, ek marketplace, aur ek chhota community thread.\n\nPehle hafte sirf step 1 karo, aur likho kitne reply aaye.")

T('r03', '2026-11-14', 'Sat 14 Nov', 'Hidden places', '3 lesser-known places to find US clients', 'HIDDEN', 'list',
  ["Upwork pe sab hain, bhai. Yeh teen spots pe kam log jaate hain.",
   "Ek new agency owner roz Upwork pe proposals bhejta raha. Competition full on, reply zero. Bhai, cooked.",
   "Jahan sab jaate hain, wahan bheed hoti hai. Simple scene.",
   "Toh yeh teen spots try karo.",
   "One. Hacker News ka freelancer thread. Companies wahan seedha freelancer dhoondti hain.",
   "Two. Clutch. Free profile banao, buyers wahan agencies dhoondte hain.",
   "Three. Sortlist. Free listing, aur buyers wahan agency dhoondte hain.",
   "Result? Kam bheed, seedhi baat. Sorted."],
  '#freelancing #findclients #usclients #smallagency #thetotalforge',
  "Kam jaani jaane wali jagah, US clients ke liye:\n1. Hacker News: har mahine Ask HN: Freelancer? Seeking freelancer? thread aata hai. SEEKING FREELANCER posts padho, aur SEEKING WORK se apna post karo (location aur remote ka zikr likho).\n2. Clutch: agency profile banao (free basic profile). Buyers wahan service ke hisaab se agencies dhoondte hain.\n3. Sortlist: free registration aur listing. Buyers wahan agencies dhoondne aate hain.\n\nHar jagah ke rules alag hain, post karne se pehle unhe padh lein. Clutch aur Sortlist agencies ke liye hain, toh solo freelancer apni chhoti team ke naam se list kar sakta hai.",
  'Sources checked 13 Nov 2026: HN Ask HN Nov 2026 thread exists (jon_north, SEEKING FREELANCER/SEEKING WORK format); Clutch help centre: free company profile; Sortlist how-it-works/pricing: free registration and free listing. Contra and Product Hunt dropped (Contra reviews mixed for new clients, PH not hidden).')

T('r04', '2026-11-15', 'Sun 15 Nov', 'Story and tips', 'A proposal that gets replies', 'PROPOSAL', 'template',
  ["Chalis proposals, reply zero. Bhai, scene kya hai?",
   "Ek freelancer ne sabko wahi copy paste proposal bheja. Pehli line thi, hello sir, I am an expert. Client ne do second mein tab close kar diya.",
   "Client ko copy paste door se pakad aa jata hai. Cringe.",
   "Toh yeh teen moves lo.",
   "One. Pehli line mein client ki problem bolo, apna intro nahi.",
   "Two. Ek relevant project ka proof do, bas do line mein.",
   "Three. End mein ek sawaal pucho, taaki reply banta ho.",
   "Result? Proposal copy paste nahi lagta, aur replies aane lagte hain."],
  '#freelancingtips #upworktips #proposalwriting #freelancer #thetotalforge',
  "Proposal template:\n1. Pehli line: client ki problem, unhi ke lafzon mein. [client ki problem]\n2. Do line: ek relevant project aur uska result. [project, result]\n3. Aakhri line: ek sawaal. Jaise: Kya main ek chhota plan bhej doon?\n\nHar proposal ko job ke hisaab se badlo. Copy paste nahi.")

T('r05', '2026-11-16', 'Mon 16 Nov', 'How to', 'Getting paid from US clients in Pakistan', 'PAYMENT', 'guide',
  ["Client ne payment bhej di. Ab paisa tumhare paas kaise aayega, bhai?",
   "Ek freelancer ne kaam khatam kiya, par payment ka rasta pehle check hi nahi kiya. Last moment pe scene bigad gaya.",
   "Bina plan ke kaam karna, bhai, lowkey risky hai.",
   "Toh yeh teen cheezein pehle sort karo.",
   "One. Payoneer account banao. Woh tumhe US bank details deta hai.",
   "Two. Local bank payout aam taur par ek se teen working days leta hai.",
   "Three. Wise Pakistan mein abhi open nahi hai, uspe plan mat banao.",
   "Result? Paisa tension free, aur plan pehle se ready."],
  '#freelancerpakistan #payoneer #getpaid #remotework #thetotalforge',
  "US clients se payment lene ka checklist:\n1. Payoneer account banao. Isse aapko US bank details milte hain.\n2. Local bank mein payout aam taur par 1 se 3 working days leta hai.\n3. Wise abhi Pakistan ke residents ke liye open nahi hai, isliye uspar plan mat banao.\n4. Kaam shuru karne se pehle client se poochho: payment kis tarah karenge?\n\nFees aur rules badalte rehte hain. Payoneer ki official site par current charges check kar lein.",
  'Checked 12 Nov: Payoneer to local bank 1-3 working days; Wise not open to Pakistan residents. Caption says rules change.')

T('r06', '2026-11-17', 'Tue 17 Nov', 'Tips', 'Pricing without underpricing', 'PRICE', 'checklist',
  ["Sasta kaam karke koi aage nahi gaya, bhai. Sach mein.",
   "Ek freelancer ne sabse kam rate rakha. Clients bohat aaye, par month end pe haath khaali.",
   "Sasta rate matlab zyada kaam, zyada paisa nahi. Seedha nuksan.",
   "Toh yeh teen cheezein badlo.",
   "One. Ghante ka nahi, project ka price batao.",
   "Two. Teen packages rakho. Basic, standard aur premium.",
   "Three. Price batane se pehle client ka budget pucho.",
   "Result? Client choose karta hai, aur tum bargain nahi karte."],
  '#freelancepricing #freelancingtips #freelancelife #pricingstrategy #thetotalforge',
  "Pricing checklist:\n1. Ghante ke bajaye project ka price batao.\n2. Teen packages: Basic, Standard, Premium. Har ek mein kya milega, likho.\n3. Price se pehle poochho: aapka budget kitna hai aur deadline kya hai?\n4. Beech wale package ko recommended rakho.")

T('r07', '2026-11-18', 'Wed 18 Nov', 'Story and tips', 'Replying to clients fast', 'REPLY', 'script',
  ["Client bola kal tak bata do. Tumne parson bataya. Cooked.",
   "Ek freelancer ne client ka message dekha, par raat ko reply kiya. Tab tak client kisi aur freelancer ke saath set ho chuka tha.",
   "Kaam mast tha, par reply late tha. Vibe kharab.",
   "Toh yeh teen cheezein yaad rakho.",
   "One. Mil gaya, kal tak bhejta hoon. Bas itna reply jaldi bhejo.",
   "Two. Apne kaam ke fixed ghante batao, taaki time zone ka scene na bane.",
   "Three. Har baat likh ke confirm karo, deadline bhi.",
   "Result? Client ko bharosa hota hai, aur kaam dobara milta hai."],
  '#clientcommunication #freelancingtips #freelancer #remotework #thetotalforge',
  "Reply script:\n1. Pehla reply (kuch ghante ke andar): Message mil gaya. Main aaj [time] tak details bhejta hoon.\n2. Apne ghante likho: Main Mon se Fri, [time] se [time] tak online hota hoon.\n3. Call ya chat ke baad: Jo humne baat ki: [1], [2], [3]. Deadline [date]. Theek hai?")

T('r08', '2026-11-19', 'Thu 19 Nov', 'Tips', 'A LinkedIn profile US clients open', 'LINKEDIN', 'checklist',
  ["Bhai, tumhari LinkedIn profile client ko kya bolti hai?",
   "Ek client ne profile kholi. Headline thi, hardworking professional. Usne ek second mein back kar diya.",
   "Kyunki usse pata hi nahi chala, tum karte kya ho. Zero clarity.",
   "Toh yeh teen cheezein theek karo.",
   "One. Headline mein likho, tum kya karte ho aur kiske liye.",
   "Two. Featured section mein apne teen best projects lagao.",
   "Three. Roz paanch sahi logon ko connect karo, chhote note ke saath.",
   "Result? Profile tumhara kaam bolti hai, aur client message karta hai."],
  '#linkedintips #linkedinprofile #freelancer #usclients #thetotalforge',
  "LinkedIn checklist:\n1. Headline: [kya karte ho] for [kiske liye]. Jaise: Shopify developer for skincare brands.\n2. Featured: apne 3 best projects.\n3. Roz 5 sahi log connect karo, note ke saath: Hi [naam], aapki [cheez] pasand aayi. Main [kaam] karta hoon, shayad kaam aaye.\n4. About ki pehli line client ki problem par likho.")

T('r09', '2026-11-20', 'Fri 20 Nov', 'Tips', 'Portfolio: 3 projects beat 20', 'PORTFOLIO', 'template',
  ["Bees projects ka portfolio, aur zero client. Scene kya hai, yaar?",
   "Ek freelancer ne har chhota bada kaam portfolio mein daal diya. Client scroll karta raha, aur kuch samajh hi nahi aaya.",
   "Zyada projects matlab clear message nahi. Overload.",
   "Toh yeh teen cheezein karo.",
   "One. Sirf apne teen best projects rakho.",
   "Two. Har project mein likho, problem kya thi aur tumne kya kiya.",
   "Three. Ek link rakho, aur mobile par kholke check karo.",
   "Result? Client ko ek minute mein samajh aata hai, tum kya kar sakte ho."],
  '#portfolio #freelancerportfolio #freelancingtips #webdeveloper #thetotalforge',
  "Portfolio template (har project ke liye):\n1. Project ka naam aur client ka type.\n2. Problem: kya masla tha?\n3. Kya kiya: 2 line.\n4. Result: jo number ya feedback sach mein mila.\n5. Ek link ya screenshot.\n\nSirf 3 best projects rakho, aur link mobile par kholkar check karo.")

T('r10', '2026-11-21', 'Sat 21 Nov', 'Story and tips', 'A cold email to a US business', 'EMAIL', 'template',
  ["Chaar line ki email, aur US client ka reply. Sach mein.",
   "Ek freelancer ne dus businesses ko lambi email bheji, apne baare mein. Reply ek bhi nahi aaya. Cooked.",
   "Kisi ke paas tumhari poori life story padhne ka time nahi.",
   "Toh yeh teen lines likho.",
   "One. Pehli line mein unki website ki ek specific cheez batao.",
   "Two. Doosri line mein ek problem aur uska chhota hal batao.",
   "Three. Aakhri line mein sawaal, kya main chhota plan bhej doon?",
   "Result? Email chhoti hai, aur reply dena easy."],
  '#coldemail #coldoutreach #freelancingtips #usclients #thetotalforge',
  "Cold email template (4 line):\nSubject: Quick idea for [business name]\n1. Maine aapki website par [specific cheez] dekhi.\n2. [Problem] ho sakti hai, aur uska ek chhota hal hai: [hal].\n3. Maine [relevant kaam] kiya hai: [link].\n4. Kya main ek chhota plan bhej doon?\n\nEk email, ek hi ask. Aur wahi likho jo sach ho.")

T('r11', '2026-11-22', 'Sun 22 Nov', 'Job to agency', 'Before you quit your job for an agency', 'QUIT', 'checklist',
  ["Job chhodke agency banani hai? Pehle yeh teen kaam karo, bhai.",
   "Ek banda ek din achanak resign maar ke nikal gaya. Teen mahine baad, na client tha, na plan.",
   "Pehle clients, phir resignation. Ulta kiya toh pressure full on.",
   "Toh yeh teen kaam pehle karo.",
   "One. Job ke saath ek chhota paying client pakdo.",
   "Two. Ek skill aur ek niche chuno, aur uske teen samples banao.",
   "Three. Resign tab karo, jab kharcha nikalne layak clients ho.",
   "Result? Tum bhaagte nahi, tayyari se agency shuru karte ho."],
  '#startanagency #quitjob #sidehustle #smallagency #thetotalforge',
  "Job chhodne se pehle checklist:\n1. Job ke saath ek chhota paying client lo (ek chhota project bhi chalega).\n2. Ek skill aur ek niche chuno, aur us niche ke teen samples banao.\n3. Apna mahine ka kharcha likho, aur dekho clients ki income us kharche ko kitna cover karti hai.\n4. Resign tab karo jab client income us kharche ke qareeb ho.\n\nYeh general checklist hai, financial advice nahi. Apni situation ke hisaab se faisla lein.",
  'No factual claims about platforms. General guidance only; caption carries a not-financial-advice line.')

T('r12', '2026-11-23', 'Mon 23 Nov', 'Story and tips', 'Scope creep', 'SCOPE', 'checklist',
  ["Bas ek chhota sa change. Phir chhe baar. Dimaag ka dahi.",
   "Ek freelancer ne logo banaya. Client ne chhe baar changes maange, aur paisa wahi raha.",
   "Scope likha nahi tha, toh kaam khatam hi nahi hua.",
   "Toh yeh teen cheezein pehle likho.",
   "One. Kaam mein kya kya milega, yeh likh ke batao.",
   "Two. Revisions ki limit rakho, jaise do rounds.",
   "Three. Shuru karne se pehle aadha advance lo.",
   "Result? Kaam bhi khatam, payment bhi."],
  '#scopecreep #freelancingtips #clientwork #freelancelife #thetotalforge',
  "Scope checklist:\n1. Kya kya milega: deliverables ki list.\n2. Kya nahi milega: extra cheezein.\n3. Revisions: 2 rounds. Uske baad extra charge.\n4. Deadline, aur client se kya chahiye (content, access).\n5. Shuru karne se pehle 50% advance.\n\nYeh sab ek message ya contract mein likhit mein bhejo.")

T('r13', '2026-11-24', 'Tue 24 Nov', 'Tips', 'Client red flags', 'FLAGS', 'checklist',
  ["Client mein yeh red flags dikhein, toh seedha ruk jao.",
   "Ek freelancer ne free test project kiya. Client ne kaam le liya, aur payment kabhi nahi bheji. Ghosted.",
   "Signs pehle hi dikh gaye the. Bas ignore kiye.",
   "Toh yeh teen flags yaad rakho.",
   "One. Free test project, ya pehle poora kaam dikhao.",
   "Two. Advance se inkaar, ya payment baad mein dene ki baat.",
   "Three. Budget clear nahi, aur har cheez urgent.",
   "Result? Tum sahi client choose karte ho, aur time bachta hai."],
  '#redflags #clientmanagement #freelancingtips #freelancer #thetotalforge',
  "Client red flags:\n1. Free test project, ya pehle poora kaam dikhao.\n2. Advance se inkaar, ya payment baad mein dene ki baat.\n3. Budget saaf nahi, aur har cheez urgent.\n\nEk flag dikhe toh ruk kar sawaal poochho. Do dikhein toh dobara soch lo.")

T('r14', '2026-11-25', 'Wed 25 Nov', 'Tips', 'Pick a niche', 'FOCUS', 'guide',
  ["Hum sab kuch karte hain. Bhai, isi wajah se kaam nahi milta.",
   "Ek agency ne bola, hum sab kuch karte hain. Client ko samajh hi nahi aaya, isse kaunsa kaam dena hai.",
   "Jo sab kuch karta hai, uski koi pehchaan nahi banti.",
   "Toh yeh teen steps lo.",
   "One. Ek tarah ka client chuno, jaise skincare brands.",
   "Two. Ek problem chuno, jaise slow Shopify store.",
   "Three. Us ek problem ka ek sample banao.",
   "Result? Tum expert lagte ho, aur client seedha tumhe chunta hai."],
  '#niche #agencyniche #smallagency #freelancingtips #thetotalforge',
  "Niche chunne ka guide:\n1. Ek tarah ka client: jaise skincare brands, dentists ya coaches.\n2. Ek problem: jaise slow website ya purani branding.\n3. Ek sample: us problem ka ek chhota kaam banao.\n4. Headline: [kaam] for [client type].\n\nShuru mein ek niche, 30 din ke liye. Phir dekho kaunsa reply aata hai.")

T('r15', '2026-11-26', 'Thu 26 Nov', 'Tips', 'A 30-minute daily routine', 'ROUTINE', 'planner',
  ["Roz sirf tees minute. Agency ka simple routine, bhai.",
   "Ek agency ek din full josh mein kaam karti, aur phir hafte bhar kuch nahi.",
   "Kabhi kabhi ka josh, clients nahi laata.",
   "Toh roz yeh teen kaam karo.",
   "One. Paanch clients ko message ya proposal bhejo.",
   "Two. Apni profile ya portfolio mein ek chhota sudhaar karo.",
   "Three. Ek sheet mein likho, kisne reply kiya aur kisne nahi.",
   "Result? Ek mahine mein tumhare paas ek system hota hai."],
  '#freelanceroutine #dailyroutine #smallagency #sidehustle #thetotalforge',
  "Roz 30 minute ka planner:\n- 15 min: 5 messages ya proposals.\n- 10 min: profile ya portfolio mein ek chhota sudhaar.\n- 5 min: sheet mein likho, kisne reply kiya.\n\nHafte ke end mein dekho: kitne bheje, kitne reply, kya sikha. Agle hafte ek cheez badlo.")


def caption(x):
    L = x['lines']; thing = x['thing'].capitalize()
    tips = [L[i].split('. ', 1)[1] for i in (4, 5, 6)]
    cap = (f"{L[0]}\n\n{L[1]}\n\n{L[3].replace('Toh ', '').capitalize().rstrip('.')}:\n"
           f"1. {tips[0]}\n2. {tips[1]}\n3. {tips[2]}\n\n"
           f"{thing} chahiye? Comment \"{x['kw']}\" karein, hum aapko DM kar denge.\n\n")
    if x['id'] in ('r03', 'r05'):
        cap += "Fees aur rules badalte rehte hain, platform par ek baar check kar lein.\n\n"
    if x['id'] == 'r11':
        cap += "Yeh general tips hain, financial advice nahi. Resign karne se pehle apni situation dekh lein.\n\n"
    cap += f"Example scenario: yeh ek misaal hai, real client nahi.\n\n{x['hashtags']}"
    return cap

def first_comment(x):
    return f"{x['thing'].capitalize()} chahiye? Comment \"{x['kw']}\" aur hum DM mein bhej denge."

def alt(x):
    return f"Animated Hinglish tips reel for freelancers and small agencies: {x['lines'][0]} Three tips, shown on screen."

if __name__ == '__main__':
    for x in TIPS:
        print(x['id'], x['chars'], x['kw'])
