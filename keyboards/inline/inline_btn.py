from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_btn_back = InlineKeyboardButton('🔙Назад', callback_data='back')
inline_kb = InlineKeyboardMarkup().add(inline_btn_back)

inline_setup_middle = InlineKeyboardButton('Змінити середній розхід!', callback_data='middle')
inline_setup_cost = InlineKeyboardButton('Змінити ціну на паливо!', callback_data='cost')

inline_middle = InlineKeyboardMarkup().add(inline_btn_back).add(inline_setup_middle).add(inline_setup_cost)
