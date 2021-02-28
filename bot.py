import telebot
from config import TOKEN
import keyboards as kb

token = TOKEN

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def process_start_command(message):
    bot.send_message(message.chat.id,
                     'Привет! Я чат-бот HR-службы Энергомера. Пока я работаю в тестовом режиме, '
                     'но ты можешь для начала, рассказать, кто ты!',
                     reply_markup=kb.keyboardWelcome)


@bot.message_handler(commands=['help'])
def process_help_command(message):
    bot.send_message(message.chat.id, 'Здесь по идее будет инфа о полезностях бота')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'kb.keyboardWelcome':
        bot.edit_message_text('Привет! Я чат-бот HR-службы Энергомера. Пока я работаю в тестовом режиме, '
                              'но ты можешь для начала, рассказать, кто ты!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardWelcome)
    elif call.data == 'employee':
        bot.edit_message_text('Это раздел для сотрудников. Выбирай, не хочу!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardEmployee)
    elif call.data == 'candidate':
        bot.edit_message_text('Это раздел для соискателей. Все самые распространнёные '
                              'ответы на вопросы Вы можете найти в разделе FAQ. Ссылки на '
                              'наши социальные сети Вы можете найти в соответствующем разделе',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardCandidate)
    elif call.data == 'faq':
        bot.edit_message_text('Выберите интересующий Вас вопрос:',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardFAQ)
    elif call.data == 'socialNetworks':
        bot.edit_message_text('Список наших сообществ в социальных сетях:',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardSocialNetworks)
    elif call.data == 'steps':
        bot.edit_message_text('Здесь будет информация об этапах подбора персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'testResultCandidate':
        bot.edit_message_text('Здесь будет информация о том, как узнать результаты тестирования',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'feedback':
        bot.edit_message_text('Здесь ты можешь оставить своё никому не нужное мнение о нашей классной'
                              ' службе УП. \n'
                              '\n'
                              'По этому адресу - test@energomera.ru',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'testTrouble':
        bot.edit_message_text('Конечно ты всё сломал. Кто бы сомневался',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'docList':
        bot.edit_message_text('Тут список всего, что нужно для приёма',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'studentsPractice':
        bot.edit_message_text('Хочешь на практику? А вот хрен тебе',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'sendResume':
        bot.edit_message_text('Отправить своё резюме можно на адрес - test@energomera.ru\n'
                              '\n'
                              'Тему сообщения нужно - такую то \n'
                              'Мы обработаем Ваше резюме в течение N часов',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'motivation':
        bot.edit_message_text('Тута раздел по мотивации',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMotivation)
    elif call.data == 'money':
        bot.edit_message_text('Тута раздел о деньгах',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMoney)
    elif call.data == 'labourOrganization':
        bot.edit_message_text('Тута раздел об организации труда',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardLabourOrganization)
    elif call.data == 'dms':
        bot.edit_message_text('Тута раздел о ДМС',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDMS)
    elif call.data == 'cnb':
        bot.edit_message_text('Тута раздел о кадровом делопроизводстве',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardCnB)
    elif call.data == 'differentiation':
        bot.edit_message_text('Тута раздел о дифференциации персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDifferentiation)
    elif call.data == 'mentoring':
        bot.edit_message_text('Тута раздел о тех, кто учит Вас',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMentoring)
    elif call.data == 'study':
        bot.edit_message_text('Тута раздел об обучении',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardStudy)
    elif call.data == 'recruitment':
        bot.edit_message_text('Тута раздел о подборе персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardRecruitment)
    elif call.data == 'covid19':
        bot.edit_message_text('Тута раздел о короне и её носителях',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardCovid19)


bot.polling()