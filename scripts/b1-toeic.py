# Banque de l'examen blanc TOEIC B1 (content/exams/b1-toeic.json), format Listening & Reading abrégé.
# Écoute 16 questions (parties 1 à 4, dont 2 photos), phrases et textes à compléter 16 (parties 5 et 6), compréhension écrite 10 (partie 7).
# Le premier choix est la bonne réponse. Usage : python3 scripts/b1-toeic.py
from en_toeic import *

NOTICE = 'NOTICE TO ALL STAFF\nThe annual staff survey has been extended until Friday 9 May. So far, only 40% of employees have completed it. The survey takes about fifteen minutes and all answers are anonymous. Results will be presented at the staff meeting in June. If you have any questions, please contact Helen Moss in Human Resources.'
EMAIL = 'From: Oliver Grant\nTo: Priya Shah\nSubject: Delivery problem\n\nDear Ms Shah,\nI am writing about order 4471, which was delivered to our Plymouth office yesterday. Unfortunately, six of the twenty chairs had been damaged during transport. I have attached some photos. I would be grateful if you could replace the damaged chairs as soon as possible, as we are opening the new office on 2 June.\nKind regards,\nOliver Grant\nOffice Manager, Avalon & Co.'
REPLY = 'From: Priya Shah\nTo: Oliver Grant\nSubject: RE: Delivery problem\n\nDear Mr Grant,\nThank you for your email and the photos. I apologise for the inconvenience. Six new chairs will be shipped from our warehouse on Monday and should arrive on Wednesday. Our driver will collect the damaged chairs at the same time. There will be no extra charge.\nBest regards,\nPriya Shah\nCustomer Service, Kernow Furniture'
JOB = 'JOB VACANCY: Marketing Assistant\nAvalon & Co. is looking for a marketing assistant to join its team in Truro. The successful candidate will help organise events and write content for our website. At least one year of experience is required. Applicants should be organised and able to work in a team. To apply, send your CV and a cover letter to jobs@avalon.co.uk by 30 April. Interviews will be held in the second week of May.'

PARTS = [
  P1(2, PHOTOS_HARD),
  P2(5, [
    LQ('M|How long have you been working on the report?', ['Since nine this morning.', 'It’s a long report.', 'I’ll work on it later.']),
    LQ('F|Has the contract been signed yet?', ['Yes, the client signed it yesterday.', 'I signed up for the gym.', 'It’s a two-year contract, isn’t it?']),
    LQ('M|Could you tell me where the conference room is?', ['It’s on the third floor, on the left.', 'Yes, I could.', 'The conference starts at ten.']),
    LQ('F|Why was the meeting postponed?', ['The director is ill.', 'It was in room four.', 'Next Thursday, I think.']),
    LQ('M|Would you like me to call the supplier?', ['That would be great, thanks.', 'I like the supplier.', 'Yes, he called me.']),
    LQ('F|You’ve met Mr Ambrose before, haven’t you?', ['Yes, at the trade fair last year.', 'No, he hasn’t met.', 'I’ll meet you there.']),
    LQ('M|What would you do if you were the manager?', ['I’d hire more staff.', 'I was the manager.', 'I do it every day.']),
    LQ('F|Who should I send the invoice to?', ['To the accounts department.', 'Yes, send it today.', 'It was sent by post.']),
    LQ('M|Didn’t you use to work in Bristol?', ['Yes, for about five years.', 'I’m used to it.', 'No, I don’t work.']),
  ]),
  P3(5, [
    LQ('F|Hello, I’m calling about the printer I ordered. It arrived yesterday, but it doesn’t work.\nM|I’m very sorry about that. Do you have your order number?\nF|Yes, it’s 6638.\nM|Thank you. We’ll send you a replacement today.', ['Send a new printer.', 'Give a full refund.', 'Repair the printer.', 'Call back later.'], text='What will the man do?'),
    LQ('M|Have you seen Kate? I need to ask her about the budget.\nF|She must be at lunch. Her coat isn’t here.\nM|OK, I’ll send her an email instead.', ['She is probably at lunch.', 'She is on holiday.', 'She is in a meeting.', 'She has gone home.'], text='What does the woman think about Kate?'),
    LQ('F|I’ve been looking at the sales figures. They’re lower than last quarter.\nM|That’s because the new shop opened late. It should improve next month.\nF|I hope so. Let’s discuss it on Friday.', ['A shop opened late.', 'Prices went up.', 'A product was recalled.', 'The staff were on strike.'], text='Why were sales lower?'),
    LQ('M|I’m applying for the sales manager position.\nF|Really? You’d be great at it. When is the interview?\nM|Next Tuesday, if my application is accepted.', ['Applying for a job.', 'Organising a party.', 'Buying a car.', 'Moving house.'], text='What is the man doing?'),
    LQ('F|Could you put me through to Mr Lee, please?\nM|I’m afraid he’s in a meeting until three. Would you like to leave a message?\nF|Yes, please ask him to call Anna Brooks.', ['He is in a meeting.', 'He is on holiday.', 'He has left the company.', 'He is on another call.'], text='Why can’t Mr Lee take the call?'),
    LQ('M|We could lower the price by 5%, provided that you order 2,000 units.\nF|That’s more than we need. How about 1,500?\nM|Let me check with my manager.', ['The number of units.', 'The delivery date.', 'The colour of the product.', 'The payment method.'], text='What are the speakers discussing?'),
    LQ('F|When I got to the station, the train had already left.\nM|Oh no. What did you do?\nF|I took a taxi, but I was still twenty minutes late.', ['She took a taxi.', 'She waited for the next train.', 'She went home.', 'She called a colleague.'], text='What did the woman do after missing the train?'),
  ]),
  P4(4, [
    LQ('N|Attention, please. Flight BA 282 to Boston has been delayed because of a technical problem. Passengers are asked to wait in the departure lounge. A new departure time will be announced at four o’clock. We apologise for the inconvenience.', ['Wait in the departure lounge.', 'Go to gate twelve.', 'Collect their luggage.', 'Book a new flight.'], text='What are passengers asked to do?'),
    LQ('N|Good afternoon, everyone. Before we start, I’d like to remind you that the office will be closed on Monday for the bank holiday. Also, the new security cards must be collected from reception by Friday.', ['Collect a security card.', 'Work on Monday.', 'Attend a training course.', 'Send a report.'], text='What must staff do by Friday?'),
    LQ('N|Hi Tom, it’s Sarah from Kernow Furniture. I’m calling about your order. I’m afraid the blue sofa is out of stock, but we could deliver a grey one next week. If you’d prefer to wait for the blue one, it should be available in a month. Please call me back on 01872 554 210.', ['A product is out of stock.', 'The delivery is cancelled.', 'The price has gone up.', 'The order was lost.'], text='Why is Sarah calling?'),
    LQ('N|Welcome to Tintagel Castle. The castle was built in the thirteenth century and, according to legend, it was the birthplace of King Arthur. The tour lasts about an hour. Please stay on the paths, as the cliffs can be dangerous.', ['Stay on the paths.', 'Take photos.', 'Keep their tickets.', 'Wear warm clothes.'], text='What does the speaker ask visitors to do?'),
    LQ('N|And now the business news. Sales at the supermarket chain Fresco have increased by 8% this year, despite higher prices. The company plans to open twenty new stores, which will create about five hundred jobs.', ['Open new stores.', 'Lower its prices.', 'Close some stores.', 'Sell the company.'], text='What does Fresco plan to do?'),
    LQ('N|Thank you for calling Avalon & Co. Our office is closed at the moment. Our opening hours are from eight thirty to five thirty, Monday to Friday. If you are calling about a delivery, please visit our website, where you can track your order.', ['Visit the website.', 'Press one.', 'Call back on Saturday.', 'Send a fax.'], text='What should callers about deliveries do?'),
  ]),
  P5(11, [
    RQ(['been', 'being', 'be', 'was'], jp='Our team has ＿ working on the new website since January.'),
    RQ(['had', 'has', 'have', 'was'], jp='When Ms Hall arrived at the airport, her flight ＿ already left.'),
    RQ(['used to', 'is used to', 'use to', 'using to'], jp='Mr Price ＿ work in a bank before he joined our company.'),
    RQ(['were', 'are', 'will be', 'have been'], jp='If I ＿ you, I would accept the offer.'),
    RQ(['be', 'been', 'being', 'to be'], jp='All expense forms must ＿ approved by a manager.'),
    RQ(['was', 'is', 'has', 'were'], jp='The new factory ＿ opened by the mayor last week.'),
    RQ(['Although', 'Despite', 'However', 'Because of'], jp='＿ the flight was delayed, we arrived on time for the meeting.'),
    RQ(['despite', 'although', 'even', 'however'], jp='Sales increased ＿ the difficult economic situation.'),
    RQ(['if', 'that', 'what', 'when'], jp='The customer asked ＿ the price included delivery.'),
    RQ(['to call', 'calling', 'call', 'called'], jp='Ms Shah told me ＿ her back after lunch.'),
    RQ(['must', 'can’t', 'mustn’t', 'would'], jp='Mr Lee isn’t in his office. He ＿ be at the trade fair.'),
    RQ(['in order to', 'so that', 'because', 'such'], jp='We changed suppliers ＿ reduce our costs.'),
    RQ(['such', 'so', 'too', 'very'], jp='It was ＿ a successful event that we will repeat it next year.'),
    RQ(['opens', 'does open', 'open', 'is open'], jp='Could you tell me what time the bank ＿?'),
    RQ(['isn’t it', 'is it', 'doesn’t it', 'wasn’t it'], jp='The deadline is next Friday, ＿?'),
  ]),
  P6(5, [
    RQ(['has been', 'was', 'is being', 'will'], passage=NOTICE.replace('has been extended', '＿ extended'), text='Choose the words for the blank.'),
    RQ(['have completed', 'completed', 'are completing', 'will complete'], passage=NOTICE.replace('have completed', '＿'), text='Choose the words for the blank.'),
    RQ(['had been', 'have been', 'are', 'were being'], passage=EMAIL.replace('had been damaged', '＿ damaged'), text='Choose the words for the blank.'),
    RQ(['grateful', 'thanking', 'pleasant', 'glad of'], passage=EMAIL.replace('be grateful', 'be ＿'), text='Choose the word for the blank.'),
    RQ(['will be shipped', 'shipped', 'have shipped', 'are shipping'], passage=REPLY.replace('will be shipped', '＿'), text='Choose the words for the blank.'),
    RQ(['apologise', 'complain', 'regret to', 'excuse'], passage=REPLY.replace('I apologise', 'I ＿'), text='Choose the word for the blank.'),
    RQ(['required', 'requiring', 'require', 'requires'], passage=JOB.replace('is required', 'is ＿'), text='Choose the word for the blank.'),
  ]),
  P7(10, [
    RQ(['Until Friday 9 May.', 'Until the end of June.', 'Until 30 April.', 'Until next Monday.'], passage=NOTICE, text='Until when can staff complete the survey?'),
    RQ(['They are anonymous.', 'They are published online.', 'They are sent to managers.', 'They are checked by Helen Moss.'], passage=NOTICE, text='What is said about the survey answers?'),
    RQ(['Not enough staff have completed it.', 'There were technical problems.', 'Helen Moss is on holiday.', 'The questions were changed.'], passage=NOTICE, text='Why has the survey probably been extended?'),
    RQ(['Some chairs were damaged.', 'The order was late.', 'The wrong chairs were sent.', 'The invoice was wrong.'], passage=EMAIL, text='Why did Oliver Grant write to Ms Shah?'),
    RQ(['Six.', 'Twenty.', 'Fourteen.', 'Two.'], passage=EMAIL, text='How many chairs were damaged?'),
    RQ(['A new office is opening.', 'A client is visiting.', 'The staff are moving to Plymouth.', 'The chairs are a gift.'], passage=EMAIL, text='Why does Mr Grant need the chairs quickly?'),
    RQ(['On Wednesday.', 'On Monday.', 'On 2 June.', 'Yesterday.'], passage=REPLY, text='When should the new chairs arrive?'),
    RQ(['Nothing extra.', 'The cost of transport.', 'Half the price.', 'The full price.'], passage=REPLY, text='How much will Avalon & Co. pay for the new chairs?'),
    RQ(['Organise events.', 'Repair computers.', 'Manage the accounts.', 'Drive the delivery van.'], passage=JOB, text='What is one task of the marketing assistant?'),
    RQ(['One year of experience.', 'A university degree.', 'A driving licence.', 'Three languages.'], passage=JOB, text='What is required for the job?'),
    RQ(['By 30 April.', 'In the second week of May.', 'By Friday 9 May.', 'In June.'], passage=JOB, text='When must applications be sent?'),
    RQ(['In Truro.', 'In Plymouth.', 'In Bristol.', 'In London.'], passage=JOB, text='Where is the job?'),
  ]),
]
write_bank('B1', PARTS, (16, 16, 10))
