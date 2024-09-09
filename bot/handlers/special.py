from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .registration import router


@router.callback_query(F.data == "cancel")
async def catalog(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("✅ Отменено")
