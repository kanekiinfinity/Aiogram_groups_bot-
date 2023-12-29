import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot
import random as r


@dp.message_handler(IsGroup(), Command("change_photo", prefixes="!/"), AdminFilter())
async def change_photo(message: types.Message):
    s_message = message.reply_to_message
    photo = s_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)

@dp.message_handler(IsGroup, Command("change_title", prefixes='!/'), AdminFilter())
async def change_photo(message: types.Message):
    s_message = message.reply_to_message
    title = s_message.text
    await bot.set_chat_title(message.chat.id, title=title)

#