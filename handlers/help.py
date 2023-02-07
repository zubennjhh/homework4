from aiogram import types
from handlers.constants import HELP_TEXT


async def help_command(message: types.Message):
	"""
		Показываем все команды пользователю
	"""
	await message.answer(text=HELP_TEXT)
	await message.delete()