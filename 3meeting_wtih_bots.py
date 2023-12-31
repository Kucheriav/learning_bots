import telebot
import os
import random

name_tg = '@my_new_test_robo_bot'
API_TOKEN = 'YOUR API CODE HERE'
bot = telebot.TeleBot(API_TOKEN)
FOLDER = 'memes'


@bot.message_handler(commands=['start'])
def say_hello(message):
    meme_list = os.listdir(f'./{FOLDER}')
    meme_name = f'./{FOLDER}/{random.choice(meme_list)}'
    bot.send_photo(message.chat.id, open(meme_name, 'rb'))


bot.infinity_polling()