import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, enums
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.start import register_start
from handlers.channels import register_channels

bot = Bot(token=os.environ.get("TOKEN"), parse_mode=enums.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
logging.basicConfig(level=logging.INFO)

def setup_routers():
    register_start(dp)
    register_channels(dp)

def main():
    setup_routers()
    
    asyncio.run(dp.start_polling(bot))

if __name__ == "__main__":
    main()