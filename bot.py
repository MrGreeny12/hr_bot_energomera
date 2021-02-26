from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    '''
    стартовое сообщение при запуске бота
    '''
    await message.reply('Привет! Я чат-бот HR-службы Энергомера. Пока я работаю в тестовом режиме, '
                        'но ты можешь для начала, рассказать, кто ты!', reply_markup=kb.keyboardWelcome)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    '''
    информация о функциях бота. запускается командой /help
    '''
    await message.reply('Запусти меня - напиши /start')


@dp.callback_query_handler(lambda c: c.data == 'candidate')
async def process_callback_candidate(callback_query: types.CallbackQuery):
    '''
    меню кандидата
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Это раздел для соискателей. Все самые распространнёные '
                                                        'ответы на вопросы Вы можете найти в разделе FAQ. Ссылки на '
                                                        'наши социальные сети Вы можете найти в соответствующем '
                                                        'разделе', reply_markup=kb.keyboardCandidate)


@dp.callback_query_handler(lambda c: c.data == 'faq')
async def process_callback_candidate_faq(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите интересующий Вас вопрос:',
                           reply_markup=kb.keyboardFAQ)


@dp.callback_query_handler(lambda c: c.data == 'steps')
async def process_callback_candidate_faq_steps(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> этапы собеседования
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Здесь мы подробно распишем этапы рассмотрения, например:\n'
                           '1. Офигенный этап.\n'
                           '2. Ещё лучше.\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')


@dp.callback_query_handler(lambda c: c.data == 'testResult')
async def process_callback_candidate_faq_testResult(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> узнать результаты тестирования
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Здесь мы подробно расскажем о том, как узнать результаты тестирования:\n'
                           '1. Позвонить туда.\n'
                           '2. Спросить сюда.\n'
                           '3. Пойти на хер например. Уж больно ты любопытный.\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')


@dp.callback_query_handler(lambda c: c.data == 'feedback')
async def process_callback_candidate_faq_feedback(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> дать обратную связь
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Давай, пёс. Расскажи, что тебе не понравилось!\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')
    #нужно добавить форму обратной связи для записи. после этого вывести сообщение типа: заебись, принято!

@dp.callback_query_handler(lambda c: c.data == 'testTrouble')
async def process_callback_candidate_faq_testTrouble(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> проблемы с прохождением тестированияы
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Не получается пройти тестирование? Значит ты довольно тупой. Пшёл отсюда!\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')
    # нужно добавить базовые варианты при некорректной работе тестирования и форму обратной связи для возможности
    # прикреплять файл и сообщение


@dp.callback_query_handler(lambda c: c.data == 'docList')
async def process_callback_candidate_faq_docList(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> список документов для приёма
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Вот, что нужно для приёма на работу:\n'
                           '1. Счастье.\n'
                           '2. Здоровье.\n'
                           '3. Удача.\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')
    # нужно добавить список документов, которые требуются.


@dp.callback_query_handler(lambda c: c.data == 'studentsPractice')
async def process_callback_candidate_faq_studentsPractice(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> информация для прохождения практики студентов
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Вот, что нужно для попадания на практику:\n'
                           '1. Счастье.\n'
                           '2. Здоровье.\n'
                           '3. Удача.\n'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')
    # нужно добавить список шагов, которые требуются.


@dp.callback_query_handler(lambda c: c.data == 'sendResume')
async def process_callback_candidate_faq_sendResume(callback_query: types.CallbackQuery):
    '''
    меню кандидата -> faq -> отправить своё резюме
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'А здесь, пёс, ты должен приложить своё сраное резюме, чтобы оно дошло к нам. '
                           'Прикладывай как подоржник к оторванной руке. '
                           'Это настолько же эффективно. Тебе уже ничего не поможет.'
                           '\n'
                           'Для возвращения в начало, нажмите на -> /start')
    # нужно добавить возможность прикладывать резюме и отправку его девчёнкам или в какой-нибудь чат.


if __name__ == '__main__':
    executor.start_polling(dp)
