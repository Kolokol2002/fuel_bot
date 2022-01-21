from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data_base import sqlite_db
from keyboards.inline import inline_back
from loader import dp
from keyboards.default import def_kb

from states import For_Start


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привіт, {message.from_user.full_name}!\nТвій id: {message.from_user.id}')
    await message.answer(f'Для початку введіть розхід та ціну на паливо!')
    await message.answer(f'Введіть середній розхід:')

    await For_Start.middle_fuel.set()


@dp.message_handler(state=For_Start.middle_fuel)
async def middle_fuel(message: types.Message, state: FSMContext):

    try:
        await state.update_data(middle_fuel=float(message.text))
        await message.answer(f'Введіть ціну на паливо:')

        await For_Start.next()
    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)


@dp.message_handler(state=For_Start.cost_fuel)
async def cost_fuel(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_middle_fuel = data.get('middle_fuel')
    try:
        answer_cost_fuel = float(message.text)

        state_list = [message.from_user.full_name, message.from_user.id, answer_middle_fuel, answer_cost_fuel]


        await message.answer(f'Середній розхід: {answer_middle_fuel}\nЦіна топлива: {answer_cost_fuel}', reply_markup=def_kb)

        try:
            await sqlite_db.sql_add_command(state=state_list)
        except:
            await sqlite_db.sql_edit(state_list)
        await state.finish()

    except:
        await message.reply('Це не ціле число!', reply_markup=inline_back)
