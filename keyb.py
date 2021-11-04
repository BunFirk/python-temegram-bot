from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnnum_1 = KeyboardButton("/Регистрация_📃")
btnnum_7 = KeyboardButton("/Вход_📄")
Mnum_1 = ReplyKeyboardMarkup().add(btnnum_1).add(btnnum_7)

btnnum2 = KeyboardButton("/Курсы_валют_📈")
btnnum3 = KeyboardButton("/📰_Новости")
btnnum4 = KeyboardButton("Текст")
btnnum5 = KeyboardButton("/Выход_🚪")
Mnum_2 =ReplyKeyboardMarkup(resize_keyboard = True).add(btnnum2).add(btnnum3).add(btnnum4).add(btnnum5)

btnnum6 = KeyboardButton("/Доллар_руб_💵")
Mnum_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum6)

btnnum8 = KeyboardButton("/Валюты")
btnnum9 = KeyboardButton("/Нефть и газ")
btnnum10 = KeyboardButton("/Крипто")
MNews = ReplyKeyboardMarkup(resize_keyboard=True).add(btnnum8).add(btnnum9).add(btnnum10)
