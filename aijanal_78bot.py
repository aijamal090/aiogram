import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tocen)
dp = Dispatcher(bot)

def get_laptops():
    url = 'https://www.sulpak.kg/f/noutbuki'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    for item in soup.select('.product__item-inner'):
        title_element = item.select_one('.product__item-name a')
        price_element = item.select_one('.product__item-price')
        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True).replace('сом', '').strip()
            laptops.append({'title': title, 'price': price})

    return laptops
манды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Используйте команду /laptops, чтобы получить список ноутбуков.")

@dp.message_handler(commands=['laptops'])
async def send_laptops(message: types.Message):
    laptops = get_laptops()
    if not laptops:
        await message.reply("Не удалось получить данные о ноутбуках.")
    else:
        for laptop in laptops:
            await message.reply(f"{laptop['title']}\nЦена: {laptop['price']} сом")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
