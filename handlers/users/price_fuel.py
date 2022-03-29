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

    url = 'https://www.okko.ua/fuels'

    options = webdriver.ChromeOptions()
    options.set_capability('general.useragent.override',
                           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')


    driver = webdriver.Chrome(
        executable_path="chromedriver",
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