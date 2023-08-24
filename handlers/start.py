from aiogram import Router, F
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from states import *

router = Router() 

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    if await state.get_state() == Play.running and await state.get_data()["step"] < 6:
        await message.answer("Your are lose!")
        await state.clear()
        return
    await state.clear()
    kb = [
        [
            KeyboardButton(text="Play"),
            KeyboardButton(text="My results")
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Hello, {message.from_user.first_name}. It's a wordle game for {'tg_channel_name_will_be_soon'}", reply_markup=keyboard)

def register_start(dp: Dispatcher):
    dp.include_router(router)