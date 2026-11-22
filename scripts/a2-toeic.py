# Banque de l'examen blanc TOEIC A2 (content/exams/a2-toeic.json), format Listening & Reading abrégé.
# Écoute 12 questions (parties 2 à 4), phrases et textes à compléter 14 (parties 5 et 6), compréhension écrite 8 (partie 7).
# Le premier choix est la bonne réponse. Usage : python3 scripts/a2-toeic.py
from en_toeic import *

MEMO = 'MEMO\nTo: All staff\nFrom: Facilities\nThe car park will be closed on Saturday 14 June for repairs. Staff who have to work that day should use the public car park on King Street. The company will pay for parking. Please keep your receipt and give it to Sarah in accounts by the end of the month.'
EMAIL = 'From: Daniel Price\nTo: Laura Evans\nSubject: Visit to Leeds\n\nHi Laura,\nI’ve just booked the hotel for our visit to the Leeds factory. We’re staying at the Park Hotel, which is ten minutes from the factory. The train leaves at 7.40 on Tuesday, so we should meet at the station at 7.15. I haven’t received the visitor badges yet, but I’ll call the factory this afternoon.\nDaniel'
AD = 'SPRING SALE at HOMESTYLE\nAll sofas: 30% off\nChairs and tables: buy two, get one free\nFree delivery on orders over £300\nSale ends Sunday 23 March. Not valid online.'

PARTS = [
  P2(5, [
    LQ('M|Have you finished the report yet?', ['Not yet, but I’ll send it tonight.', 'Yes, it’s a good report card.', 'I finish at six every day.']),
    LQ('F|How long have you worked here?', ['For about three years.', 'Since three hours ago.', 'It’s a long way.']),
    LQ('M|Which hotel is the cheapest?', ['The one near the station.', 'Yes, it’s cheaper.', 'At nine o’clock.']),
    LQ('F|Are you free on Thursday morning?', ['Sorry, I’m meeting a client then.', 'Yes, it’s free of charge.', 'I was free yesterday.']),
    LQ('M|What were you doing when I called?', ['I was driving to work.', 'I drive to work.', 'I’ll drive to work.']),
    LQ('F|Should I bring my laptop to the meeting?', ['Yes, you’ll need it for the slides.', 'No, it was in the meeting.', 'It’s a light laptop.']),
    LQ('M|Whose coat is this?', ['I think it’s Emma’s.', 'It’s a warm coat.', 'Who is it?']),
    LQ('F|Would you mind closing the window?', ['Not at all.', 'Yes, it’s closed.', 'I don’t mind the window.']),
  ]),
  P3(4, [
    LQ('F|Hi, I’d like to check in. I have a booking under the name Evans.\nM|Welcome, Ms Evans. You’re in room 305. Breakfast is from seven to ten.\nF|Thank you. Is there a lift?\nM|Yes, just behind you.', ['At a hotel.', 'At a station.', 'In a restaurant.', 'At an airport.'], text='Where does the conversation take place?'),
    LQ('M|I’m afraid the printer on the second floor isn’t working again.\nF|Oh no. I have to print the contract before eleven.\nM|You can use the one in the meeting room.', ['Use the printer in the meeting room.', 'Buy a new printer.', 'Send the contract by email.', 'Wait until eleven.'], text='What does the man suggest?'),
    LQ('F|Did you go to the conference in Bristol?\nM|Yes, it was much bigger than last year. There were a lot of people.\nF|Was it interesting?\nM|Very. I met some new clients.', ['It was bigger than last year.', 'It was cancelled.', 'It was in London.', 'It was very short.'], text='What does the man say about the conference?'),
    LQ('M|Are you going to take the train to Glasgow?\nF|No, I’m going to fly. It’s faster, and today the tickets are cheaper than the train.\nM|Good idea.', ['By plane.', 'By train.', 'By car.', 'By bus.'], text='How will the woman travel to Glasgow?'),
    LQ('F|What’s the matter, Tom?\nM|I’ve got a terrible headache.\nF|You should go home and rest. I’ll tell the manager.', ['He has a headache.', 'He lost his keys.', 'He missed the train.', 'He is late.'], text='What is the man’s problem?'),
    LQ('M|How often do you have team meetings?\nF|Once a week, usually on Monday mornings.\nM|That’s the same in our department.', ['Once a week.', 'Twice a week.', 'Every day.', 'Once a month.'], text='How often does the woman’s team meet?'),
  ]),
  P4(3, [
    LQ('N|Good morning, passengers. Because of the snow, the 8.20 train to York is delayed by forty minutes. We are very sorry for the delay. Hot drinks are free in the station cafe.', ['Because of the snow.', 'Because of a strike.', 'Because the driver is ill.', 'Because of repairs.'], text='Why is the train delayed?'),
    LQ('N|Welcome to the Science Museum. Please note that you must not take photos in the space gallery. The museum cafe is on the ground floor, and the shop closes at five thirty.', ['Take photos in the space gallery.', 'Eat in the cafe.', 'Visit the shop.', 'Go to the ground floor.'], text='What are visitors not allowed to do?'),
    LQ('N|Hi Laura, it’s Daniel. I’ve just spoken to the factory. Our badges will be ready at the reception desk when we arrive. Also, the meeting with the director is now at two, not at eleven. See you at the station!', ['The time of a meeting.', 'The name of the hotel.', 'The price of the tickets.', 'The train station.'], text='What has changed?'),
    LQ('N|Thank you for calling City Bank. Our offices are open from nine to five, Monday to Friday. If you have lost your card, please press one. For all other questions, please stay on the line.', ['Press one.', 'Call back on Monday.', 'Send an email.', 'Visit the office.'], text='What should callers do if they have lost their card?'),
    LQ('N|Tonight’s weather: it will be cold and windy in the north, with snow on the hills. In the south, it will be cloudy but dry. Tomorrow will be sunnier everywhere.', ['Sunnier.', 'Colder.', 'Wetter.', 'Windier.'], text='What will the weather be like tomorrow?'),
  ]),
  P5(10, [
    RQ(['was', 'were', 'is', 'has'], jp='When the manager arrived, Ms Lee ＿ talking to a customer.'),
    RQ(['cheaper', 'cheap', 'cheapest', 'more cheap'], jp='The new supplier is ＿ than the old one.'),
    RQ(['most', 'more', 'much', 'many'], jp='This is the ＿ popular product in our catalogue.'),
    RQ(['since', 'for', 'during', 'from'], jp='Mr Okafor has worked for the company ＿ 2018.'),
    RQ(['yet', 'already', 'still', 'just'], jp='We haven’t received the invoice ＿.'),
    RQ(['must', 'should to', 'have', 'can to'], jp='All visitors ＿ sign in at the reception desk.'),
    RQ(['carefully', 'careful', 'care', 'caring'], jp='Please check the figures ＿ before you send the report.'),
    RQ(['few', 'little', 'much', 'any'], jp='There are only a ＿ seats left on the morning flight.'),
    RQ(['rains', 'will rain', 'rained', 'raining'], jp='If it ＿ tomorrow, the garden party will move indoors.'),
    RQ(['meeting', 'to meet', 'meet', 'met'], jp='We look forward to ＿ you at the conference.'),
    RQ(['who', 'which', 'where', 'whose'], jp='The engineer ＿ fixed the machine is from our Leeds office.'),
    RQ(['going', 'go', 'will', 'goes'], jp='The company is ＿ to open two new stores next year.'),
    RQ(['too', 'enough', 'very', 'so much'], jp='The meeting room is ＿ small for thirty people.'),
    RQ(['to change', 'changing', 'change', 'changed'], jp='Ms Brown has decided ＿ her travel plans.'),
  ]),
  P6(4, [
    RQ(['should', 'must not', 'doesn’t have to', 'won’t'], passage=MEMO.replace('should use', '＿ use'), text='Choose the word or phrase for the blank.'),
    RQ(['which', 'who', 'where', 'whose'], passage=EMAIL.replace('Park Hotel, which', 'Park Hotel, ＿'), text='Choose the word for the blank.'),
    RQ(['yet', 'already', 'ago', 'since'], passage=EMAIL.replace('badges yet', 'badges ＿'), text='Choose the word for the blank.'),
    RQ(['free', 'cheap', 'expensive', 'paid'], passage=AD.replace('Free delivery', '＿ delivery').replace('get one free', 'get one free'), text='Choose the word for the blank.'),
    RQ(['have been', 'was', 'am', 'went'], passage='Dear Mr Hall,\nThank you for your letter. I ＿ a customer of your bank for ten years, and I have never had a problem until now. Last week, my card stopped working while I was paying at a shop.\nYours sincerely,\nPeter Grant', text='Choose the words for the blank.'),
    RQ(['while', 'when', 'during', 'since'], passage='Dear Mr Hall,\nThank you for your letter. I have been a customer of your bank for ten years, and I have never had a problem until now. Last week, my card stopped working ＿ I was paying at a shop.\nYours sincerely,\nPeter Grant', text='Choose the word for the blank.'),
  ]),
  P7(8, [
    RQ(['Use the car park on King Street.', 'Stay at home.', 'Come by train.', 'Park in front of the office.'], passage=MEMO, text='What should staff who work on Saturday do?'),
    RQ(['Give it to Sarah.', 'Keep it at home.', 'Send it to Facilities.', 'Throw it away.'], passage=MEMO, text='What should staff do with their parking receipt?'),
    RQ(['At 7.15.', 'At 7.40.', 'At 10.00.', 'On Monday.'], passage=EMAIL, text='When should Laura meet Daniel?'),
    RQ(['Call the factory.', 'Book the hotel.', 'Buy the train tickets.', 'Meet the director.'], passage=EMAIL, text='What will Daniel do this afternoon?'),
    RQ(['It is close to the factory.', 'It has a swimming pool.', 'It is next to the station.', 'It is very cheap.'], passage=EMAIL, text='What does Daniel say about the Park Hotel?'),
    RQ(['30% off.', '50% off.', 'Free delivery.', 'One free chair.'], passage=AD, text='What is the discount on sofas?'),
    RQ(['Online.', 'In the shop.', 'On Saturday.', 'Before Sunday.'], passage=AD, text='Where is the sale offer NOT valid?'),
    RQ(['His card stopped working.', 'He lost his card.', 'He changed his bank.', 'He moved house.'], passage='Dear Mr Hall,\nThank you for your letter. I have been a customer of your bank for ten years, and I have never had a problem until now. Last week, my card stopped working while I was paying at a shop.\nYours sincerely,\nPeter Grant', text='What problem does Peter Grant describe?'),
    RQ(['Ten years.', 'One week.', 'Two years.', 'One month.'], passage='Dear Mr Hall,\nThank you for your letter. I have been a customer of your bank for ten years, and I have never had a problem until now. Last week, my card stopped working while I was paying at a shop.\nYours sincerely,\nPeter Grant', text='How long has Peter Grant been a customer of the bank?'),
    RQ(['Orders over £300.', 'All orders.', 'Sofas only.', 'Online orders.'], passage=AD, text='Which orders get free delivery?'),
  ]),
]
write_bank('A2', PARTS, (12, 14, 8))
