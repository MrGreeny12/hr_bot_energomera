import telebot
from config import TOKEN
import keyboards as kb

token = TOKEN

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def process_start_command(message):
    bot.send_message(message.chat.id,
                     'Кто\n'
                     'Ты\n'
                     'По масти?\n'
                     '♠️♣️\n'
                     '\n'
                     'так и тестим🤷🏼‍♂️',
                     reply_markup=kb.keyboardWelcome)


@bot.message_handler(commands=['help'])
def process_help_command(message):
    bot.send_message(message.chat.id,
                     'Здесь по идее будет инфа о полезностях бота')


@bot.message_handler(commands=['authors'])
def process_help_command(message):
    bot.send_message(message.chat.id,
                     'Все эти прекрасные люди тут скоро появятся')


@bot.message_handler(commands=['feedback'])
def process_help_command(message):
    bot.send_message(message.chat.id,
                     'Все свои чудесные мысли, баги, идеи и просто доброе слово можно написать сюда\n'
                     '@ivakhnenkovd')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'kb.keyboardWelcome':
        bot.edit_message_text('Кто\n'
                              'Ты\n'
                              'По масти?\n'
                              '♠️♣️\n'
                              '\n'
                              'так и тестим🤷🏼‍♂️',
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
        bot.edit_message_text('🆘Чем мы можем помочь:',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardFAQ)
    elif call.data == 'socialNetworks':
        bot.edit_message_text('🌐Список наших сообществ в социальных сетях:',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardSocialNetworks)
    elif call.data == 'steps':
        bot.edit_message_text('Здесь будет информация об этапах подбора персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'testResultCandidate':
        bot.edit_message_text('Для получения обратной связи по результатам тестирования необходимо обратиться к '
                              'менеджеру по оценке персонала с письменным запросом. 📝\n '
                              '\n'
                              'На почту по адресу - resume@energomera.ru  направить сообщение с запросом  и указать '
                              'свои контактные данные.\n '
                              '\n'
                              'В течение 2-3 рабочих дней с Вами свяжутся и назначат дату и время консультации 🙋🏼‍♀️',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'feedback':
        bot.edit_message_text('Мы приветствуем прозрачность в отношениях с соискателями. Если Вами были выявлены '
                              'какие-то нарушения в работе специалистов, у Вас есть идеи по улучшению нашей работы '
                              'или Вы просто хотите оставить положительный отзыв о нашей работе, просим написать '
                              'об этом в письме и отправить по адресу\n'
                              '\n'
                              '✉️hr-feedback@energomera.ru\n'
                              '\n'
                              'Вы помогаете нам стать лучше 👩🏼‍💻\n'
                              '\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'testTrouble':
        bot.edit_message_text('Конечно ты всё сломал. Кто бы сомневался',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidateTestTrouble)
    elif call.data == 'excelTrouble':
        bot.edit_message_text('В документе Excel: \n'
                              '1) Внимательно ознакомьтесь с инструкцией в шапке теста ⬆️\n'
                              '2) А также с краткой инструкцией справа от вопроса. ➡️\n'
                              '3)  В конце каждого теста есть небольшая подсказка. ⬇️\n'
                              '4) Варианты ответа необходимо вводить в отведенные для этого ячейки. ✅\n'
                              '\n'
                              'Если у вас ещё остались вопросы, вы можете позвонить или написать нам\n'
                              '✉️ resume@energomera.ru\n'
                              '📱 +7(8652)-33-50-11',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageTestTrouble)
    elif call.data == 'testRoomTrouble':
        bot.edit_message_text('На сайте TestRoom: \n'
                              '1) Чтобы пройти тестирование на сайте, Вам необходимо зарегистрироваться, заполнив все '
                              'поля анкеты.\n '
                              '2) Войти на сайт, используя свой логин и пароль.\n'
                              '3) Выбрать нужный тест из списка / повторно перейти по ссылке на тест из письма от '
                              'менеджера.\n '
                              '\n'
                              'Не получается зарегистрироваться или не открывается тест? Попробуйте использовать '
                              'другой браузер.\n '
                              '\n'
                              'Если у вас ещё остались вопросы, вы можете позвонить или написать нам:\n'
                              '✉️ resume@energomera.ru\n'
                              '📱+7(8652)-33-50-11',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageTestTrouble)
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
        bot.edit_message_text('Отправить своё резюме можно нам на почту\n'
                              '✉️ resume@energomera.ru\n'
                              '\n'
                              'Также можно откликнуться на странице компании\n'
                              '🔔 https://stavropol.hh.ru/employer/24946\n'
                              '\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCandidate)
    elif call.data == 'events':
        bot.edit_message_text('Тута раздел по мотивации',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardEvents)
    elif call.data == 'idea':
        bot.edit_message_text('Тута разный движ',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageEvents)
    elif call.data == 'specialOffers':
        bot.edit_message_text('Тута разные ништячки',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageEvents)
    elif call.data == 'money':
        bot.edit_message_text('Тута раздел о деньгах',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMoney)
    elif call.data == 'dayPayment':
        bot.edit_message_text('Как мне приходят мои денежки?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'prepayment':
        bot.edit_message_text('Что там по авансику?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'sickLeave':
        bot.edit_message_text('Я болен, медсестра, несите коньяку!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'maternityLeave':
        bot.edit_message_text('В общем, я буду батей',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'doc2NDFL':
        bot.edit_message_text('Место обитания страшных аббревиатур',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'businessTrip':
        bot.edit_message_text('Инфа про мифические командировочные, которые умерли'
                              ' из-за изоляции',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'salaryTrouble':
        bot.edit_message_text('А денежка, это, не пришла(',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'labourOrganization':
        bot.edit_message_text('Тута раздел об организации труда',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardLabourOrganization)
    elif call.data == 'passLost':
        bot.edit_message_text('А как так вышло?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'prohibitions':
        bot.edit_message_text('Это нельзя, то нельзя(',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'benefits':
        bot.edit_message_text('Бывают ли в этой жизни премии?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'schedule':
        bot.edit_message_text('Можно ли приходить в 10:00 на работу? (нет)',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'dms':
        bot.edit_message_text('Тута раздел о ДМС',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDMS)
    elif call.data == 'howUseDMS':
        bot.edit_message_text('Куда здесь нажимать??',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDMS)
    elif call.data == 'familyDMS':
        bot.edit_message_text('Хочу лечить зубы своим 5737 братьям и сестрам. Помогите пжлуйста',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDMS)
    elif call.data == 'vacations':
        bot.edit_message_text('Тута раздел о кадровом делопроизводстве',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardVacations)
    elif call.data == 'leaveWithoutPay':
        bot.edit_message_text('Я не готов быть более на содержании!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'dayOff':
        bot.edit_message_text('Прогулы бывают не только в школе)',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'donor':
        bot.edit_message_text('Я здесь оставлю неприняв, своё достоинство и малость крови',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'sickLeaveOut':
        bot.edit_message_text('Бумажка есть - есть\n'
                              'Больничный нет - нет',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'differentiation':
        bot.edit_message_text('Тута раздел о дифференциации персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDifferentiation)
    elif call.data == 'whenFeedack':
        bot.edit_message_text('Когда, скажите мне - когда??',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDifferentiation)
    elif call.data == 'expertCommission':
        bot.edit_message_text('Что по экспертам?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDifferentiation)
    elif call.data == 'mentoring':
        bot.edit_message_text('Тута раздел о тех, кто учит Вас',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMentoring)
    elif call.data == 'failureMentor':
        bot.edit_message_text('А кто у нас тут прячеться такой умный и робкий?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'editMentor':
        bot.edit_message_text('Мне бы наставнику цвет волос сменить, это сюда?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'feedbackMentor':
        bot.edit_message_text('Хочу писать много слов о наставнике',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'study':
        bot.edit_message_text('Тута раздел об обучении',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardStudy)
    elif call.data == 'attestation':
        bot.edit_message_text('Здесь судьбы важные рещают',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'failureStudy':
        bot.edit_message_text('Он куда-то убежал, а я так ничего не понял. Помогите',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'training':
        bot.edit_message_text('Хочу быть как Илон Маск!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'remoteStudyPortal':
        bot.edit_message_text('Говорят, технологии таки дошли!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'absenteeism':
        bot.edit_message_text('Я мудак, который все не правильно рассчитал по времени. Что делать?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'orderQualificationCommission':
        bot.edit_message_text('Как меня будут пытать?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'preQualificationCommission':
        bot.edit_message_text('Какие слова мне надо выучить?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'failureQualificationCommission':
        bot.edit_message_text('Всё горит огнём!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'recruitment':
        bot.edit_message_text('Тута раздел о подборе персонала',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardRecruitment)
    elif call.data == 'aboutReferal':
        bot.edit_message_text('Приведи друга наконец!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageRecruitment)
    elif call.data == 'testResultEmployee':
        bot.edit_message_text('Хочу знать, что по тестам!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageRecruitment)
    elif call.data == 'covid19':
        bot.edit_message_text('Тута раздел о короне и её носителях',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardCovid19)
    elif call.data == 'recommendation':
        bot.edit_message_text('Всякие советы умных дядек',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCovid19)
    elif call.data == 'actualDoc':
        bot.edit_message_text('Что там по документикам?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCovid19)
    elif call.data == 'remoteStatement':
        bot.edit_message_text('Хочу болеть в своих палатах!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageCovid19)


bot.polling()