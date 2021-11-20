import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

import keyb as kb
from config import BOT_TOKEN

import requests # For Http requests
from bs4 import BeautifulSoup # For working with Html Script

URL = "https://www.tinkoff.ru/invest/currencies/" # Url of parsing page
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
           'accept': '*/*'} # Headers that will be sended to the page
Name = ""
Price = ""

def get_Html(url, params = None):
    result = requests.get(url, headers=HEADERS, params=params) # Making Http request
    return result

def get_CurrencyContent(source):
    global Name
    global Price
    soup = BeautifulSoup(source.text, "html.parser")
    Currency = soup.find_all('a', {"href": '/invest/currencies/USDRUB/'})

    item = Currency[0]
    Name = item.find('span', {"class": "NameColumn__nameWrapper_LWKdK"}).get_text() # Writing the Name of currency
    item = Currency[2]
    Price = item.find(("span", {"class": "Money-module__money_UwC2N"})).get_text() # Writing the Price of currency

    #print(Name)
    #print(Price)

def parse():
    Html_script = get_Html(URL) # Writing Html Script in variable

    if Html_script.status_code == 200:
        get_CurrencyContent(Html_script) # Calling function that getting data
    else:
        print("Request failed") # Error




loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

Curr_Ticker = ""

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, пожалуйста зарегестрируйтесь или войдите. (Внимание вы запишитесь как {0.username} и если у вас нет аккаунта зарегистрируйтесь! Если вы зарегистрировались но у вас еть аккаун просто нажмите выход! Если вы просто так нажмёте "Регистрация" и у вас есть аккаунт из-за этого у вас откроется новое окно и оно не будет сохронять ввод. Если у вас нет аккаунта и вы нажмёте "Вход" вы не сохранитесь и мы не сможем вернуть данные!)'.format(message.from_user), reply_markup=kb.Mnum_1)


@dp.message_handler(commands=['registration'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'регистрация'.format(message.from_user))
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()

    if (cur.execute('SELECT *FROM Users WHERE username = "{0.username}";'.format(message.from_user))):
        await bot.send_message(message.from_user.id, 'У вас уже есть аккаунт!'.format(message.from_user, reply_markup=kb.Mnum_2))
    else:
        await bot.send_message(message.from_user.id, 'Введите "/Регистрация"'.format(message.from_user), reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['login'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вход!'.format(message.from_user))
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()

    if (cur.execute('SELECT *FROM Users WHERE username = "{0.username}";'.format(message.from_user))):
        await bot.send_message(message.from_user.id, 'Введите "/Войти"'.format(message.from_user))
    else:
        await bot.send_message(message.from_user.id, 'Зарегистрируйтесь!'.format(message.from_user))

@dp.message_handler(commands=['Войти'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['registration'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте {0.username}!'.format(message.from_user), reply_markup=kb.Mnum_2)

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

@dp.message_handler(commands=['📈_Крипто'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Цены на крипту! (Внимание цены в 💵!)', reply_markup=kb.MKnum)

@dp.message_handler(commands=['Крипто'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости по крипте!', reply_markup=kb.MnBitcoin_2)

@dp.message_handler(commands=['Назад'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Назад!', reply_markup=kb.Mnum_2)

@dp.message_handler(commands=['⚙_Настройки'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Настройки', reply_markup=kb.Mse)

@dp.message_handler(commands=['Bitcoin'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bitcoin!', reply_markup=kb.MBitcoin)

@dp.message_handler(commands=['Bitcoin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Bitcoin! https://ru.investing.com/crypto/bitcoin/news', reply_markup=kb.MnBitcoin_3)

@dp.message_handler(commands=['Ethereum'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ethereum!', reply_markup=kb.MEthereum)

@dp.message_handler(commands=['Ethereum_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Ethereum! https://ru.investing.com/crypto/ethereum/news', reply_markup=kb.MNEthereum)

@dp.message_handler(commands=['Binance_Coin_News'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Новости о Binance Coin! https://ru.investing.com/crypto/binance-coin/news', reply_markup=kb.MNBinance_Coin)

@dp.message_handler(commands=['📈_Акции'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите тикет Акции!', reply_markup=kb.Ak)

@dp.message_handler(commands=['💵_Валюты'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Валюты!', reply_markup=kb.NM)

@dp.message_handler(commands=['рубль_доллор'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.NM_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "USDRUB"

@dp.message_handler(commands=['рубль_юань'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.NM_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "CNYRUB"

@dp.message_handler(commands=['рубль_евро'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.back)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "EURRUB"

@dp.message_handler(commands=['рубль_Швейцарский_Франк'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.NM_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "CHFRUB"

@dp.message_handler(commands=['рубль_Фунт'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.NM_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "GBPRUB"

@dp.message_handler(commands=['рубль_Иена'])
async def process_hello(message: types.Message):
    global Curr_Ticker
    parse()
    await bot.send_message(message.from_user.id, Price, reply_markup=kb.NM_2)
    conn = sqlite3.connect('People.db')
    cur = conn.cursor()
    Curr_Ticker = "JPYRUB"

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
