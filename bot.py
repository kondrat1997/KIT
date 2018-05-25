import time
import os
from os.path import join as jp
from commands import *

if __name__ == '__main__':
    bot.PATH = os.path.dirname(__file__)
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(f'EXCEPTION: {e}')
            time.sleep(5)
