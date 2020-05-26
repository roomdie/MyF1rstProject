from loader import bot, storage

# user_token =
# req = requests.post("https://api.telegram.org/bot{}/getMe".format(user_token))
# if req.status_code == 200:


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)

