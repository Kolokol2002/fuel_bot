import sqlite3 as sq

from keyboards.inline import inline_middle


def sql_start():
    global base, cur

    base = sq.connect('user_info.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS user_info(full_name TEXT, user_id TEXT PRIMARY KEY, middle_fuel TEXT, cost_fuel TEXT )')
    base.commit()


async def sql_add_command(state):
    cur.execute(f'INSERT INTO user_info VALUES (?, ?, ?, ?)', tuple(state))
    base.commit()


async def sql_edit(list_values):
    cur.execute(
        f'UPDATE user_info SET middle_fuel = {list_values[2]}, cost_fuel = {list_values[3]} WHERE user_id = {list_values[1]}')
    base.commit()


async def sql_read(message):
    for ret in cur.execute(f'SELECT * FROM user_info WHERE user_id={message.from_user.id}').fetchall():
        await message.answer(f'Ваш середній розход: {ret[2]}\nЦіна топлива: {ret[3]}', reply_markup=inline_middle)


async def sql_give_cost_and_middle(message):
    for ret in cur.execute(f'SELECT * FROM user_info WHERE user_id={message.from_user.id}').fetchall():
        list_value = [ret[2], ret[3]]
        return list_value
