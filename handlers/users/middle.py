from aiogram import types
from aiogram.dispatcher import FSMContext

from data_base import sqlite_db
from loader import dp
from aiogram.dispatcher.filters import Text

from keyboards.default import kb

from states import For_Answer, For_Start


@dp.message_handler(Text(equals='Разход', ignore_case=True))
async def middle(message: types.Message):

    await For_Answer.middle.set()

    await sqlite_db.sql_read(message)

    @dp.callback_query_handler(text='back', state=For_Answer.middle)
    async def keyboard_back(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer(text='🔙Назад', reply_markup=kb)

        await state.finish()

    @dp.callback_query_handler(text='middle', state=For_Answer.middle)
    async def keyboard_middle(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer(text='Установіть разход')
        await call.message.answer(text='Введіть середній розхід:')
        await state.finish()
        await For_Start.middle_fuel.set()


