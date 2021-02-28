from telebot import types


#главная страница
keyboardWelcome = types.InlineKeyboardMarkup()
keyEmployee = types.InlineKeyboardButton('Сотрудник', callback_data='employee')
keyCandidate = types.InlineKeyboardButton('Кандидат', callback_data='candidate')
keyboardWelcome.add(keyEmployee, keyCandidate)


#клавиатура для кандидата
keyboardCandidate = types.InlineKeyboardMarkup()
keyFaq = types.InlineKeyboardButton('FAQ', callback_data='faq')
keySocialNetworks = types.InlineKeyboardButton('Наши социальные сети', callback_data='socialNetworks')
keyBackMainMenu = types.InlineKeyboardButton(text='Назад', callback_data='kb.keyboardWelcome')
keyboardCandidate.add(keyFaq, keySocialNetworks).add(keyBackMainMenu)


#клавиатура раздела FAQ
keyboardFAQ = types.InlineKeyboardMarkup()
keySteps = types.InlineKeyboardButton('Этапы подбора персонала', callback_data='steps')
keyTestResultCandidate = types.InlineKeyboardButton('Узнать результаты тестирования', callback_data='testResultCandidate')
keyFeedback = types.InlineKeyboardButton('Хочу пожаловаться', callback_data='feedback')
keyTestTrouble = types.InlineKeyboardButton('Не получается пройти тестирование', callback_data='testTrouble')
keyDocList = types.InlineKeyboardButton('Документы для приёма на работу', callback_data='docList')
keyStudentsPractice = types.InlineKeyboardButton('Как попасть на практику?', callback_data='studentsPractice')
keySendResume = types.InlineKeyboardButton('Хочу отправить резюме', callback_data='sendResume')
keyBackCandidate = types.InlineKeyboardButton(text='Назад', callback_data='candidate')
keyboardFAQ.add(keySteps).add(keyTestResultCandidate).add(keyFeedback).add(keyTestTrouble).add(keyDocList)\
    .add(keyStudentsPractice).add(keySendResume).add(keyBackCandidate)


#клавиатура раздела Социальные сети
keyboardSocialNetworks = types.InlineKeyboardMarkup()
keyVK = types.InlineKeyboardButton('ВКонтакте', url='http://vk.com/concern_energomera', callback_data='vk')
keyFacebook = types.InlineKeyboardButton('Facebook', url='https://www.facebook.com/energomera.ru', callback_data='facebook')
keyInstagram = types.InlineKeyboardButton('Instagram', url='https://instagram.com/energomera_careers?igshid=eynr8657nskp', callback_data='instagram')
keyHeadHunter = types.InlineKeyboardButton('Head Hunter', url='https://stavropol.hh.ru/employer/24946', callback_data='headHunter')
keyMainSite = types.InlineKeyboardButton('Официальный сайт Компании', url='http://www.energomera.com', callback_data='mainSite')
keyboardSocialNetworks.add(keyVK).add(keyFacebook).add(keyInstagram).add(keyHeadHunter).add(keyMainSite).add(keyBackCandidate)


#клавиатура для всех страниц с информацией
keyboardPageCandidate = types.InlineKeyboardMarkup()
keyMainMenu = types.InlineKeyboardButton('В начало', callback_data='kb.keyboardWelcome')
keyBackFAQ = types.InlineKeyboardButton('Назад', callback_data='faq')
keyboardPageCandidate.add(keyMainMenu).add(keyBackFAQ)


#клавиатура для страницы сотрудника
keyboardEmployee = types.InlineKeyboardMarkup()
keyMotivation = types.InlineKeyboardButton('Мотивация персонала', callback_data='motivation')
keyMoney = types.InlineKeyboardButton('Вопросы о деньгах', callback_data='money')
keyLabourOrganization = types.InlineKeyboardButton('Организация труда', callback_data='labourOrganization')
keyDMS = types.InlineKeyboardButton('Дополнительное медицинское страхование', callback_data='dms')#поменять название
keyCnB = types.InlineKeyboardButton('Кадровое делопроизводство', callback_data='cnb')#поменять название
keyDifferentiation = types.InlineKeyboardButton('Дифференциация персонала', callback_data='differentiation')
keyMentoring = types.InlineKeyboardButton('Всё о наставниках', callback_data='mentoring')
keyStudy = types.InlineKeyboardButton('Обучение персонала', callback_data='study')
keyRecruitment = types.InlineKeyboardButton('Подбор персонала', callback_data='recruitment')
keyCOVID19 = types.InlineKeyboardButton('Короновирус (COVID-19)', callback_data='covid19')
keyBackMainMenu = types.InlineKeyboardButton(text='Назад', callback_data='kb.keyboardWelcome')
keyboardEmployee.add(keyMotivation).add(keyMoney).add(keyLabourOrganization).add(keyDMS)\
    .add(keyCnB).add(keyDifferentiation).add(keyMentoring).add(keyStudy)\
    .add(keyRecruitment).add(keyCOVID19).add(keyBackMainMenu)


#клавиатура раздела мотивация персонала
keyboardMotivation = types.InlineKeyboardMarkup()
keyActivity = types.InlineKeyboardButton('Хочу устроить концерт или хотя бы чаепитие!', callback_data='activity')
keySpecialOffers = types.InlineKeyboardButton('Корпоративные скидки, акции и предложения', callback_data='specialOffers')
keyBackEmployee = types.InlineKeyboardButton(text='Назад', callback_data='employee')
keyboardMotivation.add(keyActivity).add(keySpecialOffers).add(keyBackEmployee)


#клавиатура раздела о деньгах
keyboardMoney = types.InlineKeyboardMarkup()
keySalaryPayment = types.InlineKeyboardButton('Как начисляется заработная плата?', callback_data='salaryPayment')
keyPrepayment = types.InlineKeyboardButton('Как рассчитывается аванс?', callback_data='prepayment')
keySickLeave = types.InlineKeyboardButton('Как рассчитывать больничный?', callback_data='sickLeave')
keyMaternityLeave = types.InlineKeyboardButton('Как рассчитываются декретные?', callback_data='maternityLeave')
keyDoc2NDFL = types.InlineKeyboardButton('Как получить справку 2НДФЛ?', callback_data='doc2NDFL')
keySalaryTrouble = types.InlineKeyboardButton('Не пришла заработная плата, что делать?', callback_data='salaryTrouble')
keyboardMoney.add(keySalaryPayment).add(keyPrepayment).add(keySickLeave).add(keyMaternityLeave).add(keyDoc2NDFL)\
    .add(keySalaryTrouble).add(keyBackEmployee)


#клавиатура раздела об организации труда
keyboardLabourOrganization = types.InlineKeyboardMarkup()
keyPassLost = types.InlineKeyboardButton('Потерял пропуск, что делать?', callback_data='passLost')
keyProhibitions = types.InlineKeyboardButton('Какие существуют запреты на предприятии?', callback_data='prohibitions')
keyBenefits = types.InlineKeyboardButton('Что такое премии?', callback_data='benefits')
keySchedule = types.InlineKeyboardButton('Узнать график работы', callback_data='schedule')
keyRemote = types.InlineKeyboardButton('Как перейти на удалёнку?', callback_data='remote')
keyboardLabourOrganization.add(keyPassLost).add(keyProhibitions).add(keyBenefits).add(keySchedule).add(keyRemote)\
    .add(keyBackEmployee)


#клавиатура раздела о ДМС (дополнительное медицинское страхование)
keyboardDMS = types.InlineKeyboardMarkup()
keyHowUseDMS = types.InlineKeyboardButton('Как воспользоваться ДМС?', callback_data='howUseDMS')
keyCashOutDMS = types.InlineKeyboardButton('Можно ли обналичить ДМС?', callback_data='cashOutDMS')
keyFamilyDMS = types.InlineKeyboardButton('Могу  ли я перевести ДМС на родственников?', callback_data='familyDMS')
keyboardDMS.add(keyHowUseDMS).add(keyCashOutDMS).add(keyFamilyDMS).add(keyBackEmployee)


#клавиатура раздела о кадровом делопроизводстве
keyboardCnB = types.InlineKeyboardMarkup()
keyLeaveWithoutPay = types.InlineKeyboardButton('Как взять отпуск без содержания?', callback_data='leaveWithoutPay')
keyDayOff = types.InlineKeyboardButton('Что такое отгул?', callback_data='dayOff')
keyDonor = types.InlineKeyboardButton('Что такое донорские?', callback_data='donor')
keySickLeaveOut = types.InlineKeyboardButton('Что делать с больничным листом?', callback_data='sickLeaveOut')
keyboardCnB.add(keyLeaveWithoutPay).add(keyDayOff).add(keyDonor).add(keySickLeaveOut).add(keyBackEmployee)


#клавиатура раздела о дифференциации персонала
keyboardDifferentiation = types.InlineKeyboardMarkup()
keyWhenFeedback = types.InlineKeyboardButton('Когда ждать обратную связь?', callback_data='whenFeedack')
keyExpertCommission = types.InlineKeyboardButton('Кто будет меня оценивать?', callback_data='expertCommission')
keyMyDFGroup = types.InlineKeyboardButton('Как узнать в какой я группе?', callback_data='myDFGroup')
keyboardDifferentiation.add(keyWhenFeedback).add(keyExpertCommission).add(keyMyDFGroup).add(keyBackEmployee)


#клавиатура раздела о наставниках
keyboardMentoring = types.InlineKeyboardMarkup()
keyFailureMentor = types.InlineKeyboardButton('Наставник отсутствует, что делать?', callback_data='failureMentor')
keyEditMentor = types.InlineKeyboardButton('Как можно поменять наставника?', callback_data='editMentor')
keyboardMentoring.add(keyFailureMentor).add(keyEditMentor).add(keyBackEmployee)


#клавиатура раздела об обучении
keyboardStudy = types.InlineKeyboardMarkup()
keyAttestation = types.InlineKeyboardButton('Аттестация персонала', callback_data='attestation')
keyFailureStudy = types.InlineKeyboardButton('Преподаватель не провёл обучение', callback_data='failureStudy')
keyTrainig = types.InlineKeyboardButton('Как мне повысить квалификацию?', callback_data='training')
keyRemoteStudyPortal = types.InlineKeyboardButton('Можно ли попасть на портал обучения дистанционно?', callback_data='remoteStudyPortal')
keyAbsenteeism = types.InlineKeyboardButton('Я не могу пройти обучение по плану - что делать?', callback_data='absenteeism')
keyOrderQualificationCommission = types.InlineKeyboardButton('Как будет проходить квалификацонная комиссия?', callback_data='orderQualificationCommission')
keyPreQualificationCommission = types.InlineKeyboardButton('Что готовить на квалификационную комиссию?', callback_data='preQualificationCommission')
keyFailureQualificationCommission = types.InlineKeyboardButton('Что делать, если просрал всё перед комиссией?', callback_data='failureQualificationCommission')
keyboardStudy.add(keyAttestation).add(keyFailureStudy).add(keyTrainig).add(keyRemoteStudyPortal)\
    .add(keyAbsenteeism).add(keyOrderQualificationCommission).add(keyPreQualificationCommission)\
    .add(keyFailureQualificationCommission).add(keyBackEmployee)


#клавиатура раздела о подборе персонала
keyboardRecruitment = types.InlineKeyboardMarkup()
keyAboutReferal = types.InlineKeyboardButton('Подробно о реферальной программе', callback_data='aboutReferal')
keyTestResultEmployee = types.InlineKeyboardButton('Как узнать результаты тестирования?', callback_data='testResultEmployee')
keyboardRecruitment.add(keyAboutReferal).add(keyTestResultEmployee).add(keyBackEmployee)


#клавиатура раздела о COVID-19
keyboardCovid19 = types.InlineKeyboardMarkup()
keyRecommendation = types.InlineKeyboardButton('Рекомендации от правительства Ставропольского края', callback_data='recommendation')
keyActualDoc = types.InlineKeyboardButton('Актуальные документы', callback_data='actualDoc')
keyRemoteStatement = types.InlineKeyboardButton('Заявление на удалёнку', callback_data='remoteStatement')
keyboardCovid19.add(keyRecommendation).add(keyActualDoc).add(keyRemoteStatement)\
    .add(keyBackEmployee)