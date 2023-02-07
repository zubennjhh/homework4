
from aiogram import types

async def echo(message: types.Message):
    await message.reply(text=message.text.upper())
