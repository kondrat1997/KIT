from init import *

# dict of commands
commands = {}
CMD = commands.keys()
# list of hidden commands
hCMD = []


@bot.message_handler(commands=['start'])
def start(message):
    ans = 'Привет! Меня зовут KIT. Чтобы узнать что я умею, нажми /help .'
    bot.send_message(message.chat.id, ans)
commands['/start'] = start


@bot.message_handler(commands=['help'])
def help(message):
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
    os.system("kill -9 `ps -ef | grep python\ bot| grep -v grep | awk '{print $2}'`")
commands['/kill'] = kill
hCMD.append('/kill')
