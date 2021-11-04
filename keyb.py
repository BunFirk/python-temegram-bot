from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Back = KeyboardButton("/Назад")

btnnum_1 = KeyboardButton("/Регистрация_📃")
btnnum_7 = KeyboardButton("/Вход_📄")
Mnum_1 = ReplyKeyboardMarkup().add(btnnum_1).add(btnnum_7)

btnnum2 = KeyboardButton("/Курсы_валют_📈")
btnnum3 = KeyboardButton("/📰_Новости")
btnnum4 = KeyboardButton("/⚙_Настройки")
btnnum21 = KeyboardButton("Текст")
Mnum_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum2).add(btnnum3).add(btnnum4)

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
btnnum17 = KeyboardButton("/hash_token")
MKnum = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum11).add(btnnum12).add(btnnum13).add().add(Back)

btnnum19 = KeyboardButton("/Узнать цену")
btnnum18 = KeyboardButton("/Вывести график")
MBitcoin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum18).add(btnnum19).add(Back)

btnnum5 = KeyboardButton("/Выход_🚪")
btnnum20 = KeyboardButton("/Частота_отправки_цены")
Mse = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum20).add(btnnum5).add(Back)
