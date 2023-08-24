from aiogram import Router, F
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import Play
from keyboards import get_start_kb
from utils import get_channels

disp: Dispatcher = None

router = Router() 

@router.message(
    Command("start")
)
async def start(message: Message, state: FSMContext):
    global disp
    if await state.get_state() == Play.running and await state.get_data()["step"] < 6:
        await message.answer("Your are lose!")
        await state.clear()
        return
    await state.clear()
    text = f"Hello, {message.from_user.first_name}. It's a wordle game of your favourite telegram channel."
    await message.answer(text, reply_markup=get_start_kb())

def register_start(dp: Dispatcher):
    global disp
    dp.include_router(router)
    disp = dp