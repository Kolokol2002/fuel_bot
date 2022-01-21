from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('✅Км'),
    KeyboardButton('✅Грн'),
    KeyboardButton('Разход'),
]

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, )
kb.add(*btn)