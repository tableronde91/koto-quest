# Banque de l'examen blanc TOEIC B2 (content/exams/b2-toeic.json), format Listening & Reading abrégé.
# Écoute 18 questions (parties 1 à 4, dont 2 photos), phrases et textes à compléter 18 (parties 5 et 6), compréhension écrite 12 (partie 7).
# Le premier choix est la bonne réponse. Usage : python3 scripts/b2-toeic.py
from en_toeic import *

MEMO = 'MEMO\nTo: All department heads\nFrom: Rhys Morgan, Finance Director\nRe: Travel expenses\n\nOwing to rising costs, the following changes will take effect on 1 September. All business travel must be approved in advance by your department head. Staff travelling by train should book standard class tickets, unless the journey lasts more than three hours. Hotel costs will be reimbursed up to 120 pounds per night in London and 90 pounds elsewhere. Claims submitted more than 30 days after the trip will not be accepted.'
ARTICLE = 'CARDIFF - Welsh software firm Draig Systems has announced that it is to be taken over by the American group Northstar for 85 million pounds. The deal, which is expected to be completed by the end of the year, will allow Draig to expand into the US market. Founded in 2011 by two former university friends, Draig now employs 240 people. Its chief executive, Ffion Price, said that no jobs would be lost and that the company would remain in Cardiff. Shares in Northstar rose by 4% following the announcement.'
EMAIL = 'From: Gareth Lloyd\nTo: Marketing team\nSubject: Survey results\n\nHi all,\nThe results of the customer survey are in. Overall, satisfaction has risen to 82%, up from 74% last year. What customers appreciate most is our delivery speed. However, a large number of respondents found our website difficult to use, which is something we need to address. I suggest holding a meeting next Thursday to discuss possible changes. Please let me know if you are unable to attend.\nGareth'
NOTICE = 'BRECON CONFERENCE CENTRE\nAnnual Sales Conference - 14 to 16 October\nParticipants wishing to attend the gala dinner on 15 October must register by 30 September. Accommodation has been reserved at the Castle Hotel, located five minutes from the centre. A shuttle bus will run between the station and the centre every 30 minutes. Please note that parking at the centre is limited and cannot be guaranteed.'

PARTS = [
  P1(2, PHOTOS_HARD),
  P2(6, [
    LQ('M|If you had known about the delay, would you have taken a later train?', ['Yes, I would have stayed for lunch.', 'I take the train every day.', 'It was delayed by an hour.']),
    LQ('F|Who was the report written by?', ['The finance team prepared it.', 'It’s about last year’s sales.', 'I wrote it down.']),
    LQ('M|Will you be using the meeting room this afternoon?', ['No, you can have it.', 'Yes, I used it yesterday.', 'It’s on the second floor.']),
    LQ('F|Haven’t you had the printer repaired yet?', ['The technician is coming tomorrow.', 'Yes, I printed it.', 'It’s a colour printer.']),
    LQ('M|Why don’t we postpone the launch until spring?', ['That might give us more time.', 'It was launched in spring.', 'Because of the launch.']),
    LQ('F|Do you remember meeting Ms Price at the trade fair?', ['Vaguely. Was she from Cardiff?', 'Remember to meet her.', 'The fair is in March.']),
    LQ('M|How much did sales rise last quarter?', ['By about six per cent.', 'They rose quickly.', 'In the last quarter.']),
    LQ('F|Is the new model due to be released this month?', ['No, it has been delayed until June.', 'It’s a very good model.', 'Yes, I released it.']),
    LQ('M|Which candidate was shortlisted?', ['Both of them, actually.', 'The list is short.', 'He was a candidate last year.']),
    LQ('F|By the time the client arrives, will we have finished the slides?', ['I think so, if nothing goes wrong.', 'The client arrived yesterday.', 'There are twenty slides.']),
  ]),
  P3(6, [
    LQ('M|Have you seen the quarterly figures? Revenue rose sharply, but profits fell slightly.\nF|That’s because of the new factory. The building costs were higher than expected.\nM|Well, it should pay for itself within two years.', ['Building costs were high.', 'Sales went down.', 'A client cancelled an order.', 'Prices were reduced.'], text='Why did profits fall?'),
    LQ('F|I’m calling about the conference in Brecon. I’d like to attend the gala dinner, but I missed the registration deadline.\nM|I’m afraid registration closed yesterday. Let me see if there are any cancellations.\nF|Thank you. I’d really appreciate it.', ['Check for cancellations.', 'Extend the deadline.', 'Book a hotel room.', 'Send an invoice.'], text='What will the man do?'),
    LQ('M|Did you hear that Gareth resigned?\nF|Really? I thought he was about to be promoted.\nM|Apparently he’s been offered a better position at a competitor.', ['He has resigned.', 'He has been promoted.', 'He has been laid off.', 'He has retired.'], text='What does the man say about Gareth?'),
    LQ('F|We need to get the air conditioning serviced before the summer.\nM|I’ll have the facilities team call a technician.\nF|Great. Ask them to do it on a Friday, when the office is quieter.', ['On a Friday.', 'On a Monday.', 'In the summer.', 'At the weekend.'], text='When does the woman want the work done?'),
    LQ('M|If we had hired a second designer, we wouldn’t be so behind schedule.\nF|I agree, but it’s too late now. What we need is to extend the deadline.\nM|I’ll speak to the client this afternoon.', ['Extend the deadline.', 'Hire a designer.', 'Cancel the project.', 'Reduce the price.'], text='What does the woman suggest?'),
    LQ('F|Your flight has been cancelled, I’m afraid. The next one leaves at 6 a.m.\nM|That means I’ll miss my meeting in Dublin. Can I be reimbursed?\nF|Yes, or we can book you on a flight with another airline at 9 tonight.', ['A flight was cancelled.', 'He lost his luggage.', 'His meeting was moved.', 'He missed his train.'], text='What is the man’s problem?'),
    LQ('M|The survey shows that few customers use our app.\nF|That’s not surprising. It is said to be very slow.\nM|Then let’s ask the IT team to look at it before the campaign starts.', ['The app is slow.', 'The app is expensive.', 'The app is new.', 'The app is popular.'], text='What does the woman say about the app?'),
  ]),
  P4(4, [
    LQ('N|Good morning, everyone. As you know, the merger with Northstar will be completed in December. I do understand that many of you are worried about your jobs, so let me be clear: no positions will be cut. What will change is our reporting structure, which I will explain in detail next week.', ['Employees are worried about their jobs.', 'The merger has been cancelled.', 'Sales have fallen.', 'The office is moving.'], text='What concern does the speaker address?'),
    LQ('N|This is a message for passengers travelling to Swansea. Due to engineering works, trains will not be running between Cardiff and Swansea this weekend. A replacement bus service will operate from outside the main entrance. Journeys are expected to take thirty minutes longer than usual.', ['Take a replacement bus.', 'Change at Bristol.', 'Travel on Monday.', 'Buy a new ticket.'], text='What should passengers to Swansea do?'),
    LQ('N|Thank you for joining this webinar. Over the next hour, I’ll be looking at how online sales have developed. As you can see on this slide, sales rose steadily until 2022, peaked in 2023 and have since levelled off. Moving on, I’d like to highlight three reasons for this.', ['They have levelled off.', 'They are rising sharply.', 'They have fallen dramatically.', 'They peaked last month.'], text='What does the speaker say about online sales since 2023?'),
    LQ('N|Hi Ffion, it’s Rhys. I’ve just had the contract checked by our lawyers. Not only is the price too high, but the delivery terms are unclear. I suggest we ask the supplier to rewrite section four before we sign. Could you call me back before five?', ['Ask the supplier to rewrite part of the contract.', 'Sign the contract today.', 'Find a new lawyer.', 'Lower the price.'], text='What does Rhys suggest?'),
    LQ('N|Welcome to Caerphilly Castle, which is believed to be the second largest castle in Britain. Please note that the tower is closed for repairs. Visitors are not allowed to climb on the walls. The audio guide, available in six languages, can be collected at the shop.', ['Climb on the walls.', 'Visit the shop.', 'Use an audio guide.', 'Take photos.'], text='What are visitors not allowed to do?'),
    LQ('N|And finally, the weather. After a week of heavy rain, conditions will improve gradually from Wednesday. By the weekend, temperatures will have risen to around eighteen degrees, with plenty of sunshine in the south.', ['It will gradually improve.', 'It will get colder.', 'Heavy rain will continue.', 'It will snow.'], text='What will happen to the weather?'),
  ]),
  P5(13, [
    RQ(['had', 'has', 'would', 'was'], jp='If the shipment ＿ arrived on time, we would not have lost the client.'),
    RQ(['would be', 'would have been', 'will be', 'is'], jp='If Ms Lloyd had accepted the offer, she ＿ living in New York now.'),
    RQ(['whose', 'who', 'which', 'whom'], jp='The firm ＿ software we use has been taken over by Northstar.'),
    RQ(['which', 'that', 'what', 'who'], jp='The meeting was cancelled at the last minute, ＿ annoyed many participants.'),
    RQ(['submitted', 'submitting', 'submit', 'to submit'], jp='All claims ＿ after 30 days will be rejected.'),
    RQ(['hearing', 'hear', 'to hear', 'heard'], jp='We look forward to ＿ from you at your earliest convenience.'),
    RQ(['repaired', 'repair', 'repairing', 'to repair'], jp='Mr Evans had his car ＿ at the garage next to the office.'),
    RQ(['will have completed', 'will complete', 'completes', 'has completed'], jp='By the end of next month, the team ＿ the installation.'),
    RQ(['to have', 'having', 'have', 'had'], jp='The director is reported ＿ left the company for personal reasons.'),
    RQ(['taking', 'to take', 'take', 'taken'], jp='The employee denied ＿ the documents home.'),
    RQ(['by', 'to', 'at', 'of'], jp='Production costs rose ＿ 3% compared with last year.'),
    RQ(['Few', 'Little', 'A little', 'Much'], jp='＿ customers complained about the new design, so we will keep it.'),
    RQ(['did we', 'we did', 'we have', 'have we'], jp='Not only ＿ exceed our sales target, but we also reduced costs.'),
    RQ(['should', 'are', 'have', 'being'], jp='Under no circumstances ＿ visitors enter the laboratory without a badge.'),
    RQ(['What', 'That', 'It', 'Which'], jp='＿ our clients value most is reliability.'),
    RQ(['due', 'since', 'because', 'thanks'], jp='The flight was diverted ＿ to fog at Cardiff airport.'),
    RQ(['unable', 'impossible', 'incapable', 'not able of'], jp='Unfortunately, we are ＿ to offer refunds on sale items.'),
  ]),
  P6(5, [
    RQ(['Owing', 'Because', 'Despite', 'Although'], passage=MEMO.replace('Owing to', '＿ to'), text='Choose the word for the blank.'),
    RQ(['approved', 'approving', 'approve', 'approval'], passage=MEMO.replace('must be approved', 'must be ＿'), text='Choose the word for the blank.'),
    RQ(['submitted', 'submitting', 'submits', 'to submit'], passage=MEMO.replace('Claims submitted', 'Claims ＿'), text='Choose the word for the blank.'),
    RQ(['which', 'who', 'what', 'where'], passage=ARTICLE.replace('The deal, which', 'The deal, ＿'), text='Choose the word for the blank.'),
    RQ(['expected', 'expecting', 'expect', 'expectation'], passage=ARTICLE.replace('is expected to', 'is ＿ to'), text='Choose the word for the blank.'),
    RQ(['What', 'That', 'Which', 'It'], passage=EMAIL.replace('What customers', '＿ customers'), text='Choose the word for the blank.'),
    RQ(['holding', 'to hold', 'hold', 'held'], passage=EMAIL.replace('suggest holding', 'suggest ＿'), text='Choose the word for the blank.'),
    RQ(['wishing', 'wished', 'wish', 'wishes'], passage=NOTICE.replace('Participants wishing', 'Participants ＿'), text='Choose the word for the blank.'),
  ]),
  P7(12, [
    RQ(['They must be approved in advance.', 'They are no longer allowed.', 'They must be booked online.', 'They are paid by the client.'], passage=MEMO, text='What is said about business trips from 1 September?'),
    RQ(['When the journey is over three hours.', 'When travelling to London.', 'When the manager agrees.', 'When the train is full.'], passage=MEMO, text='When can staff travel first class by train?'),
    RQ(['90 pounds.', '120 pounds.', '30 pounds.', 'The full cost.'], passage=MEMO, text='How much will be reimbursed for a hotel in Swansea?'),
    RQ(['To reduce costs.', 'To reward staff.', 'To simplify booking.', 'To protect the environment.'], passage=MEMO, text='Why are the changes being made?'),
    RQ(['It is being bought by another company.', 'It is opening an office in the US.', 'It is laying off staff.', 'It is moving to London.'], passage=ARTICLE, text='What is happening to Draig Systems?'),
    RQ(['No jobs will be lost.', 'Some staff will move to the US.', 'Profits will rise by 4%.', 'She will leave the company.'], passage=ARTICLE, text='What did Ffion Price say?'),
    RQ(['By the end of the year.', 'In 2011.', 'Next month.', 'It has already happened.'], passage=ARTICLE, text='When will the deal probably be completed?'),
    RQ(['It has risen.', 'It has fallen.', 'It has not changed.', 'It was not measured.'], passage=EMAIL, text='What happened to customer satisfaction?'),
    RQ(['The website.', 'Delivery times.', 'Prices.', 'The product range.'], passage=EMAIL, text='What do many customers find difficult?'),
    RQ(['Hold a meeting.', 'Run a new survey.', 'Hire a web designer.', 'Lower prices.'], passage=EMAIL, text='What does Gareth propose?'),
    RQ(['By 30 September.', 'On 15 October.', 'By 14 October.', 'On 16 October.'], passage=NOTICE, text='When must participants register for the gala dinner?'),
    RQ(['Parking may not be available.', 'The shuttle bus is expensive.', 'The hotel is far away.', 'The centre is closed on Sunday.'], passage=NOTICE, text='What problem is mentioned in the notice?'),
    RQ(['Every 30 minutes.', 'Every hour.', 'Twice a day.', 'Only in the morning.'], passage=NOTICE, text='How often does the shuttle bus run?'),
    RQ(['Five minutes from the centre.', 'Next to the station.', 'In Cardiff.', 'Thirty minutes away.'], passage=NOTICE, text='Where is the Castle Hotel?'),
  ]),
]
write_bank('B2', PARTS, (18, 18, 12))
