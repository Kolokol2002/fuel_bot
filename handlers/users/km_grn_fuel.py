from aiogram import types
from aiogram.dispatcher import FSMContext

from data_base import sqlite_db
from loader import dp
from aiogram.dispatcher.filters import Text

from keyboards.inline import inline_back
from keyboards.default import def_kb

from states import For_km_rgn_fuel


@dp.message_handler(Text(equals=['✅Км', '✅Грн', '✅Літрів'], ignore_case=True))
async def km_grn_fuel(message: types.Message):
    if message.text == '✅Км':
        await message.answer('Напишіть кілометри:')
        await For_km_rgn_fuel.km.set()

    elif message.text == '✅Грн':
        await message.answer('Напишіть скільки гривень ви готові витратити:')
        await For_km_rgn_fuel.grn.set()

    elif message.text == '✅Літрів':
        await message.answer('Напишіть скільки літрів розрахувати:')
        await For_km_rgn_fuel.fuel.set()


@dp.message_handler(state=For_km_rgn_fuel.km)
async def km(message: types.Message, state: FSMContext):
    try:
        list_cost_middle = await sqlite_db.sql_read(message)
        medium_fuel = float(list_cost_middle[2])
        cost_fuel = float(list_cost_middle[3])
        fuel_res = round((medium_fuel * int(message.text)) / 100, 1)
        rgn_res = round(fuel_res * cost_fuel, 1)
        await message.reply(f'Грн: {rgn_res}\nТоплива: {fuel_res}', reply_markup=inline_back)


    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)


@dp.message_handler(state=For_km_rgn_fuel.grn)
async def grn(message: types.Message, state: FSMContext):
    try:
        list_cost_middle = await sqlite_db.sql_read(message)
        medium_fuel = float(list_cost_middle[2])
        cost_fuel = float(list_cost_middle[3])
        fuel_res = round(float(message.text) / cost_fuel, 1)
        km_res = round((fuel_res * 100) / medium_fuel, 1)
        await message.reply(f'Км: {km_res}\nЛітрів: {fuel_res}', reply_markup=inline_back)

    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)

@dp.message_handler(state=For_km_rgn_fuel.fuel)
async def fuel(message: types.Message, state: FSMContext):
    try:
        list_cost_middle = await sqlite_db.sql_read(message)
        medium_fuel = float(list_cost_middle[2])
        cost_fuel = float(list_cost_middle[3])
        rgn_res = round(float(message.text) * cost_fuel, 1)
        km_res = round((float(message.text) * 100) / medium_fuel, 1)
        await message.reply(f'Км: {km_res}\nГрн: {rgn_res}', reply_markup=inline_back)

    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)


@dp.callback_query_handler(text='back', state='*')
async def next_keyboard(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='🔙Назад', reply_markup=def_kb)

    await state.finish()



