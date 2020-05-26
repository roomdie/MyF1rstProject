import pymysql
import random

# host, user, password, db
con = pymysql.connect('localhost', 'root', '', 'channel_bot')


with con:
    cur = con.cursor()
    # cur.execute(
    #     """
    #     INSERT INTO first_step
    #     (`id_user`, `id_channel`, `count_users`, `datatime`, `none`)
    #     VALUES ('23', 'Dmitriy', '1', '2020-05-05', '4')
    #     """
    # )
    cur.execute(
        """
        SELECT * FROM first_step;
        """
    )
    # channel id

    def inspector(id_channel, count_users):
        if id_channel and count_users == 0:
            raise ValueError("can't be '0'")
        else:
            channel_list = cur.fetchall()
            random_int = random.randint(0, len(channel_list) - 1)
            link = channel_list[random_int][id_channel]
            subs = channel_list[random_int][count_users]
            print("Канал: {}\nКол-во Подписчиков: {}".format(link, subs))
    inspector(1, 2)

    # print(channelList[randomInt][0])
    # # print("Database version: {}".format(version[0]))