
def save_user_id(user_id):
    with open("users.txt", "a+") as f:
        f.seek(0)
        users = f.read().splitlines()
        if str(user_id) not in users:
            f.write(f"{user_id}\n")

import telebot
import config
import sqlite3
bot = telebot.TeleBot(config.TOKEN)
def start(message):
    try:
        db = sqlite3.connect('users.db', check_same_thread=False)
        sql = db.cursor()
        bot.send_message(message.chat.id, config.start)
        sql.execute("SELECT user_id FROM user WHERE user_id = ?",(message.from_user.id,))
        db.commit()
        if sql.fetchone() is None:
            sql.execute("INSERT INTO user VALUES(?)",(message.from_user.id,))
            db.commit()
        sql.close()
        db.close()
    except Exception as e:
        print(str(e))