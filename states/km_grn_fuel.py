from aiogram.dispatcher.filters.state import StatesGroup, State


class For_km_rgn_fuel(StatesGroup):
    km = State()
    grn = State()
    fuel = State()
