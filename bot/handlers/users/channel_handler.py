import requests

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from states.token import UserToken, ChannelId
# from bot_db import add, update, select_all, channel_db.select_row, delete_bot, first_try
import bot_db
import channel_db

import logging
import aiohttp
import time
import datetime

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def begin(message: types.Message):
    user_id = message.from_user.id
    username_user = message.from_user.username
    x = channel_db.first_try(user_id, username_user)
    print(x)
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


async def channel_handler(message: types.Message):
    # user id of bot
    user_id = message.from_user.id
    channel_row = channel_db.select_row(user_id)
    count_subs = 0
    # add bot check
    bot_row = bot_db.select_column(user_id)
    user_bot = bot_row[3]
    # channels
    first_channel = channel_row[3]
    second_channel = channel_row[5]
    # just inline keyboard
    markup = types.InlineKeyboardMarkup()
    if first_channel == '':
        add_button = types.InlineKeyboardButton(text="+", callback_data="add_channel")
        markup.row(add_button)
    else:
        if second_channel == '':
            info_button = types.InlineKeyboardButton(text="@{}".format(first_channel), callback_data="about_channel")
            add_button = types.InlineKeyboardButton(text="+", callback_data="add_channel")
            markup.row(info_button)
            markup.row(add_button)
        else:
            # first channel
            first_channel_button = types.InlineKeyboardButton(
                text="@{}".format(first_channel), callback_data="about_first_channel"
            )
            # second channel
            second_channel_button = types.InlineKeyboardButton(
                text="@{}".format(second_channel), callback_data="about_second_channel"
            )
            markup.row(first_channel_button)
            markup.row(second_channel_button)

    await message.answer(
        "Your Channel's", reply_markup=markup
    )

    # @dp.callback_query_handler(state=None)


async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "add_channel":
        await callback_query.message.answer(
            "Please write your channel id:"
        )
        await callback_query.answer(text="")
        await ChannelId.id.set()
    elif callback_query.data == "yes_delete_channel":
        delete_channel(user_id, username_user, username_bot)
        await message.answer(
            "Channel deleted."
        )
        await callback_query.answer(text="")
        await state.finish()

    elif callback_query.data == "cancel_delete_bot":
        await message.answer(
            "Cancel."
        )
        await callback_query.answer(text="")
        await state.finish()
    elif callback_query.data == "delete_bot":
        rows = channel_db.select_all()
        for i in rows:
            if username_bot in i:
                markup_delete = types.InlineKeyboardMarkup()
                button_yes = types.InlineKeyboardButton(text="Yes", callback_data="delete_bot_real_1")
                button_no = types.InlineKeyboardButton(text="No", callback_data="about_channel")
                markup_delete.insert(button_yes)
                markup_delete.insert(button_no)
                await callback_query.message.answer(
                    "Delete your Channel?", reply_markup=markup_delete
                )
                await callback_query.answer(text="")
    elif callback_query.data == "about_first_channel":
        markup_about = types.InlineKeyboardMarkup()
        delete_button = types.InlineKeyboardButton(
            text="Delete Channel", callback_data="delete_first_channel"
        )
        back_button = types.InlineKeyboardButton(text="←", callback_data="channels")
        markup_about.insert(back_button)
        markup_about.insert(delete_button)
        await callback_query.message.answer(
            "<b>Information</b>\n\n<i>Link:</i> @{}\n"
            "<i>Subs:</i> {}".format(first_channel, count_subs),
            reply_markup=markup_about, parse_mode="HTML"
        )
        await callback_query.answer(text="")
    elif callback_query.data == "channels":
        markup_channels = types.InlineKeyboardMarkup()
        first_channel_btn = types.InlineKeyboardButton(
            text="@{}".format(first_channel), callback_data="about_first_channel"
        )
        second_channel_btn = types.InlineKeyboardButton(
            text="@{}".format(second_channel), callback_data="about_first_bot"
        )
        markup_channels.row(first_channel_btn)
        markup_channels.row(second_channel_btn)
        await message.answer(
            "Your Channel's", reply_markup=markup_channels
        )
        await callback_query.answer(text="")


# @dp.message_handler(state=ChannelId.id)
# async def token_handler(message: types.Message, state: FSMContext):
#     # token of bot
#     id = message.text
#     # user id of bot
#     user_id = message.from_user.id
#     user_bot = bot_db.select_column[user_id]
#     print(user_bot)
#     # it's send to DB
#     username_user = message.from_user.username
#     # response = requests.post("https://api.telegram.org/bot{}/getMe".format(token))\
#     column = channel_db.select_row(user_id)
#     if column[3] == '':
#         channel_db.update("first_channel", id, "user_id", user_id)
#         channel_db.update("first_subs", 0, "user_id", user_id)
#         await message.answer(
#             "Канал 1 добавлен."
#         )
#         await state.finish()
#     elif column[5] == '':
#         channel_db.update("second_channel", id, "user_id", user_id)
#         channel_db.update("second_subs", 0, "user_id", user_id)
#         await message.answer(
#             "Канал 2 добавлен."
#         )
#         await state.finish()
#     else:
#         await message.answer("Произошел сбой.")
#         await state.finish()


    # if len(id) >= 2:
    #     await state.update_data(id1=id)
    #     rows = channel_db.select_all()
    #     y = 1
    #     for i in rows:
    #         if id in i:
    #             await message.answer("Бот уже добавлен.")
    #             break
    #         elif id not in i and y == len(rows):
    #             channel_db.update("first_channel", id, "user_id", user_id)
    #             await message.answer(
    #                 "Канал добавлен. Нажмите снова на кнопку 🤖 Bot, чтобы узнать информацию про вашего бота. "
    #             )
    #             break
    #         else:
    #             y += 1
    #             continue
    #     await state.finish()
    #     # await UserToken.bot_answer.set()
    # else:
    #     await message.answer("Ваш токен не валидный.")
    #     await state.finish()