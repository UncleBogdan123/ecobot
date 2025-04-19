import telebot
from config import token
from botlogic import value,sendkeys
bot = telebot.TeleBot(token)
from botlogic import trash


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграмм бот по защите окружающей среды. Чем я могу быть полезен?")

@bot.message_handler(commands=['help'])
def sendhelp(message):
    bot.reply_to(message, f"Всё команды: {', '.join([f'/{key}' for key in trash.keys()])}")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    key = message.text.strip().lower()
    if key.startswith('/'):
        key = key[1:]  #
        if key in trash:
            bot.reply_to(message, trash[key])
        else:
            bot.reply_to(message, "Неизвестная команда. Введите /help для списка команд.")
    else:
        bot.reply_to(message, "Пожалуйста, используйте команды, начинающиеся с /")


def value(key):
    return trash.get(key, "Информация по этой категории отсутствует")

def sendkeys():
    return list(trash.keys())

bot.infinity_polling()
