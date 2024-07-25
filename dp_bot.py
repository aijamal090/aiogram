from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token='7060288127:AAFIqP6HL1siXQuJohVZu6sAEyO3ymAgY_A')
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Товары'),
    types.KeyboardButton('Заказать'),
    types.KeyboardButton('Контакты'),
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'Здравствуйте,  {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message:types.Message):
    await message.reply("tehno_shop — это  интернет магазин по продаже различных смартфонов")

@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.answer(f'{message.from_user.full_name}, вот нащи контакты: ')
    await message.answer_contact("+996552110212", "Aijamal", "Kadyrova")
    await message.answer_contact("+996999689828", "Gulnara", "Kadyrova")

@dp.message_handler(text="Заказать")
async def order(message:types.Message):
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:types.Message):
    # await message.answer(message)
    await bot.send_message(6490369099, f'Новый заказ:\nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nUsername пользователя: {message.from_user.username}\nТелефон: {message.contact.phone_number}\n')
    await message.answer("Спасибо что зделали заказ\nМы свяжемся с вами в скором времени!")
    await start(message)


course = [
    types.KeyboardButton("Apple"),
    types.KeyboardButton("Samsung"),
    types.KeyboardButton("Xiaomi"),
    types.KeyboardButton("Redmi"),
    types.KeyboardButton("Nokia"),  
]

courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*course)

@dp.message_handler(text='Товары')
async def about(message: types.Message):
    await message.answer("Вот наши товары:", reply_markup=courses_keyboard)

@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await start(message)

@dp.message_handler(text='Samsung Galaxy s24 ultra')
async def back(message:types.Message):
    await message.reply("""https://login.kg/phones/samsung/samsung-galaxy-s24-ultra-5g-12-256gb-eu""")
    await message.answer("74500")
    
    @dp.message_handler(text='Apple 15 pro max,256 гб')
async def back(message:types.Message):
    await message.reply("""https://asiastore.kg/apple-iphone/iphone-15-pro-max/iphone-15-pro-max-256-gb-natural-titanium
""")
    await message.answer("128990")
    
    @dp.message_handler(text='Xiaomi 14gb+512gb')
async def back(message:types.Message):
    await message.reply("""https://asiastore.kg/apple-iphone/iphone-15-pro-max/iphone-15-pro-max-256-gb-natural-titanium
""")
    await message.answer("86000")

    @dp.message_handler(text='Redmi not 13(8+256)')
async def back(message:types.Message):
    await message.reply("""https://www.gadget.kg/catalog/telefony/xiaomi/6630
""")
    await message.answer("86000")

    @dp.message_handler(text='Nokia C50 4+65gb ')
async def back(message:types.Message):
    await message.reply("""https://www.gadget.kg/catalog/telefony/xiaomi/6630
""")
    await message.answer("2300000")
