from telebot import apihelper

# you should define your bot-token here
token = ''

# proxy
# h means remote DNS, because faggots from RKN banned it
proxy = {'http': 'socks5h://localhost:1080', 'https': 'socks5h://localhost:1080'}
apihelper.proxy = {'http': 'socks5h://localhost:1080', 'https': 'socks5h://localhost:1080'}
