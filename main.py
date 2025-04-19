import telebot
from config import token
from botlogic import gen_pass
from botlogic import coin
import random
import os
import requests
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['generate_password'])
def send_password(message):
    bot.send_message(message.chat.id, gen_pass(10))

@bot.message_handler(commands=['Coin_Flip'])
def send_result_coin(message):
    bot.send_message(message.chat.id, coin('flip'))

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
Доступные команды:
/start - Начать работу с ботом
/hello - Приветствие
/bye - Попрощаться
/generate_password - Сгенерировать случайный пароль (10 символов)
/Coin_Flip - Подбросить монетку
/poll - Создать тест на артикли
/help - Показать это сообщение
/cs_maps - Карты для игры в КС2
"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['cs_maps'])
def maps(message):
    maps_name= """
/Aim_maps - Аимки
/HS_maps - Прятки
/Guide_maps - Карты с гайдами на что либо
/Funny_maps - Карты для игры с друзьями
"""
    
    bot.reply_to(message, maps_name)

@bot.message_handler(commands=['Aim_maps'])
def aim(message):
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3084291314&searchtext=AIM")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=594315388&searchtext=AIM")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3070244462&searchtext=AIM")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=1687663948&searchtext=AIM")

@bot.message_handler(commands=['HS_maps'])
def hide(message):
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3406406223&searchtext=Hide+and+seek")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3326282876&searchtext=Hide+and+seek")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3325831241&searchtext=Hide+and+seek")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3387070705&searchtext=Hide+and+seek")

@bot.message_handler(commands=['Guide_maps'])
def guide(message):
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3379564935&searchtext=AIM")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3100869952&searchtext=recoil")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3355497176&searchtext=movement")

@bot.message_handler(commands=['Funny_maps'])
def fun(message):
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3331706760&searchtext=jetpack+joyrider")
    bot.reply_to(message,"https://steamcommunity.com/sharedfiles/filedetails/?id=3408062754&searchtext=squid")


@bot.message_handler(commands=['csmem'])
def send_mem(message):    
    img_name=random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass

bot.infinity_polling()