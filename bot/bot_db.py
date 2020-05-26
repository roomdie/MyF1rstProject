import pymysql
import time

try:
    con = pymysql.connect('localhost', 'root', '', 'channel_bot')
except:
    print("\n404 DB\n")
    time.sleep(10)
    exit()


def first_try(user_id):
    with con:
        cur = con.cursor()
        # add username
        cur.execute(
            "INSERT INTO `bot_list` VALUES ('{}', '', '', '', '0000-00-00')".format(
                user_id
            ))


def add(user_id, id_bot, id_channel, count_subs):
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO `bot_list` VALUES ({}, '{}', '{}', {})".format(
                user_id, id_bot, id_channel, count_subs
            ))


def update(first_row, new_value, second_row, old_value):
    with con:
        cur = con.cursor()
        cur.execute(
            "UPDATE `bot_list` SET `{}` = '{}' WHERE `{}` = '{}'".format(
                first_row, new_value, second_row, old_value
            ))


def select_column(user_id):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `bot_list` WHERE `user_id` = '{}'".format(user_id))
        all_rows = cur.fetchone()
    return all_rows


def select_all():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `bot_list`")
        all_rows = cur.fetchall()
    return all_rows


def delete_bot(user_id, username_user, username_bot):
    with con:
        cur = con.cursor()
        # cur.execute("DELETE FROM `bot_list` WHERE `username_bot` = '{}'".format(use))
        cur.execute("UPDATE `bot_list`"
                    "SET user_id = {}, username_user = '{}', token = '', username_bot = '', date_time = '0000-00-00'"
                    "WHERE `username_bot` = '{}'".format(user_id, username_user, username_bot)
                    )