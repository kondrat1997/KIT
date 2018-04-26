import config
import telebot
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def simple_echo(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            time.sleep(5)