import requests
import bot_db
import channel_db

from aiogram import types
from aiogram.dispatcher.filters import Command


async def start(message: types.Message):
    user_id = message.from_user.id
    bot_db.first_try(user_id)
    channel_db.first_try(user_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('🤖 Bot')
    # itembtn2 = types.KeyboardButton('🔍 Search')
    # itembtn3 = types.KeyboardButton('🌐 Language')
    itembtn4 = types.KeyboardButton('⚙ Settings')
    itembtn5 = types.KeyboardButton('💳 Subscription')
    itembtn2 = types.KeyboardButton('1148665047:AAGSO2XzvBIxC3Vz_sWruiMYHC3IRb7_5lQ')
    itembtn3 = types.KeyboardButton('@tes155')
    itembtn6 = types.KeyboardButton('🆘 Help')
    itembtn7 = types.KeyboardButton('📢 Channel')
    markup.row(itembtn1, itembtn7)
    markup.row(itembtn2, itembtn3)
    markup.row(itembtn4, itembtn5, itembtn6)

    await message.answer("Hi", reply_markup=markup)