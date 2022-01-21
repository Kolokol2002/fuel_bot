from aiogram import types
from aiogram.dispatcher import FSMContext

from data_base import sqlite_db
from loader import dp
from aiogram.dispatcher.filters import Text

from keyboards.inline import inline_kb
from keyboards.default import kb

from states import For_Answer


@dp.message_handler(Text(equals=['✅Км', '✅Грн'], ignore_case=True))
async def km_and_grn(message: types.Message):
    if message.text == '✅Км':
        await message.answer('Напишіть кілометри:')
        await For_Answer.km.set()

    elif message.text == '✅Грн':
        await message.answer('Напишіть скільки гривень ви готові витратити:')
        await For_Answer.grn.set()


@dp.message_handler(state=For_Answer.km)
async def km_2(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        list_cost_middle = await sqlite_db.sql_give_middle_and_cost(message)
        medium_fuel = int(list_cost_middle[0])
        cost_fuel = int(list_cost_middle[1])
        fuel_res = round((medium_fuel * int(message.text)) / 100, 1)
        rgn_res = round(fuel_res * cost_fuel, 1)
        await message.reply(f'Грн: {rgn_res}\nТоплива: {fuel_res}', reply_markup=inline_kb)

    else:
        await message.reply('Це не ціле число!', reply_markup=inline_kb)


@dp.message_handler(state=For_Answer.grn)
async def grn_2(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        list_cost_middle = await sqlite_db.sql_give_middle_and_cost(message)
        print(list_cost_middle)
        medium_fuel = int(list_cost_middle[0])
        cost_fuel = int(list_cost_middle[1])
        fuel_res = round(int(message.text) / cost_fuel, 1)
        km_res = round((fuel_res * 100) / medium_fuel, 1)
        await message.reply(f'Км: {km_res}\nЛітрів: {fuel_res}', reply_markup=inline_kb)

    else:
        await message.reply('Це не ціле число!', reply_markup=inline_kb)


@dp.callback_query_handler(text='back', state=[For_Answer.km, For_Answer.grn])
async def next_keyboard(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='🔙Назад', reply_markup=kb)

    await state.finish()



