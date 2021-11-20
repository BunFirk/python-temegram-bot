from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Back = KeyboardButton("/Назад")

btnnum_1 = KeyboardButton("/registration")
btnnum_7 = KeyboardButton("/login")
Mnum_1 = ReplyKeyboardMarkup().add(btnnum_1).add(btnnum_7)

btnnum2 = KeyboardButton("/Курсы_валют_📈")
btnnum3 = KeyboardButton("/📰_Новости")
btnnum4 = KeyboardButton("/⚙_Настройки")
btnnum21 = KeyboardButton("/📈_Акции")
Mnum_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum2).add(btnnum3).add(btnnum21).add(btnnum4)

btnnum6 = KeyboardButton("/📈_Крипто")
btnnum14 = KeyboardButton("/💵_Валюты")
Mnum_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum6).add(btnnum14).add(Back)

btnnum8 = KeyboardButton("/Валюты")
btnnum9 = KeyboardButton("/Нефть и газ")
btnnum10 = KeyboardButton("/Крипто")
MNews = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum8).add(btnnum9).add(btnnum10).add(Back)

btnnum11 = KeyboardButton("/Ethereum")
btnnum12 = KeyboardButton("/Bitcoin")
btnnum13 = KeyboardButton("/Binance_Coin")
MKnum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum11).add(btnnum12).add(btnnum13).add().add(Back)

btnnum23 = KeyboardButton("/Узнать_цену_Bitcoin")
btnnum18 = KeyboardButton("/Вывести_график_Bitcoin")
MBitcoin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum18).add(btnnum23).add(Back)

btnnum5 = KeyboardButton("/Выход_🚪")
btnnum20 = KeyboardButton("/Текст")
Mse = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum20).add(btnnum5).add(Back)

MNBitcoin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum23).add(Back)

btnnum22 = KeyboardButton("/Bitcoin_News")
btnnum26 = KeyboardButton("/Ethereum_News")
btnnum27 = KeyboardButton("/Binance_Coin_News")
MnBitcoin_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum22).add(btnnum26).add(btnnum27).add(Back)


MnBitcoin_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum23).add(Back)

btnnum24 = KeyboardButton("/Узнать_цену_Ethereum")
btnnum25 = KeyboardButton("/Вывести_график_Ethereum")
MEthereum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum24).add(btnnum25).add(Back)

MNEthereum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum24).add(Back)

btnnum28 = KeyboardButton("/Узнать_цену_Binance_Coin")
MNBinance_Coin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum28).add(Back)


Ak = ReplyKeyboardMarkup(resize_keyboard=True).add(Back)

btnnum29 = KeyboardButton("/рубль_доллор")
btnnum30 = KeyboardButton("/рубль_юань")
btnnum31 = KeyboardButton("/рубль_евро")
btnnum32 = KeyboardButton("/рубль_Швейцарский_Франк")
btnnum33 = KeyboardButton("/рубль_Фунт")
btnnum34 = KeyboardButton("/рубль_Иена")
NM = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum29).add(btnnum30).add(btnnum31).add(Back)

btnnum35 = KeyboardButton("/Узнать цену ещё раз")
NM_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum35).add(Back)

back = ReplyKeyboardMarkup(resize_keyboard=True).add(Back)
