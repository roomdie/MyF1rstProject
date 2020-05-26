import requests
import telebot
import time
from telebot import types
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random

# TOKEN = '1113616160:AAEOm6FGeKizLGGFm5UoMOog-IpXHMtSCH0'
# url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
#
# channel_id = input()
# url = 'https://tgstat.ru/channel/{}'.format(channel_id)
# # with open('test.html', 'wb') as input_file:
# # input_file.write(r.text.encode('utf-8'))
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# statusCode = requests.get(url)
# # make exception
# if statusCode.status_code == 404:
#     print("Error 404\nBad Request")
#     exit()
# data = urlopen(req).read()
# # with open('test.html', 'rb') as output_file:
# # content = output_file.read()
# soup = BeautifulSoup(data, "html.parser")
# search = soup.find('div', class_='align-center')
#
# channel_name = "{}".format(search.getText())
#
# splits = (' ', '', '\n')
# countUsersList = [i for i in channel_name if i not in splits]
# countUsersStroke = ''.join(countUsersList)
countUsersStroke = input()
countUsersInt = int(countUsersStroke)


def levels_distributor(count_subs):
    def levels_generator():
        key = 2
        value = 1000
        int_levels = {1: 100, 2: 1000}
        while value <= 1000000:
            key += 1
            # value *= 1.5 make more levels
            value *= 2
            int_levels.update({key: int(value)})
        return int_levels

    str_levels = {
        1: "100 - 1000",
        2: "1000 - 2000",
        3: "2000 - 4000",
    }
    # checking count subscribers
    for i in levels_generator():
        if (count_subs >= levels_generator()[i]) and (count_subs < levels_generator()[i+1]):
            # return of count subscribers
            print(str_levels[i])
            break
        elif count_subs < 100:
            print("От 100 подписчиков")
            break
        else:
            continue

levels_distributor(countUsersInt)
if countUsersInt >= 100:
    pass
else:
    print("need more subs\nwrite us")


