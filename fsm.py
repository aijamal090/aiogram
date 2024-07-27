from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import token
from database import Database
import logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('sql.db')
db.create_table()
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    username = State() 

@dp.message_handler(commands='start')
async def start(message:Message):
    await Form.username.set()
    await message.reply("Привет! Как тебя зовут ?")
    
@dp.message_handler(state=Form.username)
async def process_username(message:Message, state: FSMContext):
    username = message.text
    db.add_user(message.from_user.id, username)
    await state.finish()
    await message.reply(f'Приятно познакомиться, {username}')
    
@dp.message_handler(commands='me')
async def get_me(message:Message):
    user = db.get_user(message.from_user.id)
    if user:
        await message.reply(f'Ты зарегистрирован как {user[2]}')
    else:
        await message.reply("Ты еще не зарегистрирован")
    
async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command='/start', description='Start bot'),
        BotCommand(command='/me', description='Info me')
    ])
    logging.info("Настройки базы данных")
    db.create_table()
    logging.info("База загружена")
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)



from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import token
from database import Database
import logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('sql.db')
db.create_table()
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    username = State()
    age = State()

@dp.message_handler(commands='start')
async def start(message: Message):
    await Form.username.set()
    await message.reply("Привет! Как тебя зовут ?")

@dp.message_handler(state=Form.username)
async def process_username(message: Message, state: FSMContext):
    username = message.text
    await state.update_data(username=username)
    await Form.next()  
    await message.reply('Сколько тебе лет?')

@dp.message_handler(state=Form.age)
async def process_age(message: Message, state: FSMContext):
    age = message.text
    user_data = await state.get_data()
    username = user_data.get('username')
    db.add_user(message.from_user.id, username, age)  
    await state.finish()
    await message.reply(f'Приятно познакомиться, {username}. Твой возраст: {age}')

@dp.message_handler(commands='me')
async def get_me(message: Message):
    user = db.get_user(message.from_user.id)
    if user:
        markup = InlineKeyboardMarkup()
        back_button = InlineKeyboardButton("Назад", callback_data="back")
        markup.add(back_button)
        await message.reply(f'Ты зарегистрирован как {user[2]}, возраст: {user[3]}', reply_markup=markup)
    else:
        await message.reply("Ты еще не зарегистрирован")

@dp.callback_query_handler(lambda c: c.data == 'back')
async def process_callback_back(callback_query: CallbackQuery):
    await Form.username.set()
    await callback_query.message.reply("Привет! Как тебя зовут?")

async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command='/start', description='Start bot'),
        BotCommand(command='/me', description='Info me')
    ])
    logging.info("Настройки базы данных")
    db.create_table()
    logging.info("База загружена")

executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
