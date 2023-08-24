from aiogram import Router, F
from aiogram import Dispatcher
from aiogram.types import Message

from keyboards import get_link_kb

router = Router() 

@router.channel_post()
async def channel_post_handler(channel_post: Message):
    await channel_post.edit_reply_markup(reply_markup=get_link_kb())

def register_channels(dp: Dispatcher):
    dp.include_router(router)