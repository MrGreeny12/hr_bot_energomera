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
keyTestResult = types.InlineKeyboardButton('Узнать результаты тестирования', callback_data='testResult')
keyFeedback = types.InlineKeyboardButton('Хочу пожаловаться', callback_data='feedback')
keyTestTrouble = types.InlineKeyboardButton('Не получается пройти тестирование', callback_data='testTrouble')
keyDocList = types.InlineKeyboardButton('Документы для приёма на работу', callback_data='docList')
keyStudentsPractice = types.InlineKeyboardButton('Как попасть на практику?', callback_data='studentsPractice')
keySendResume = types.InlineKeyboardButton('Хочу отправить резюме', callback_data='sendResume')
keyBackCandidate = types.InlineKeyboardButton(text='Назад', callback_data='candidate')
keyboardFAQ.add(keySteps).add(keyTestResult).add(keyFeedback).add(keyTestTrouble).add(keyDocList)\
    .add(keyStudentsPractice).add(keySendResume).add(keyBackCandidate)


#клавиатура раздела Социальные сети
keyboardSocialNetworks = types.InlineKeyboardMarkup()
keyVK = types.InlineKeyboardButton('ВКонтакте', url='wwww.com', callback_data='vk')
keyFacebook = types.InlineKeyboardButton('Facebook', url='wwww.com', callback_data='facebook')
keyInstagram = types.InlineKeyboardButton('Instagram', url='wwww.com', callback_data='instagram')
keyboardSocialNetworks.add(keyVK).add(keyFacebook).add(keyInstagram).add(keyBackCandidate)