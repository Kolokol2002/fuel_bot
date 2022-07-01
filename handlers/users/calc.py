
from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    list_simvol = ['+', '-', '*', '/']
    for i in list_simvol:
        if i in message.text.strip(''):
            await message.answer(eval(message.text))