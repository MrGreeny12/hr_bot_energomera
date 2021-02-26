import telebot
from telebot import types
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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'kb.keyboardWelcome':
        bot.edit_message_text('Привет! Я чат-бот HR-службы Энергомера. Пока я работаю в тестовом режиме, '
                              'но ты можешь для начала, рассказать, кто ты!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=kb.keyboardWelcome)
    elif call.data == 'employee':
        next_menu = types.InlineKeyboardMarkup()
        key3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='key3')
        back = types.InlineKeyboardButton(text='Назад', callback_data='kb.keyboardWelcome')
        next_menu.add(key3, back)
        bot.edit_message_text('Это раздел для сотрудников. Он пока не работает',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=next_menu)
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


bot.polling()