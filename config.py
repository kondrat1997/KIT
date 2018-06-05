from telebot import apihelper

# you should define your bot-token here
token = ''

# proxy
# h means remote DNS, because faggots from RKN banned it
proxy = {'http': 'socks5h://localhost:1080', 'https': 'socks5h://localhost:1080'}
apihelper.proxy = {'http': 'socks5h://localhost:1080', 'https': 'socks5h://localhost:1080'}

# list of telegram ids
# who will be allowed to communicate with the bot

access_list = {'Володя': 215500416, 'Лена': 475413364}
user_ids = access_list.values()
user_names = access_list.keys()
