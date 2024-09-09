import enum

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

async def status_keyboard(status: enum.Enum):
    keyboard = []
    
    for status_option in status:
        button = InlineKeyboardButton(
            text=status_option.name.capitalize(),
            callback_data=f"status_{status_option.value.capitalize()}"
        )
        keyboard.append([button])

    cancel_button = InlineKeyboardButton(text="❌", callback_data="cancel")
    keyboard.append([cancel_button])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
