import os

from aiogram import Dispatcher
from aiogram.types import Message

from utils.args import parse_args

async def start(message: Message):
    pass

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*", is_admin=False)