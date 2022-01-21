from aiogram import types
from aiogram.dispatcher import FSMContext

from data_base import sqlite_db
from keyboards.inline import inline_back, inline_middle
from loader import dp
from aiogram.dispatcher.filters import Text

from keyboards.default import def_kb

from states import For_Set_middle_cost


@dp.message_handler(Text(equals='Разход', ignore_case=True))
async def middle(message: types.Message):

    list_value = await sqlite_db.sql_read(message)

    await message.answer(f'Ваш середній розход: {list_value[2]}\nЦіна топлива: {list_value[3]}', reply_markup=inline_middle)

@dp.callback_query_handler(text='middle')
async def keyboard_middle(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Введіть середній розхід:')
    await For_Set_middle_cost.middle.set()

@dp.callback_query_handler(text='cost')
async def keyboard_cost(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Введіть ціну на паливо:')
    await For_Set_middle_cost.cost.set()

@dp.message_handler(state=For_Set_middle_cost.middle)
async def cost_fuel(message: types.Message, state: FSMContext):
    try:
        list_values = await sqlite_db.sql_read(message)
        answer_middle_fuel = float(message.text)
        answer_cost_fuel = list_values[3]

        state_list = [message.from_user.full_name, message.from_user.id, answer_middle_fuel, answer_cost_fuel]

        await message.answer(f'Середній розхід: {answer_middle_fuel}\nЦіна топлива: {answer_cost_fuel}', reply_markup=def_kb)

        try:
            await sqlite_db.sql_add_command(state=state_list)
        except:
            await sqlite_db.sql_edit(state_list)
        await state.finish()
    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)

@dp.message_handler(state=For_Set_middle_cost.cost)
async def middle_fuel(message: types.Message, state: FSMContext):
    try:
        list_values = await sqlite_db.sql_read(message)
        answer_middle_fuel = list_values[2]
        answer_cost_fuel = message.text

        state_list = [message.from_user.full_name, message.from_user.id, answer_middle_fuel, answer_cost_fuel]

        await message.answer(f'Середній розхід: {answer_middle_fuel}\nЦіна топлива: {answer_cost_fuel}', reply_markup=def_kb)

        try:
            await sqlite_db.sql_add_command(state=state_list)
        except:
            await sqlite_db.sql_edit(state_list)
        await state.finish()
    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)



