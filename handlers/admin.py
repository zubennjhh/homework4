from aiogram import types
from handlers.constants import CURSES_TEXT


async def example(message: types.Message):
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")
    print(f"{message.from_user.id=}")
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()
        print(admins)


async def check_user_is_admin(message: types.Message):
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False


async def check_curses(message: types.Message):
    BAD_WORDS = ["тупой", 'дурак', "мал"]
    if message.chat.type != 'private':
        for word in BAD_WORDS:
            if message.text.lower().replace(' ', '').count(word):
                await message.answer(text=CURSES_TEXT.format(first_name=message.from_user.first_name))
                await message.delete()
                break


async def pin_messages(message: types.Message):
    print(message.text)
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        if admin_author and message.reply_to_message:
            await message.reply_to_message.pin()


async def ban_user(message: types.Message):
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(chat_id=message.chat.id,user_id=message.reply_to_message.from_user.id)



async def yes_no(message: types.Message):
    '''
    функция которая обрабатывает ответы админов и удаляет пользователя
    '''
    if message.chat.type != 'private':
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
           # await message.reply(message.reply_to_message.from_user.username)
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )