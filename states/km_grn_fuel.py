#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import StatesGroup, State


class For_km_rgn_fuel(StatesGroup):
    km = State()
    grn = State()
    fuel = State()
