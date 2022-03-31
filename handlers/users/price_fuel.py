#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram import types

from keyboards.inline import inline_back
from loader import dp
from aiogram.dispatcher.filters import Text

from bs4 import BeautifulSoup
from selenium import webdriver


@dp.message_handler(Text(equals='Ціна топлива', ignore_case=True))
async def price_fuel(message: types.Message):
    try:
        url = 'https://www.okko.ua/fuels'

        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        }

        # s = requests.Session()
        # response = s.get(url=url, headers=header)
        # time.sleep(10)
        # print(response.text)
        # await message.answer(response.text)

        options = webdriver.ChromeOptions()
        options.set_capability('general.useragent.override',
                               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')

        driver = webdriver.Chrome(
            executable_path="/home/maks_karalash/fuel_bot/chromedriver",
            options=options
        )
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        soup = soup.find_all('span', class_='price')
        price = []
        list_for_fuels = ['ДП pulls', 'ДП Євро', '95 pulls', '95 Євро', '92 Євро', 'Газ']
        for i in soup:
            text = i.text
            pars_text = text.translate(str.maketrans('', '', '\n ', ))
            price.append(f'{pars_text[:2]},{pars_text[2:]}')

        await message.answer(f'{list_for_fuels[0]} - {price[0]}\n'
                             f'{list_for_fuels[1]} - {price[2]}\n'
                             f'{list_for_fuels[2]} - {price[2]}\n'
                             f'{list_for_fuels[3]} - {price[3]}\n'
                             f'{list_for_fuels[4]} - {price[4]}\n'
                             f'{list_for_fuels[5]} - {price[5]}\n', reply_markup=inline_back)
    except Exception as exc:
        await message.answer(exc)
