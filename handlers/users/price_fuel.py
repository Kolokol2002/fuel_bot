#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline import inline_back
from loader import dp


@dp.message_handler(Text(equals='Ціна топлива', ignore_case=True))
async def price_fuel(message: types.Message):
    try:
        import requests
        from bs4 import BeautifulSoup

        url = 'https://auto.ria.com/uk/toplivo/okko/'

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        }

        list_for_fuels = ['95 pulls', '95 Євро', '92 Євро', 'ДП Євро', 'Газ']

        response = requests.get(url, header)

        soup = BeautifulSoup(response.text, 'lxml')

        result = soup.find_all('div', class_='t-cell bold size18')
        price = []
        for i in result:
            text = i.text
            price.append(text)

        await message.answer(f'{list_for_fuels[0]} - {price[0]}\n'
                             f'{list_for_fuels[1]} - {price[2]}\n'
                             f'{list_for_fuels[2]} - {price[2]}\n'
                             f'{list_for_fuels[3]} - {price[3]}\n'
                             f'{list_for_fuels[4]} - {price[4]}\n', reply_markup=inline_back)
    except Exception as exc:
        await message.answer(exc)
