from commands import *

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f'EXCEPTION: {e}')
            time.sleep(5)