import telebot
from config import TOKEN
import keyboards as kb

token = TOKEN

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def process_start_command(message):
    bot.send_message(message.chat.id,
                     'Привет!🙋🏼‍♂️\n'
                     'Что тебя интересует?',
                     reply_markup=kb.keyboardWelcome)


@bot.message_handler()


@bot.message_handler(commands=['authors'])
def process_help_command(message):
    bot.send_message(message.chat.id,
                     '@ivakhnenkovd - разработка, логика, текст 💻\n'
                     '\n'
                     '@GottliebPaw - логика, текст, лого 🖥 \n'
                     '\n'
                     'Саша Доценко - лого 🎨 \n'
                     '\n'
                     'Инна Попова, Алина Шапошникова - текст 🧾 \n')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'kb.keyboardWelcome':
        bot.edit_message_text('Привет!🙋🏼‍♂️\n'
                              'Что тебя интересует?',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardWelcome)
    elif call.data == 'employee':
        bot.edit_message_text('Всё о твоей работе и не только 💼\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardEmployee)
    elif call.data == 'events':
        bot.edit_message_text('Акции, скидки, предложения от вас и нас 💎\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardEvents)
    elif call.data == 'idea':
        bot.edit_message_text('Присылай интересные скидки и акции для сотрудников\n'
                              '\n'
                              'Предлагай мероприятия для нашей мотивации и развития\n'
                              '\n'
                              '✉️ hr-feedback@energomera.ru\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageEvents)
    elif call.data == 'specialOffers':
        bot.answer_callback_query(text='Мы работаем над этим 👨🏻‍🏭',
                                  callback_query_id=call.id)
    elif call.data == 'money':
        bot.edit_message_text('То, что мы стесняемся спросить 🙈\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMoney)
    elif call.data == 'dayPayment':
        bot.edit_message_text('Начисление происходит раз в 15 дней 📅\n'
                              'В начале месяца приходит зарплата 💳\n'
                              'В конце месяца аванс 💶\n'
                              '\n'
                              'Оплата надбавок, премий и прочих стимулирующих выплат '
                              'происходит только в день зарплаты 🗓',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'prepayment':
        bot.edit_message_text('Аванс рассчитывается по формуле ♾\n'
                              '\n'
                              '(Оклад за весь месяц / Количество рабочих дней месяца) * '
                              'Количество отработанных дней по 15 число месяца = Аванс 🎉\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'sickLeave':
        bot.edit_message_text('Начисления поступят через 15 дней после сдачи листка нетрудоспособности '
                              'или его номера в отдел кадров 💁🏼‍♀️\n'
                              '\n'
                              'Размер выплат зависит от стажа и средней заработной платы за '
                              'предыдущие 2 года 🛋\n'
                              '\n'
                              'Узнать подробности\n'
                              '➡️ https://r62.fss.ru/archive/555899.shtml \n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'maternityLeave':
        bot.edit_message_text('Смотри раздел "Больничный"  👀\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'doc2NDFL':
        bot.edit_message_text('Запроси любую справку о начислениях, через корпоративный портал\n'
                              '\n'
                              'Корпоративный портал ➡️ Новый портал: узел коллективной работы ⬆️ '
                              'Виртуальные ячейки ➡️ ВЯ на выдачу бухгалтерских справок 🎉 \n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'businessTrip':
        bot.edit_message_text('Командировочные вычисляются по формуле ♾\n'
                              '\n'
                              '(Среднемесячный заработок за прошлый год / Количество рабочих дней месяца) * '
                              'Количество дней в командировке = Командировочные 🎉\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'salaryTrouble':
        bot.edit_message_text('Не может быть! Перепроверь все предыдущие пункты 📋\n'
                              '\n'
                              'Перепроверил и ничего не изменилось? Тебе сюда\n'
                              '1С ➡️ Общая подсистема ➡️ Обращения по расчёту З/П ➡️ Создать 🎉\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'benefits':
        bot.edit_message_text('По согласованию с генеральным директором, любой сотрудник может '
                              'получить премию в Компании 🎁\n'
                              '\n'
                              'Премия приходит в день зарплаты 📅\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMoney)
    elif call.data == 'labourOrganization':
        bot.edit_message_text('Часть экипажа - часть корабля 🏴‍☠️\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardLabourOrganization)
    elif call.data == 'passLost':
        bot.edit_message_text('Забыл дома - пиши служебку на временный пропуск 🕰\n'
                              '\n'
                              'Потерял - выдадим новый, но удержим из зарплаты 💯\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'prohibitions':
        bot.edit_message_text('У нас нельзя 🚫\n'
                              '\n'
                              '🍾 Проносить спиртное\n'
                              '🚬 Курить в здании\n'
                              '💊 Проносить наркотические вещества\n'
                              '🔪 Проносить оружие\n'
                              '💻 Личные ноутбуки и планшеты\n'
                              '🔖 Проходить без пропуска\n'
                              '🔞 Проходить с несовершеннолетними\n'
                              '🍽 Есть на рабочем месте\n'
                              '\n'
                              'Можно ✅\n'
                              '\n'
                              '👩🏼‍💻 Работать и много работать\n'
                              '🙃 Улыбаться\n'
                              '🤗 Нести добро\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageLabourOrganization)
    elif call.data == 'schedule':
        bot.answer_callback_query(text='Мы работаем над этим 👨🏻‍🏭',
                                  callback_query_id=call.id)
    elif call.data == 'dms':
        bot.edit_message_text('Категории А и В+ ежегодно получают средства ДМС для оплаты своего '
                              'лечения 👩🏼‍⚕️ и отдыха 🌴\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDMS)
    elif call.data == 'howUseDMS':
        bot.edit_message_text('В твоём полисе ДМС указаны контакты страхового агента 📲\n'
                              '\n'
                              'Сообщи ему, где и какую услугу, ты хочешь получить 📑\n'
                              '\n'
                              'Дождись сообщения о выделении средств 💰\n'
                              '\n'
                              '*если ты не знаешь, где оказывают какую услугу, они найдут варианты\n'
                              '\n'
                              '**официально обналичить ДМС нельзя 😏\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDMS)
    elif call.data == 'familyDMS':
        bot.edit_message_text('Деньги даны тебе и только тебе! 🧘\n'
                              '\n'
                              'Никаких родственников, друзей и знакомых 😈 (будь жадным)\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDMS)
    elif call.data == 'vacations':
        bot.edit_message_text('Как законно прогулять работу 🌚\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardVacations)
    elif call.data == 'leaveWithoutPay':
        bot.edit_message_text('Ты без проблем уходишь в отпуск, если он есть в графике на год. Мы даже '
                              'тебе напомним об этом, когда придёт время! 📅\n'
                              '\n'
                              'Во всех остальных случаях бери отпуск за свой счёт, по согласованию с '
                              'руководителем. (но он может не отпустить 🙅‍♂️)\n'
                              '\n'
                              'Образец заявления ждёт тебя в отделе кадров 👩🏼‍💻\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'dayOff':
        bot.edit_message_text('Отгулы полагаются, если ты официально\n'
                              '\n'
                              'Работал в выходные дни 📅\n'
                              '\n'
                              'Сдавал кровь 🩸\n'
                              '\n'
                              'Отгул можно взять в любой момент времени по согласованию с руководителем\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'donor':
        bot.edit_message_text('Если ты сдавал кровь - ты молодец! 😉\n'
                              '\n'
                              'Сдай квиток в отдел кадров - тебе полагается 2 дня отгула, которые ты '
                              'можешь взять в любой день года 🗓\n'
                              '\n'
                              'Только не забудь предупредить руководителя, что ты берёшь отгул!\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'sickLeaveOut':
        bot.edit_message_text('Мы принимаем бумажный и электронный больничный лист\n'
                              '\n'
                              '📄 Бумажный сдаётся в отдел кадров лично\n'
                              '\n'
                              '✉️ Для сдачи электронного больничного в отдел кадров, тебе нужен скриншот из '
                              'ГосУслуг или фотография этого больничного из поликлиники\n'
                              '\n'
                              '‼️ В день открытия больничного, сообщи об этом руководителю\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageVacations)
    elif call.data == 'differentiation':
        bot.edit_message_text('Ежегодный отбор кадрового резерва на вышестоящие должности компании 🎩\n'
                              '\n'
                              'Отбор проводит экспертная комиссия по единым оценочным листам 📄\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardDifferentiation)
    elif call.data == 'whenFeedack':
        bot.edit_message_text('Результаты утверждает генеральный директор предприятия, доводит их до твоего директора, '
                              'а потом они доходят до тебя 🧘\n'
                              '\n'
                              'Если этого по какой-то причине не случилось, попроси об этом сам своего '
                              'руководителя или HR-a 🙋🏼‍♂️\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDifferentiation)
    elif call.data == 'expertCommission':
        bot.edit_message_text('Состав комиссий всегда знает того, кого оценивает:\n'
                              '\n'
                              '- Твой директор\n'
                              '- Твой руководитель\n'
                              '- Менеджер по РПС\n'
                              '- HR менеджер\n'
                              '- Кто-то из твоих коллег\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageDifferentiation)
    elif call.data == 'mentoring':
        bot.edit_message_text('Наставник твой друг, мать и сержант 💂🏼‍♂️\n'
                              '\n'
                              'Он отвечает за твоё обучение и адаптацию в первые 3 месяца\n'
                              '\n'
                              'Если ты сам захочешь стать наставником, будет круто!\n'
                              'Пиши сюда\n'
                              '✉️ hr-feedback@energomera.ru\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardMentoring)
    elif call.data == 'failureMentor':
        bot.edit_message_text('Если твоего наставника нет на месте, его замещает твой руководитель\n'
                              '\n'
                              'Со всеми вопросами иди к нему 👨🏼‍🎓\n'
                              '\n'
                              'Если он не помог, обращайся к HR-у 💡\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'editMentor':
        bot.edit_message_text('Если ты видишь, что вам с наставником не по пути, обратись к HR-у. Он поможет ✋\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'feedbackMentor':
        bot.edit_message_text('Ежемесячно HR будет узнавать, как у вас дела\n'
                              '\n'
                              'Но если хочешь, можешь оставить свой отзыв на наставника по адресу\n'
                              '\n'
                              '✉️hr-feedback@energomera.ru\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageMentoring)
    elif call.data == 'study':
        bot.edit_message_text('Все об освоении профессии и дальнейшем росте 🧑‍🎓👨‍🎓\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardStudy)
    elif call.data == 'failureStudy':
        bot.edit_message_text('Если ты пришел на занятие, а преподаватель опаздывает уже на 5 минут - сообщи HR-у ☝️\n'
                              '\n'
                              'Если занятие все же не состоялось, то уточни у HR-а когда будет следующее 👉\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'training':
        bot.edit_message_text('Раз в 3 месяца формируются планы на сторонние и дополнительные обучения.\n'
                              'Если ты видишь, что тебе для работы необходимо попасть на конкретное обучение, '
                              'то согласуй его с руководителем для внесения в план.\n'
                              '\n'
                              'Если ты хочешь поработать на смежном участке, то обсуди это с руководителем. '
                              'Если он одобрит, то HR выдаст тебе программу обучения и закрепит за тобой наставника.\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'remoteStudyPortal':
        bot.edit_message_text('На работе слишком много задач, чтобы учиться?\n'
                              'Наш портал обучения доступен и из дома (кроме книжной библиотеки).\n'
                              '\n'
                              'Для доступа к внешнему порталу обучения обратись к HR-у - он поможет.\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'absenteeism':
        bot.edit_message_text('Уведоми HR-а о том, что не сможешь посетить занятие. Он подберет другую '
                              'дату и время 👍\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'QualificationCommission':
        bot.edit_message_text('После 3-х месяцев освоения специальности с наставником, компания хочет проверить '
                              'твои знания и готовность к самостоятельной работе\n'
                              '\n'
                              'Оценка проводится в формате комиссии, где присутствуют:\n'
                              '- Твой директор\n'
                              '- Твой руководитель\n'
                              '- Наставник\n'
                              '- HR\n'
                              '\n'
                              'Ответь на вопросы комиссии и получи допуск к самостоятельной работе. '
                              'Для этого лишь нужно знать свои прямые обязанности и рассказать, '
                              'что ты освоил за прошедшее время.\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardQualificationCommission)
    elif call.data == 'docListQualification':
        bot.edit_message_text('Ты готовишь:\n'
                              '- заполненную программу обучения\n'
                              '- отметку о сдаче экзамена по СМК\n'
                              '- презентацию о проделанной работе\n'
                              '\n'
                              'Руководитель готовит Cправку об эффективности по рабочей инструкции\n'
                              '\n'
                              'HR готовит Протокол комиссии и добрые слова\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardBackQualificationCommission)
    elif call.data == 'lostQualificationCommission':
        bot.edit_message_text('Если ты не успел подготовиться к комиссии - значит ты не готов к '
                              'самостоятельной работе.\n'
                              'Трех месяцев не хватило, чтобы все освоить или чтобы сделать документы?\n'
                              '\n'
                              'Если не успел сделать документы - скорее все сдавай, нет смысла откладывать\n'
                              '\n'
                              'Если ты реально что-то не успел выучить, скажи об этом наставнику или HR-у.\n'
                              'Если ты болел или наставник был недоступен, то мы продлим срок подготовки '
                              'до 2 недель.\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardPageStudy)
    elif call.data == 'testEmployee':
        bot.edit_message_text('Для получения обратной связи по результатам тестирования необходимо обратиться к '
                              'менеджеру по оценке персонала с запросом. 📝\n '
                              '\n'
                              'На почту по адресу - resume@energomera.ru  направить сообщение с запросом  и указать '
                              'свои контактные данные.\n '
                              '\n'
                              'В течение 2-3 рабочих дней с Вами свяжутся и назначат дату и время консультации 🙋🏼‍♀️',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardBackEmployee)
    elif call.data == 'covid19':
        bot.edit_message_text('Надеемся, что тебе просто интересно 🔎\n'
                              '\n'
                              'Из важного\n'
                              '\n'
                              '- Носи маску\n'
                              '- Мой руки\n'
                              '- Держи дистанцию\n'
                              '- Мерь температуру на входе\n'
                              '- При недомогании останься дома и позвони руководителю\n'
                              '\n'
                              'Если это всё-таки случилось, скорее выздоравливай! 💙\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardCovid19)
    elif call.data == 'referal':
        bot.edit_message_text('Ты наш герой, если рекомендуешь нас друзьям! 🦸‍♂️\n'
                              '\n'
                              'Поделись с ними нашими вакансиями\n'
                              '➡️ http://energomera.com/career\n'
                              '\n'
                              'Будем благодарны 🙌\n',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardBackEmployee)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text:
        bot.send_message(message.chat.id, 'Чтобы запустить бот используй команду\n'
                                          '➡️ /start')


if __name__ == '__main__':
    bot.polling(none_stop=True)