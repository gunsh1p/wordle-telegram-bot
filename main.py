import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, enums
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from filters import IsAdmin
from handlers.start import register_start

bot = Bot(token=os.environ.get("TOKEN"), parse_mode=enums.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
logging.basicConfig(level=logging.INFO)

def setup_filters():
    dp.filters_factory.bind(IsAdmin)

def setup_handlers():
    register_start(dp)

def main():
    setup_filters()
    setup_handlers()
    
    asyncio.run(dp.start_polling(bot))

if __name__ == "__main__":
    main()