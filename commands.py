from os.path import abspath, dirname
from os.path import join as jp

from init import *

# dict of commands
commands = {}
CMD = commands.keys()
# list of hidden commands
hCMD = []


def get_abs_path(r_path):
    my_path = abspath(dirname(__file__))
    return jp(my_path, r_path)



@bot.message_handler(commands=['start'])
def start(message):
    ans = 'Привет! Меня зовут KIT. Чтобы узнать что я умею, нажми /help'
    bot.send_message(message.chat.id, ans)
commands['/start'] = start


@bot.message_handler(commands=['help'])
def help(message):
    with open(get_abs_path('img/help.jpg'), 'rb') as pic:
        bot.send_photo(message.chat.id, pic)

    ans = 'Вот что я умею:\n'
    for cmd in CMD:
        if cmd not in hCMD:
            ans = ans + cmd + '\n'

    bot.send_message(message.chat.id, ans)


commands['/help'] = help

@bot.message_handler(commands=['hhelp'])
def hhelp(message):
    ans = 'Скрытый help. Вот что я умею:\n'
    for cmd in CMD:
        ans = ans + cmd + '\n'

    bot.send_message(message.chat.id, ans)
commands['/hhelp'] = hhelp
hCMD.append('/hhelp')


@bot.message_handler(commands=['kill'])
def kill(message):
    ans = 'Оййй'
    bot.send_message(message.chat.id, ans)
    os.system("kill -9 `ps -ef | grep python\ *bot| grep -v grep | awk '{print $2}'`")

commands['/kill'] = kill
hCMD.append('/kill')


@bot.message_handler(func=lambda m: (m.text.startswith('/')) and (m.text.split(' ')[0] not in CMD))
def check_command(message):
    wrong_command = message.text.split(' ')[0]
    ans = f'Я не знаю, что такое {wrong_command}. Нажмите /help , чтобы узнать, что я умею'
    bot.send_message(message.chat.id, ans)
