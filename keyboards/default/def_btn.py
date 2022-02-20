from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('✅Км'),
    KeyboardButton('✅Грн'),
    KeyboardButton('✅Літрів'),
    KeyboardButton('✅Ціна топлива'),
    KeyboardButton('Разход', ),
]

def_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,)
def_kb.add(*btn)

