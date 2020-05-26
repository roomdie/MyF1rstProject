import requests
# import channel_handler as x

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from loader import dp, bot
from states.token import UserToken
from bot_db import add, update, select_all, select_column, delete_bot, first_try

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.handlers.users.channel_handler import channel_handler, callback_handler
from bot.handlers.users.start_handler import start
from bot.handlers.users.bot_handler import bot_handler

dp.register_message_handler(start, commands='start')
dp.register_message_handler(bot_handler, regexp="🤖 Bot")
dp.register_message_handler(channel_handler, regexp="📢 Channel")
dp.register_callback_query_handler(callback_handler)
