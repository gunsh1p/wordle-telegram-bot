import os

from aiogram import Router
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import exceptions

from keyboards import get_link_kb

router = Router() 

@router.channel_post()
async def channel_post_handler(channel_post: Message):
    if len(channel_post.html_text) == 0 and (len(channel_post.photo) > 0 or len(channel_post.video)):
        return
    try:
        await channel_post.edit_reply_markup(reply_markup=get_link_kb())
    except exceptions.TelegramBadRequest:
        await channel_post.reply(f"<a href=\"https://t.me/{os.environ.get('BOT_NAME')}\">Play Wordle</a>")

def register_channels(dp: Dispatcher):
    dp.include_router(router)