import pymysql
import time

try:
    con = pymysql.connect('localhost', 'root', '', 'channel_bot')
except:
    print("\n404 DB\n")
    time.sleep(10)
    exit()


def first_try(user_id, username_user):
    with con:
        cur = con.cursor()
        # add username
        cur.execute(
            "INSERT INTO `channel_list` VALUES ('{}', '{}', '', '', 0, '', 0)".format(
                user_id, username_user
            )
        )


def add(user_id, id_bot, id_channel, count_subs):
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO `channel_list` VALUES ('{}', '{}', '{}', '{}')".format(
                user_id, id_bot, id_channel, count_subs
            ))


def add_first_channel(user_id, channel_id, count_subs):
    with con:
        cur = con.cursor()
        cur.execute(
            "UPDATE `channel_list` SET `first_channel` = '{}' WHERE `user_id` = '{}'".format(
                channel_id, user_id
            ))
        cur.execute(
            "UPDATE `channel_list` SET `first_subs` = '{}' WHERE `user_id` = '{}'".format(
                count_subs, user_id
            ))


def add_second_channel(user_id, channel_id, count_subs):
    with con:
        cur = con.cursor()
        cur.execute(
            "UPDATE `channel_list` SET `second__channel` = '{}' WHERE `user_id` = '{}'".format(
                channel_id, user_id
            ))
        cur.execute(
            "UPDATE `channel_list` SET `second_subs` = '{}' WHERE `user_id` = '{}'".format(
                count_subs, user_id
            ))


def update(first_row, new_value, second_row, old_value):
    with con:
        cur = con.cursor()
        cur.execute(
            "UPDATE `channel_list` SET `{}` = '{}' WHERE `{}` = '{}'".format(
                first_row, new_value, second_row, old_value
            ))


def select_row(user_id):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `channel_list` WHERE `user_id` = '{}'".format(user_id))
        all_rows = cur.fetchone()
    return all_rows


def select_all():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `channel_list`")
        all_rows = cur.fetchall()
    return all_rows


def delete_first_channel(user_id):
    with con:
        cur = con.cursor()
        # cur.execute("DELETE FROM `channel_list` WHERE `channel_id` = '{}'".format(use))
        cur.execute("UPDATE `channel_list`"
                    "SET `first_channel` = '', `first_subs` = 0"
                    "WHERE `user_id` = '{}'".format(user_id))


def delete_second_channel(user_id):
    with con:
        cur = con.cursor()
        # cur.execute("DELETE FROM `channel_list` WHERE `channel_id` = '{}'".format(use))
        cur.execute("UPDATE `channel_list`"
                    "SET `second_channel` = '', `second_subs` = 0"
                    "WHERE `user_id` = '{}'".format(user_id))