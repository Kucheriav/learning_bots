import telebot
import requests
from telebot import types # для указание типов

name_tg = '@my_new_test_robo_bot'
API_TOKEN = '6656798397:AAH5mluzrSlL2FjT80nlDK9znAg0Rz7xenk'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет! Я котиков высылаю. Хочешь что-нибудь?'
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Факт')
    button2 = types.KeyboardButton('Картинка')
    button3 = types.KeyboardButton('Ничего не хочу')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.register_next_step_handler(message, check_answer)



@bot.message_handler()
def check_answer(message):
    if message.text == 'Факт':
        fact = get_fact()
        bot.send_message(message.chat.id, fact)
    elif message.text == 'Картинка':
        img = 42
        bot.send_message(message.chat.id, img)
    elif message.text == 'Ничего не хочу':
        text = 'Ну и ладно....'
        bot.send_message(message.chat.id, text)
    else:
        text = 'Не понял вас'
        bot.send_message(message.chat.id, text)


def get_fact():
    url = 'https://cat-fact.herokuapp.com/facts'
    responce = requests.get(url)
    responce = responce.json()
    responce = responce[0]['text']
    return responce

bot.infinity_polling()
