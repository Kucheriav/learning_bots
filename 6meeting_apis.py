import telebot
import requests
from telebot import types

name_tg = '@my_new_test_robo_bot'
API_TOKEN = 'YOUR API CODE HERE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет! Мы тут котиками балуемся. Хочешь чего?'
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
        fact = get_fact('cat', 1)
        bot.send_message(message.chat.id, fact)
    elif message.text == 'Картинка':
        img = get_picture(200)
        bot.send_photo(message.chat.id, img)
    elif message.text == 'Ничего не хочу':
        bot.send_message(message.chat.id, 'Ну и ладно')
    else:
        text = 'Не понял вас'
        bot.send_message(message.chat.id, text)



def get_fact(animal_type, amount):
    url = f'https://cat-fact.herokuapp.com/facts/random?animal_type={animal_type}&amount={amount}'
    responce = requests.get(url)
    responce = responce.json()['text']
    return responce

def get_picture(code):
    url = f'https://http.cat/{code}'
    responce = requests.get(url)
    responce = responce.content
    return responce



bot.infinity_polling()