from aiogram import types


async def image_sender(message: types.Message):
	await message.answer_photo(
        open('image/.jpg', 'rb'),
        caption="кроссовки"
    )
	await message.delete()