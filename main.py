from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.constants import HELP_TEXT, START_TEXT
from handlers.start import start_command
from handlers.help import help_command
from handlers.pictures import image_sender
from handlers.shop import shop_start
from handlers.all_messages import echo
from handlers.shop_categories import show_clothes
from handlers.admin import (example, check_curses, pin_messages, ban_user)
from handlers.user_info_form import (Form, cancel_handler, form_start, process_name, process_age, process_day, process_done)
from handlers.admin import yes_no
from db.base import (init_db, create_table , populate_products)

async  def startapp(_):
    init_db()
    create_table()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv('BOT_TOKEN'))
    dp = Dispatcher(bot)
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(image_sender, commands=['picture'])
    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_message_handler(show_clothes, Text(equals='одежды'))
    dp.register_callback_query_handler(shop_start, text='buy_item')
    dp.register_message_handler(pin_messages, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_age, state=Form.age)
    dp.register_message_handler(process_day, state=Form.day)
    dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
    dp.register_message_handler(yes_no, commands=['да'], commands_prefix=['!'])

    # всегда в конце
    dp.register_message_handler(example)
    dp.register_message_handler(echo)
    dp.register_message_handler(check_curses)


    executor.start_polling(dp, skip_updates=True,
                           on_startup=startapp)

