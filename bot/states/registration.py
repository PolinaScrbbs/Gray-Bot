from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    username = State()
    password = State()
    confirm_password = State()

    full_name = State()
    phone_number = State()
    sity = State()
    adress = State()
    status = State()

    card_number = State()
