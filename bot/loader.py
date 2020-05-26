import logging
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

#config.API_TOKEN

PROXY_URL = 'socks5://45.89.19.2:9313'
PROXY_AUTH = aiohttp.BasicAuth(login='xH6y1z', password='871xvl90fD')
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
