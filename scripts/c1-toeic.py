# Banque de l'examen blanc TOEIC C1 (content/exams/c1-toeic.json), format Listening & Reading abrégé.
# Écoute 18 questions (parties 2 à 4), phrases et textes à compléter 20 (parties 5 et 6), compréhension écrite 14 (partie 7).
# Le premier choix est la bonne réponse. Usage : python3 scripts/c1-toeic.py
from en_toeic import *

POLICY = 'AVALON & CO. - REMOTE WORKING POLICY (REVISED)\nFollowing a review carried out in the spring, the board has approved a revised remote working policy, which will come into effect on 1 March. Employees may work remotely for up to three days per week, subject to their manager’s approval. It is essential that all staff be available during core hours, from 10 a.m. to 3 p.m. Equipment provided by the company remains its property and must be returned should the employee leave. Requests for exceptions should be submitted in writing to Human Resources.'
REPORT = 'Annual Sustainability Report - Summary\nOver the past year, the Group has reduced its carbon emissions by 18%, albeit slightly short of its 20% target. This reduction was largely achieved through the transition to renewable energy at our two Scottish plants. Packaging waste, on the other hand, rose by 4%, owing to a sharp increase in online orders. Given that e-commerce is likely to keep growing, the Group intends to introduce reusable packaging by the end of next year. Had the new logistics centre opened on schedule, the overall results would arguably have been stronger.'
LETTER = 'Dear Ms Campbell,\nFurther to our telephone conversation of 12 June, I am writing to confirm the terms we discussed. Kernow Logistics will handle all deliveries in the south-west for an initial period of two years, at a rate of 4.20 pounds per parcel. Should volumes exceed 10,000 parcels per month, this rate will be reduced to 3.90 pounds. Please find enclosed two copies of the contract. I would be grateful if you could sign both and return one to us by 30 June.\nYours sincerely,\nAlistair Reid\nCommercial Director'
EMAIL = 'From: Mairi Fraser\nTo: Alistair Reid\nSubject: RE: Contract\n\nAlistair,\nThank you for sending the contract so promptly. Having gone through it with our legal team, we are happy with the terms, with one exception: clause 9 states that either party may terminate the agreement with one month’s notice. Given the investment we will be making, we would rather the notice period were three months. Provided you can agree to this change, we will sign immediately.\nBest regards,\nMairi'

PARTS = [
  P2(6, [
    LQ('M|Should the client call while I’m out, could you take a message?', ['Of course, I’ll make a note of it.', 'Yes, he should call.', 'I was out yesterday.']),
    LQ('F|Had you heard about the merger before it was announced?', ['Only rumours, nothing official.', 'I hear it every day.', 'It will be announced soon.']),
    LQ('M|Isn’t it time we updated the website?', ['Absolutely, it looks very outdated.', 'It’s ten past three.', 'I visited it yesterday.']),
    LQ('F|Why was the launch called off?', ['The supplier deal fell through.', 'It was called on Monday.', 'Because I launched it.']),
    LQ('M|Would you rather I sent the figures now or after the meeting?', ['Now would be better, thanks.', 'I’d rather the meeting.', 'The figures are correct.']),
    LQ('F|Who’s going to draw up the new contract?', ['Our lawyers are working on it.', 'I drew a picture.', 'It’s a two-year contract.']),
    LQ('M|Do you think the deal is likely to go ahead?', ['It’s hard to say at this stage.', 'Yes, go ahead and sit down.', 'It went ahead last year.']),
    LQ('F|Hardly anyone came to the presentation, did they?', ['No, it clashed with the board meeting.', 'Yes, it was hard.', 'I presented it well.']),
    LQ('M|What would it take for you to sign today?', ['A slightly longer payment period.', 'It takes about an hour.', 'I signed it yesterday.']),
    LQ('F|Has the warranty expired on this printer?', ['I’ll check the purchase date.', 'It prints very well.', 'Yes, I bought ink.']),
  ]),
  P3(7, [
    LQ('M|Had we brought the launch forward, we would have beaten our competitors to market.\nF|True, but we couldn’t have guaranteed the quality. Cutting corners would have damaged our reputation.\nM|I suppose you’re right.', ['Protecting the company’s reputation.', 'Reducing costs.', 'Hiring more staff.', 'Changing suppliers.'], text='What is the woman most concerned about?'),
    LQ('F|I’ve gone through the contract and clause 9 is a problem. One month’s notice is far too short.\nM|Would they accept two months?\nF|Possibly, but I’d rather we asked for three and met them halfway if necessary.', ['Ask for three months’ notice.', 'Accept one month’s notice.', 'Cancel the contract.', 'Hire a new lawyer.'], text='What does the woman want to do?'),
    LQ('M|Morale has been low since the restructuring. People feel they’re not being consulted.\nF|Then it’s high time we involved them. Why don’t we hold a series of workshops?\nM|That’s a good idea. I’ll draw up a schedule.', ['Low staff morale.', 'A drop in sales.', 'A delayed project.', 'A shortage of equipment.'], text='What problem are the speakers discussing?'),
    LQ('F|Our carbon emissions fell by 18%, albeit short of our target.\nM|Packaging waste went up, though, didn’t it?\nF|Yes, owing to online orders. We’re looking into reusable packaging.', ['Online orders increased.', 'A factory closed.', 'Suppliers changed.', 'Prices rose.'], text='Why did packaging waste increase?'),
    LQ('M|Given the delays, it’s unlikely the new centre will open before March.\nF|In that case, we should warn our major clients now rather than later.\nM|Agreed. I’ll ask the communications team to draft a message.', ['Inform major clients.', 'Open the centre in January.', 'Hire extra staff.', 'Cancel the project.'], text='What do the speakers decide to do?'),
    LQ('F|I’m afraid the conference room is being renovated, so the workshop will have to take place elsewhere.\nM|What about the hotel next door? They have meeting facilities.\nF|Good thinking. I’ll inquire about availability.', ['Contact the hotel.', 'Postpone the workshop.', 'Renovate the room.', 'Hold the workshop online.'], text='What will the woman do next?'),
    LQ('M|So successful was the trial that the client wants to roll the system out across all its sites.\nF|That’s fantastic news. Do we have the capacity?\nM|Not yet. We’ll need to recruit at least five engineers.', ['Recruit more engineers.', 'Reduce the price.', 'Repeat the trial.', 'Find a new client.'], text='What will the company need to do?'),
  ]),
  P4(5, [
    LQ('N|Good morning. I’d like to begin by thanking you all for your hard work this year. Admittedly, it has not been easy: the loss of our largest client was a serious blow. Having said that, we have not only replaced that business but grown by 6%. What we need now is to consolidate these gains.', ['The company has grown despite losing a client.', 'The company has lost money.', 'A new director has been appointed.', 'The staff will receive a bonus.'], text='What is the main point of the talk?'),
    LQ('N|This is a recorded message from Highland Rail. Due to unforeseen circumstances, services between Inverness and Thurso are suspended until further notice. Replacement buses will run from outside the station. Passengers holding advance tickets may claim a full refund. We apologise for any inconvenience.', ['Claim a refund.', 'Travel on another day.', 'Exchange their tickets.', 'Wait in the station.'], text='What may passengers with advance tickets do?'),
    LQ('N|Welcome to this afternoon’s session. Over the next forty minutes, I’ll be looking at how companies can reduce their carbon footprint without hurting profits. I’ll start with a brief overview, then move on to three case studies. Should you have any questions, please hold them until the end.', ['Wait until the end to ask questions.', 'Introduce themselves.', 'Read the case studies.', 'Switch off their phones.'], text='What does the speaker ask the audience to do?'),
    LQ('N|Hi Alistair, it’s Mairi. I’ve just come out of the meeting with our legal team. Provided you can extend the notice period to three months, we’ll sign this week. Otherwise, I’m afraid the deal is unlikely to go ahead. Let me know what you think.', ['Extend the notice period.', 'Lower the price.', 'Meet the legal team.', 'Sign immediately.'], text='What does Mairi want Alistair to do?'),
    LQ('N|And in business news, shares in Draig Systems rose by 12% today after the company announced record profits. Analysts say the firm is bound to attract interest from foreign investors, although its chief executive insists that it has no plans to sell.', ['Its share price rose.', 'It was taken over.', 'Its profits fell.', 'Its chief executive resigned.'], text='What happened to Draig Systems today?'),
    LQ('N|Attention, all staff. As part of our new safety procedures, it is essential that everyone attend a fire drill on Thursday at 11 a.m. When the alarm sounds, please leave the building by the nearest exit and gather in the car park. Under no circumstances should you use the lifts.', ['Use the lifts.', 'Leave by the nearest exit.', 'Gather in the car park.', 'Attend the fire drill.'], text='What are staff told NOT to do?'),
  ]),
  P5(15, [
    RQ(['Should', 'Would', 'Had', 'Were'], jp='＿ you need any further information, please do not hesitate to contact us.'),
    RQ(['Had', 'Should', 'Were', 'Did'], jp='＿ the shipment arrived on time, we would not have lost the contract.'),
    RQ(['to', 'for', 'that', 'and'], jp='Were the company ＿ relocate to Glasgow, many employees would leave.'),
    RQ(['But for', 'Unless', 'Otherwise', 'In case'], jp='＿ the strong pound, our exports would have increased significantly.'),
    RQ(['in case', 'unless', 'provided', 'whereas'], jp='Please keep a printed copy of your ticket ＿ the app does not work.'),
    RQ(['attend', 'attends', 'attended', 'will attend'], jp='The committee recommends that every manager ＿ the leadership course.'),
    RQ(['be', 'is', 'are', 'being'], jp='It is imperative that all personal data ＿ stored securely.'),
    RQ(['replaced', 'replace', 'will replace', 'have replaced'], jp='It is high time we ＿ the outdated software.'),
    RQ(['Having reviewed', 'Reviewed', 'To review', 'Having review'], jp='＿ your application, we are pleased to offer you an interview.'),
    RQ(['hence', 'whereby', 'albeit', 'whereas'], jp='Demand has fallen sharply; ＿ the decision to reduce production.'),
    RQ(['albeit', 'hence', 'despite', 'whereby'], jp='The campaign was a success, ＿ a costly one.'),
    RQ(['whereby', 'whereas', 'wherever', 'hence'], jp='We have introduced a scheme ＿ employees can buy shares at a discount.'),
    RQ(['did we realise', 'we realised', 'we did realise', 'realised we'], jp='Only after the audit ＿ how serious the problem was.'),
    RQ(['than', 'when', 'then', 'that'], jp='No sooner had the product been launched ＿ orders started pouring in.'),
    RQ(['likely', 'probably', 'likelihood', 'possibly'], jp='Interest rates are ＿ to remain high for the rest of the year.'),
    RQ(['affect', 'effect', 'afflict', 'effective'], jp='The new regulations will ＿ small businesses in particular.'),
    RQ(['comply', 'respect', 'agree', 'conform'], jp='All suppliers must ＿ with our code of conduct.'),
    RQ(['implementation', 'implement', 'implementing', 'implemented'], jp='The ＿ of the new system will take approximately six months.'),
  ]),
  P6(5, [
    RQ(['which', 'who', 'what', 'whose'], passage=POLICY.replace('policy, which', 'policy, ＿'), text='Choose the word for the blank.'),
    RQ(['subject', 'object', 'according', 'due'], passage=POLICY.replace('subject to their', '＿ to their'), text='Choose the word for the blank.'),
    RQ(['be', 'are', 'will be', 'being'], passage=POLICY.replace('all staff be available', 'all staff ＿ available'), text='Choose the word for the blank.'),
    RQ(['albeit', 'despite', 'hence', 'although of'], passage=REPORT.replace('18%, albeit', '18%, ＿'), text='Choose the word for the blank.'),
    RQ(['owing', 'because', 'thanks', 'given'], passage=REPORT.replace('owing to a sharp', '＿ to a sharp'), text='Choose the word for the blank.'),
    RQ(['Should', 'Would', 'Unless', 'Provided'], passage=LETTER.replace('Should volumes', '＿ volumes'), text='Choose the word for the blank.'),
    RQ(['Having', 'Have', 'Had', 'Being'], passage=EMAIL.replace('Having gone through', '＿ gone through'), text='Choose the word for the blank.'),
    RQ(['were', 'is', 'will be', 'be'], passage=EMAIL.replace('period were three', 'period ＿ three'), text='Choose the word for the blank.'),
  ]),
  P7(14, [
    RQ(['Up to three days per week.', 'Five days per week.', 'Only on Fridays.', 'Two days per month.'], passage=POLICY, text='How often may employees work remotely?'),
    RQ(['From 10 a.m. to 3 p.m.', 'From 9 a.m. to 5 p.m.', 'All day.', 'In the mornings only.'], passage=POLICY, text='When must staff be available?'),
    RQ(['It must be returned.', 'It may be kept.', 'It must be paid for.', 'It will be sold.'], passage=POLICY, text='What happens to company equipment if an employee leaves?'),
    RQ(['In writing to Human Resources.', 'By phone to their manager.', 'At a staff meeting.', 'Online to the board.'], passage=POLICY, text='How should requests for exceptions be made?'),
    RQ(['It almost reached its target.', 'It exceeded its target.', 'It failed completely.', 'It did not set a target.'], passage=REPORT, text='What is said about the reduction in carbon emissions?'),
    RQ(['Switching to renewable energy.', 'Closing factories.', 'Reducing online sales.', 'Buying new vehicles.'], passage=REPORT, text='How was the reduction mainly achieved?'),
    RQ(['Introduce reusable packaging.', 'Stop selling online.', 'Open a new plant in Scotland.', 'Raise prices.'], passage=REPORT, text='What does the Group plan to do?'),
    RQ(['It did not open on time.', 'It was too expensive.', 'It closed last year.', 'It is in Scotland.'], passage=REPORT, text='What is implied about the new logistics centre?'),
    RQ(['To confirm an agreement.', 'To complain about a delivery.', 'To request a meeting.', 'To cancel a contract.'], passage=LETTER, text='Why did Alistair Reid write to Ms Campbell?'),
    RQ(['3.90 pounds.', '4.20 pounds.', '10 pounds.', '2 pounds.'], passage=LETTER, text='What will the rate be if volumes exceed 10,000 parcels a month?'),
    RQ(['Sign both copies and return one.', 'Call Mr Reid.', 'Send a cheque.', 'Visit the warehouse.'], passage=LETTER, text='What is Ms Campbell asked to do?'),
    RQ(['The notice period.', 'The price per parcel.', 'The length of the contract.', 'The delivery area.'], passage=EMAIL, text='What does Mairi want to change?'),
    RQ(['Because of the investment involved.', 'Because of a legal error.', 'Because prices have risen.', 'Because the contract is too long.'], passage=EMAIL, text='Why does Mairi request the change?'),
    RQ(['She will sign immediately.', 'She will look for another supplier.', 'She will call a meeting.', 'She will ask for a discount.'], passage=EMAIL, text='What will Mairi do if the change is accepted?'),
    RQ(['Two years.', 'One month.', 'Three months.', 'One year.'], passage=LETTER, text='How long is the initial period of the agreement?'),
  ]),
]
write_bank('C1', PARTS, (18, 20, 14))
