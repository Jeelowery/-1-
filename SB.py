import telebot
from telebot import types
token = "5222216535:AAGs28Ul3c3Pi7RHVSRFI06Mh75PQwqB6A0"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("да", "нет", "/help", "/music", "/end")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать, куда можно сходить в Москве?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу отправить тебя гулять \nТакже я могу тебе предложить тебе послушать популярную музыку на сегодня: /music \nНу и, конечно, если сильно устал, можешь остаться дома и поспать \nЕсли хочешь закончить общение со мной нажми /end')
@bot.message_handler(commands=['music'])
def start_message(message):
    bot.send_message(message.chat.id, 'Популярная музыка на сегодня: https://vk.com/audios137987627?block=tracks_chart&section=explore')
@bot.message_handler(commands=['end'])
def start_message(message):
    bot.send_message(message.chat.id, 'Удачи! Жду тебя снова!')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "да":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("осень", "зима", "весна", "лето")
        bot.send_message(message.chat.id, 'Какое сейчас время года?', reply_markup=keyboard)
    if message.text.lower() == "лето":
        bot.send_message(message.chat.id, 'Сходи в парк Горького')
    if message.text.lower() == "зима":
        bot.send_message(message.chat.id, 'Сходи на каток ВДНХ')
    if message.text.lower() == "весна":
        bot.send_message(message.chat.id, 'Сходи в Сыто Пьяно')
    if message.text.lower() == "осень":
        bot.send_message(message.chat.id, 'Купи чекушку и сиди дома')
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Маме привет')
bot.infinity_polling()
