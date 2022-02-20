from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from data_base import sqlite_db
from loader import dp
from aiogram.dispatcher.filters import Text

from keyboards.inline import inline_back
from keyboards.default import def_kb

from states import For_km_rgn_fuel
from loader import bot
import requests
from bs4 import BeautifulSoup



cost_fuel = None

def cost_fuel_def(id):

    time_out = 5
    url = 'https://auto.ria.com/uk/toplivo/brsm-nafta/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    while 1 > 0:
        req = requests.get(url, headers)

        text = req.content

        soup = BeautifulSoup(text, 'lxml')

        find_text = soup.find(class_='bold pl20 t-cell mhide480 dt').find_all('span')
        cost_fuel = find_text[0].text
        bot.send_message(chat_id=id, text=f'Ціна: {cost_fuel}')
        sleep(time_out)


@dp.message_handler(Text(equals='✅Ціна топлива', ignore_case=True))
async def cost_fuel(message: types.Message):

    cost_fuel_def(message.message_id)

    await message.answer(f'Ціна БРСМ-Нафта ДП: {cost_fuel}', reply_markup=inline_back)
