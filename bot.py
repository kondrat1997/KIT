import config
import telebot
import time
import os
from os.path import join as jp
from config import *

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def simple_echo(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.PATH = os.path.dirname(__file__)
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(f'EXCEPTION: {e}')
            time.sleep(5)
            break
