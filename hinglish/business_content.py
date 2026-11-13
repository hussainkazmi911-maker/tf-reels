# Business reels (Reel 1 style): relatable pain for a Pakistani small business, "hum apne clients ke liye teen cheezein banate hain", comment keyword.
# Hook, example scenario (invented, labelled), bridge, three things we build, result, CTA. Gen Z Hinglish, voiced with "hussain voice".
# No dates yet: Hussain picks the day when he sends the mp3. Ids b01..b07. Animation specs get added when the audio arrives.
# usage: imported by make_scripts_page.py
BRIDGE = "Isiliye hum apne clients ke liye teen cheezein banate hain."
BIZ = []

def B(id, who, kw, topic, lines, cap1, builds, tags, q, demo):
    L = list(lines)
    assert len(L) == 9, (id, len(L))
    assert L[3] == BRIDGE, id
    chars = sum(len(x) for x in L) + 8
    assert chars <= 640, (id, chars)
    assert len(tags.split()) == 5 and tags.endswith('#thetotalforge'), id
    assert len(builds) == 3, id
    caption = (f"{L[0]}\n\n{cap1}\n\nHum apne clients ke liye teen cheezein banate hain:\n"
               + '\n'.join(f"{i + 1}. {b}" for i, b in enumerate(builds))
               + f"\n\n{who}? Comment \"{kw}\" karein, hum aapko DM kar denge.\n\n"
               "Example scenario: yeh ek misaal hai, real client nahi.\n\n" + tags)
    comment = f"{who}? Comment \"{kw}\" aur hum DM mein details bhej denge."
    dm = (f"Shukriya! {who} ke liye hum teen cheezein banate hain:\n"
          + '\n'.join(f"{i + 1}. {b}" for i, b in enumerate(builds))
          + f"\n\n{q} Phir hum aapko suggest kar denge ke aapke liye kya sahi rahega.")
    BIZ.append(dict(id=id, who=who, kw=kw, topic=topic, lines=L, caption=caption, comment=comment, dm=dm, tags=tags,
                    chars=chars, demo=demo))

B('b01', 'Food business', 'MENU', 'Home bakers and cloud kitchens: WhatsApp orders get lost',
  ["Order WhatsApp pe aaya, par kitchen ko pata hi nahi chala.",
   "Ek home baker ko WhatsApp pe das orders aaye. Do miss ho gaye, aur ek customer ko wrong cake mila.",
   "Chats mein orders dhoondna, lowkey sabse bada stress hai.",
   BRIDGE,
   "One. A menu page. Customer item chunta hai, aur order seedha aata hai.",
   "Two. An auto-confirmation, so every order gets a reply in seconds.",
   "Three. One kitchen screen: new, cooking, ready.",
   "Result? Orders chats mein nahi khote, aur kitchen sorted rehta hai.",
   "Want this for your kitchen? Comment MENU, hum aapko DM kar denge."],
  "Ek home baker ko WhatsApp pe das orders aaye. Do miss ho gaye, aur ek customer ko galat cake mil gaya.",
  ["Menu page: customer item chunta hai, aur order seedha aata hai", "Auto-confirmation: har order ka jawab seconds mein",
   "Kitchen screen: new, cooking, ready"],
  '#homebaker #cloudkitchen #foodbusinesspakistan #orderautomation #thetotalforge', 'Aap abhi orders kaise sambhalte hain, aur roz taqreeban kitne orders aate hain?', 'form+chat+board')

B('b02', 'Salon owner', 'BOOKING', 'Salons: DM bookings lead to double bookings',
  ["DMs mein appointments, aur do log ek hi slot pe. Scene kya hai?",
   "Ek salon DMs mein bookings leta tha. Do clients ek hi time pe aa gaye, aur dono naraz hoke chale gaye.",
   "DMs calendar nahi hote, bhai. Double booking pakki hai.",
   BRIDGE,
   "One. A booking page. Customer service aur time khud chunta hai.",
   "Two. An auto-reminder, so nobody forgets their slot.",
   "Three. One calendar jahan har appointment dikhta hai: booked, confirmed, done.",
   "Result? Double booking khatam, aur calendar saaf rehta hai.",
   "Want this for your salon? Comment BOOKING, hum aapko DM kar denge."],
  "Ek salon DMs mein bookings leta tha. Do clients ek hi time pe aa gaye, aur dono naraz hoke chale gaye.",
  ["Booking page: customer service aur time khud chunta hai", "Auto-reminder: slot koi nahi bhoolta",
   "Calendar: booked, confirmed, done"],
  '#salonowner #beautysalon #salonbusiness #onlinebooking #thetotalforge', 'Aap abhi bookings kaise lete hain, aur hafte mein taqreeban kitni bookings hoti hain?', 'form+chat+board')

B('b03', 'Clinic owner', 'CLINIC', 'Clinics: appointments on calls and paper registers',
  ["Patient aaya, par register mein uska appointment hi nahi tha.",
   "Ek clinic mein appointments calls pe lagti thi. Ek entry likhna reh gayi, aur patient ghanta bhar wait karta raha.",
   "Calls aur register pe sab kuch chalana, lowkey risky hai.",
   BRIDGE,
   "One. An online booking page. Patient apna time khud book karta hai.",
   "Two. An auto-reminder before every appointment.",
   "Three. One screen jahan har visit dikhti hai: booked, arrived, done.",
   "Result? Register ki tension khatam, aur front desk relaxed.",
   "Want this for your clinic? Comment CLINIC, hum aapko DM kar denge."],
  "Ek clinic mein appointments calls pe lagti thin. Ek entry likhna reh gayi, aur patient ghanta bhar wait karta raha.",
  ["Online booking page: patient apna time khud book karta hai", "Auto-reminder: har appointment se pehle",
   "Ek screen: booked, arrived, done"],
  '#clinicowner #clinicmanagement #onlinebooking #healthcarebusiness #thetotalforge', 'Aap abhi appointments kaise sambhalte hain, aur roz taqreeban kitne patients aate hain?', 'form+chat+board')

B('b04', 'Property dealer', 'LEADS', 'Property dealers: slow follow-up loses leads',
  ["Lead ne raat ko inquiry bheji, aur aapne agle din reply kiya.",
   "Ek property dealer ko raat ko ek inquiry aayi. Subah tak buyer kisi aur dealer se baat kar chuka tha.",
   "Leads wait nahi karte, bhai. Speed hi game hai.",
   BRIDGE,
   "One. An inquiry form jo har lead ko seedha save karta hai.",
   "Two. An instant reply, so every lead hears back in seconds.",
   "Three. One board jahan har lead dikhta hai: new, contacted, closed.",
   "Result? Koi lead miss nahi hota, aur follow-up easy ho jata hai.",
   "Want this for your office? Comment LEADS, hum aapko DM kar denge."],
  "Ek property dealer ko raat ko ek inquiry aayi. Subah tak buyer kisi aur dealer se baat kar chuka tha.",
  ["Inquiry form: har lead seedha save hota hai", "Instant reply: har lead ko seconds mein jawab",
   "Board: new, contacted, closed"],
  '#propertydealer #realestatepakistan #leadmanagement #crm #thetotalforge', 'Aap abhi inquiries kaise sambhalte hain, aur hafte mein taqreeban kitni leads aati hain?', 'form+chat+board')

B('b05', 'Gym owner', 'MEMBERS', 'Gyms: fees in a notebook, members quietly leave',
  ["Member ne fees nahi di, aur kisi ko yaad bhi nahi tha.",
   "Ek gym owner fees notebook mein likhta tha. Teen members chup chaap chale gaye, aur usse mahine ke end mein pata chala.",
   "Notebook yaad nahi dilata, bhai. Paisa chala jata hai.",
   BRIDGE,
   "One. A member app jahan har member ka plan aur due date dikhta hai.",
   "Two. An auto-reminder, so fees time pe yaad dila di jaye.",
   "Three. One screen jahan har member dikhta hai: active, due, expired.",
   "Result? Fees yaad rehti hain, aur members ka track rehta hai.",
   "Want this for your gym? Comment MEMBERS, hum aapko DM kar denge."],
  "Ek gym owner fees notebook mein likhta tha. Teen members chup chaap chale gaye, aur usse mahine ke end mein pata chala.",
  ["Member app: har member ka plan aur due date", "Auto-reminder: fees time pe yaad dila di jaye",
   "Ek screen: active, due, expired"],
  '#gymowner #fitnessbusiness #gymmanagement #membershipapp #thetotalforge', 'Aap abhi fees aur members ka record kaise rakhte hain, aur taqreeban kitne members hain?', 'form+chat+board')

B('b06', 'Academy owner', 'ACADEMY', 'Tuition academies: chasing fees every month',
  ["Fees ka hisaab copy mein, aur parents ko roz yaad dilana. Thak gaye?",
   "Ek academy owner har mahine WhatsApp pe fees chase karta tha. Kuch parents late, kuch bhool gaye, aur record sab ka alag.",
   "Chasing hi poora kaam ban jata hai. Padhai kab karwaoge?",
   BRIDGE,
   "One. An enrolment form. Parent aur student ki details ek hi jagah.",
   "Two. An auto fee reminder, so every parent gets a message on time.",
   "Three. One screen jahan har student ki fee dikhti hai: paid, due, late.",
   "Result? Chasing kam, aur record hamesha ready.",
   "Want this for your academy? Comment ACADEMY, hum aapko DM kar denge."],
  "Ek academy owner har mahine WhatsApp pe fees chase karta tha. Kuch parents late, kuch bhool gaye, aur record sab ka alag.",
  ["Enrolment form: parent aur student ki details ek hi jagah", "Auto fee reminder: har parent ko time pe message",
   "Ek screen: paid, due, late"],
  '#academyowner #tuitioncentre #feemanagement #educationbusiness #thetotalforge', 'Aap abhi fees ka record kaise rakhte hain, aur taqreeban kitne students hain?', 'form+chat+board')

B('b07', 'Shop owner', 'STOCK', 'Shops: counter stock and online stock never match',
  ["Shop mein cheez bik gayi, par online abhi bhi available hai.",
   "Ek shop owner ne last piece counter pe bech diya. Online customer ne wahi order kar diya, aur refund dena pada.",
   "Stock do jagah alag chale, toh scene bigadna hi hai.",
   BRIDGE,
   "One. Ek stock screen jahan shop aur online ka stock saath dikhta hai.",
   "Two. A low-stock alert, so you reorder before it runs out.",
   "Three. A daily sales report, so you know what sold.",
   "Result? Stock mismatch khatam, aur refund ki tension bhi.",
   "Want this for your shop? Comment STOCK, hum aapko DM kar denge."],
  "Ek shop owner ne last piece counter pe bech diya. Online customer ne wahi order kar diya, aur refund dena pada.",
  ["Stock screen: shop aur online ka stock ek saath", "Low-stock alert: khatam hone se pehle reorder",
   "Daily sales report: kya bika, ek nazar mein"],
  '#shopowner #retailbusiness #inventorymanagement #smallbusinesspakistan #thetotalforge', 'Aap abhi stock ka record kaise rakhte hain, aur kya shop ke ilawa online bhi bechte hain?', 'form+chat+board')
