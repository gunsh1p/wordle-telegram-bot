import os

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types

from states import *

async def start(message: Message, state: FSMContext):
    if state.get_state == Play.running and state.get_data()["step"] < 6:
        await message.answer("Your are lose!")
        await state.reset_state()
        return
    await state.reset_state()
    kb = [
        [
            types.KeyboardButton(text="Play"),
            types.KeyboardButton(text="My results")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Hello, {message.from_user.first_name}. It's a wordle game for {'tg_channel_name_will_be_soon'}", reply_markup=keyboard)

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")