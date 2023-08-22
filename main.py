import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command

from filters import IsAdmin
from handlers.start import register_start

bot = Bot(token=os.environ.get("TOKEN"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

def setup_filters():
    dp.filters_factory.bind(IsAdmin)

def setup_handlers():
    register_start(dp)

@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

def main():
    setup_filters()
    setup_handlers()
    
    asyncio.run(dp.start_polling())

if __name__ == "__main__":
    main()