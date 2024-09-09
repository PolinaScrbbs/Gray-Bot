from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import bot.keyboards as kb
import bot.states as st
import bot.utils as ut
import bot.enums as en
import bot.validators as vr

from .start import router


@router.message(lambda message: message.text == "Регистрация")
async def registration_start(message: Message, state: FSMContext):
    await message.answer("Создайте username", reply_markup=kb.cancel)
    await state.set_state(st.Registration.username)


@router.message(st.Registration.username)
async def get_username(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["username"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_username(message.text)

        await state.set_state(st.Registration.password)
        await message.answer("🔑Создайте пароль", reply_markup=kb.cancel)

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await message.answer("Создайте username", reply_markup=kb.cancel)


@router.message(st.Registration.password)
async def get_password(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["password"] = message.text
    await state.update_data({user_id: user_data})

    await state.set_state(st.Registration.confirm_password)
    await message.answer("🔑Подтвердите пароль", reply_markup=kb.cancel)


@router.message(st.Registration.confirm_password)
async def get_confirm_password(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["confirm_password"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_password(
            user_data["password"], message.text
        )

        await state.set_state(st.Registration.full_name)
        await message.answer("🔑Введите ФИО", reply_markup=kb.cancel)

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await state.set_state(st.Registration.password)
        await message.answer("🔑Создайте пароль", reply_markup=kb.cancel)


@router.message(st.Registration.full_name)
async def get_full_name(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["full_name"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_full_name(message.text)

        await state.set_state(st.Registration.phone_number)
        await message.answer("🔑Введите номер телефона", reply_markup=kb.cancel)

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await message.answer("🔑Введите ФИО", reply_markup=kb.cancel)


@router.message(st.Registration.phone_number)
async def get_phone_number(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["phone_number"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_phone_number(message.text)

        await state.set_state(st.Registration.sity)
        await message.answer(
            "🔑Введите город вашего проживания", reply_markup=kb.cancel
        )

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await message.answer("🔑Введите номер телефона", reply_markup=kb.cancel)


@router.message(st.Registration.sity)
async def get_sity(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["city"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_city(message.text)

        await state.set_state(st.Registration.adress)
        await message.answer(
            "🔑Введите адрес вашего проживания", reply_markup=kb.cancel
        )

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await message.answer(
            "🔑Введите город вашего проживания", reply_markup=kb.cancel
        )


@router.message(st.Registration.adress)
async def get_adress(message: Message, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["adress"] = message.text
    await state.update_data({user_id: user_data})

    try:
        await vr.RegistrationValidator.validate_city(message.text)

        await state.set_state(st.Registration.status)
        await message.answer(
            "🔑Выберите статус", reply_markup=await kb.status_keyboard(en.Status)
        )

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

        await message.answer(
            "🔑Введите город вашего проживания", reply_markup=kb.cancel
        )


@router.callback_query(lambda query: query.data.startswith("status_"))
async def get_status(callback: CallbackQuery, state: FSMContext):
    status_fields = callback.data.split("_")
    status = status_fields[1]

    user_id, user_data = await ut.get_user_data(callback, state)

    user_data["status"] = status
    await state.update_data({user_id: user_data})

    await state.set_state(st.Registration.card_number)
    await callback.message.edit_text(
        "🔑Введите номер банковской карты", reply_markup=kb.cancel
    )


@router.message(st.Registration.card_number)
async def get_card_number(message: CallbackQuery, state: FSMContext):
    user_id, user_data = await ut.get_user_data(message, state)

    user_data["card_number"] = message.text

    try:
        print(user_data)

    except Exception as e:
        await message.answer(f"❌*Ошибка:* {str(e)}", parse_mode="Markdown")

    finally:
        await state.clear()
