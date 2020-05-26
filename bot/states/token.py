from aiogram.dispatcher.filters.state import StatesGroup, State


class UserToken(StatesGroup):
    token = State()
    call = State()
    bot_answer = State()


class ChannelId(StatesGroup):
    id = State()