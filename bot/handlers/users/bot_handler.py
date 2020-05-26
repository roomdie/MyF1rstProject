import requests

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher

from states.token import UserToken
from bot_db import add, update, select_all, select_column, delete_bot, first_try

import logging
import aiohttp
import time
import datetime

from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = 'socks5://45.89.19.2:9313'
PROXY_AUTH = aiohttp.BasicAuth(login='xH6y1z', password='871xvl90fD')


async def bot_handler(message: types.Message):
    # user id of bot
    user_id = message.from_user.id
    # user username
    username_user = message.from_user.username
    # bot username
    x = select_column(user_id)
    username_bot = x[3]
    # add time
    date_time = select_column(user_id)
    date_time = date_time[4]
    # just inline keyboard
    markup = types.InlineKeyboardMarkup()
    if username_bot == '':
        add_button = types.InlineKeyboardButton(text="+", callback_data="add_bot")
        markup.row(add_button)
    else:
        info_button = types.InlineKeyboardButton(text="@{}".format(username_bot), callback_data="about_bot")
        markup.row(info_button)

    await message.answer(
        "Your Bot", reply_markup=markup
    )

    # @dp.callback_query_handler()
    async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
        if callback_query.data == "add_bot":
            await callback_query.message.answer(
                "Please write your token of the Bot (created by @BotFather):"
            )
            await callback_query.answer(text="")
            await UserToken.token.set()
        elif callback_query.data == "yes_delete_bot":
            delete_bot(user_id, username_user, username_bot)
            await message.answer(
                "Bot deleted."
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
            rows = select_all()
            for i in rows:
                if username_bot in i:
                    markup_delete = types.InlineKeyboardMarkup()
                    button_yes = types.InlineKeyboardButton(text="Yes", callback_data="delete_bot_real_1")
                    button_no = types.InlineKeyboardButton(text="No", callback_data="about_bot")
                    markup_delete.insert(button_yes)
                    markup_delete.insert(button_no)
                    await callback_query.message.answer(
                        "Delete your Bot?", reply_markup=markup_delete
                    )
                    await callback_query.answer(text="")
        elif callback_query.data == "about_bot":
            markup_about = types.InlineKeyboardMarkup()
            delete_button = types.InlineKeyboardButton(text="Delete the Bot", callback_data="delete_bot")
            back_button = types.InlineKeyboardButton(text="←", callback_data="bot")
            markup_about.insert(back_button)
            markup_about.insert(delete_button)
            await callback_query.message.answer(
                "<b>Information</b>\n\n<i>Username:</i> @{}\n"
                "<i>Added:</i> {}".format(username_bot, date_time),
                reply_markup=markup_about, parse_mode="HTML"
            )
            await callback_query.answer(text="")
        elif callback_query.data == "bot":
            markup_bot = types.InlineKeyboardMarkup()
            button_bot = types.InlineKeyboardButton(text="@{}".format(username_bot), callback_data="about_bot")
            markup_bot.insert(button_bot)
            await message.answer(
                "Your Bot", reply_markup=markup_bot
            )
            await callback_query.answer(text="")


# @dp.message_handler(state=UserToken.token)
async def token_handler(message: types.Message, state: FSMContext):
    # token of bot
    token = message.text
    # user id of bot
    user_id = message.from_user.id
    # time of add bot
    # it's send to DB
    date_time = datetime.datetime.now().date()
    username_user = "{}".format(message.from_user.username)
    # response = requests.post("https://api.telegram.org/bot{}/getMe".format(token))
    if len(token) >= 46 and ":" in token:
        await state.update_data(token1=token)
        user_bot = Bot(token=token, parse_mode=types.ParseMode.HTML, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
        getting_username_bot = await user_bot.get_me()
        print(getting_username_bot)
        username_bot = getting_username_bot["username"]
        rows = select_all()
        y = 1
        for i in rows:
            if username_bot in i:
                await message.answer("Бот уже добавлен.")
                break
            elif username_bot not in i and y == len(rows):
                update("username_bot", username_bot, "user_id", user_id)
                update("username_user", username_user, "user_id", user_id)
                update("token", token, "user_id", user_id)
                update("date_time", date_time, "user_id", user_id)

                await message.answer(
                    "Бот добавлен. Нажмите снова на кнопку 🤖 Bot, чтобы узнать информацию про вашего бота. "
                )
                break
            else:
                y += 1
                continue
        await state.finish()
        # await UserToken.bot_answer.set()
    else:
        await message.answer("Ваш токен не валидный.")
        await state.finish()


# @dp.message_handler(state=UserToken.bot_answer)
# async def first(message: types.Message, state: FSMContext):
#     print("here2")
#     data = await state.get_data()
#     answer1 = data.get("token1")
#     answer2 = message.text
#     print(answer1)
#     # config.API_TOKEN
#     # try:
#
#     t = await state.update_data(call_t=x)
#     print(t)
#     id_admin = []
#     for i in admin_list:
#         y = i.user.id
#         id_admin.append(y)
#     if message.from_user.id in id_admin:
#         await message.answer("Твой канал")
#     else:
#         await message.answer("Врунишка")
#         await state.finish()
#     # except:
#     #     await message.answer("Ошибка доступа.")
#     #     await state.finish()
#
#     # print(count[0][0])
#     await state.finish()

# @dp.message_handler()
# async def channel_handler(message: types.Message, state: FSMContext):
#     # user_token =
#     req = None
#
#
#     if req.status_code == 200:
#     if (message.text[0] == '@') or (message.text[0:22] == 'https://t.me/joinchat/'):
#         try:
#             req = requests.post("https://api.telegram.org/bot{}/getMe".format(user_token))
#             admin = await bot.get_chat_administrators(chat_id=message.text[8:])
#             chat = await bot.get_chat(chat_id=message.text[8:])
#             id_admin = admin[1].user["id"]
#         except:
#             await message.answer("Ваш токен не валидный.")
#             await state.finish()
#         # add channel
#         else:
#             await message.answer(
#                 "⚠ Ошибка\n"
#                 "\nПричины:"
#                 "\n🔑 Вы не добавили меня в ваш канал."
#                 "\n🔗 Ошибка в ссылке на канал."
#                 "\n😮 Вы не являетесь администратором данного канала.".format(message.text))
#     else:
#         await message.answer("⚠ Неправильный формат.\n\n"
#                              "📢 Публичный канал: @канал\n"
#                              "🔒 Приватный канал: httрs://t.me/joinchat/различные_символы")