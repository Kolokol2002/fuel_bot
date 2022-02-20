#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import StatesGroup, State


class For_Start(StatesGroup):
    middle_fuel = State()
    cost_fuel = State()