#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    KeyboardButton('✅Км'),
    KeyboardButton('✅Грн'),
    KeyboardButton('✅Літрів'),
    KeyboardButton('⚙Разход', ),
    KeyboardButton('⛽Ціна топлива', ),
]

def_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,)
def_kb.add(*btn)

