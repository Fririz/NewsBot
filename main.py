
import usersData
import telebot
from telebot import types
from secr import TOKEN 
import pars

bot = telebot.TeleBot(TOKEN)

chat_id = 688419885

parser = pars.prs("https://itc.ua/techno/")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    db = usersData.usrDataEdit()
    if db.checkIDInDataBase(message.chat.id):
        db.addUsersToDataBase(message.chat.id, message.from_user.username)
        print(f"Добавляю пользователя: {message.chat.id}, {message.from_user.username}")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Подивитись новини")
    markup.add(btn)
    bot.send_message(message.chat.id, "Привіт, натисни кнопку нижче щоб побачити новини", reply_markup=markup)

    
# Обработка кнопки
@bot.message_handler(func=lambda message: message.text == "Подивитись новини")
def show_news(message):
    bot.send_message(message.chat.id, parser)



# Запуск бота
bot.polling()
