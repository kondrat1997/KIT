import time
import os
from os.path import join as jp
import subprocess
from commands import *

@bot.message_handler(commands=['help'])
def help(message):
    with open(jp(bot.PATH,'img/help.jpg'), 'rb') as pic:
        bot.send_photo(message.chat.id, pic)

    ans = 'Вот что я умею:\n'
    for cmd in CMD:
        if cmd not in hCMD:
            ans = ans + cmd + '\n'

    bot.send_message(message.chat.id, ans)
commands['/help'] = help

if __name__ == '__main__':
    bot.PATH = os.path.dirname(__file__)
    print(bot.PATH)
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f'EXCEPTION: {e}')
            time.sleep(5)