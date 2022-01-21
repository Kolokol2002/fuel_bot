from aiogram.dispatcher.filters.state import StatesGroup, State


class For_Start(StatesGroup):
    middle_fuel = State()
    cost_fuel = State()