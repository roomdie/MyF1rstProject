from handlers import dp
from loader import bot, storage

# async def on_shutdown(dp):
#     await bot.close()
#     await storage.close()
async def on_shutdown(dp):
    await bot.close()
    await storage.close()

if __name__ == '__main__':
    from handlers import dp
    print(dp)

    # executor.start_polling(dp, on_shutdown=on_shutdown)

