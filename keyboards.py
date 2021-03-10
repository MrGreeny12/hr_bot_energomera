from telebot import types


# главная страница
keyboardWelcome = types.InlineKeyboardMarkup()
keyEmployee = types.InlineKeyboardButton('Сотрудник', callback_data='employee')
keyCandidate = types.InlineKeyboardButton('Кандидат', callback_data='candidate')
keyboardWelcome.add(keyEmployee, keyCandidate)


# клавиатура для кандидата
keyboardCandidate = types.InlineKeyboardMarkup()
keyFaq = types.InlineKeyboardButton('Популярные вопросы', callback_data='faq')
keySocialNetworks = types.InlineKeyboardButton('Наши контакты', callback_data='socialNetworks')
keyBackMainMenu = types.InlineKeyboardButton(text='Назад', callback_data='kb.keyboardWelcome')
keyboardCandidate.add(keyFaq, keySocialNetworks).add(keyBackMainMenu)


# клавиатура раздела FAQ
keyboardFAQ = types.InlineKeyboardMarkup()
keySteps = types.InlineKeyboardButton('Этапы подбора персонала', callback_data='steps')
keyTestResultCandidate = types.InlineKeyboardButton('Узнать результаты тестирования', callback_data='testResultCandidate')
keyFeedback = types.InlineKeyboardButton('Оставить отзыв', callback_data='feedback')
keyTestTrouble = types.InlineKeyboardButton('Проблемы с тестированием', callback_data='testTrouble')
keyDocList = types.InlineKeyboardButton('Документы для приёма на работу', callback_data='docList')
keyStudentsPractice = types.InlineKeyboardButton('Как попасть на практику', callback_data='studentsPractice')
keySendResume = types.InlineKeyboardButton('Отправить резюме', callback_data='sendResume')
keyBackCandidate = types.InlineKeyboardButton(text='Назад', callback_data='candidate')
keyboardFAQ.add(keySendResume).add(keySteps).add(keyTestTrouble).add(keyTestResultCandidate)\
    .add(keyStudentsPractice).add(keyDocList).add(keyFeedback).add(keyBackCandidate)


# клавиатура раздела Социальные сети
keyboardSocialNetworks = types.InlineKeyboardMarkup()
keyVK = types.InlineKeyboardButton('ВКонтакте', url='http://vk.com/concern_energomera', callback_data='vk')
keyFacebook = types.InlineKeyboardButton('Facebook', url='https://www.facebook.com/energomera.ru', callback_data='facebook')
keyInstagram = types.InlineKeyboardButton('Instagram', url='https://instagram.com/energomera_careers', callback_data='instagram')
keyHeadHunter = types.InlineKeyboardButton('Head Hunter', url='https://stavropol.hh.ru/employer/24946', callback_data='headHunter')
keyMainSite = types.InlineKeyboardButton('Официальный сайт Компании', url='http://www.energomera.com', callback_data='mainSite')
keyboardSocialNetworks.add(keyVK).add(keyFacebook).add(keyInstagram).add(keyHeadHunter).add(keyMainSite)\
    .add(keyBackCandidate)


# клавиатура для всех страниц с информацией
keyboardPageCandidate = types.InlineKeyboardMarkup()
keyMainMenu = types.InlineKeyboardButton('В начало', callback_data='kb.keyboardWelcome')
keyBackFAQ = types.InlineKeyboardButton('Назад', callback_data='faq')
keyboardPageCandidate.add(keyMainMenu, keyBackFAQ)


# клавиатура для всех странице с информации о проблемах с тестированием
keyboardPageCandidateTestTrouble = types.InlineKeyboardMarkup()
keyExcelTrouble = types.InlineKeyboardButton('Проблемы с тестом в Excel', callback_data='excelTrouble')
keyTestRoomTrouble = types.InlineKeyboardButton('Проблемы с тестом в Testroom', callback_data='testRoomTrouble')
keyboardPageCandidateTestTrouble.add(keyExcelTrouble).add(keyTestRoomTrouble).add(keyMainMenu, keyBackFAQ)
keyboardPageTestTrouble = types.InlineKeyboardMarkup()
keyBackTestTrouble = types.InlineKeyboardButton('Назад', callback_data='testTrouble')
keyboardPageTestTrouble.add(keyMainMenu, keyBackTestTrouble)


# клавиатура для страницы сотрудника
keyboardEmployee = types.InlineKeyboardMarkup()
keyEvents = types.InlineKeyboardButton('Мероприятия компании', callback_data='events')
keyMoney = types.InlineKeyboardButton('Мои начисления', callback_data='money')
keyLabourOrganization = types.InlineKeyboardButton('Правила работы', callback_data='labourOrganization')
keyDMS = types.InlineKeyboardButton('Добровольное медицинское страхование', callback_data='dms')
keyVacations = types.InlineKeyboardButton('Отпуска и больничные', callback_data='vacations')
keyDifferentiation = types.InlineKeyboardButton('Дифференциация персонала', callback_data='differentiation')
keyMentoring = types.InlineKeyboardButton('Наставничество', callback_data='mentoring')
keyStudy = types.InlineKeyboardButton('Обучение персонала', callback_data='study')
keyTestEmployee = types.InlineKeyboardButton('Психологическое тестирование', callback_data='testEmployee')
keyCOVID19 = types.InlineKeyboardButton('Короновирус (COVID-19)', callback_data='covid19')
keyReferal = types.InlineKeyboardButton('Пригласи друга на работу', callback_data='referal')
keyBackMainMenu = types.InlineKeyboardButton(text='Назад', callback_data='kb.keyboardWelcome')
keyboardEmployee.add(keyEvents).add(keyMoney).add(keyLabourOrganization).add(keyDMS)\
    .add(keyVacations).add(keyDifferentiation).add(keyMentoring).add(keyStudy)\
    .add(keyTestEmployee).add(keyReferal).add(keyCOVID19).add(keyBackMainMenu)


# клавиатура раздела о мероприятиях компании
keyboardEvents = types.InlineKeyboardMarkup()
keyIdea = types.InlineKeyboardButton('Предложить идею', callback_data='idea')
keySpecialOffers = types.InlineKeyboardButton('Акции для сотрудников (в разработке)', callback_data='specialOffers')
keyBackEmployee = types.InlineKeyboardButton(text='Назад', callback_data='employee')
keyboardEvents.add(keyIdea, keySpecialOffers).add(keyBackEmployee)
keyboardPageEvents = types.InlineKeyboardMarkup()
keyBackEvents = types.InlineKeyboardButton(text='Назад', callback_data='events')
keyboardPageEvents.add(keyMainMenu, keyBackEvents)


# клавиатура раздела о начислениях
keyboardMoney = types.InlineKeyboardMarkup()
keyDayPayment = types.InlineKeyboardButton('Дни начисления', callback_data='dayPayment')
keyPrepayment = types.InlineKeyboardButton('Аванс', callback_data='prepayment')
keySickLeave = types.InlineKeyboardButton('Больничный', callback_data='sickLeave')
keyBenefits = types.InlineKeyboardButton('Премии', callback_data='benefits')
keyMaternityLeave = types.InlineKeyboardButton('Декретные', callback_data='maternityLeave')
keyDoc2NDFL = types.InlineKeyboardButton('Справки о зарплате', callback_data='doc2NDFL')
keyBusinessTrip = types.InlineKeyboardButton('Командировочные', callback_data='businessTrip')
keySalaryTrouble = types.InlineKeyboardButton('Ошибка в начислениях', callback_data='salaryTrouble')
keyboardMoney.add(keyDayPayment).add(keyPrepayment, keySickLeave).add(keyBenefits, keyMaternityLeave)\
    .add(keyDoc2NDFL).add(keyBusinessTrip).add(keySalaryTrouble).add(keyBackEmployee)
keyboardPageMoney = types.InlineKeyboardMarkup()
keyBackMoney = types.InlineKeyboardButton(text='Назад', callback_data='money')
keyboardPageMoney.add(keyMainMenu, keyBackMoney)


# клавиатура раздела о правилах работы
keyboardLabourOrganization = types.InlineKeyboardMarkup()
keyPassLost = types.InlineKeyboardButton('Отсутствие пропуска', callback_data='passLost')
keyProhibitions = types.InlineKeyboardButton('Ограничения', callback_data='prohibitions')
keySchedule = types.InlineKeyboardButton('График работы (в разработке)', callback_data='schedule')
keyboardLabourOrganization.add(keyPassLost, keyProhibitions).add(keySchedule).add(keyBackEmployee)
keyboardPageLabourOrganization = types.InlineKeyboardMarkup()
keyBackLabourOrganization = types.InlineKeyboardButton(text='Назад', callback_data='labourOrganization')
keyboardPageLabourOrganization.add(keyMainMenu, keyBackLabourOrganization)


# клавиатура раздела о ДМС (добровольное медицинское страхование)
keyboardDMS = types.InlineKeyboardMarkup()
keyHowUseDMS = types.InlineKeyboardButton('Потратить ДМС', callback_data='howUseDMS')
keyFamilyDMS = types.InlineKeyboardButton('Перевод средств ДМС', callback_data='familyDMS')
keyboardDMS.add(keyHowUseDMS, keyFamilyDMS).add(keyBackEmployee)
keyboardPageDMS = types.InlineKeyboardMarkup()
keyBackDMS = types.InlineKeyboardButton(text='Назад', callback_data='dms')
keyboardPageDMS.add(keyMainMenu, keyBackDMS)


# клавиатура раздела об отпусках и больничных
keyboardVacations = types.InlineKeyboardMarkup()
keyLeaveWithoutPay = types.InlineKeyboardButton('Взять отпуск', callback_data='leaveWithoutPay')
keyDayOff = types.InlineKeyboardButton('Взять отгул', callback_data='dayOff')
keyDonor = types.InlineKeyboardButton('Донорские', callback_data='donor')
keySickLeaveOut = types.InlineKeyboardButton('Больничный лист', callback_data='sickLeaveOut')
keyboardVacations.add(keyLeaveWithoutPay, keyDayOff).add(keyDonor, keySickLeaveOut).add(keyBackEmployee)
keyboardPageVacations = types.InlineKeyboardMarkup()
keyBackVacations = types.InlineKeyboardButton(text='Назад', callback_data='vacations')
keyboardPageVacations.add(keyMainMenu, keyBackVacations)


# клавиатура раздела о дифференциации персонала
keyboardDifferentiation = types.InlineKeyboardMarkup()
keyWhenFeedback = types.InlineKeyboardButton('Мои результаты', callback_data='whenFeedack')
keyExpertCommission = types.InlineKeyboardButton('Состав комиссии', callback_data='expertCommission')
keyboardDifferentiation.add(keyWhenFeedback, keyExpertCommission).add(keyBackEmployee)
keyboardPageDifferentiation = types.InlineKeyboardMarkup()
keyBackDifferentiation = types.InlineKeyboardButton(text='Назад', callback_data='differentiation')
keyboardPageDifferentiation.add(keyMainMenu, keyBackDifferentiation)


# клавиатура раздела о наставниках
keyboardMentoring = types.InlineKeyboardMarkup()
keyFailureMentor = types.InlineKeyboardButton('Нет наставника', callback_data='failureMentor')
keyEditMentor = types.InlineKeyboardButton('Поменять наставника', callback_data='editMentor')
keyFeedbackMentor = types.InlineKeyboardButton('Оставить отзыв на наставника', callback_data='feedbackMentor')
keyboardMentoring.add(keyFailureMentor, keyEditMentor).add(keyFeedbackMentor).add(keyBackEmployee)
keyboardPageMentoring = types.InlineKeyboardMarkup()
keyBackMentoring = types.InlineKeyboardButton(text='Назад', callback_data='mentoring')
keyboardPageMentoring.add(keyMainMenu, keyBackMentoring)


# клавиатура раздела об обучении
keyboardStudy = types.InlineKeyboardMarkup()
keyFailureStudy = types.InlineKeyboardButton('Обучение не состоялось', callback_data='failureStudy')
keyTrainig = types.InlineKeyboardButton('Повысить квалификацию', callback_data='training')
keyRemoteStudyPortal = types.InlineKeyboardButton('Обучение из дома', callback_data='remoteStudyPortal')
keyAbsenteeism = types.InlineKeyboardButton('Не могу присутствовать', callback_data='absenteeism')
keyQualificationCommission = types.InlineKeyboardButton('Как будет проходить квалификацонная комиссия?',
                                                        callback_data='QualificationCommission')
keyboardStudy.add(keyFailureStudy).add(keyTrainig).add(keyRemoteStudyPortal)\
    .add(keyAbsenteeism).add(keyQualificationCommission).add(keyBackEmployee)
keyboardPageStudy = types.InlineKeyboardMarkup()
keyBackStudy = types.InlineKeyboardButton(text='Назад', callback_data='study')
keyboardPageStudy.add(keyMainMenu, keyBackStudy)


# клавиатура возврата на страницу обучения
keyboardQualificationCommission = types.InlineKeyboardMarkup()
keyDocListQualification = types.InlineKeyboardButton('Обучение из дома', callback_data='docListQualification')
keyLostQualificationCommission = types.InlineKeyboardButton('Не могу присутствовать',
                                                            callback_data='lostQualificationCommission')
keyboardQualificationCommission.add(keyDocListQualification).add(keyLostQualificationCommission).add(keyBackStudy)
keyboardBackQualificationCommission = types.InlineKeyboardMarkup()
keyBackQualificationCommission = types.InlineKeyboardButton('Назад', callback_data='QualificationCommission')
keyboardBackQualificationCommission.add(keyMainMenu, keyBackQualificationCommission)


# клавиатура возврата на страницу сотрудников
keyboardBackEmployee = types.InlineKeyboardMarkup()
keyboardBackEmployee.add(keyMainMenu, keyBackEmployee)


# клавиатура раздела о COVID-19
keyboardCovid19 = types.InlineKeyboardMarkup()
keyRecommendation = types.InlineKeyboardButton('Рекомендации от правительства Ставропольского края',
                                               url='https://www.stavregion.ru/podderzhka-nko/novosti-nko/rekomendacii-'
                                                   'po-profilaktike-novoj-koronovirusnoj-infekcii-covid/',
                                               callback_data='recommendation')
keyActualDoc = types.InlineKeyboardButton('Актуальные документы',
                                          url='http://docs.cntd.ru/document/570711319',
                                          callback_data='actualDoc')
keyboardCovid19.add(keyRecommendation).add(keyActualDoc).add(keyBackEmployee)
keyboardPageCovid19 = types.InlineKeyboardMarkup()
keyBackCovid19 = types.InlineKeyboardButton(text='Назад', callback_data='covid19')
keyboardPageCovid19.add(keyMainMenu, keyBackCovid19)