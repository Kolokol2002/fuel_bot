from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_btn_back = InlineKeyboardButton('🔙Назад', callback_data='back')
inline_kb = InlineKeyboardMarkup().add(inline_btn_back)

inline_setup_middle = InlineKeyboardButton('Уст. разход!', callback_data='middle')

inline_middle = InlineKeyboardMarkup().add(inline_btn_back).add(inline_setup_middle)
