from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


button = KeyboardButton("Adminga ma'lumot jo'natish")
button1 = KeyboardButton("Buyurtma")
keyboard = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button,button1)
