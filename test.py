import logging
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import requests
import telebot
import time
from telebot import types
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random

API_TOKEN = '1113616160:AAEOm6FGeKizLGGFm5UoMOog-IpXHMtSCH0'
PROXY_URL = 'socks5://45.89.19.36:5937'
PROXY_AUTH = aiohttp.BasicAuth(login='xH6y1z', password='871xvl90fD')

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cats(message: types.Message):
    await message.answer("Hello, write me your channel and I say you, how many subscribers there.\n")


@dp.message_handler()
async def echo(message: types.Message):
    channel_id = message.text
    url = 'https://tgstat.ru/channel/{}'.format(channel_id)
    # with open('test.html', 'wb') as input_file:
    # input_file.write(r.text.encode('utf-8'))
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    statusCode = requests.get(url)
    # make exception
    if statusCode.status_code == 404:
        print("Error 404\nBad Request")
        exit()
    data = urlopen(req).read()
    # with open('test.html', 'rb') as output_file:
    # content = output_file.read()
    soup = BeautifulSoup(data, "html.parser")
    search = soup.find('div', class_='align-center')

    channel_name = "{}".format(search.getText())

    splits = (' ', '', '\n')
    countUsersList = [i for i in channel_name if i not in splits]
    countUsersStroke = ''.join(countUsersList)
    await message.answer(countUsersStroke)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)