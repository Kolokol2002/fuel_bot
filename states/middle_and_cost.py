#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import StatesGroup, State


class For_Set_middle_cost(StatesGroup):
    middle = State()
    cost = State()