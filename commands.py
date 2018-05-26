import time
from os.path import abspath, dirname
from os.path import join as jp

import requests
import vlc

from config import proxy
from init import *

# dict of commands
commands = {}
CMD = commands.keys()
# list of hidden commands
hCMD = []

user_ids = [215500416, 475413364]


def filter(func):
    def wrapped(message, *args, **kwargs):
        if message.chat.id not in user_ids:
            ans = ''
            if message.text[:6] == '/start':
                ans = 'Привет. Я KIT, и буду разговаривать только с Леной и Володей.\n' \
                      + 'Возможно, с Дмитрием Артуровичем.\nНо это не точно.'
            ans = ans + 'Ты кто такой?. Уходи.'
            bot.send_message(message.chat.id, ans)
            return 0
        else:
            return func(message=message, *args, **kwargs)

    return wrapped

# some stuff

def play_sound(path, s=0):
    p = vlc.MediaPlayer(path)
    p.play()

    if s:
        time.sleep(s)
        p.stop()

def get_abs_path(r_path):
    my_path = abspath(dirname(__file__))
    return jp(my_path, r_path)

####################

@filter
@bot.message_handler(commands=['start'])
def start(message):
    ans = 'Привет! Меня зовут KIT. Чтобы узнать что я умею, нажми /help'
    bot.send_message(message.chat.id, ans)
commands['/start'] = start


@filter
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


@filter
@bot.message_handler(commands=['hhelp'])
def hhelp(message):
    ans = 'Вот что я умею:\n'
    hans = ''
    ans = ans + 'Не спрятанные:\n'
    for cmd in CMD:
        if cmd not in hCMD:
            ans = ans + cmd + '\n'
        else:
            hans = hans + cmd + '\n'
    ans = ans + 'Cпрятанные:\n' + hans

    bot.send_message(message.chat.id, ans)
commands['/hhelp'] = hhelp
hCMD.append('/hhelp')


@filter
@bot.message_handler(commands=['kill'])
def kill(message):
    ans = 'Оййй'
    bot.send_message(message.chat.id, ans)
    os.system("kill -9 `ps -ef | grep python\ *bot| grep -v grep | awk '{print $2}'`")

commands['/kill'] = kill
hCMD.append('/kill')


@filter
@bot.message_handler(
    func=lambda m: False if m.text is None else ((m.text.startswith('/')) and (m.text.split(' ')[0] not in CMD)))
def check_command(message):
    wrong_command = message.text.split(' ')[0]
    ans = f'Я не знаю, что такое {wrong_command}. Нажмите /help , чтобы узнать, что я умею'
    bot.send_message(message.chat.id, ans)


@filter
@bot.message_handler(commands=['meow'])
def say_meow(message):
    play_sound(get_abs_path('sounds/meow-1.mp3'), s=2)

commands['/meow'] = say_meow


@filter
@bot.message_handler(commands=['pur'])
def say_pur(message):
    play_sound(get_abs_path('sounds/purring-1.mp3'), s=4)

commands['/pur'] = say_pur


@filter
@bot.message_handler(commands=['sneeze'])
def say_sneeze(message):
    play_sound(get_abs_path('sounds/sneeze-1.mp3'), s=2)

commands['/sneeze'] = say_sneeze


@filter
@bot.message_handler(content_types=["voice"])
def voice_messages(message):
    file_info = bot.get_file(message.voice.file_id)
    voice_link = f'https://api.telegram.org/file/bot{config.token}/{file_info.file_path}'
    t = message.voice.duration + 1

    r = requests.get(voice_link, allow_redirects=True, proxies=proxy)
    open(get_abs_path('temp/sound.wav'), 'wb').write(r.content)

    play_sound(get_abs_path('temp/sound.wav'), s=t)
    print(message)
