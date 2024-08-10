from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import schedule
import time
import requests

bot = Bot(token=tocen)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Я бот для покупок. Вы можете искать товары, сравнивать цены и оформлять заказы.")

@dp.message_handler(commands=['search'])
async def search_product(message: types.Message):
    product_name = message.get_args()
    await message.reply(f"Результаты поиска для '{product_name}':\n1. Товар A - $100\n2. Товар B - $200")

@dp.message_handler(commands=['order'])
async def order_product(message: types.Message):
    product_name = message.get_args()
    await message.reply(f"Вы оформили заказ на '{product_name}'.")

    executor.start_polling(dp, skip_updates=True)
