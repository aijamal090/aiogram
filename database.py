from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import logging
import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    username TEXT
                )
            """)
            
    def add_user(self, user_id, username):
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    
    def get_user(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            return self.cursor.fetchone()

db = Database('database.db')
db.create_table()

token = '7414989713:AAFgoakiyyPL-ZVtIstDSjK-x9SAUfomHIM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

class Form(StatesGroup):
    username = State()
    age = State()

@dp.message_handler(commands='start', state='*')
async def start(message: types.Message):
    await Form.username.set()
    await message.answer("Привет! Как тебя зовут?")

@dp.message_handler(state=Form.username)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await Form.next()
    await message.answer("Сколько тебе лет?")

@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    db.add_user(message.from_user.id, data['username'])
    
    await message.answer(f"Тебя зовут {data['username']} и тебе {data['age']} лет.")
    await state.finish()

@dp.message_handler(commands='me')
async def me(message: types.Message, state: FSMContext):
    user = db.get_user(message.from_user.id)
    if user:
        username = user[2]
        age = user[3] if len(user) > 3 else 'Неизвестно'
    else:
        username = 'Неизвестно'
        age = 'Неизвестно'

    back_button = InlineKeyboardMarkup().add(InlineKeyboardButton("Назад", callback_data="back"))
    await message.answer(f"Твое имя: {username}\nТвой возраст: {age}", reply_markup=back_button)

@dp.callback_query_handler(lambda c: c.data == 'back')
async def back_to_name(callback_query: types.CallbackQuery, state: FSMContext):
    await Form.username.set()
    await callback_query.message.edit_text("Как тебя зовут?")

# Запуск бота
if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
