import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

import keyb as kb
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, пожалуйста зарегестрируйтесь или войдите. (Внимание вы запишитесь как {0.username} и если у вас нет аккаунта зарегистрируйтесь из-за этого ваши настройки не сохранятся и мы их не сложем вернуть!)'.format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['регистрация_📃'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)
    conn = sqlite3.connect('People.db')

    cur = conn.cursor()

    cur.execute('INSERT INTO Users VALUES ("{0.username}", NULL, "{0.id}");'.format(message.from_user))
    conn.commit()

@dp.message_handler(commands=['Вход_📄'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)
    conn = sqlite3.connect('users.db')
    '''
    cur = conn.cursor()

    cur.execute('SELECT *FROM Users WHERE username = "Programmer_f" AND userid = "1350804202";'.format(message.from_user))
    conn.commit()
    '''
@dp.message_handler(commands=['регистрация_📃'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)


@dp.message_handler(commands=['курсы_валют_📈'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот список валют!'.format(message.from_user), reply_markup=kb.Mnum_3)

@dp.message_handler(commands=['Выход_🚪'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выход из аккаунта!'.format(message.from_user), reply_markup=kb.Mnum_1)

@dp.message_handler(commands=['доллар_руб_💵'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'этого нету пока что.', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['📰_Новости'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот сводка новостей', reply_markup=kb.MNews)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
