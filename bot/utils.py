from typing import Dict, Tuple
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

async def get_user_data(message: Message, state: FSMContext) -> Tuple[int, Dict]:
    user_id = message.from_user.id
    data = await state.get_data()
    user_data = data.get(user_id, {})

    return user_id, user_data