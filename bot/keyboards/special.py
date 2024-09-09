from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

cancel = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="❌", callback_data="cancel")]]
)