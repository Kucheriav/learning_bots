import telebot
import random

name_tg = '@my_new_test_robo_bot'
API_TOKEN = '6656798397:AAH5mluzrSlL2FjT80nlDK9znAg0Rz7xenk'
bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    text = '''Привет!\nВыбери направление разговора!\n1. загадка\n2. погода\n3. поболтать\nУкажите цифру'''
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, check_direction)

@bot.message_handler()
def check_direction(message):
    if message.text == '1':
        text = say_question()
        bot.send_message(message.chat.id, text[0])
        bot.register_next_step_handler(message, check_answer, answer=text[1])
    elif message.text == '2':
        bot.send_message(message.chat.id, 'Погода отличная!')
        start(message)
    elif message.text == '3':
        bot.send_message(message.chat.id, "Как дела?")
        bot.register_next_step_handler(message, lets_chat)

def say_question():
    file = open('questions.txt', encoding='utf8')
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].split('*')
    return random.choice(data)

@bot.message_handler()
def check_answer(message, answer:str):
    if message.text.lower() in answer:
        bot.send_message(message.chat.id, 'Верно!')
        start(message)
    else:
        bot.send_message(message.chat.id, 'Неверно! Попробуй еще раз')
        bot.register_next_step_handler(message, check_answer, answer=answer)

@bot.message_handler()
def lets_chat(message):
    if message.text.lower() in ['отличн', 'супер', 'волшеб']:
        bot.send_message(message.chat.id, 'Это круто!')
        bot.register_next_step_handler(message, lets_chat)
    elif message.text.lower() in ['плох', 'ужас', 'отвратит']:
        bot.send_message(message.chat.id, 'Это плохо!')
        bot.register_next_step_handler(message, lets_chat)
    elif message.text.lower() in ['норм', 'никак', '']:
        bot.send_message(message.chat.id, 'Это норма!')
        bot.register_next_step_handler(message, lets_chat)
    elif message.text.lower() in ['все', 'хватит', 'закончит']:
        bot.send_message(message.chat.id, 'Заканчиваем')
        start(message)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял!')
        bot.register_next_step_handler(message, lets_chat)


bot.infinity_polling()