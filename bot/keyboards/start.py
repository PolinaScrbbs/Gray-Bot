from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from aiogram.utils.keyboard import (
    KeyboardBuilder,
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder,
)

start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Регистрация")],
        [
            KeyboardButton(
                text="О нас",
                web_app=WebAppInfo(url="https://github.com/PolinaScrbbs"),
            )
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)