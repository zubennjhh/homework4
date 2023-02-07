from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products


def buy_kb(product_id):
    buy_item_kb = InlineKeyboardMarkup()
    buy_item_kb.add(
    InlineKeyboardButton('купить', callback_data=f'buy_item {product_id}')
)
async def show_clothes(message: types.Message):
    product = get_products()[0]
    print(product)
    await message.answer(text='вот ваши одежды)')
    await message.answer_photo(
    open(product[4]),'rb'),
    caption=f"Товар: {product[1]}, Описание: {product[2]}",
    reply_markup = buy_kb(product[0])
